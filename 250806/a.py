x,y = map(int, input().split())
arr = []
for i in range(x, x + 10):
  for j in range(y, y + 10):
    arr.append([i,j])

print(len(arr))