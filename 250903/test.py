import heapq
n = int(input())
arr = [int(input()) for _ in range(n)]

heapq.heapify(arr) # 리스트를 최소 힙으로 변환

all_v = 0

while len(arr) > 1:
  sum_v = heapq.heappop(arr) + heapq.heappop(arr) 
  all_v += sum_v
  heapq.heappush(arr, sum_v)

print(all_v)