varA="hai"
varB="hello"
if type(varA)==str or type(varB)==str :
	print("strings involved")
elif varA>varB:
	print("bigger")
elif varA==varB:
	print("equal")
else:
	print("smaller")