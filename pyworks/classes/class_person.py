# 정보은닉(보안을 유지하기 위해 접근을 허용하지 않음
# 접근 제어자 - public(기본), private, protected (접근 제어 키워드 C++에서 자세히 다룸)
# 외부로 기록하지 않고 내부적으로 작동함
class Person :
    # 언더스코어(__) 2개를 쓰면 접근할 수 없음
    def __init__(self):
        self._name = ""
        self._age = 0
    # get, set 매서드를 만들어서 접근
    # set - 입력, get - 출력
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
#실행영역
p1 = Person()
# set, get 호출
p1.set_name("Jerry")
print(p1.get_name())
p1.set_age(20)
print(p1.get_age())

