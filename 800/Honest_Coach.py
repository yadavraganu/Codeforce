import sys
t=int(sys.stdin.readline().strip())
result=[]
for i in range(0,t):
	athn=int(sys.stdin.readline().strip())
	strn=sorted(map(int,sys.stdin.readline().strip().split()))
	result.append(min([abs(strn[i]-strn[i+1]) for i in range(0,len(strn)-1)])) 
for m in result:
	print(m)
