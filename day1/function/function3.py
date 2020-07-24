def leap_year(x=365.25):
	if(x % 4) == 0:
		if(x % 100) == 0:
			if(x % 400) == 0:
				print("true")
			else:
				print("false")
		else:
			print("true")
	else:
		print("false")
a=int(input(""))
leap_year(a)

	
