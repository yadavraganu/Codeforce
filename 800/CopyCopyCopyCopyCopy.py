import sys
t=int(sys.stdin.readline().strip())
for i in range(0,t):
    len1=int(sys.stdin.readline().strip())
    array=list(map(int,sys.stdin.readline().strip().split()))
    print(len(set(array)))