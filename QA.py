
import game 
import pirate
import engine 
import player
from bot import Bot
from vector import Vector
miki = player.Player("miki" , 1)
_game = game.Game(miki)

dudu = player.Player("dudu" , 0)
_game2 = game.Game(dudu)
 
_pirate = pirate.pirate(dudu , 0 , 0 )
_pirate2 = pirate.pirate(miki ,Vector(0,2) ,1 )

engine.pirates=[_pirate,_pirate2]

bot1 = Bot("bot1",_game)

for i in range(50):
	bot1()
	engine.update() 

