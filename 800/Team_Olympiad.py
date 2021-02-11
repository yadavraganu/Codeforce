import sys
from collections import Counter
number=int(sys.stdin.readline().strip())
skill=list(map(int,sys.stdin.readline().strip().split()))
if len(set(skill))==3:
	team=min(Counter(skill).values())
else:
	team=0
Lst=[]
for k,n in enumerate(skill):
	Lst.append((n,k+1))
one=[]
two=[]
three=[]
for b in Lst:
	if b[0]==1:
		one.append(b[1])
	if b[0]==2:
		two.append(b[1])
	if b[0]==3:
		three.append(b[1])
print(team)
for k in zip(one,two,three):
	print(' '.join(map(str,k)))
