arr=list(map(int,input().strip().split()))
print('Yes') if arr[0]<=min(arr[1],arr[2]) else print('No')