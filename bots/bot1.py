	

import random 
import vector

class Runer():

	def __init__(self ,game , runer):
		self.esacpe = False
		self.esacpe_value = None
		self.esacpe_counter = 3
		self._Distance = []
		self.runer = runer
		self.game = game
		self.target = None

	def _do_turn(self):
		

		if self.esacpe :
			enemys = self.game.get_enemy_pirates()
			self._Distance += [[enemy.location - self.runer.location for enemy in enemys]]

			if self.esacpe_counter > 0 :
				ret = self.game.set_sail(self.runer , self.esacpe_value[0])
				if not ret :
					self.game.set_sail(self.runer , self.esacpe_value[-1])
				self.esacpe_counter -= 3
			else :
				self.esacpe = False
		else :

			self.esacpe_counter = 1
			
			
			enemys = self.game.get_enemy_pirates()

			self._Distance += [[enemy.location - self.runer.location for enemy in enemys]]

			if len(self._Distance ) > 8:
				_distance = self._Distance[-5:]


				attack_me = [True for _ in _distance[0]]

				zero = vector.Vector(0,0)

				for e in range(len(_distance[0])):
					prev , an = None , None 
					for v in _distance:
						if not (prev is None) :
							an1 = distanse(v[e] - prev , zero)
							if not (an is None) :				
								if (an1 - an> 0) or distanse(v[e],zero)  > 20:
									attack_me[e] = False
							an = an1
						prev = v[e]

				if not any(attack_me):
					
					if not self.target in self.game.get_not_my_islands(): 
						Move_to_Closer_Island(self.game , self.runer , self)
					else :
						d = self.game.get_directions(self.runer , self.target)
						if len(d) > 0 :
							ret = self.game.set_sail(self.runer , d[0])
							if not ret :
								ret = self.game.set_sail(self.runer , d[-1])
						return	
				else :
					for (i , who_is_attack) in zip([i for i in range(len(attack_me))], attack_me):
						if who_is_attack :
							traget = ooo()
							setattr(traget , 'location' ,self.runer.location - (2*self._Distance[-1][i]))
							d = self.game.get_directions(self.runer ,traget)
							self.esacpe = True
							self.esacpe_value = d
							if len(d) > 0:
								self.game.set_sail(self.runer ,d[0])
							break 


class ooo():
	"""docstring for ooo"""
	def __init__(self):
		pass
		


def Move_to_Closer_Island(game , pirate , runer):
	target= game.get_not_my_islands()[0]
	mini = 1000	
	second = game.get_not_my_islands()[0]

	if target is None :
		return 

	for island in game.get_not_my_islands():
		t = distanse(pirate.location , island.location)
		if t < mini :
			mini = t 
			second = target
			target = island

	if pirate.uniq % 2 == 0:
		target = second

	if target != None :
		d = game.get_directions(pirate, target)
		if len(d) > 0:
			ret = game.set_sail(pirate, d[0])
			runer.target = target	
		
	
def distanse(a,b):
	return abs(a.x-b.x)+abs(a.y-b.y)

