## 붕어빵 틀(클래스) : 설계도. 같은 모양의 붕어빵 계속 만들기 가능
## 실제붕어빵(객체) : 틀로 찍어낸 결과물, 각각 개별의 붕어빵으로 나타남

class Dog:
    def __init__(self,name,age): ## 생성자
        self.name=name
        self.age=age
    
    def bark(self):
        print(f"{self.name}:멍멍~")

    def info(self):
        print(f"이름: {self.name}, 나이:{self.age}세")

## 객체 생성(붕어빵 찍어내기)
dog1=Dog("바둑이",3)
dog2=Dog("초코",5)

## 메서드 호출 : 클래스 내부 함수 호출
dog1.bark()
dog1.info()
print()
dog2.bark()
dog2.info()


class Dog: ##클래스 : 설계도
    def __init__(self, name):
        self.name = name
        self.energy = 100

    ## 강아지가 짖을 때마다 -10씩 에너지 감소
    def brak(self): 
        print(f"{self.name}: 멍멍~~")
        self.energy -= 10

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹었습니다.")
        self.energy =100

    def status(self):
        print(f"{self.name}의 에너지:{self.energy}")

my_dog =Dog("흰둥이") ## 객체 == 실제로 만든 것

##내사랑흰둥이
my_dog.status()
my_dog.brak()
my_dog.brak()
my_dog.status()
my_dog.eat()
my_dog.status()