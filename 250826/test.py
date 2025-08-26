from collections import deque

t = int(input())

def printer():
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  q = deque((p, i) for i, p in enumerate(arr))  # (우선순위, 원래 인덱스) 형태로 큐에 저장
  order = 0  # 몇 번째로 인쇄됐는지 카운트

  while q:
      now = q.popleft()
      # 현재 문서보다 우선순위가 큰 문서가 남아있으면 뒤로 보냄
      # any( … ) : 조건이 하나라도 참이면 True
      if any(now[0] < other[0] for other in q):
          q.append(now)
      else:
          # 인쇄
          order += 1
          if now[1] == m:  # 내가 찾는 문서면 출력
              print(order)
              break
          
for _ in range(t):printer()