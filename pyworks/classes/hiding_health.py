class Health :
    # 생성자에 넣으면 set이 생략될수 있다. p2 = Health("한잔해")에 입력되었으니까
    def __init__(self, name):
        self.__name = name
        self.__hp = 100 #hp 멤버변수 초기화값 100
    def get_name(self):
        return self.__name
    def set_hp(self, hp):
        #제한을 둬야하기 때문에 if로 범위 제안을 둠
        if hp < 0: # 최소값. -5여도 0으로 도출되도록
            hp = 0
        elif hp > 100: #최대값. 105여도 100으로 도출되도록
             hp = 100
        self.__hp = hp
    def get_hp(self):
        return "hp: " +  str(self.__hp) #hp: 문자로 받아야하니까 str 써줘야함
    def exercise(self, hours):
        self.set_hp(self.__hp + hours)
        print("{}시간 운동하다".format(hours)) # ~.format() 텍스트 함수
        # print(f'{hours}시간 운동하다')
    def drink(self, cups):
        self.set_hp(self.__hp - cups)
        print("술을 {0}잔 마시다".format(cups)) #0으로 써도 가능

p1 = Health("나몸짱")
p1.set_hp(90)
p1.exercise(3)
print(f'{p1.get_name()} - {p1.get_hp()}')

p2 = Health("한잔해")
p2.set_hp(80)
p2.drink(4)
print(f'{p2.get_name()} - {p2.get_hp()}')
