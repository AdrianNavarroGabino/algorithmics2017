# {n/k} = {n-1/k-1} + k*{n-1/k}
# Amount of forms you can divide a set of n numbers in k subsets
# Adrián Navarro Gabino

def subset(n,k):
	if k == 1 or k == n:
		return 1
	else:
		return subset(n-1,k-1) + k*subset(n-1,k)

n = int(input("n: "))
k = int(input("k: "))
print(subset(n,k))
