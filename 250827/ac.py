from collections import deque

t = int(input())
def ac(): 
  p = list(input())
  n = int(input())
  s = input()
  if s == '[]':
      arr = deque()
  else:
      arr = deque(map(int, s[1:-1].split(",")))

  revers = False
  for i in p:
    if i == 'R': revers = not revers
    else:
      if not arr: return 'error'
      # reverse가 True면 배열을 reversed 해서 poleft를 해야 하는데 그럴 필요 없이 뒤에 걸 빼준다.
      if revers:arr.pop()
      # 아니면 원래대로 앞에 걸 뺀다.
      else: arr.popleft()
  # 마지막에 reverse를 해도 앞에서 뺄걸 뒤에서 뺏으니까 마지막에 한번만 reverse하면 된다.
  if revers: arr.reverse()
  # 덱을 리스트로 바로 반환하니까 계속 틀려서 문자열로 바꿔서 반환
  return "[" + ",".join(map(str, arr)) + "]"


for _ in range(t): print(ac()) 