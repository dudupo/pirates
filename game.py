


#
#   the object we wand is mach more similer to grids (or latitue) then cordinate system
#   so i will crate a new object which will be simple and limited to the "Integer world" .
#
#   
#   Sum(a) = a.x + a.y
#   distance(a ,b) = Sum(a) - Sum(b)  
#        
#



#dont forget : pip install enum34
from enum import Enum
from numpy import sign
import emulator


global NUM_OF_BOTS


class _location (object):
    def __init__(self ,x,y ,ocupaier = None):
        self.location = x , y
        self.Sum = x + y

        # Can be island or pirate
        self.ocupaier = None 


        

def get_distance(location1 , location2):
    'calculate the distance between a pair of locations'
    if location1 is _location and location2 is _location:
        return abs( location1.Sum - location2.Sum)

    raise Exception("the arguments must be a locations")
  
def get_direction(location1 , location2):
    'return the a possible path'
    if location1 is _location and location2 is _location:
        pass
    raise Exception("the arguments must be a locations")


#
#   about directions , each direction is immpleamented by atuple  
#                      the idea that when we will try add direction
#                      to location it will seems as : 
#                       
#                      _Pirate.loaction[[direction[0]] += direction[1]
#

class _Directions(Enum):
    east  = 0 ,  1 
    west = 0 , -1 
    north = 1 ,  1
    south = 1 , -1


# ------------------- with Complex Number -------------------------------------- #



def _abs(z):
    return abs(z.real) + abs(z.imag)

class _Clocation():
    def __init__ (self ,z):
        self.z = z 
    def __abs__(self):
        return _abs(self.z)
    def __sub__(other , self):
        return Cget_direction(self , other)
    def __mul__(self ,other):
        return abs(self - other)
# 
#   get_distance stay as it was
#


def Cget_distance(location1 , location2):
    'calculate the distance between a pair of locations'
    try:
        return _abs(Cget_direction(location1 , location2))
    except:
        raise Exception("the arguments must be a locations")


#
# you must to admit that the Directions look mach better
#


class _CDirections(Enum):
    east  =  1 
    west  = -1 
    north =  1j 
    south = -1j 

#
#
#   note that : sign(n) =  if n positive : 1
#                          else : 0
#
#   z_path = z1 - z2  = (x1 -x2)  + (y1 - y2)j
#   Sail diraction = 1*sign(z_path.real) + 1j * sign(z_path.imag)
#   
#   there will be suach precdore as :
#       
#       counter = 0 
#       while counter < speed 
#           counter += Sail(z-path)
#
#   speed in ouer equal 2 .
#       
#


def Cget_direction(location1 , location2):
    'return the a possible path'

    try:
        return location2.z - location1.z
    except:
        raise Exception("the arguments must be a locations")


# just to demostrate the idea . 
def CSail_to_direction(pirate,direction ,speed = 2):

    counter = 0 
    z = direction
    while counter < speed :
        
        sail_path = 1 * sign(z.real) + 1j * sign(z.imag)
        counter += _abs(sail_path)

        #just for the dibuging
        pirate.location = _Clocation(pirate.location.z + sail_path)
    try:
        emulator.update(pirate)
    except:
        pass

def CSail_to_location(pirate ,location ,speed =2):

    #  direction = Cget_direction(pirate.location , location)
    #   
    #   the above statement and under are the same 
    #
    direction = location - pirate.location  
    CSail_to_direction(pirate ,direction ,speed)
    

#------------------------game----------------------------#

class game():
    def __init__(self,init_Map):
        self.islands = init_Map.init_islands()
        self.pirates = init_Map.init_pirates()
    def GetPiratesByPlayerId(self , PlayerId):
        return self.pirates[PlayerId]
    def GetIslands(self , PlayerId):
        return self.islands[PlayerId]


class gameApi():
    def __init__(self , game , PlayerId):
        self.game = game
        self.PlayerId = PlayerId
    def GetMyPirates(self):
        return self.game.GetPiratesByPlayerId(self.PlayerId)
    def GetEnemeyPirates(self):
        #
        #   look as shit ,one day i will make it smarter 
        #
        return self.game.GetPiratesByPlayerId((self.PlayerId + 1) % NUM_OF_BOTS)
    def GatPirates(self):
        return self.game.pirates
    def GetFreeIslands(self):
        return self.game.GetIslands(0)
    def GetMyIslands(self):
        return self.game.GetIslands(self.PlayerId + 1)
    def GetEnemyIslands(self):
        return self.game.GetIslands((self.PlayerId + 2) % (NUM_OF_BOTS+1))




