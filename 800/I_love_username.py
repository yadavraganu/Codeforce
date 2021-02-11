import sys
number=int(sys.stdin.readline().strip())
array=list(map(int,sys.stdin.readline().strip().split()))
i=0
x=array[:1]
for i in array:
    number-=min(x)<=i<=max(x)
    x+=[i]
print(number)