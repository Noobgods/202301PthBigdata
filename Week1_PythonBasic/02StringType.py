# 문자열 선언
strdec0 = "Python!"
strdec1 = 'Python!'
strdec2 = '''Python!'''

# 이스케이프 코드
'''
\n	    문자열 안에서 줄을 바꿀 때 사용
\t	    문자열 사이에 탭 간격을 줄 때 사용
\\	    문자 \를 그대로 표현할 때 사용
\'	    작은따옴표(')를 그대로 표현할 때 사용
\"	    큰따옴표(")를 그대로 표현할 때 사용
\r	    캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
\f	    폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
\a	    벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b	    백 스페이스
\000	널 문자
'''

# 문자열 연산
## 문자열 연결하기
head = "Hello"
tail = " World!"
head + tail

## 문자열 곱하기 
multi = "Python"
multi * 2

## 문자열 길이
len(multi)


# 문자열 인덱싱과 슬라이싱
indexstr = "Believe in yourself."
print(indexstr[4] + indexstr[9] + indexstr[-1])

print(indexstr[3:4] + indexstr[:-2] + indexstr[7:])
# indexstr[3:4] == (3 <= indexstr < 4)


# 문자열 포맷 코드
'''
%s	    문자열(String)
%c	    문자 1개(character)
%d	    정수(Integer)
%f	    부동소수(floating-point)
%o	    8진수
%x	    16진수
%%	    Literal % (문자 % 자체)
'''

print("I eat %s apples." % "five")     # 한가지
print("I eat %s %s." % ("five", "apples"))

# 문자열 관련 함수들

'''
count   : 문자 개수 세기
find    : 문자열 찾아서 위치 알려주기 (못찾으면 -1)
index   : 문자열 찾아서 위치 알려주기 (못찾으면 error)
join    : 문자열 삽입
upper   : 대문자로 바꾸기
lower   : 소문자로 바꾸기
lstrip  : 왼쪽 공백 지우기
rstrip  : 오른쪽 공백 지우기 
strip   : 양쪽 공백 지우기
replace : 문자열 변경
split   : 문자열 분리
'''