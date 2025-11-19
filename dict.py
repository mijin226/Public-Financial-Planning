## 새파일 : dict.py

name = "Kim"
age = "20"
email = "kim@example.com"

## list

user = ["Kim", 20, "kim@example.com"]

## 배열로 넣으면 찾기 어려움. 접근 방식을 KEY와 VALUE를 씀
## 아래와 같이 이름표를 통해 접근하는 방식임

## Dictionary = Key(이름표)와 Value(값)
user1 = {
    "name":"Kim",
    "age":20,
    "email":"Kim@example.com"
}

user2 = dict(name="Lee", age=25, email="asdf@asdf.com")
empty_dict={}

## 값 가져오기
print(user1["name"])
print(user1["age"])

print()
print(user1.get("name"))
print(user1.get("phone")) ##None 발생
## print(user1["phone"]) ##KeyError발생
print(user1.get("phone","없음")) ##없을 시, 지정값 출력됨

## 모든 키와 값 출력
print()
print(user1.keys()) ## Key의 명칭만 가져옴
print(list(user1.keys()))
print(user1.values()) ## Value 값만 가져옴
print(list(user1.values()))


## 값 추가
print()
user1["city"] = "seoul"
print(user1)

## 값 수정
print()
user1["age"] = 99
print(user1)

## 값 삭제
print()
del user1["city"]
print(user1)

## 값 꺼내기(삭제+리턴)
print()
age11 = user1.pop("age")
print(age11)
print(user1)

## 전체 삭제
print()
user1.clear()
print(user1)


## 중첩 딕셔너리(딕셔너리 내 딕셔너리)
users={
    "user1" : {
        "name" : "Kim",
        "age" : 20
    },
    "user2" : {
        "name":"Lee",
        "age":22
    }
}

print()
print(users["user1"]["name"])
print(users["user2"]["age"])

print()
user={}

##2. 정보 추가
user["name"] = "Kim"
user["age"] = 22
user["city"] = "Seoul"

print(user)
print("이름 : " + user["name"])
#print("나이 : " + user["age"] +"세" )## 문자+숫자 연결 허용치x
print("나이 : " + str(user["age"]) + "세") ## 숫자를 문자로 변환

##f-string
print()
print(f"이름 : {user['name']}")
print(f"나이 : {user['age']}세")

##딕셔너리 만들기
##book =
##    title : 점프투파이썬
##    price : 10000
##    page : 100

##1. 책 제목과 가격 출력
##2. 가격을 20000원으로 변경
##3. pulbisher 정보 추가 : 이지스퍼블리싱
##4. 전체 정보 출력

book = {
    "book1" : {
        "title" : "점프투파이썬",
        "price" : 10000,
        "page" : 100
    }
}
print(f"제목: {book['book1']['title']}")
print(f"가격: {book['book1']['price']}")

book['book1']['price'] = 20000

## 정보 추가
book['book1']["publisher"]="이지스퍼블리싱"

## 전체 정보 출력
print(book)



#집합(set) = 중복 없는 데이터 모음
fruits = {"사과", "바나나", "포도"}
numbers = {1,2,3,3,3}

empty_set = set() # 빈집합 만듦

print(numbers) # 중복제거
print(fruits) #순서 개념 없음
#print(fruits[0])

print(3 in numbers)





## 중복된 값이 있는 리스트
numbers=[1,2,3,3,4,4,5,5,5]

## 집합으로 변환 -> 중복 제거
unique_numbers= list(set(numbers))
print(unique_numbers)