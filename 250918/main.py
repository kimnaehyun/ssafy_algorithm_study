import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

homes = []     # 집 좌표 저장
chickens = []  # 치킨집 좌표 저장

# 집과 치킨집 좌표 수집
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

min_total = float('inf')  # 도시 치킨 거리 최소값 초기화
selected = []             # DFS로 선택된 치킨집 조합

# 치킨집 조합 생성
def dfs(start, depth):
    global min_total
    
    # M개의 치킨집 선택 완료
    if depth == M:
        total = 0  # 현재 조합으로 계산한 도시 치킨 거리 합 초기화
        
        # 모든 집에 대해
        for hy, hx in homes:
            dist = float('inf')  # 집에서 가장 가까운 치킨집 거리 초기화
            
            # 선택된 치킨집 중에서 최소 거리 계산
            for cy, cx in selected:
                dist = min(dist, abs(hy - cy) + abs(hx - cx))  
            
            total += dist  # 각 집의 최소 치킨 거리 합산
        
        # 최소 도시 치킨 거리 갱신
        min_total = min(min_total, total)
        return
    
    # 치킨집 선택
    for i in range(start, len(chickens)):
        selected.append(chickens[i])       
        dfs(i + 1, depth + 1)              
        selected.pop()                      

dfs(0, 0)
print(min_total)
