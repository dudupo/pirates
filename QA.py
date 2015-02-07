

import game 
import pirate

a = game._Clocation(18 + 5j)
b = game._Clocation(1 + 20j)

print("\n")
print(">>bob the pirate locate at point a: " + str(a.z) +" \nhis traget locate at point b: " + str(b.z))


bob = pirate.pirate(a)


while game.Cget_distance(bob.location ,b) > 1 :
	game.CSail_to_location(bob , b , 2)
	print (">>bob now at " + str(bob.location.z))

