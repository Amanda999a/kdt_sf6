# 클래스의 상속 - 매서드 오버라이딩(재정의)
class Airplane:
    # __init__() 생략해도 기본적으로 작동한다.
    # def __init__(self): # 기본생성자
    #     print("비행기 클래스가 생성되었습니다.")
    def take_off(self):
        print("비행기가 이륙합니다.")
    def fly(self):
        print("비행기가 일반 비행합니다.")
    def land(self):
        print("비행기가 착륙합니다.")
    #객체를 생성해야 메모리에 올라감 ; 힙
'''
air1 = Airplane()
air1.take_off()
air1.fly()
air1.land()
'''


class SuperSonicAirplane(Airplane):
      # 비행모드   1  - NOMAL, 2 - SUPERSONIC   > 상수(숫자를 문자로)
      NOMAL = 1 #클래스 상수(대문자 쓰는게 관례)
      SUPERSONIC = 2

      #멤버 변수 선언 - 비행모드
      def __init__(self):
          self.fly_mode = SuperSonicAirplane.NOMAL


      # 메서드 재정의
      def fly(self):
          if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
              print("비행기가 초음속 비행합니다.")
          else:
              super().fly()  # 매서드 상속때도 super() 사용
              # print("비행기가 일반 비행합니다.")

# 실행 영역
sa = SuperSonicAirplane() #객체(인스턴스) 생성
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SUPERSONIC
sa.fly()
sa.land()
