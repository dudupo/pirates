


def deptu(enemy_pirates ,Range , K=2 , A=4):
	'''just a brifer name'''
	return divide_enemy_pirates_to_units(enemy_pirates ,Range , K , A)


#		the range is the maximum distance between pirate to the closet for him
#	for shearing same unit.

def divide_enemy_pirates_to_units(enemy_pirates ,Range , K=2 , A=4):
	p = p_genrator()

	sets = list()
	dict_sets = dict()

	divide_and_conquer(enemy_pirates , Range ,p ,sets , dict_sets , K , A)

	return sets , dict_sets	




SOME_UNINTRESTING_CONST = 4
#			sets -> list of units , each set represents a unit . 
# 			K -> the number of partitions which the list will divided to . 
#			A -> (1/A) the size of 'overlap' (as says google translate) area/places 
#		between two partition .
def divide_and_conquer(enemy_pirates , Range , p ,sets , dict_sets , K = 2 , A = 4 ):
	'''main recursion function'''
	
	if len(enemy_pirates) < SOME_UNINTRESTING_CONST:
		make_unit(enemy_pirates ,Range ,sets ,dict_sets)
		return


	_sort(enemy_pirates , p)

	partitions = set_partition(enemy_pirates , K , A)
	for partition in partitions:
		divide_and_conquer(partition , Range ,p ,sets , dict_sets , K , A)
 		
#			stil not final version . in the futhere i will-
#		-implemment it more effective . i have a feeling that if- 
#		-we will save the orginal sorted lists by x and by y , then-
#		.... :)  				
def _sort(enemy_pirates , p):
	_key = next(p)
	enemy_pirates = sorted(enemy_pirates , key = _key)

def set_partition(enemy_pirates , K , A):
	
	step = int( len(enemy_pirates) / K )
	
	#for the 'overlap' places .
	second_step = int ( len(enemy_pirates) / A )
	if second_step == 0:
		second_step = 1
	
	if step < 2 :
		step = 1
		second_step = 1

	steps = range(step , len(enemy_pirates) , step)

	partitions = list()

	start = 0		# steps[:-1] -> exclude last step. 
	for end in steps[:-1]:
		partitions.append(enemy_pirates[start: end + second_step ])
		start = end

	#last partitin | note start equel to the len(...) - step .  
	partitions.append(enemy_pirates[start : start + step])

	return partitions

def p_genrator():
	'genrator which return x , y ,x ,y....'
	
	f = lambda a : a.location.x 
	g = lambda a : a.location.y
	while True:
		yield f
		yield g  

def distance(p1 ,p2):
	return abs(p1.location.x-p2.location.x) + abs(p1.location.y - p2.location.y)

def make_unit(enemy_pirates ,Range ,sets , dict_sets):
	
	if len(enemy_pirates) < 2:
		return


	pirate1 , pirate2 = enemy_pirates[0] ,enemy_pirates[1]


	# when SOME_UNINTRESTING_CONST = 3
	if distance(pirate1 , pirate2) < Range :
		_set1 = None
		_set2 = None
		
		if pirate1 in dict_sets:
			_set1 = dict_sets[pirate1]
			if _set1 in sets:
				sets.remove(_set1)
		else:
			_set1 = { pirate1 }
			dict_sets[pirate1] = _set1

		if pirate2 in dict_sets:
			_set2 = dict_sets[pirate2]
			if _set2 in sets:
				sets.remove(_set2)
		else:
			_set2 = { pirate2 }
			dict_sets[pirate2] = _set2

		# union 
		_set1 |= _set2
		
		# for dict calling
		_set2 = _set1

		sets.append(_set1)

		if len(enemy_pirates) > 2 :
			make_unit(enemy_pirates[1:] ,Range ,sets ,dict_sets)
			make_unit(enemy_pirates[-1:1:-1] ,Range ,sets ,dict_sets)
		return