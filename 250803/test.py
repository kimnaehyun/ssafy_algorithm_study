# 입력값 저장용 배열
arr = []

# 사용자로부터 10개의 정수를 입력받아 리스트에 저장
for _ in range(10) :
  arr.append(int(input()))

# 배열의 요소들을 42로 나눈 나머지로 변경
for i in range(len(arr)) :
  arr[i] = arr[i] % 42

# 배열을 세트로 변경하여 중복 제거 후 길이 출력
print(len(set(arr)))