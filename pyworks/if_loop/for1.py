# for 반복문
'''
for i range(시작값, 종료값, 증감값):
    실행문

for i in 리스트:
  실행문
'''
# 초기값이 생략되면 0부터 시작
# 끝값은 실제(끝값-1)임
# 세번째 인자 - 증감값(step)

a = range(10)
print(list(a)) # 0~9까지 - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = range(1,11)
print(list(b)) # 1~10까지 - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = range(1,11,2)
print(list(c))  # 1~10까지 2씩 증가 - [1, 3, 5, 7, 9]

# for문 - 1부터 10까지 출력. 리스트가 아니고 i변수가 변합니다.
'''
for i in range(1, 11):
    print(i, end = " ")
'''
# 1부터 10까지 더하기(합계)
total = 0 #초기값 설정 필요. 합계 저장 변수 - 초기화(보통 0으로 값을 저장)
for i in range(1, 101):
    # total = total + i
    total += i
    print("i =", i, "total =", total) # 디버깅 명령
print(total)
    # print(i, end = " ")





