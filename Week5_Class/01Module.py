# 모듈에서 함수, 변수, 클래스를 지정해서 포함 가능

#from animal import Dog     # Dog 클래스만 가져옴
from animal import *        # *은 해당 모듈의 함수, 변수, 클래스를 모두 import 해준다.

poodle = Dog(2)             # Dog가 import 되어야한다.
print(poodle.cry())
print(poodle.count)

# Dog만 import 하면 안되고 Cat도 import 되어야한다.
maine_coon = Cat(3)
print(maine_coon.cry())

# import inheritance    # 이와 같이 사용한다면 Dog를 호출할때
# inheritance.Dog() 처럼 사용해야 함.

# 모듈에서 선언되어 있는 변수, 함수도 불러올 수 있다. (import 해야함)
print(chihuahua.cry())