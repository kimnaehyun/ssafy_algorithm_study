N, M = map(int, input().split())
used = [0] * (N + 1)
path = []

def KFC(lev):
  # M개의 카드를 뽑는다.
  if lev == M:return print(*path)

  # 카드의 숫자가 1~N까
  for i in range(1, N + 1):
    # 만약 used배열에 기록이 되어있으면
    # 재귀 호출 하지않는다 : 다음 레벨로 탐색하지 않는다
    if used[i] == 1: continue
    used[i] = 1 # 기록
    path.append(i)
    KFC(lev + 1)
    path.pop()
    used[i] = 0  # 지워준다


KFC(0)