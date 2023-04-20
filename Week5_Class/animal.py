# 부모클래스 Animal
class Animal:
    count = 0
    def __init__(self, count) : # 부모클래스의 생성자. 생성자도 함수이기 때문에 인자를 줄 수 있다.
        self.count = count

    def cry(self):  # 자식클래스 cry()의 원형. 자식클래스에서 메소드 오버라이딩이 일어난다.
        pass

# Animal 자식클래스 Dog
class Dog(Animal):
    def __init__(self, count):
        Animal.__init__(self, count)    # 자식클래스의 생성자에서 부모클래스의 생성자를 호출할 수 있다.

    def cry(self) : # 부모클래스의 cry()는 덮어씌워 실행된다.
        return "woof"

# 아래 두 클래스는 00Class.py 파일의 선언에 생성자를 수정한 것과 같다.
# Animal 자식클래스 Cat
class Cat(Animal):
    bell = False
    def __init__(self, count):
        Animal.__init__(self, count)

    def cry(self) :
        if self.bell == True :
            return "jingle"
        else :
            return "meow"
    
    def setData(self, bell) :
        self.bell = bell

# Animal 자식클래스 Cow
class Cow(Animal):
    milk = False
    def __init__(self, milk, count):
        Animal.__init__(self, count)
        self.milk = milk
    
    def cry(self) :
        return "moo"

# 인스턴스 생성, 초기값 설정
jindodog = Dog(1)
chihuahua = Dog(2)

Ragdoll = Cat(1)
Ragdoll.setData(True)

milk_cow = Cow(True, 7)

# 아래 if문을 추가하면 다른 파일에서 실행하지 않게 된다.
if __name__ == "__main__":
    print(jindodog.cry(), chihuahua.cry(), Ragdoll.cry(), milk_cow.cry())
    print(jindodog.count, chihuahua.count, Ragdoll.count, milk_cow.count)
