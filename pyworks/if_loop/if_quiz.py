# 실습 1
# 조건 - 시내에서 자동차의 주행속도가 50km 이상이면 "속도위반입니다."를 출력하고
# 아니면 "규정속도준수!!"

speed = float(input('자동차의 주행속도 :'))
if speed >= 60 :
    print("속도위반입니다. 과태료 10만원 부과")
else :
    print("규정속도준수!! 당신은 좋은 사람!!")
print(f'자동차의 주행속도가 {speed}km입니다.')