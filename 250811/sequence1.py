# 테스트케이스를 입력 받을 변수 T 초기화
T = int(input())

# 함수 정의
def sequence1():
    # 수열의 길이를 변수 N에 초기화
    N = int(input())
    # 0과 1로 이루어진 수열을 input()으로 받아 변수 str에 초기화
    str = input()
    # 1이 연속으로 가장 많이 나오는 값을 저장할 big_count 0으로 초기화
    big_count = 0
    # 연속으로 나오는 1의 갯수를 저장 할 count는 변수를 0으로 초기화
    count = 0
    # 문자열을 문자 하나하나 반복
    for s in str:
        # 문자가 '1'인 경우
        if s == '1':
            # count 변수에 1을 증가시켜 재할당
            count +=1
            # big_count 값이 count 값보다 작으면
            if big_count < count:
                # big_count에 count는 값 재할당
                big_count = count
        # s가 '1'이 아닐 경우나 연속된 '1'이 끝나는 경우('0'이 나오는 경우) count를 0으로 다시 재할당 
        else:count = 0
    # 문자열을 반복문으로 모든 문자를 돌아 확인 후 big_count return
    return big_count

# 테스트 케이스만큼 함수를 실행하고 print
for t in range(T):print(f'#{t + 1} {sequence1()}')
        