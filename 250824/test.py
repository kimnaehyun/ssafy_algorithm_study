k = int(input())
bt = list(map(int, input().split()))
levels = [[] for _ in range(k)]


def build(inorder, depth):
    # inorder: 현재 서브트리의 중위순회 결과
    # depth: 현재 트리 깊이

    if not inorder: return  # 더 이상 노드가 없으면 종료

    mid = len(inorder) // 2   # 가운데가 루트
    root = inorder[mid]

    # 레벨별로 저장 (예: levels[depth]에 넣기)
    levels[depth].append(root)

    # 왼쪽, 오른쪽 서브트리 재귀
    build(inorder[:mid], depth + 1)   # 왼쪽
    build(inorder[mid+1:], depth + 1) # 오른쪽


build(bt,0)

for i in levels:
    for j in i:
      print(j, end=' ')
    print()