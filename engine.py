



#------------- some numeric function ------------------- #

def sign (n):
    ret = 0
    
    if n > 0 :
        ret = 1
    
    elif n < 0 :
        ret = -1

    return ret

def _abs(z):
    return abs(z.real) + abs(z.imag)



#--------------- constants ---------------- #


FIRERANGE = 5

#------------------------------------------ #



#   location will presant as complex number ,

#   pirates -> two list's sorted by x and y position  
#
#






pirates   =[]
hashReal  ={}
hashImag  ={}

satattr(hashReal ,"insert" , _insert)
satattr(hashImag , "insert" , _insertImag)


def _insert(pirate , hashList ,_key=lambda pirate1 : \
 pirate1.location.real):
    hashReal[pirate.id] = pirate 

    sortRangeRadious = pirate.speed
    start = pirate.id - sortRangeRadious
    end   = pirate.id + sortRangeRadious + 1

    hashReal[start:end].sort(key = _key)

def _insertImag(pirate ,hashList):
    _insert(pirate , hashList , _key = lambda pirate1 : \
        pirate1.location.imag)


def runInfireRange (pirate , tuplehash):
    z = pirate.location

    # position in the lists
    position = pirate.id 

    ValueLists = (tuplehash[0].values() , \
     tuplehash[1].values()) 

    for pirate2 in reversed(ValueLists[:position]):

        realAxeisDistance = abs(z.real - pirate2.location.real)
        if  realAxeisDistance > FIRERANGE :
            break

        imagAxeisDistance = abs(z.imag - pirate2.location.imag)
        elif realAxeisDistance + imagAxeisDistance < FIRERANGE :
            yield pirate2  

    for pirate2 in ValueLists[position:]:
        realAxeisDistance = abs(z.real - pirate2.location.real)
        if  realAxeisDistance > FIRERANGE :
            break

        imagAxeisDistance = abs(z.imag - pirate2.location.imag)
        elif realAxeisDistance + imagAxeisDistance < FIRERANGE :
            yield pirate2    

def PiratesItear(pirates , _filter = lambda pirate1 : True):
    for pirate in pirates : 
        if _filter(pirate):
            yield pirate


def battle(pirate , hashReal , hashImag):
    CountEnemey , CountFriends = 0 , 0
    _id = pirate.id

    for pirate2 in runInfireRange(pirate ,(hashReal , hashImag)):
        if pirate2.id == _id :
            CountFriends += 1
        else :
            CountEnemey  += 1

    if (CountFriends < CountEnemey):
        pass #'kill'




#
# every function as SetSail(,) push a tokens to Stack 
#

#Stacklist -> will contain each stack of every player
def ExecuteTurn (Stacklist):

    # for mixing the tokens order 
    jumble = zip(Stacklist)
    for tok in jumble:
        