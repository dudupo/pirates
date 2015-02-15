

import game 
import pirate
import engine 
import player
from bot import Bot

miki = player.Player("miki" , 1)
_game = game.Game(miki)

dudu = player.Player("dudu" , 0)
_game2 = game.Game(dudu)

# with follwing exmple there is a problem 
'''
piratesA = [pirate.pirate(miki ,2*i + i* 1j, i ,4 ,2) for i in range(0,5)]
piratesA += [pirate.pirate(dudu ,2*i + i* 1j, i ,4 ,2) for i in range(5,10)]

hashlistX = [[i for i in range(0,10)] ,[_pirate for _pirate in piratesA]]
hashlistY = [[i for i in range(0,10)] ,[_pirate for _pirate in piratesA]]
hashlists = hashlistX ,hashlistY

engine.init(piratesA ,hashlistX[0] , hashlistX[1] , \
	hashlistY[0] , hashlistY[1 ])

# ---------------------- .  
piratesA[2].power = 3
piratesA[2].speed = 3
piratesA[6].speed = 7
piratesA[6].power = 7
# ---------------------- . 
_game.SetSail(piratesA[2] , "eeeeeeeeeeeeeeee")
_game2.SetSail(piratesA[6] , "wwwwwwww")
engine.update()

for _pirate in hashlistX[1]:
	print(_pirate)
	if not _pirate.alive :
		print ("^ is dead...")
'''

_pirate = pirate.pirate(dudu , 0 , 0 , 4 ,3)
_pirate2 = pirate.pirate(miki ,7 + 11j ,1 ,4 ,3)
print(str(_game.get_my_pirates()) )

engine.init([_pirate , _pirate2] ,[0,1] , [_pirate , _pirate2] , \
	[0,1] , [_pirate , _pirate2])
bot1 = Bot("bot1",_game)

for i in range(50):
	_game2.SetSail(_pirate,"en")
	bot1()
	engine.update() 

engine.build()