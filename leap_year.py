year = int(input("Please enter a year to calculate leap years between 1600 and the mentioned year:\n"))
ctr=0
for i in range(1600, year+1):
	if ((i%4==0) & (i%100!=0) | (i%400==0)):
		ctr+=1
print("There are",ctr," leap years between 1600 and",year,".")