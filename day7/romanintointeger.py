#Write a Python class to convert an roman to a number


class integerroman:
	def intoroman(self,s):
		roman_value={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		int_value=0
		for i in range(len(s)):
			if i>0 and roman_value[s[i]]>roman_value[s[i-1]]:
				int_value+=roman_value[s[i]]-2*roman_value[s[i-1]]
			else:
				int_value+=roman_value[s[i]]
		return int_value
a=input("Enter the number")
print(integerroman().intoroman(a))

