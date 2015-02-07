
NUM_OF_TURNS=1000
matrix = None

def init_matrix(matrix,width,hight):
	matrix = [[None]*width]*hight
	return matrix

def get_player_bots():
	'''gets the player bots do_turn function. returns array with the functions and the player instanse
		[(mybot1,032940528),(mybot2,032940528)]
	'''
	pass

def main():
	init_matrix(matrix)
	bots= get_player_bots()
	winner=None
	
	#turn loop
	for turn in range(NUM_OF_TURNS):
		#win check
		if len(bots)==1:
			winner= bots[0][0]
			break
		elif len(bots)<1:
			winner="nobody"
			break
		
		#bot loop
		for (owner ,do_turn) in bots:
			#points check
			if owner.points >=1000:
				winner=owner
			try:
				do_turn()
			except:
				debug( str(owner) + " loses - illigal execution" )
				bots.remove((owner ,do_turn))
		
		#winner check 
		if winner != None:
			break
	print(str(winner)+" wins!")