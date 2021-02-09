import sys
number=int(sys.stdin.readline().strip())
numlist=list(map(int,sys.stdin.readline().strip().split()))
sereja=0
dima=0
i=0
while len(numlist)>0:
	if numlist[0]>numlist[-1]:
		pick=numlist[0]
		numlist.remove(numlist[0])
	else:
		pick=numlist[-1]
		numlist.pop()
	if i%2==0:
		sereja+=pick
	else:
		dima+=pick
	i+=1
print(sereja,dima)
