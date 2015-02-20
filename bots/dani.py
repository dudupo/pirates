import random

def do_turn(game):


	if len(game.get_not_my_islands())<=0:
		return

	searching=[]
	l=0
	for pirate in game.get_my_pirates():
		l+=1
		if l>4:
			searching=[]
		target=None
		mini=100000

		for island in [i for i in game.get_not_my_islands() if i not in searching]:
			
			t=distanse(pirate.location,island.location)
			
			if t < mini:
				target=island
				mini=t
		
		if target != None:
			d = game.get_directions(pirate,target)
			searching.append(target)
			if len(d) > 0:
				ret = game.set_sail(pirate,d[0])
			
			else:
				continue
		
		else:
			continue
	
def distanse(a,b):
	return abs(a.x-b.x)+abs(a.y-b.y)