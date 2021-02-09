import sys
t=int(sys.stdin.readline().strip())
result=[]
for i in range(0,t):
	num=int(sys.stdin.readline().strip())
	num_split=num//2
	sum_odd=num_split**2
	sum_even=num_split*(num_split+1)
	if num%4==0:
		even=[]
		odd=[]
		for q in range(1,num+1):
			if q%2==0:
				even.append(q)
			else:
				odd.append(q)
		odd[-1]=odd[-1]+abs(sum_odd-sum_even)
		result.append('YES')
		result.append(' '.join(map(str,even+odd)))
	else:
		result.append('NO')
for k in result:
	print(k)
