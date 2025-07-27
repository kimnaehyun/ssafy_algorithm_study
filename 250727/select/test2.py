T = list(filter(lambda x: int(x) % 2 != 0 ,input().split()))
T1 = sorted(list(map(lambda x : int(x) ** 2, T)))
print(*T1)