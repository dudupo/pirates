import game 
import pirate
import engine 
import player
i=0

def do_turn(game):
	global i 
	i+=1
	print("turn number "+str(i))
	game.set_sail(game.get_my_pirates()[0],'en')