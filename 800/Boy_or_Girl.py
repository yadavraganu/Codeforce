import sys
n=sys.stdin.readline().strip()
number=len(set(list(n)))
if number%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
