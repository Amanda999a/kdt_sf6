
class Calculator:
    def __init__(self): #외부에서 안넣습니다
        self.x = 0 #class안에서 self 넣어줘야 멤버로 쓰임

    def add(self, y):
        self.x += y
        return self.x

# sub()매서드 생성
class Calculator:
    def __init__(self):
        self.x = 0 #멤버변수,인스턴스변수(지역변수). 멤버이니까 값이 초기화 되지 않는다

    def add(self, y):
        self.x += y
        return self.x

    def sub(self, y):


c1 = Calculator()
print(c1.x)
print(c1.add(10)) #10은 매개변수로 y로 들어감
print(c1.sub(5))