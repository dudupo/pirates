from game import Game
from vector import Vector
import engine
class Player:
	def __init__(self,name ,_id):
		self.name=name
		self.id =_id
		self._spawn_area=None
		self._pirates=list()
		if self.id==0:
			self.sign='H'
		elif self.id==1:
			self.sign='X'	
	def _add_pirate(self,pirate):
		pirate.player=self
		self._pirates.append(pirate)
	
	def StartLocation(self):
		return 0 + 0j # just for now 
	
	@property
	def spawn_area(self):
		'returns a list with all spawn posiotins'
		if self._spawn_area==None:
			area=list()
			numopirates=Game.MAX_AMOUNT_OF_PIRATES
			#default base
			if self.id==0:
				base = Vector(0,numopirates)
				for x in range(numopirates):
					area.append(base + Vector(x,-(numopirates-x)))
			elif self.id==1:
				base = Vector(engine.boardsize.x-1,numopirates)
				for x in range(numopirates):
					area.append(base + Vector(-x,-(numopirates-x)))
			return area
		else:
			return self._spawn_area
	@spawn_area.setter
	def spawn_area(self, value):
		if len(value)!=Game.MAX_AMOUNT_OF_PIRATES:
			raise Exception("spawn area must be at the size of the number of pirates")
		self._spawn_area=value
	def __str__(self):
		return self.name