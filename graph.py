import sys
import numpy as np

fin = 'graph.txt'
sys.stdin = open(fin, 'r')

fout = 'graph.dot'
sys.stdout = open(fout, 'w')

n = int(input())
hashgraph = []
line = input()
while(line!='Done'):
	line = line.split(' ')
	event = [int(x) if x != 'NULL' else "NULL" for x in line]
	hashgraph.append(event)
	line = input()

print("digraph G{")
arr = np.array(range(n))+1
print("{node[style=filled fillcolor=black fontcolor=white]")
print(*arr)
print("}")
for event in hashgraph:
	A = event[2]
	B = event[3]
	C = event[1]
	if A == "NULL":
		A = event[0]
	if B == "NULL":
		B = event[0]
	
	print("{"+str(A)+" "+str(B)+"} -> "+str(C))
print("rank=same{",*arr,"}")
print("}")


