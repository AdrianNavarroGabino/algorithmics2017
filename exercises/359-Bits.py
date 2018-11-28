# Digits in a number
# Adrián Navarro Gabino

def bits(n):
	if 0 <= n <= 9:
		return 1
	else:
		return 1 + bits(n//10)

n=int(input())
print(bits(n))
