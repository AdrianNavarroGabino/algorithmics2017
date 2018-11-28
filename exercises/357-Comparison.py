# Comparing two numbers
# Adrián Navarro Gabino

def comparison(a,b):
	if b == 0:
		return False
	elif a == 0:
		return True
	else:
		return comparacion(a-1,b-1)


a = int(input("a: "))
b = int(input("b: "))
print(comparison(a,b))
