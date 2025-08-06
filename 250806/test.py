# 입력값 저장용 배열
arr = []

# 색종이 갯수
n = int(input())

# 색종이 갯수만큼 반복
for _ in range(n):
  # 색종이의 왼쪽하단의 x좌표와 y 좌표
  x,y = map(int, input().split())
  for i in range(x, x + 10):
    for j in range(y, y + 10):
      # 배열 어펜드
      # 배열 가변이라 해시값이 달라 세트가 중복 제거 불가능
      # 튜플은 불변이라 해시 값이 같아 세트가 중복 제거 가능
      # 튜플 어펜드
      arr.append((i,j))

# 배열을 세트로 변환하여 중복 제거 후 길이 반환
print(len(set(arr)))