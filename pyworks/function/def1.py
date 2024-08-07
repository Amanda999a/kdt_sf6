# 출력
# print("Hello!")
# 함수 위치는 상관없지만 주로 위에 해주는 편
# 인사하는 함수 - greet
# 재사용이 가능한 코드 블럭(조각)
def greet():
    print("안녕!!") # 지역 영역

def greeting(name):
    print("안녕~", name)

def get_gugu(dan):
    for i in range(1,10):
        print(f'{dan} x {i} = {dan * i}')

def add(x, y):
    total = x + y
    print("더하기:", total)

# 메인 영역(메모리에서 실행되는 영역. Run time ; 실행영역)
greet() # 함수 호출. 부르는 순간 메모리에 올라감
greeting("현수") # name = "현수"
greeting("민선") # name = "민선"

#구구단 호출
get_gugu(4) #dan = 4

#더하기 호출
add(10, 11)

