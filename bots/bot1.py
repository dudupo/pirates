


x = 0 
c = 0
def do_turn(game):

	global x
	global c 

	c+=1 
	d = {0:'e' , 1 : 'n' , 2: 'w' , 3 : 's'}


	for pirate in game.get_my_pirates():
		game.set_sail(pirate , d[x])
		
	if c % 100 == 0 :
		x += 1
		x %= 4

	# now i understod the problem which you pointed about , 
	# you can see that in clerly in this exmple when the pirates try to- 
	# -turn 'west' . untill i will fix that , don`t run on standart loop- 
	# -as 'for pirate in pirates' . instead of that, try to move the redicals first . 