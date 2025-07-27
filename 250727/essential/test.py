n = int(input())

arr = list(map(int, input().split()))

v = int(input())

number = 0

for i in range(n) :
  if arr[i] == v :
    number += 1

print(number)
