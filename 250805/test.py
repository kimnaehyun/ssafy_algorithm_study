# 입력값 저장용 배열
arr = []

# 숫자가 바꾸기거나 할 때를 대시해서 자주 사용된 9를 변수 n에 초기화
n = 9

# 2차원 배열의 최고값을 저장할 변수 max_v 0으로 초기화
max_v = 0

# 2차원 배열의 최고값의 행을 저장할 변수 max_y 0으로 초기화
max_y = 0

# 2차원 배열의 최고값의 열을 저장할 변수 max_x 0으로 초기화
max_x = 0

# n번 만큼 input을 받아 split으로 문자열을 배열로 변환해준 뒤 map 함수로 배열의 각 요소를 정수로 변형하여 배열을 arr 변수에 append 시킨다.
for _ in range(n):
    arr.append(list(map(int,input().split())))
    
# 2차원 배열을 돌며 가장 큰 수와 행, 열을 찾아 재할당한다.
for y in range(n):
    for x in range(n):
        if max_v < arr[y][x] :
            max_v = arr[y][x]
            max_y = y
            max_x = x
            
print(max_v)
print(max_y + 1, max_x + 1)            