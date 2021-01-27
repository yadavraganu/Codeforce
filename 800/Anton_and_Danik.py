import sys
word=int(sys.stdin.readline().strip())
word1=sys.stdin.readline().strip()
a=d=0
for i in range(0,word):
	if word1[i]=='A':
		a+=1
	else:
		d+=1
if a>d:
   print('Anton')
elif d>a:
    print('Danik')
else:
    print('Friendship')    