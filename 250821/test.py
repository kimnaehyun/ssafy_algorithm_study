import sys
import heapq

input = sys.stdin.readline
n = int(input())

pq = []

for _ in range(n):
    i = int(input())
    if i:heapq.heappush(pq,(abs(i), i))
    else: 
        if pq: print(heapq.heappop(pq)[1])
        else: print(0)