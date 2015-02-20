import bots.bot1

init = True
runers = []
searching=[[] ,[] ,[]]

def do_turn(game):
	
	global init
	global runers
	global searching

	if init :
		c = 0
		for pirate in game.get_my_pirates():
			runers.append(bots.bot1.Runer(game ,pirate , searching[c]))
			c+= 1
			c%=3
		init = False 

	for runer in runers:
		runer._do_turn() 

