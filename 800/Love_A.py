import sys
n=sys.stdin.readline().strip()
c=n.count('a')
req_len=c*2-1
l=len(n)
if req_len<l:
	print(req_len)
else:
	print(l)
