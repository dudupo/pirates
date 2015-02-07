
NUM_OF_BOTS = 2
NUM_OF_TURNS=1000
matrix = None


#
#	meaby should we replace the matrix to list? (which doesn't contain eampty location)
#
#


import sys
from _do_turn import _do_turn 

def init_matrix(matrix,width,hight):
	matrix = [[None]*width]*hight
	return matrix

def get_player_bots():
	'''gets the player bots do_turn function. returns array with the functions and the player instanse
		[(mybot1,032940528),(mybot2,032940528)]
	'''

	if len(sys.argv) != (NUM_OF_BOTS+1):
		raise Exception("requerie at least " + NUM_OF_BOTS + " bots")

	botsNames = sys.argv[1:]

	bots = (_do_turn(botName) for botName in botsNames)

	bots = [(bot , bot.do_turn) for bot in Bots]
	
	return bots


def main():
	init_matrix(matrix)
	bots= get_player_bots()
	winner=None
	
	#
	#	here will be some call to init emulator(?) .
	#

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