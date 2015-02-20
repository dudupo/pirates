import bots.bot1

init = True
runers = []
def do_turn(game):
	
	global init
	global runers

	if init :
		for pirate in game.get_my_pirates():
			runers.append(bots.bot1.Runer(game ,pirate))
		init = False 

	for runer in runers:
		runer._do_turn() 

