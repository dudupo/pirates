	

import random 
import vector

class Attacker():
	def __init__(self , game ,attacker):
		self.game = game
		self.attacker = attacker

	def _do_turn(self):
		enemys = self.game.get_enemy_pirates()
		if len(enemys) > 0:
			enemys = [enemy for enemy in enemys if enemy.alive]
		
		if len(enemys) > 0:
			enemy = min(enemys , key = lambda enemy : distanse(self.attacker.location ,enemy.location))
			d= self.game.get_directions(self.attacker ,enemy)
			if len(d) > 0:
				self.game.set_sail(self.attacker , d[0])




class Runer():

	def __init__(self ,game , runer):
		self.esacpe = False
		self.esacpe_value = None
		self.esacpe_counter = 1
		self._Distance = []
		self.runer = runer
		self.game = game
		self.target = None
		self.c = 10
		#if self.game.get_my_pirates()[0].location.x  < 7 :
		#	self.c = -10


	def _esacpe(self):
		
		if self.esacpe_counter > 0 :
			self.game.set_sail(self.runer ,random.choice(self.esacpe_value))
			self.esacpe_counter -= 1
		else :
			self.esacpe = False
			self._do_turn()

	def _do_turn(self ,attack = None):
		
		enemys = self.game.get_enemy_pirates()
		self._Distance += [[enemy.location - self.runer.location for enemy in enemys]]

		if self.esacpe :
			self._esacpe()
		
		else :
			self.esacpe_counter = 1
			

			if len(self._Distance ) > 8:
				_distance = self._Distance[-3:]


				attack_me = [True for _ in _distance[0]]

				zero = vector.Vector(0,0)

				for e in range(len(_distance[0])):
					prev , an = None , None 
					for v in _distance:
						if not (prev is None) :
							an1 = distanse(v[e] - prev , zero)
							if not (an is None) :				
								if (an1 - an > 0) or distanse(v[e],zero)  > 8:
									attack_me[e] = False
							an = an1
						prev = v[e]

				if not any(attack_me):

					flag = (not self.target in self.game.get_not_my_islands()) and \
					len(self.game.get_not_my_islands()) > 0

					if flag: 
						Move_to_Random_Island(self.game , self.runer , self)
					else :
						d = self.game.get_directions(self.runer , self.target)
						if len(d) > 0 :
							ret = self.game.set_sail(self.runer , random.choice(d))
						return	
				else :
					b = False
					v = self.runer.location
					for (i , who_is_attack) in zip([i for i in range(len(attack_me))], attack_me):
						if who_is_attack : 

							m = distanse(self._Distance[-1][i] , zero)
							m = 1000000 / m
							m = int(m)
							v = v -  (self._Distance[-1][i]*m)
							b = True
					if b :
						traget = ooo()
						setattr(traget , 'location' ,v)
						d = self.game.get_directions(self.runer ,traget)
						if len(d) > 0:
							self.esacpe = True
							self.esacpe_value = d
							self.game.set_sail(self.runer ,random.choice(d))
							self.target = None
			else:
				Move_to_Random_Island(self.game ,self.runer , self)

							 


class ooo():
	"""docstring for ooo"""
	def __init__(self):
		pass
		


def Move_to_Random_Island(game , pirate , runer):
	target = list()



	if len(game.get_enemy_islands()) > 0 :
		target+= game.get_enemy_islands()
	if len(game.get_not_my_islands()) > 0:
		target+= game.get_not_my_islands()
	else :
		target+= game.get_my_islands()
	if len(target) > 0 :
		target = random.choice(target)

		d = game.get_directions(pirate, target)
		if len(d) > 0:
			ret = game.set_sail(pirate, random.choice(d))
			runer.target = target	
	



	
def distanse(a,b):
	return abs(a.x-b.x)+abs(a.y-b.y)

