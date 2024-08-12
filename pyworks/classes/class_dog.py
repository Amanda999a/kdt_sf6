# 클래스 변수는 값을 공유하고 유지하는 속성이 있고,
# 클래스 이름으로 직접 접근한다(생성자 넣어서 하지 않는다!)
class Dog:
    kind = "진돗개" #클래스 변수 ; 공유함 전역변수 같음
    def __init__(self, name):
        self.name = name #인스턴스 변수
# 객체 생성 - 클래스의 인스턴스 생성
dog1 = Dog("송이") #객체=dog1=인스턴스
dog2 = Dog("백구")

'''
print(dog1.name)
print(dog2.name)
# 사용하지 않음
print(dog1.kind)
print(dog2.kind)
'''
#클래스 이름으로 접근해야함
print(Dog.kind)
#객체 리스트
dogs = [
    Dog('멍이'),
    Dog('해피'),
    Dog('사랑이')
]
#리스트는 포인문으로 출력
for dog in dogs:
    print(dog.name)



#코드볼때 대문자로 써있으면 클래스변수



