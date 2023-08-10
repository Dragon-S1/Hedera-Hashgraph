import sys
import numpy as np
import random

args = len(sys.argv)

n = 3
m = 20
type = None

if args > 1:
	n = int(sys.argv[1])
if args > 2:
	m = int(sys.argv[2])
if args > 3:
	type = sys.argv[3]

spare = np.array(range(1000,9999))
curr_event = [None]*n
curr_time = [0]*n
curr_isolated = [False]*n
partition_flag = False
hashgraph = []

curr_m = 0

if type=='isolated' and n>1:
	isolated_num = random.randint(1,n-1)
	isolated_nodes = np.array([0]*n)
	isolated_till = np.array([0]*n)
	isolated_after = np.array([0]*n)
	for i in range(isolated_num):
		isolated_node = random.choice(*np.where(isolated_nodes == 0))
		isolated_nodes[isolated_node] = 1
		isolated_till[isolated_node] = random.randint(int(m/4)+1, m)
		isolated_after[isolated_node] = random.randint(0,int(m/4))
if type=='partition' and n>1:
	partition = np.array([0]*n)
	for i in range(int(n/2)):
		node = random.choice(*np.where(partition==0))
		partition[node]=1
	partition_after = random.randint(0,int(m/4))
	partition_till = random.randint(int(m/2),int(3*m/4))

while(curr_m<m):
		for node in range(0,n):
			create = random.choice([True, False])
			if create and not curr_isolated[node]:
				if curr_event[node] is None:
					span = np.array([node])
				else:
					span = np.array([x for x in range(n) if x != node and not curr_isolated[x]])
					if partition_flag:
						span = np.array([x for x in range(n) if x != node and not curr_isolated[x] and partition[x]==partition[node]])
				gossip_node= random.choice(span)
				event_id = random.choice(range(0,spare.size))
				timestamp = max(curr_time[node], curr_time[gossip_node]) + 1
				event = [gossip_node+1,spare[event_id],curr_event[node],curr_event[gossip_node],timestamp]
				curr_time[gossip_node] = timestamp
				curr_event[gossip_node] = spare[event_id]
				hashgraph.append(event)
				spare = np.delete(spare,event_id)
				curr_m += 1
			if type=='isolated':
				for i in range(n):
					if(m==isolated_after[i]):
						curr_isolated[i] = True
					if(m==isolated_till[i]):
						curr_isolated[i] = False
			if type=='partition':
				if(m==partition_after):
					partition_flag = True
				if(m==partition_till):
					partition_flag = False
			curr_time[node] += 1

fout = 'graph.txt'
sys.stdout = open(fout, 'w')
print(n)
for i in hashgraph:
	print(i[0], i[1], "NULL" if i[2] is None else i[2], "NULL" if i[3] is None else i[3], i[4])
print("Done")