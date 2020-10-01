#program for css colour code identification


import re
for _ in range(int(input())):
	line=input()
	z=re.findall(r'.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})',line)
	if z:
		print(*z,sep="\n")
