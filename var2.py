x = 'Global x'

def demo():
	#y = 'Local Y'
	global x 
	#x = 'Local X'
	x = x + '2'
	print(x)
	
demo()
print(x)
