n=int(input())
arr=sorted(list(map(int,input().split())))
if sum(arr[0:n])!=(sum(arr[n:])):
    print(*arr,sep=' ')
else:
    print('-1')               