
import outPut

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
        # print("\ni was here\n")
        return _list
    if right:
        return _list[1:] + [_list[0]]
    else:
        return [_list[-1]] + _list[0:-1]

#--------------- constants ---------------- #


FIRERANGE = 5

#------------------------------------------ #
Tasks = []
DeadPirates =[]
pirates =    []
hashLists =  []
def init (_pirates ,hashRealIndex ,hashReal , hashImagIndex ,hashImag):
    global hashLists
    hashLists = [[hashRealIndex ,hashReal] , [hashImagIndex ,hashImag]]
    
    from main import NUM_OF_BOTS 


    global Tasks
    Tasks = [[] for _ in range(NUM_OF_BOTS)]

    restTasks = Tasks

    global pirates
    pirates = _pirates


# abstract....
#hashReal  = h(index) , pirates 
#hashImag  = h(index) , pirates

def updateLists(pirate):
    global hashLists
    _insert(pirate , hashLists[0] ,pirate.speed)
    _insertImag(pirate , hashLists[1])
    outPut.Add(pirate)

def _insert(pirate , hashList ,  sortRangeRadious , \
    _key=lambda pirate1 : pirate1.location.real ):
    
    # the id of pirate is constant
    lastIndex = hashList[0][pirate.id]
    hashList[1][lastIndex] = pirate

    gen = genforSort(sortRangeRadious , hashList[1] , lastIndex)

    # position refers to other pirate , just for buety i called it 'position'
    for index , position ,left in gen:
        smaller = _key(pirate) < _key(position)
        grater =  _key(pirate) > _key(position)

        if (((left) and (smaller)) or ((not left) and (grater))):
            if left: 
                lastIndex += 1
                hashList[1][index:lastIndex] = \
                Rotation(hashList[1][index:lastIndex] , right = False)

                hashList[0][index:lastIndex] = \
                Rotation(hashList[0][index:lastIndex] , right = False)



            else :
                index += 1 

                hashList[1][lastIndex:index] = \
                Rotation(hashList[1][lastIndex:index] , right = True)
                

                hashList[0][lastIndex:index] = \
                Rotation(hashList[0][lastIndex:index] , right = True )



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
        end = len(_List) - 1

    index = start
    for otherPirate in _List[start:startPosition]:
        if otherPirate.alive :
            yield index , otherPirate ,True     
        index += 1

    index = end
    for otherPirate in _List[end : startPosition : -1]:
        if otherPirate.alive :
            yield index , otherPirate ,False
        index -= 1


        
def PiratesItear(pirates , _filter = lambda pirate1 : True):
    for pirate in pirates : 
        if _filter(pirate):
            yield pirate


def battle():
    global hashLists
    global pirates
    life = {}

    for pirate in pirates :
        if pirate.alive :
            life[pirate] = 0

    for pirate in hashLists[0][1]:
        if pirate.alive :
            position = hashLists[0][0][pirate.id]
            start = 0
            end   = len(hashLists[0][1])

            for otherPirate in hashLists[0][1][position:start:-1]:
                if otherPirate.alive :
                    if pirate.location.real - otherPirate.location.real < pirate.fireRange:
                        if _abs(pirate.location - otherPirate.location) < pirate.fireRange:
                            if otherPirate.player.id != pirate.player.id:
                                life[otherPirate] -= 1
                            else :
                                life[otherPirate] += 1
                    else:
                        break
            for otherPirate in hashLists[0][1][position:end]:
                if otherPirate.alive :
                    if otherPirate.location.real - pirate.location.real < pirate.fireRange:
                        if _abs(pirate.location - otherPirate.location) < pirate.fireRange:
                            if otherPirate.player.id != pirate.player.id:
                                life[otherPirate] -= 1
                            else :
                                life[otherPirate] += 1
                    else:
                        break

    global DeadPirates 

    for pirate in pirates :
        if life[pirate] < 0 :
            pirate.alive = False
            pirate.timeToDiead = 40
            pirate.location = pirate.player.StartLocation()
            DeadPirates += [pirate]

        # print ("life number of pirate " + str(pirate.id) + " is " + str(life[pirate])) -> for dibuging

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
                c += 1

    for Turn in tokens:
        # print("\n" + str(Turn.arg[0])) -> for dibuging
        Turn.work()



    global DeadPirates
    for pirate in DeadPirates :
        pirate.timeToDiead -= 1


    battle()
        
    global pirates
    for pirate in pirates:
        pirate.power = pirate.speed

    
    from main import NUM_OF_BOTS
    Tasks = [[] for _ in range(NUM_OF_BOTS)]


    outPut.build()
