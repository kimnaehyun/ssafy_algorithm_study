
n = int(input())
arr = list(range(n+1))
if n <= 1 :
  print(n)
else :
    for i in range(n+1) :
      if i <= 1 :
        arr[i] = i
      else :
        arr[i] = arr[i-1] + arr[i-2]
print(arr[-1])