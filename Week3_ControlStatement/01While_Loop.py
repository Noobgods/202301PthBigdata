x = 0
while x < 10:
    x += 1
    print(f"실행 {x}번.")
    if x == 5:
        print("실행 끝")

# f-string : 기존 포매팅(%, .format함수) 이외에 3.6이상에서 사용할 수 있는 포매팅방법

# X의 값을 1씩 계속 더하다 원할때 종료하는 코드
option = '''
    1. add
    2. exit
'''
select = 0
x = 0
while select != 2:
    print(f"\nx = {x}")
    print(option)
    select = int(input())
    if select == 1:
        x = x + 1
    elif select != 2:
        print("Not on the menu")

# while 문에선 break/continue도 사용할 수 있다.
# break 반복문 빠져나가기
# continue 맨 처음으로 돌아가기
# 무한루프

