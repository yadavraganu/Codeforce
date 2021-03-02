n=int(input())
arr=list(map(int,input().split()))
arr1=arr.copy()
arr1[arr.index(n)]=1
arr1[arr.index(1)]=n
print(' '.join(list(map(str,arr1))))