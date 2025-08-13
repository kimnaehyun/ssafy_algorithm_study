import math

N = int(input())
arr = []

# 10진수를 2로 나누어 나머지를 배열에 저장하고, 재귀로 몫을 계속 나눔
# 마지막에 배열을 뒤집어 읽으면 이진수 형태가 됨
def binary_conversion(n):
  if n == 0: return
  arr.append(n % 2)
  binary_conversion(math.floor(n / 2))


binary_conversion(N)

# reversed 내장 함수를 사용하여 배열을 역순으로 변경
# 반환 하는 값이 리스트가 아닌 map처럼 객체라 list로 변경해야 함
# 변경된 배열을 문자열로 만들려면 int형 변수들을 str로 바꿔주어야 함
print(''.join(list(map(str, list(reversed(arr))))))