import sys 
lnr=int(sys.stdin.readline())
vote=[]
for lines in range(lnr):
    sum1=sys.stdin.readline().strip().split(' ')
    sum2=0
    for i in sum1:
        sum2=sum2+int(i)
    vote.append(sum2)
print(len([x for x in vote if x>=2]))