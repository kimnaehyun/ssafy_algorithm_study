path = []
# in 탐색 복잡도: O(N)
# vowel = ['a', 'e', 'i', 'o', 'u']

# in 탐색 복잡도: O(N), 메모리 적음
# vowel = ('a', 'e', 'i', 'o', 'u')

# in 탐색 복잡도:	평균 O(1), 최악 O(N)
vowel = {'a', 'e', 'i', 'o', 'u'}

def KFC(lev, start, L, C, arr):
  if lev == L: 
      cnt = 0
      for i in path:
          if i in vowel:
              cnt += 1

      if 1 <= cnt and (L - cnt) >= 2: print(''.join(path))
      return

  for i in range(start, C):
    path.append(arr[i])
    KFC(lev + 1, i + 1, L, C, arr)
    path.pop()


def make_pw():
  L, C = map(int, input().split())
  arr = input().split()
  arr.sort()
  KFC(0, 0, L, C, arr)

make_pw()
