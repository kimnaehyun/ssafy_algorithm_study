def snake_bird():
    N, L = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    
    for i in h:
        if L >= i : L += 1
        
    return L

print(snake_bird())