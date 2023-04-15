# 내용 작성중 입니다. 늦어서 죄송합니다... 우선 코드만 봐주세요!


# 목차
> 1. 클래스
> 2. 모듈
> 3. 패키지   
> - 부록 : 표준, 외부 라이브러리

- - -
## 1. 클래스

.   
.   
.   
- - -
## 2. 모듈


.   
.   
.   
- - -
## 3. 패키지


.   
.   
.   
# 표준 라이브러리
## datetime
datetime.date() : 날짜표현 함수

## time : 시간 관련 모듈
time.time() : 현재시간을 실수 형태로 리턴 (70.01.01 0000000)기준 지난시간   
time.localtime(time.time()) : 위의 시간을 연, 월, 일, 시, 분, 초로 바꾸어 출력   
time.asctime(time.localtime(time.time())) : 위의 시간을 알아보기 쉽게 출력   
time.ctime() : 위의 함수 간편하게   
time.strftime() : 시간을 세밀하게 표현   

## math
math.lcm() : 최소공배수   
math.random() : 실수로 난수 생성(실수 0 ~ 1.0)
math.randint() : 정수로 난수 생성(지정한 범위)

## functools
- - -
# 외부 라이브러리
pip : 모듈이나 패키지 쉽게 설치하도록 도와주는 도구

```pip install SomePackage``` : 패키지 설치   
```pip uninstall SomePackage``` : 패키지 삭제   
```pip install SomePackage==1.0.4``` : 특정 버전의 패키지 설치   
```pip install --upgrade SomePackage``` : 패키지 최신버전으로 업데이트   
```pip list``` : 설치되어 있는 패키지 출력
