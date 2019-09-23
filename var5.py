x = 'Global x'

def demo():
	x = 'X in Demo'

	def test():
		#x = 'X in Test'	
		nonlocal x
		x = x + '2'
		print(x)
		
	test()
	print(x)
	
demo()
print(x)
