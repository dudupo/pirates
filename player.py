class Player:
	def __init__(self,name ,_id):
		self.name=name
		self.id =_id
	
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
			for x in xrange(numopirates):
				area.append(base + x - x*1j)
			return area
		else:
			return self._spawn_area
	@spawn_area.setter
	def spawn_area(self, value):
		if len(value)!=Game.MAX_AMOUNT_OF_PIRATES:
			raise Exception("spawn area must be at the size of the number of pirates")
		self._spawn_area=value