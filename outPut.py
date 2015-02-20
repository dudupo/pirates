


_SleepTime = 10
_file = open('out.html' , 'w')
number_of_printis = 0

html_code = ''
end_html_code =''

images_html_code = ""

def init_drawing():
	global images_html_code

	from engine import pirates

	for pirate in pirates:
		images_html_code += "<img id='"+ str(pirate.uniq) + \
		"' src='pirate"+ str(pirate.player.id) \
		+ ".png' style='position:absolute; z-index:1' height='42' width='42'/>"

	from engine import islands

	for island in islands:			
		images_html_code += "<img src='island" + \
		".png' style='position:absolute" + ";left:" +str(island.location.x*7) + "px ;top:" + \
		str(island.location.y*7) + "px' height='42' width='42'/>"

	

	global html_code
	#just html code
	html_code = '<!DOCTYPE html>' +\
		  '<html>' + \
		  	'<head>' + \
		  		'<title>' +'Pirates Game'+'</title>' + \
		  			'<script type="text/javascript">'

	global end_html_code
	end_html_code = "</script>" + \
				"</head>" + \
				"<body>" + \
					 images_html_code + \
				"</body>" + \
				"</html>"



def open_bloack():
	global html_code 
	html_code += "setTimeout(" + \
		"function(){"

	global number_of_printis
	number_of_printis += 1


# called when one of the pirates Change is location
def print_change_pirate_location(pirate):
	global _SleepTime
	global flag 
	global html_code
	_SleepTimeString = str(_SleepTime)

	javascript = ""

	javascript += \
		"var x"+str(pirate.uniq)+" = document.getElementById('"+str(pirate.uniq)+"');"+\
		"x"+str(pirate.uniq)+".style.left = '"+ str(pirate.location.x*7) +"px';"+\
		"x"+str(pirate.uniq)+".style.top= '" + str(pirate.location.y*7) +"px';"
	
	

	html_code += javascript


# close all the function and build the html file .
def build():
	global _SleepTime
	global end_html_code
	global _file
	global html_code
	global number_of_printis

	_SleepTimeString = str(_SleepTime)
	# close all the functions 

	for i in range(number_of_printis):
		html_code += "} , "+ _SleepTimeString +")"

	html_code += end_html_code
	_file.write(html_code)

	_file.close()


