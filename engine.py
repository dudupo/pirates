

#------------ imports --------------------------------- #

import Enum as enum

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

def Rotation(_list , right = True):
    if right:
        return _list[-1] + _list[0:-1]
    else:
        return _list[1:] + _list[0]

#--------------- constants ---------------- #


FIRERANGE = 5

#------------------------------------------ #



#   location will presant as complex number ,

#   pirates -> two list's sorted by x and y position  
#
#






pirates   =[]

# abstract....
hashReal  = h(index) , pirates 
hashImag  = h(index) , pirates

setattr(hashReal ,"insert" , _insert)
setattr(hashImag , "insert" , _insertImag)




def insert(pirate ,hashLists):
    _insert(pirate , hashLists[0])
    _insertImag(pirate , hashLists[1])



def _insert(pirate , hashList ,_key=lambda pirate1 : \
 pirate1.location.real , sortRangeRadious = pirate.speed):
    
    # the id of pirate is constant
    lastIndex = hashList[0][pirate.id]
    hashList[1][lastIndex] = pirate

    gen = genforSort(sortRangeRadious , hashList[1] , lastIndex)

    # position refers to other pirate , just for buety i called it 'position'
    for index , position ,left in gen():
        smaller = _key(pirate) < _key(position)
        if (not smaller and left) or (smaller and not left):
            
            if left: 
                hashList[1][lastIndex:index] = \
                Rotation(hashList[1][lastIndex:index] , right = True)

                hashList[0][lastIndex:index] = \
                Rotation(hashList[0][lastIndex:index] , right = True)
            else :
                hashList[1][lastIndex:index] = \
                Rotation(hashList[1][lastIndex:index] , right = False)

                hashList[0][lastIndex:index] = \
                Rotation(hashList[0][lastIndex:index] , right = False)

            #command to the generator to stop
            gen.send(False)

        # command to the generator to continue
        gen.send(True)
    
def _insertImag(pirate ,hashList):
    _insert(pirate , hashList , _key = lambda pirate1 : \
        pirate1.location.imag ,pirate.speed)


def genforSort (Range , _List ,startPosition):
    """generator which help to excute inserting in the sort list"""
    start = startPosition - Range
    if start < 0 :
        start = 0

    end = startPosition + Range + 1
    if end > len(_List):
        end = len(_List)

    index = start
    flag = True 
    for otherPirate in _List[start:startPosition]:
        flag = yield index , otherPirate ,True
        if not flag:
            break
        index += 1

    index = end
    if flag :
        for otherPirate in _List[end , startPosition , -1]:
            flag = yield index , otherPirate ,False
            if not flag :
                break
            index -= 1

def genforbattle(pirate , hashList):
    
    fireRange = pirate.fireRange

    gen = genforSort(fireRange ,hashList[1] ,hashLists[0][pirate.id])
    for index , position , left in gen():
        if _abs(position.location - pirate.location) < fireRange :
            yield position
        gen.send(True)


def PiratesItear(pirates , _filter = lambda pirate1 : True):
    for pirate in pirates : 
        if _filter(pirate):
            yield pirate


def battle(pirate , hashReal , hashImag):
    CountEnemey , CountFriends = 0 , 0
    _id = pirate.id

    gen = genforbattle(pirate ,(hashReal , hashImag))

    for pirate2 in gen() :
        if pirate2.id == _id :
            CountFriends += 1
        else :
            CountEnemey  += 1

    if (CountFriends < CountEnemey):
        pass #'kill'




#
# every function as SetSail(,) push a tokens to Stack 
#



class TokenCommand(object):
    def __init__(self , function ,arguments):
        self.arguments = arguments
        command = lambda : function(arguments)
        setattr(self ,"__call__" , command)

class commandsEnum(enum):
    pass 
        
    
#Stacklist -> will contain each stack of every player
def ExecuteTurn (Stacklist):

    # for mixing the tokens order 
    jumble = zip(Stacklist)
    for tok in jumble:
        tok()        

        