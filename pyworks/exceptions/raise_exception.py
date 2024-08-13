# raise exception - 예외 미루기(raise throw 예외 던지기)
# 예외처리를 미루면 호출하는 쪽에서 예외처리를 함


class Animal:
    def breathe(self):
        print("동물이 숨을 쉰다.")

    # 매서드를 구현하지 않고 미뤄둠 = 매서드를 구현하도록 강제함
    def cry(self): # 동물의 울음소리는 다 달라서 미뤄둠.

        raise NotImplementedError
class Dog(Animal):
    def sleep(self):
        print("강아지가 잠을 잔다.")

    def cry(self):
        print("멍~멍~")

dog = Dog()
dog.breathe()
dog.sleep()
dog.cry()

# 고양이 클래스 구현
class Cat(Animal):
    def sleep(self):
        print("고양이가 잠을 잔다.")
    def cry(self):
        print("야옹~앍옹!")

cat = Cat()
cat.breathe()
cat.sleep()
cat.cry()