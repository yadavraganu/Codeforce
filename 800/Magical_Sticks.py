import sys
number=int(sys.stdin.readline().strip())
lst=[]
for i in range(0,number):
    number1=int(sys.stdin.readline().strip())
    lst.append((number1+1)//2)
for j in lst:
    print(j)
