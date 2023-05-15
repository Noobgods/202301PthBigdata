# 목차
> 1. 데이터 분석
> 2. 데이터 분석 시작하기
> 3. 데이터 시작하기   

- - -

# 데이터 분석

데이터 분석이 중요한 이유

데이터 분석 : 유용한 정보를 발견하고 결론까지 유추하거나, 의사 결정을 돕기 위해 데이터를 조사, 정제, 변환, 모델링하는 과정
인공지능을 활용하여 원하는 결과를 얻기 위해선 유의미한 데이터를 모아 학습 시켜야한다.
데이터가 '유의미'해야 중요함. 잘못된 데이터로 학습시키는 경우 잘못된 결과가 나온다.

데이터 과학은 통계학, 데이터 분석, 머신러닝, 데이터 마이닝 등을 아우르는 큰 개념

- - - 
# 코랩
이번 강좌는 구글 코랩을 이용하여 실습한다.

코랩은 주피터 노트북(다양한 프로그래밍 언어로 코드를 작성 및 실행하는 개발 환경)을 구글이 개조해서 제작한 것.
구글에서 기본적으로 제공하는 자원을 이용하여 데이터 분석에 필요한 실행 환경을 구축하지 않아도 실습을 진행할 수 있게 해준다.
(사용자가 직접 패키지를 설치하고 개발 환경을 갖출 수도 있다.)

내용 편집해보기   

쓸만한 단축키   
> Ctrl + M B    : 새로운 코드 셀    
> Ctrl + M D    : 셀 삭제   
> Ctrl + Enter  : 초점이 맞춰진 코드 셀 실행   
> Ctrl + S      : 현재 문서 저장

셀 : 코드 또는 텍스트의 덩어리

csv를 불러 읽어올때 인코딩이 어떻게 되어있는지 확인해야한다.   
한국어 인코딩은 보통 두가지 (UTF-8, EUC-KR)   

<br/>

### pandas
파이썬으로 데이터를 분석할때 사용하는 패키지.   
CSV 파일을 읽어 **데이터 프레임** 이라는  표 형식 데이터로 저장   

시리즈라는 데이터 구조도 있음 시리즈는 데이터 구조에 포함되어 있다.   

> 배열의 예로   
> 1차원 = 시리즈   
> 2차원 = 데이터 프레임   
> 시리즈의 객체 모임 = 데이터 프레임   

첫번째 열 : 인덱스(index)

<br/>

### 데이터 프레임을 CSV 파일로 저장하기 : to_csv() 메서드

데이터 프레임을 csv로 저장하는 메서드   
index도 함께 저장되기 때문에 index_col 매개변수를 사용해 인덱스가 있다고 알려준다.

<br/><br/>

- - -
# 데이터 수집하기

데이터 수집은 API를 이용해 할 수 있다.   
> - API란?   
> 두 프로그램이 서로 대화하기 위한 방법을 정의한 것

HTTP 프로토콜을 사용하는 웹기반 API가 널리 사용됨 (요즘에는 https가 사용되는데 http의 암호화된 버전 http + secure)   

웹 기반 API는 주로 CSV, JSON, XML 형태로 데이터를 전달   

<br/>

- - -
## JSON (Javascript Object Notation)
Javascript를 위해 만들어 졌지만 현재는 범용적인 포맷으로 사용됨(vscode에서도 JSON을 이용하여 설정 할 수 있음)   

딕셔너리와 리스트를 중첩해놓은 구조와 비슷   
키와 값으로 구분되고 콜론으로 연결   
```
{"name" : "데이터 분석"}   #키와 값에 큰따옴표를 사용함
```

JSON 형식으로 파이썬 딕셔너리를 만들어보면 아래와 같다.
```
d = {"name": "데이터 분석"}
print (d['name'])
```

<br/>

### JSON 관련 메서드 사용하기
- json.dumps() : 파이썬의 객체를 json에 맞는 문자열로 바꿀 수 있다.   
```
import json     # json을 파이썬에서 사용하기 위해 패키지 import

d_str = json.dumps(d, ensure_ascii=False)   # 한글을 사용하기 위하여 ensure_ascii 매개변수 False로 지정
print(d_str)        # d_str 출력 (문자열 형식)
print(type(d_str))  # d_str의 타입 출력 (str 타입)
```

<br/>

- json.loads() : JSON 문자열을 파이썬 객체로 변환
```
d2 = json.loads(d_str)
print(d2['name'])   # d2의 'name' 출력
print(type(d2))     # d2의 타입 출력 (dict 타입)

d3_str = '''
{
    "name": "데이터 분석",
    "author": ["홍길동", "김철수"],
    "year": 2002
}
'''
d3 = json.loads(d3_str)
print(d3['author'][1])
```

<br/>

- pandas.read_json() : JSON 문자열을 데이터프레임으로 변환
```
import pandas as pd

pd.read_json({str})         # json 문자열 -> 데이터 프레임
pd.DataFrame({list})        # DataFrame 클래스에 파이썬 리스트를 넣어줌
```

<br/>

- - -

## XML (eXtensible Markup Language)

XML은 HTML과 비슷하지만 HTML과는 달리 XML은 컴퓨터와 사람이 모두 읽고 쓰기 편한 문서 포맷을 위해 고안되었음.

```
<book>  # 부모 
    <{시작태그}> {엘리먼트} <{종료태그}>    # 자식
    <name>데이터 분석</name>
    <author>홍길동</author>
    <year>2022</year>
</book>
```

<br/>

### XML 관련 메서드 사용하기

- fromstring() : XML 문자열을 파이썬 객체로 변환   
```
import xml.etree.ElementTree as et

# {Elements} = et.fromstring({str})

```
fromstring이 반환하는 객체는 Element 클래스 객체이다.
안에 들어있는 엘리먼트를 확인하기 위해선 태그로 호출해야 한다.

<br/>

- findtext() : 자식 엘리먼트 확인   

가장 먼저 book 객체를 리스트로 변환하여 자식 엘리먼트를 구한다.
변환한 리스트에는 각 엘리먼트가 담겨있는데 그 리스트의 각 항목을 변수에 할당하고 text 속성으로 엘리먼트를 출력해야한다.   
그리고 findtext()를 이용해 자식 엘리먼트를 탐색하여 자동으로 텍스트로 반환시킨다.

```
{Element} = {Elements}.findtext('{tagname}')
```

findtext()를 사용하지 않으면 엘리먼트를 순서대로 찾아 변수에 할당해야하기 때문에 안전하지 못하다.

<br/>

- findall() : 여러 개의 자식 엘리먼트 확인
```
for {변수} in {상위 부모 엘리먼트}.findall({가져올 엘리먼트}):
    {부모 엘리먼트의 자식 엘리먼트들을 변수에 대입}
    ...
```

<br/><br/>
