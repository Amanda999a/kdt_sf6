# 상속(inheritance) - 이미 구현된 class(부모 클래스)를 상속받아서 속성(멤버변수)이나
# 기능(매서드)이 확장되는 클래스(자식 클래스)를 구현하는 특성
# 클래스 이름(상속할 클래스 이름)
class Person:
    def __init__(self, name, age): #set이 여기서 해결됨 get만 생성
        self.name = name
        self.age = age

    def get_name(self):
        return  self.name

    def get_age(self):
        return  self.age

p1 = Person("John", 25)
print(p1.get_name(), p1.get_age())

# Employee가 상속
class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age) # 부모 멤버를 super()로 명시함
        self.id = id #Employee(자신)의 값. 자신의 멤버 초기화
    def get_id(self):
        return self.id

e1 = Employee("Jack", 25, 'Jack4321')
print("이름 : ", e1.get_name())
print("나이 : ", e1.get_age())
print("id : ", e1.get_id())

