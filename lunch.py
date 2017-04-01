import random
resultgood=[]
resultbad=[]

for n in range(1000000):
	a=random.randint(0,100001)
	b=random.randint(0,100001)
	result=abs(a-b)
	if result<=25000:
		resultgood.append(result)
	else:
		resultbad.append(result)

good=len(resultgood)
bad=len(resultbad)

print("Good results:",good,"Bad results:",bad)
