for i in range(int(input())):
    inp=list(map(int,input().split()))
    string=input()
    dx,dy=inp[0],inp[1]
    R=0;L=0;U=0;D=0
    for j in string:
        if j=='R':
            R+=1
        elif j=='L':
            L+=1
        elif j=='U':
            U+=1
        else:
            D+=1
    if ((dx<=0 and L>=abs(dx)) or (dx>=0 and R>=abs(dx))) and ((dy>=0 and U>=abs(dy)) or (dy<=0 and D>=abs(dy))):
        print('YES')
    else:
        print('NO')                
