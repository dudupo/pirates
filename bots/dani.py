import random
def do_turn(game):
	if len(game.get_not_my_islands())<=0:
		return
	for pirate in game.get_my_pirates():
		target=None
		mini=1000
		for island in game.get_not_my_islands():
			t=distanse(pirate.location,island.location)
			if t < mini:
				target=island
				mini=t
		
		if target != None:
			d = game.get_directions(pirate,target)
			if len(d) > 0:
				game.set_sail(pirate,d[0])
			else:
				continue
		
		else:
			continue
	
def distanse(a,b):
	return abs(a.x-b.x)+abs(a.y-b.y)