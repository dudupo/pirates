

import game 
import pirate
import engine 
import player


miki = player.Player("miki" , 0)
_game = game.Game(miki)

dudu = player.Player("dudu" , 1)
_game2 = game.Game(dudu)



piratesA = [pirate.pirate(2*i + i* 1j, i ,4 ,2) for i in range(0,10)]

hashlistX = [[i for i in range(0,10)] ,[_pirate for _pirate in piratesA]]
hashlistY = [[i for i in range(0,10)] ,[_pirate for _pirate in piratesA]]
hashlists = hashlistX ,hashlistY
engine.initHashLists(hashlistX[0] , hashlistX[1] , \
	hashlistY[0] , hashlistY[1 ])

# ---------------------- .  
piratesA[2].power = 5
piratesA[6].speed = 2
# ---------------------- . 
_game.SetSail(piratesA[2] , "eeeee")
_game2.SetSail(piratesA[6] , "www")
engine.update()

for _pirate in hashlistX[1]:
	print(_pirate)




