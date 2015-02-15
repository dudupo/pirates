from game import Game
class Player:
	def __init__(self,name ,_id):
		self.name=name
		self.id =_id
		self._spawn_area=None
		self.__pirates=list()
	
	def _add_pirate(self,pirate):
		pirate.player=self
		self.__pirates.append(pirate)
	
	def StartLocation(self):
		return 0 + 0j # just for now 
	
	@property
	def spawn_area(self):
		'returns a list with all spawn posiotins'
		if self._spawn_area==None:
			area=list()
			numopirates=Game.MAX_AMOUNT_OF_PIRATES
			#default base 
			base = 0 + (numopirates)*1j 
			for x in range(numopirates):
				area.append(base + x - x*1j)
			return area
		else:
			return self._spawn_area
	@spawn_area.setter
	def spawn_area(self, value):
		if len(value)!=Game.MAX_AMOUNT_OF_PIRATES:
			raise Exception("spawn area must be at the size of the number of pirates")
		self._spawn_area=value
	