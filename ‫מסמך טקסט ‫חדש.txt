

#
#   the object we wand is mach more similer to grids (or latitue) then cordinate system
#   so i will crate a new object which will be simple and limited to the "Integer world" .
#
#   
#   Sum(a) = a.x + a.y
#   distance(a ,b) = Sum(a) - Sum(b)  
#        
#

from enum import Enum

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



def C_Sum(z):
    return z.real + z.imag

class _Clocation():
    def __init__ (self ,z):
        self.z = z 
        self.Sum = C_Sum(z)


# 
#   get_distance stay as it was
#


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
    if location1 is _location and location2 is _location:
        pass
    raise Exception("the arguments must be a locations")