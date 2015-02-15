


mili = 50 
_file = open('out.html' , 'w')
flag = False
counter = -1 

Str = '<!DOCTYPE html><html><head><title>Pirates Game</title><script type="text/javascript">'

End = "</script></head><body><img id='1' src='pirate2.png' style='position:absolute' height='42' width='42'><img id='0' src='pirate.png' style='position:absolute' height='42' width='42'></body></html>"


def Add(pirate):
	global mili
	miliS = str(mili)
	global flag 
	global Str
	global counter
	Java = ""
	if flag :
 		Str = Str[:-len(";} , "+miliS+")")]
	Java +="setTimeout(function(){var x = document.getElementById('"+str(pirate.id)+"');x.style.left = '"+ str(pirate.location.real*10) +"px';x.style.bottom= '" + str(pirate.location.imag*10) +"px'; } , "+miliS+")"
	
	counter += 1

	if not flag:
		flag = True
	Str += Java



def build():
	global mili
	global End
	global _file
	global Str
	global counter

	miliS = str(mili)
	for i in range(counter):
		Str += ";} , "+miliS+")"

	Str += End
	_file.write(Str)


