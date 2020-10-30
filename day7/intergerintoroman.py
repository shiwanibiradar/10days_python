#Write a Python class to convert an integer to a roman numeral


class integerroman:
	def intoroman(self,num):
		val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
		syb=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
		roman_num= ''
		i=0
		while num>0:
			for _ in range(num//val[i]):
				roman_num=roman_num+syb[i]
				num = num-val[i]
			i=i+1
		return roman_num
a=int(input("Enter the number"))
print(integerroman().intoroman(a))

