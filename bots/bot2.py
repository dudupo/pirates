import bots.bot1
import bots.bot_functions

init = True
runers = []
attackers =[]


def do_turn(game):
	
	global init
	global runers
	global attackers 


	
	if init :
		for pirate in game.get_my_pirates()[0:4]:
			runers.append(bots.bot1.Runer(game ,pirate))
		for pirate in game.get_my_pirates()[4:6]:
			attackers.append(bots.bot1.Attacker(game,pirate))
		init = False 

	for runer in runers:
		runer._do_turn() 


	for attacker in attackers :
		attacker._do_turn()
	'''
	sets = list()
	
	enemys = game.get_enemy_pirates()
	if len(enemys) > 0:
		enemys = [enemy for enemy in enemys if enemy.alive]
		sets , dict_sets = bots.bot_functions.deptu(enemys , 5)
		if len(sets) > 0 :
			for _set in sets:
				print (_set)
			print("----")
	'''