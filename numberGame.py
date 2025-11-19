import random

number = random.randint(1,100)
print(f"랜덤숫자: {number}")

## 게임로직
## 1. 컴퓨터가 1~100 사이 숫자를 하나 정함
## 2. 사용자가 숫자를 입력
## 3. 컴퓨터가 힌트 제공 : 높음, 낮음, 정답
## 4. 몇 번만에 맞추는지 카운트

## 1단계 랜덤 함수 생성
answer = random.randint(1,100)
tries = 0
print(answer)

## 2단계 게임루프
while True:
    ## 사용자 입력
    user = int(input("\n 숫자를 입력하세요: "))
    tries += 1

    ## 3단계 정답확인
    if (answer == user):
        print(f"정답! {tries}번만에 맞췄습니다.")
    elif(answer > user):
        print(f"{user}보다 up!")
    else:
        print(f"{user}보다 down!")
