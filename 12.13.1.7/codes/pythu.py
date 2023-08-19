from scipy.stats import bernoulli

x1=bernoulli.rvs(size=10000,p=0.5)
x2=bernoulli.rvs(size=10000,p=0.5)

countI1=0
countF1=0
countI2=0
countF2=0

for i in range(0,10000):
	if (x1[i]==1 and x2[i]!=1) or (x2[i]==1 and x1[i]!=1):
		countF1=countF1+1
		if  (x1[i]==0 and x2[i]!=0) or (x2[i]==0 and x1[i]!=0):
			countI1=countI1+1
	if (x1[i]==0 and x2[i]==0):
		countF2=countF2+1
		if  (x1[i]==1 and x2[i]==1):
			countI2=countI2+1
print(countI1/countF1)
print(countI2/countF2)
