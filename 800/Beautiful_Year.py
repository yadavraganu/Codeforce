import sys
n=int(sys.stdin.readline().strip())
while n>0:
	n+=1
	if len(set(list(str(n))))==len(str(n)):
		print(n)
		break;
