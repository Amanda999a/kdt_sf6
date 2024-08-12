# 실습 3
class Calculator:
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value
        return self.value


class LimitCalculator(Calculator):
    def sub(self, value):
        # self.value -= value
        super().sub(value) #단독 if 일때 위치가 올라가야함
        if self.value < 0 :
            self.value = 0
        return self.value

lc = LimitCalculator()
print(lc.sub(20))
print(lc.sub(90))