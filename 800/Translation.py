import sys
word=sys.stdin.readline().strip()
word1=sys.stdin.readline().strip()
if word==word1[::-1]:
	print('YES')
else:
	print('NO')