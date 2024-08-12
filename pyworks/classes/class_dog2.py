#인스턴스 변수와 클래스 변수
class Dog :
    # tricks = [] # 전역변수니까 유지해주는 기능 #클래스 변수. 클래스 이름으로 접근
    def __init__(self, name):
        self.name = name
        self.tricks = [] # 인스턴스는 self.가 필요함
        print("생성자 매서드입니다")

    def add_tricks(self, trick):
        self.tricks.append(trick) #무언가 넣을때(셋)는 리턴할 필요가 없다

dog1 = Dog('John')
dog1.add_tricks('몸 뒤집기')
print(dog1.tricks) #파이썬이라 자유롭게 사용가능한 예시
# print(Dog.tricks)

dog2 = Dog('Jerry')
dog2.add_tricks(('죽은척 하기'))
print(dog2.tricks) #파이썬이라 자유롭게 사용가능한 예시
# print(Dog.tricks)