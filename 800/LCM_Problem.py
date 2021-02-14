for i in range(int(input())):
    arr=list(map(int,input().strip().split()))
    x=arr[0]
    y=arr[0]*2
    if y<=arr[1]:
        print(x,y,end=' \n')
    else:
        print('-1 -1')    