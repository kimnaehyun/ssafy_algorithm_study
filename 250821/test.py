import sys
import heapq

input = sys.stdin.readline
n = int(input())

arr = []

pq = []

for _ in range(n):
    i = int(input())
    if i:
        heapq.heappush(arr,(abs(i), i))
        heapq.heappush(pq, heapq.heappop(arr))
    else: 
        if len(pq): print(heapq.heappop(pq)[1])
        else: print(0)