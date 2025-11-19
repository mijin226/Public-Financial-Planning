# fruits는 순서가 있는 리스트로 선언
fruits = ["사과", "바나나", "포도"]

#while index <len(fruits):

for fruit in fruits:
    print(fruit)

#range()숫자 범위 만들기
print()
for i in range(5): ## 0 ~ -1까지
    print(i)

print()
for i in range(1,6):
    print(i)

## 시작 끝 증가값 => 증가값만큼 증가(건너뛰기)
print()
for i in range(0,10,2):
    print(i)


##딕셔너리
user = {"name" : "kim", "age" : 30 }
for key, value in user.items():
    print(f"{key}:{value}")

print("29라인")
for key in user:
    print(key)

print("--값만 필요--")
for value in user.values():
    print(value)



## 구구단 만들기
dan = int(input("몇 단 출력?(1~9단까지)"))

for i in range(1,10):

    result = dan * i 
    print(f"{dan} * {i} = {result}")

