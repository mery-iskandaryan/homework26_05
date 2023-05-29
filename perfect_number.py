for i in range (1,7):
	sum=0
	for j in range(1,7):
		if ((i%j==0) & (j!=i)):
			sum=sum+j
print(sum)
			