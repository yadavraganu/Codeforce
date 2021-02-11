import sys
number=int(sys.stdin.readline().strip())
for h in range(0,number):
    number1=int(sys.stdin.readline().strip())
    List1=[0]*number1
    for i in range(1,number1):
        List1[i]=str(i)
        List1[0]=str(number1)
    print(' '.join(List1))        