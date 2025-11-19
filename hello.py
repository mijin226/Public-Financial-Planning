print("===주석===")
## 자신을 위해서
## x = price * 1.1 #10% 할인 적용

## 협업 위해서
## verify_token() #결제 API 호출 전 반드시 인증 토큰 확인 필요

# 나쁜 주석 
# 단순히 눈으로 보아도 알정도 수준의 코드를 해석해두는 것

num1 = 256
num2 = 8 
share = num1%num2
##print(share)

userName = "다영희"
totalPrice = 10000
noteBook = "노트북"

# 일을 혼자하지 않음
# 일관성...

## 일괄성
    ## 가독성 향상 / 협업 효율성 /

fruits=["사과","바나나","메론"]
fruits.append("귤") ##귤 추가
print(fruits)       ## 배열리스트 출력
print(len(fruits))  ## 과일 개수
print(fruits[0])    ##0번째 ㅣ인덱스 0번째 수(사과)
print(fruits[-1])   ##마지막 과일(귤)

##  슬라이싱 : 여러 개를 잘라내기
print(fruits[1:11])
print(fruits[0:3])

fruits[1] = fruits
print(fruits)

fruits. insert(1, "망고")
print(fruits)

##//마지막 값 꺼내서 삭제 + 리턴값 사용하기
print()
last= fruits.pop()
print(last)
print(fruits)