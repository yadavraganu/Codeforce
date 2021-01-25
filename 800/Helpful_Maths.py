import sys 
a=sys.stdin.readline().strip()
b=sorted(a.split('+'))
print('+'.join(b))