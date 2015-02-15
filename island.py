import engine
class Island:
	EMPTY_CAP_TIME = 20
	TAKEN_CAP_TIME = EMPTY_CAP_TIME
	
	def __init__(self,posiotin):
		self.__posiotin=posiotin
		self.__owner=None
		self.tried_to_cap_this_turn ={}
		self.capscore={}
		for player in engine.players:
			self.tried_to_cap_this_turn[player]=False
			self.capscore[player]=0
	
	def on_turn_stage(self,stage):
		'this functions is called each time a stage begins'
		
		if stage == engine.turn_stage['cap']:
			#TODO: search all pirates in range and run a _try_cap on them
			pass

	def get_owner(self):
		return self.__owner
	def get_postion(self):
		return self.__posiotin

	def _try_cap(self,pirate):
		if self.__owner==pirate.player:
			pass
		
		elif not tried_to_cap_this_turn[pirate.player]:
			#add score on cap
			for player, score in self.capscore:
				if  player == pirate.player:
					self.capscore[player]+=1
				else:
					self.capscore[player]=0
			#change owner ship
			if self.__owner==None and self.capscore[pirate.player] >= EMPTY_CAP_TIME:
				self.__owner=pirate.player
			elif self.__owner!= None and self.capscore[pirate.player] >=TAKEN_CAP_TIME:
				self.__owner=None
		else:
			pass
		