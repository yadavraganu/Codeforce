import sys
number=int(sys.stdin.readline().strip())
result=[]
for i in range(0,number):
	lst=[]
	call=sys.stdin.readline().strip()
	distinct=int(list(set(list(call)))[0])
	for i in range(1,distinct+1):
		number=[str(i)*1,str(i)*2,str(i)*3,str(i)*4]
		for j in number:
			if not(len(j)>len(call) and j.find(str(distinct))>=0) :
				lst.append(j)
	a=[len(x) for x in lst]
	result.append(sum(a))
for k in result:
	print(k)
