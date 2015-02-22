import bots.bot1

init = True
runers = []
attackers =[]

def do_turn(game):
	
	global init
	global runers
	global attackers 

	if init :
		for pirate in game.get_my_pirates()[0:3]:
			runers.append(bots.bot1.Runer(game ,pirate))
		for pirate in game.get_my_pirates()[3:6]:
			attackers.append(bots.bot1.Attacker(game,pirate))
		init = False 

	for runer in runers:
		runer._do_turn() 
	for attacker in attackers :
		attacker._do_turn()

