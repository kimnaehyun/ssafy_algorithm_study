import heapq
n = int(input())
arr = []

for _ in range(n): heapq.heappush(arr, int(input()))

all_v = 0

while len(arr) > 1:
  sum_v = heapq.heappop(arr) + heapq.heappop(arr) 
  all_v += sum_v
  heapq.heappush(arr, sum_v)

print(all_v)