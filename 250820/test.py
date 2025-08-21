# 리스트 사용
N = int(input())

arr = []

for i in range(1, N + 1): arr.append(i)

while arr: 
    print(arr.pop(0), end = ' ')
    if len(arr) > 1:arr.append(arr.pop(0))


# deque 사용
from collections import deque

N = int(input())

deck = deque(i for i in range(1, N + 1))

while deck: 
    print(deck.popleft(), end = ' ')
    if len(deck) > 1: deck.append(deck.popleft())
