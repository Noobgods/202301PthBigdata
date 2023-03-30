money = True
if money:
    print("택시를 타고 간다.")
else:
    print("걸어간다")

# 콜론을 주의해서 작성할 것!
# C언어는 괄호로 블록을 만들어야 하고, 파이썬은 들여쓰기로 구분함
# if True:
# '''
# 주석 에러
# '''
#     print("첫번째")
#         print("두번째")


# 비교
x = 4
y = 4
3 > 1   # True
x != y  # False
x == y  # True

# 논리
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 포함
1 in [1, 2, 3] 
1 not in [1, 2, 3] 

# 리스트, 튜플, 문자열에 사용
a = [1, 2, 3]
1 in a


# 조건문 내용 무시 pass
x = True
if x:
    pass
else:
    print("패스안함")

# elif
score = 70
if score >= 80:
    print("합격입니다.")
elif score >= 70:
    print("재시험입니다.")
elif score >= 50:
    print("불합격입니다.")
else:
    print("벌칙을 수행하세요.")


# 조건부 표현식
message = "합격" if score >= 60 else "불합격"

