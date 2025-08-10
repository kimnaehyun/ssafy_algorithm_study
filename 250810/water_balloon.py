# 테스트케이스를 입력 받을 변수 T 초기화
T = int(input())

# 함수 정의
def water_ballon():

  # 물풍선이 홀수에 떨어질때 방향 변수 초기화
  dy = [-1, 1, 0, 0]
  dx = [0, 0, -1, 1]
  # 물풍선이 짝수에 떨어질때 방향 변수 초기화
  dy2 = [-2, 2, 0, 0]
  dx2 = [0, 0, -2, 2]
  
  # 배열의 크기(가로X세로)를 입력 받을 변수 N 초기화 
  N = int(input())

  # 배열의 저장할 값들을 리스트컴프리헨션을 사용하여 변수 arr 초기화
  arr = [list(map(int, input().split())) for _ in range(N)]

  # 뭂풍선이 떨어진 곳 중에 가장 큰 값을 저장할 변수 max_total을 0으로 초기화
  max_total = 0

  # 가로(행) 길이만큼 반복
  for y in range(N):
    # 세로(열) 길이 만큼 반복
    for x in range(N):
        # max_total의 값을 찾기 전에 풍선이 떨어지는 각각의 곳의 합산 값을 알기 위해 변수 total을 arr[y][x] 자기 자신(좌표)으로 초기화
        total = arr[y][x]
        # 상하좌우 모든 방향의 값들을 모두 더하기 위해 4번 반복
        for i in range(4):
          # 물풍선이 떨어지는 좌표가 홀수 일떄
          if arr[y][x] % 2 != 0:
            # 행 구하기
            ny = y + dy[i]
            # 열 구하기
            nx = x + dx[i]
            # 행과 열이 0보다 적거나 배열의 범위를 벗어 날 경우 continue
            if ny < 0 or ny >= N or nx < 0 or nx >= N:continue
            # 범위를 벗어나지 않은 행과열을 사용하여 total에 값을 더하여 재할당한다.
            total += arr[ny][nx]
          # 홀수가 아닐때 (짝수일때)
          else:
            ny2 = y + dy2[i]
            nx2 = x + dx2[i] 
            if ny2 < 0 or ny2 >= N or nx2 < 0 or nx2 >= N:continue
            total += arr[ny2][nx2]
        # max_total 값이 total 값보다 작을경우 max_total 값을 total 값으로 재할당한다.
        if max_total < total:
          max_total = total
  # 최종적으로 가장 큰 값이 저장된 변수 max_total을 가장 위의 반복문이 끝나고 return으로 반환한다.
  return max_total

# 변수로 받은 T만큼 함수를 반복하여 출력사항대로 출력한다.
for t in range(T):
  print(f'#{t + 1} {water_ballon()}')