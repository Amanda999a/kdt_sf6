# 사원의 사번을 자동 부여

class Employee :
    serial_num = 1000 # 초기화가 안되고 값을 공유하여 누적됨
    def __init__(self, name):
        self.name = name
        Employee.serial_num += 1 #시리얼번호를 1씩 증가시킴
        self.id = Employee.serial_num #시리얼번호를 사원 번호에 저장함

    # __str__() : 객체정보를 출력하는 매서드
    def __str__(self): #show info()와 get 을 쓰는 대신에 자동화. 문자열
        return "사번 : {0}, 이름: {1}".format(self.id, self.name)

emp1 = Employee("최사원")
print(emp1) #객체니까 부를 수없어서 emp1을 부름
emp2 = Employee("정사원")
print(emp2)
emp3 = Employee("박사원")
print(emp3)