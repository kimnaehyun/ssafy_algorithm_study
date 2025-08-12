# N = int(input())
# stack = []
# for _ in range(N):
#   t = input().split()
#   if t[0] == 'push': stack.append(int(t[1]))
#   elif t[0] == 'top': print(stack[-1]) if stack else print(-1)
#   elif t[0] == 'size': print(len(stack))
#   elif t[0] == 'empty': print(0) if stack else print(1)
#   else: print(stack.pop()) if stack else print(-1)


# 입력 속도 개선 → sys.stdin.readline 사용
import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []

for _ in range(N):
    t = input().split()
    if t[0] == 'push': stack.append(t[1])
    elif t[0] == 'top': result.append(str(stack[-1]) if stack else "-1")
    elif t[0] == 'size': result.append(str(len(stack)))
    elif t[0] == 'empty': result.append("0" if stack else "1")
    else: result.append(str(stack.pop()) if stack else "-1")

# 출력 속도 개선 → 출력 내용을 리스트에 담았다가 한 번에 출력
print("\n".join(result))