def findGcd(n,m):
	if n==m:
		return n
	else:
		if n>m:
			return findGcd(n-m,m)
		return findGcd(m-n,n)

print(findGcd(14,35))