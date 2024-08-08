
# 생성자(constructor) ; 저절로 내부에서 생성되게 하는 것
#self를 사용해서 표현
# def __init__()
class Car :
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def show_info(self):
        print(f'모델명 : {self.model}, 연식 : {self.year}')
'''
#car_a(인스턴스)는 메모리 힙(heap)을 사용한다
car_a = Car('아이오닉6', 2023) #캡슐화. 객체는 힙에 들어감
car_a.show_info()

car_b = Car("스포티지", 2020)
car_b.show_info()
'''

# 객체 리스트(여러개)
cars = [
    Car("소나타", 2020),
    Car("K5", 2017),
    Car("모닝", 2022),
]
cars[0].show_info() #car 0번 인덱싱
cars[-1].show_info()
print('******승용차 List******')
for car in cars:
    car.show_info()
