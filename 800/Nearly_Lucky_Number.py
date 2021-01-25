import sys
inp=sys.stdin.readline().strip()
c=inp.count('4')+inp.count('7')
print('YES') if (c==4 or c==7 )and c!=0 else print('NO')
    