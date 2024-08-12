# 모듈(module) 불러오기. 항상 상위폴더로 부터 와야함
from classes.class_quiz import Calculator
import sys
# 객체 생성
cal_a = Calculator(4,5)
print(cal_a.add())
print(cal_a.sub())
print(cal_a.mul())
print(cal_a.div())

#Calculator 상속 받기
class MoreCalculator(Calculator):
    #거듭 제곱 계산 기능 추가 (매서드)
    def pow(self):
        return self.n1 ** self.n2

    def div(self):
        try:
            # return self.n1 / self.n2
            super().div()
        except:
            print("0으로 나눌 수 없습니다.")
            sys.exit(0)

mc = MoreCalculator(6,0)
print(mc.add())
print(mc.pow())
print(mc.div())

