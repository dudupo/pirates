import game 
import pirate
import engine 
import player
i=0

def do_turn(game):
	if len(game.get_not_my_islands())>0:
		pirate=game.get_my_pirates()[0]
		island=game.get_not_my_islands()[0]
		directions= game.get_directions(pirate,island)
		if len(directions)>0:
			direaction=directions[0]
			game.set_sail(pirate,direaction)