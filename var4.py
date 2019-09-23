x = 'Global x'

def demo():
	x = 'X in Demo'
	
	def test():
		x = 'X in Test'	
		print(x)
		
	test()
	print(x)
	
demo()
print(x)
