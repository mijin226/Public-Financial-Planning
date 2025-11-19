## while 조건

## 반복 코드 진행, 조건, 증감요소, 종료시점명시 필요

count = 1
while count <= 5:
    print(f"{count}번째 안녕하세요.")
    count = count + 1

    print("END")

count = 0
while count < 5:
    count += 1
    if count ==3:
        print(f"{count}이 되었으니 종료")
        break
    print(count)

count = 0
while count < 5:
    count += 1

    if count ==3:
        continue

    print(count)