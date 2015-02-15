import engine
class Island:
	EMPTY_CAP_TIME = 20
	TAKEN_CAP_TIME = EMPTY_CAP_TIME
	
	def __init__(self,area):
		self.area=area
		self._owner=None
		self.tried_to_cap_this_turn ={}
		self.capscore={}
		for player in engine.players:
			self.tried_to_cap_this_turn[player]=False
			self.capscore[player]=0

	def get_owner(self):
		return self._owner
	def get_postion(self):
		return self.__posiotin

	def _try_cap(self,pirate):
		if self._owner==pirate.player:
			pas
		
		elif not tried_to_cap_this_turn[pirate.player]:
			#add score on cap
			for player, score in self.capscore:
				if  player == pirate.player:
					self.capscore[player]+=1
				else:
					self.capscore[player]=0
			#change owner ship
			if self._owner==None and self.capscore[pirate.player] >= EMPTY_CAP_TIME:
				self._owner=pirate.player
			elif self._owner!= None and self.capscore[pirate.player] >=TAKEN_CAP_TIME:
				self._owner=None
		else:
			pass
		