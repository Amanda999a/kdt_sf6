# while 반복문
# 초기값, 조건문(종료값), 증감값
i = 0
while i < 5: # 조건문의 범위
    #i = i + 1의 대입연산자
    i += 1
    print("안녕하세요", i)

    '''디버깅
    i = 0, True, 1, 안녕하세요, 1
    i = 1, True, 2, 안녕하세요, 2
    i = 2, True, 3, 안녕하세요, 3
    i = 3, Ture, 4, 안녕하세요, 4
    i = 4, True, 5, 안녕하세요, 5
    i = 5, Flase
    '''