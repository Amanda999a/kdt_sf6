# 실습 1
while True:
    try:
        num = int(input("숫자입력 : "))
        break #정수 입력시 반복문 탈출

    except ValueError as e:
        print("정수가 아님! 정수를 입력해주세요!")

print(f'정수 입력 성공 : {num}')

''' 다른 방법
while True:
    try:
        num = int(input("숫자입력 : "))
    except ValueError:
        print("정수가 아님! 정수를 입력해주세요!")
    else :
        print(f'정수 입력 성공 : {num}')
        break
'''