total=int(input())
balloons=list(map(int,input().split()))
flag=True
if len(balloons)==1:
    flag=True
else:
    for i in range(len(balloons)):
        if balloons[i]!=(sum(balloons)-balloons[i]):
            print(1)
            print(i+1)
            flag=False
            break
        else:
            flag=True

if flag:
    print(-1)