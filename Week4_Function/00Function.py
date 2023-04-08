def function(x, y):
    return x + y

print(function(3, 4))
# print()도 함수의 종류!

# 위의 함수는 f(x, y) = x + y 이고 f의 이름이 add인 것

# 매개변수가 없는 함수
def welcome():
    return 'hello world!'

# 반환값이 없는 함수
def printAdd(x, y):
    print(f"x + y = {x+y}")

# 당연히 매개변수, 반환값이 둘다 없는 함수도 만들 수 있음.

# 리스트의 합계를 반환하는 함수
def listSum(args):
    sum = 0
    for i in args:
        sum += i
    return sum

tmpList = [1,2,3,4,5,6,7,8,9,10]
print(listSum(tmpList))

tmpList2 = [3,5,7,12,15,2]
print(listSum(tmpList2))

# 변수의 범위
def valRange(arg):
    arg = 7
    return arg

num1 = 20
num2 = valRange(num1)

print(num1)     # 20 출력
print(num2)     # 7 출력
# print(arg)    error!!


# 디폴트 매개 변수
def add(x, y = 7):      # 매개변수의 값을 지정해 놓으면 인수로 전달 생략시 해당 값으로 초기화
    return x + y

add(3) # x = 3, y = 7 을 계산하여 10 반환 


# 함수를 변수에 할당
def add(x, y):
    return x + y

function = add  # function이라는 변수에 add함수를 할당함
print(function(1, 4))   # function을 add함수와 같이 사용


# 람다함수
lambdaFunc = lambda x, y : x + y    # 람다식을 변수에 할당하여 함수로 활용 가능하다.
print(lambdaFunc(1, 7))