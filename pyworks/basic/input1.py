# 입력함수 - input(문자열)
#name = "jerry" 값을 정해져 있음

#name = input("이름 입력: ")
#print("당신의 이름은" + name + "이군요")

#number = input("숫자 입력: ")
#print(number)
#print(int(number) + 1)

int_num = int(10.5)
print(int_num)
num1 = input("첫번째 수 입력: ")
num2 = input("두번째 수 입력: ")



"""
#오류처리(try ~ except) ; 계산은 안되도 에러 안나게 해줌
# :(콜론) - 코드 블럭({})
# 다음 줄에서 4칸 띄어쓰기(indent)
try:
    실행문(오류가 나올 수 있는 문)
except:
     오류를 처리할 수 있는 구문
"""

try :
    num1 = input("첫번째 수 입력: ")
    num2 = input("두번째 수 입력: ")
    print(int(num1) + int(num2))
except :
    print("정수를 입력해주세요.")




