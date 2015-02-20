import random
def do_turn(game):


	if len(game.get_not_my_islands())<=0:
		return
	for pirate in game.get_my_pirates():
		target=None
		mini=100000
		for island in game.get_not_my_islands():
			t=distanse(pirate.location,island.location)
			if t < mini:
				target=island
				mini=t
		
		if target != None:
			d = game.get_directions(pirate,target)
			if len(d) > 0:
				ret = game.set_sail(pirate,d[0])
				if not ret :
					if d[0] == "e" or "w":
						game.set_sail(pirate,random.choice(["n" ,"s"]))
					else :
						game.set_sail(pirate,random.choice(["e" ,"w"]))
			else:
				continue
		
		else:
			continue
	
def distanse(a,b):
	return abs(a.x-b.x)+abs(a.y-b.y)