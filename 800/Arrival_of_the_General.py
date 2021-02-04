import sys
number=sys.stdin.readline().strip()
word=list(map(int,sys.stdin.readline().strip().split()))
max_index=word.index(max(word))
min_index=len(word)-1-word[::-1].index(min(word))
if max_index>min_index:
	print(max_index+(len(word)-min_index)-2)
else:
	print(max_index+(len(word)-min_index)-1)
