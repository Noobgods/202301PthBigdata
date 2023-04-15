# 객체, 인스턴스, 클래스 차이
# 객체 : 구현할 대상 (이론적인)
# 클래스 : 객체를 구현할 설계도
# 인스턴스 : 구현된 실체 (메모리에 작성되는 기점으로 생성됨)

# 클래스 생성
class Animal:
    pass

# 함수가 있는 클래스
class Dog:
    def cry(self) :
        return "woof"
    
# 인스턴스 생성
jindodog = Dog()
chihuahua = Dog()

# 출력
print(chihuahua.cry())
print(jindodog.cry())

# 변수가 있는 클래스
class Cat:
    bell = False

    def cry(self) :     # 벨이 있으면 딸랑, 없으면 냐옹
        if self.bell == True :
            return "jingle"
        else :
            return "meow"
    
    def setData(self, bell) :   # bell을 설정하는 함수
        self.bell = bell

# 인스턴스 생성
Ragdoll = Cat()
Ragdoll.setData(True)

# 출력
print(Ragdoll.bell)
print(Ragdoll.cry())

# 생성자가 있는 클래스
class Cow:
    milk = False

    def __init__(self, milk):   # 생성자 함수의 이름은 __init__ 으로 
        self.milk = milk
    
    def cry(self) :
        return "moo"
    
    def drink(self) :
        if self.milk :
            return "Taste good."
        else :
            return "No milk"
    
milk_cow = Cow(True)
print(milk_cow.drink())

# :: 복사해서 Inheritance.pt 작성