#실습1
import sys
class Calculator:
    # 생성자 매서드(함수)
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2
    def sub(self):
        return self.n1 - self.n2
    def mul(self):
        return self.n1 * self.n2
    def div(self):
        if self.n2 == 0:
            print("0으로 나눌 수 없음")
            return sys.exit(0)
        else:
            return self.n1 / self.n2


c1 = Calculator(4,2)
print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())



