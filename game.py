import engine 
from vector import Vector
class Game:
	MAX_AMOUNT_OF_PIRATES=6;
	direaction = {
		"e"  :    Vector(1, 0) , 
		"w"  :    Vector(-1,0),
		"n"  :    Vector(0 ,1),
		"s"  :    Vector(0,-1)   }

	'each player has his own "game" instanse' 
	def __init__(self ,player):
		''' * engine is the phsical world that stores all the ships and islands.
			* player is the instanse that this game belongs to.'''
		self.player = player

	def get_my_pirates(self):
		'returns all of the pirates belonging to that player '
		return  [i for i in self.player._pirates if i in engine.living_pirates]
	def get_my_dead_pirates(self):
		'returns a list with all dead pirates'
		return [i for i in self.player._pirates if i in engine.dead_pirates]
	def get_enemy_pirates(self):
		'returns all the enemy pirates'
		enemy= list()
		for player in engine.players:
			if player != self.player:
				enemy+=player._pirates
		return enemy
	def get_islands(self):
		'returns all islands'
		return engine.islands
	def get_my_islands(self):
		'returns all of the islands that belong to this player'
		return [i for i in engine.islands if i.get_owner() == self.player]
	def get_not_my_islands(self):
		'returns all of the islands that do not belong to this players'
		return [i for i in engine.islands if i.get_owner() != self.player]
	def set_sail(self,pirate,direaction):
		if not isinstance(direaction, Vector):
			direaction=Game.direaction[direaction]
		engine.tasks.append(('MOVE',pirate,direaction))
		

	def get_directions(self,obja,objb):
		toret=list()
		if obja.location.y > objb.location.y:
			toret.append('s')
		if obja.location.y < objb.location.y:
			toret.append('n')
		if obja.location.x > objb.location.x:
			toret.append('w')
		if obja.location.x < objb.location.x:
			toret.append('e')
		for dire in toret:
			for p in engine.pirates:
				if obja.location+Game.direaction[dire]==p.location:
					toret.remove(dire)
		return toret
