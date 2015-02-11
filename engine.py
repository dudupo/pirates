

#------------ imports --------------------------------- #

from enum import Enum  

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
    if len(_list) < 2:
        return _list
    if right:
        return _list[1:] + [_list[0]]
    else:
        return [_list[-1]] + _list[0:-1]

#--------------- constants ---------------- #


FIRERANGE = 5

#------------------------------------------ #


hashLists =[]
def initHashLists(hashRealIndex ,hashReal , hashImagIndex ,hashImag):
    global hashLists
    hashLists = [[hashRealIndex ,hashReal] , [hashImagIndex ,hashImag]]
    
    from main import NUM_OF_BOTS 
    global Tasks
    Tasks = [[] for _ in range(NUM_OF_BOTS)]

# abstract....
#hashReal  = h(index) , pirates 
#hashImag  = h(index) , pirates

def updateLists(pirate):
    global hashLists
    _insert(pirate , hashLists[0] ,pirate.speed)
    _insertImag(pirate , hashLists[1])

def _insert(pirate , hashList ,  sortRangeRadious , \
    _key=lambda pirate1 : pirate1.location.real ):
    
    # the id of pirate is constant
    lastIndex = hashList[0][pirate.id]
    hashList[1][lastIndex] = pirate

    gen = genforSort(sortRangeRadious , hashList[1] , lastIndex)

    # position refers to other pirate , just for buety i called it 'position'
    for index , position ,left in gen:
        smaller = _key(pirate) < _key(position)

        if ((not smaller) and left) or (smaller and (not left)):
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
            break

    
def _insertImag(pirate ,hashList):
    _insert(pirate , hashList ,pirate.speed , \
     _key = lambda pirate1 : pirate1.location.imag)


def genforSort (Range , _List ,startPosition):
    """generator which help to excute inserting in the sort list"""
    start = startPosition - Range
    if start < 0 :
        start = 0

    end = startPosition + Range + 1
    if end > len(_List):
        end = len(_List)

    index = start
    for otherPirate in _List[start:startPosition]:
        yield index , otherPirate ,False     
        index += 1

    index = end
    for otherPirate in _List[end : startPosition : -1]:
        yield index , otherPirate ,True
        index -= 1

def genforbattle(pirate , hashList):
    
    fireRange = pirate.fireRange

    gen = genforSort(fireRange ,hashList[1] ,hashList[0][pirate.id])
    for index , position , left in gen:
        if _abs(position.location - pirate.location) < fireRange :
            yield position


def PiratesItear(pirates , _filter = lambda pirate1 : True):
    for pirate in pirates : 
        if _filter(pirate):
            yield pirate


def battle(pirate , hashReal):
    CountEnemey , CountFriends = 0 , 0
    _id = pirate.id

    gen = genforbattle(pirate ,hashReal)

    for pirate2 in gen :
        if pirate2.id == _id :
            CountFriends += 1
        else :
            CountEnemey  += 1

    if (CountFriends < CountEnemey):
        pass #'kill'



Tasks = []

class _task:
    def __init__(self , function , arg):
        self.work = lambda : function(*arg)
        # self.arg = arg -> for dibuging

def push_Task(Task , player):
    global Tasks
    Tasks[player.id] += [Task]

def update():
    global Tasks
    
    tokens = []
    c = 0
    while (c < len(Tasks)):
        c = 0
        for player in Tasks:
            if len(player) > 0 :
                tokens += [player.pop()] 
            else:
                c+= 1
            
    for Turn in tokens:
        # print("\n" + str(Turn.arg[0])) -> for dibuging
        Turn.work()
    
    Tasks = []
