import game 
import pirate
import engine 
import player
i=0

def do_turn(game):
	global i 
	i+=1
	for pirate in game.get_my_pirates():

		if pirate.location.x<19:
			game.set_sail(pirate,'e')
		elif pirate.location.y<10:
			game.set_sail(pirate,'n')
		else:
			if i%5==0:
				print("waiting")