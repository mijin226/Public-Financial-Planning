a=10
b=5
result1 =a+b
print(f"{a} + {b} = {result1}")


print("=========================")


## 함수 정의 
## def:함수 정의 / add:함수명 / (a,b):인풋값
def add(a,b):
    result = a+b
    print(f"{a} + {b} = {result1}")

## 함수 호출
add(10,5)
add(5,10)

## 매개변수(parameter): 함수에 정보 전달값
def great(name):
    print(f"안녕하세요, {name}님")
great("user01")
great("user02")


## 여러 개 매개변수
def introduce(name, age):
    print(f"이름 : {name}")
    print(f"나이 : {age}세")

introduce("kim", 22)


## return : 함수 반환값 전달
def add(a,b):
    return a + b
result = add(10,5)
print(result)
print(result * 2)
