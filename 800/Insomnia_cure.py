import sys
k=int(sys.stdin.readline().strip())
l=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
n=int(sys.stdin.readline().strip())
d=int(sys.stdin.readline().strip())

list1=[k,l,m,n,]
lst1=[]
final=0
for i in range(1,d+1):
	final=final+all(i%x for x in list1)
print(d-final)
