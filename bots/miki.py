import game 
import pirate
import engine 
import player

def do_turn(game):
	for pirate in game.get_my_pirates():
		if pirate.location.x<6:
			game.set_sail(pirate,'e')