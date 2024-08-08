# 지역변수, 매개변수
# 스택구조. 메모리가 나중에 쓰인 total>num2>num1순으로 씀
'''
메모리에서 순서(생성) - 그릇처럼 쌓이는 구조
3. total
2. num2
1. num1
메모리에서 순서(소멸)
1.total 2. num2 3. num1
'''
def calc():
    x = 2 * num1
    print("x =", x)

# 지역 변수
num1 = 10 #전역 변수
num2 = 20
total = num1 + num2
calc()

