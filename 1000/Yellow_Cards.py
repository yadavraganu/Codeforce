a1=int(input())
a2=int(input())
k1=int(input())
k2=int(input())
n=int(input())
if k1<k2:
    if a1*k1<n:
        print(n-(a1*(k1-1)+a2*(k2-1)) if n-(a1*(k1-1)+a2*(k2-1))>0 else 0 ,a1+(n-(a1*k1))//k2)
    else:
        print(n-(a1*(k1-1)+a2*(k2-1)) if n-(a1*(k1-1)+a2*(k2-1))>0 else 0 ,n//k1)    
else:
    if a2*k2<n:
        print(n-(a1*(k1-1)+a2*(k2-1)) if n-(a1*(k1-1)+a2*(k2-1))>0 else 0,a2+(n-(a2*k2))//k1)
    else:
        print(n-(a1*(k1-1)+a2*(k2-1)) if n-(a1*(k1-1)+a2*(k2-1))>0 else 0,n//k2) 

