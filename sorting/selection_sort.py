# selection sort
a = [64,25,12,22,11]

for i in range(len(a)):
	temp=i
	for j in range(i+1,len(a)):
		if a[temp]>a[j]:
			temp = j
	a[i],a[temp] = a[temp],a[i]

print(a)