# 입력
str = input()

number = input("숫자를 입력하세요 : ")
# 위의 입력 숫자는 숫자형이 아닌 문자열!

print(type(number))

# 이전에 int로 형변환을 해서 사용한 적이 있음.
real_number = int(number)

print(type(real_number))


# 출력
# print 함수는 실행 이전에 str로 변환해줌
# print(real_number) -> print(str(real_number))

# 이어쓰기
print("life""is""too short")
cat_str1 = "life" "is" "too short"
cat_str2 = "life" + "is" + "too short"
tup_str = "life", "is", "too short"

print(cat_str1)     # 이어서 출력
print(cat_str2)     # 이어서 출력
print("life", "is", "too short")    # 띄워서 출력
print(tup_str)  # 튜플로 저장되어 출력

# 구분자
print("save key", "Ctrl", "C", sep = " | ")     # 구분자 (기본값 ' ')

# 출력의 끝
print("save key", end = " | ")      # 출력의 끝을 지정 (기본값 '\n')
print("Ctrl", " C")