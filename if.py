weater = "비"

if weater == "비":
    print("우산을 챙기세요")

    ## = vs ==
    ## x=5  =>  할당 => x에 5를 저장
    ## x==5 =>  비교 => x와 5와 같은지 비교

    ## 비교 연산자들
    age = 20

    ## 같다
    if age == 20:
        print("같음")

    ## 다르다
    if age != 25:
        print("나이가 25살이 아님")
    
    ## 크다
    if age>18:
        print("성인")

    ## 작다
    if age < 30:
        print("30살 미만")
        ## 크거나 같다(이상) age>= 
        ## 작거나 같다(이하) age<=


    ##if-else: 둘중 하나
    if weater == "비":
        print("우산 챙겨!")
    else:
        print("좋은 날씨!")


    ## if-elif-else: 여러 조건
    ## 효율적 자원 활용
    score = 85
    if score >= 90:
        print("a등급")
    elif score >=80:
        print("b")
    elif(score >= 70):
        print("c")
    elif(score >= 60):
        print("d")
    else:
        print("F")


    ##논리 연산자
    age = 25
    height = 180

    if age >= 18 and height >= 170:
        print("논리연산자 예시 : 놀이기구 탑승 가능")

    ## or : 하나라도 참이면 참
    day = "토요일"

    if day == "토요일" or day == "일요일":
        print("주말~~!")

    
    ##NOT
    is_raining = False

    if not is_raining:  ##true로 전환
        print("비가 안 와")

##영화관 입장료 계산
print()
age = int(input("나이 입력 : "))
print(age)

if age < 13:
    price = 5000
elif age >= 13 and age < 18:
    price = 8000
elif age >=18 and age < 85:
    price=12000
else :
    price=7000
print(f"나이 {age}세이므로, 입장료 {price}원 입니다.")


