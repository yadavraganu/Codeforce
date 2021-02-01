import sys 
a=sys.stdin.readline()
s=sys.stdin.readline().split(' ')
n,k=int(a.split(' ')[0]),int(a.split(' ')[1])
i=0
for j in range(n):
    if int(s[j])>=int(s[k-1]) and int(s[j])>0:
        i+=1  
print(i)