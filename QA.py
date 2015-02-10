

import game 
import pirate
import engine 


piratesA = [pirate.pirate(2*i + i* 1j, i ,4 ,2) for i in range(0,10)]

gen = engine.PiratesItear(piratesA)

for _pirate in gen:
	print (_pirate)

hashlistX = [[i for i in range(0,10)] ,[_pirate for _pirate in piratesA]]
hashlistY = [[i for i in range(0,10)] ,[_pirate for _pirate in piratesA]]
hashlists = hashlistX ,hashlistY

# lets give to pirate 2 a little speed .  
piratesA[2].speed = 13

# now we can let him sell .
piratesA[2].location = 17 + 3j


try:
	engine.insert(piratesA[2] ,hashlists)

except StopIteration: 
	pass # done
	
print("\nnow one of the pirate is moving... \n")



for (index ,_pirate) in zip(hashlistX[0] ,hashlistX[1] ):
	print (_pirate)