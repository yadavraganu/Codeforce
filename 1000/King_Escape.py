n=int(input())
a=input().split()
ax=int(a[0])
ay=int(a[1])
b=input().split()
bx=int(b[0])
by=int(b[1])
c=input().split()
cx=int(c[0])
cy=int(c[1])
qs=0;qt=0
if (ax>bx and ay>by):
    qs=3
elif ax>bx and ay<by:
    qs=2
elif ax<bx and ay>by:
    qs=4
else:
    qs=1
if cx==ax and cy==ay:
    print('NO')
else:                   
    if (ax>cx and ay>cy):
        qt=3
    elif ax>cx and ay<cy:
        qt=2
    elif ax<cx and ay>cy:
        qt=4
    else:
        qt=1 
    if qs==qt and (cx-cy)!=(ax-ay):
        print('YES')
    else:
        print('NO')        