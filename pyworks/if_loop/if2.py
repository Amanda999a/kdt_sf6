# 다중 조건문
'''
if 조건1 :
실행문(조건1 참일때)
elif 조건2 :
실행문(조건2 참일때)
else:
실행문(조건1과 조건2가 거짓일때)
'''

'''
age = 30
if age >= 0 and age < 20 : # 0<= age <20 파이썬만 가능
    print("미성년자 입니다.")
elif age >= 20 and age < 30 :
    print("20대 입니다.")
elif age >= 30 and age < 40 :
    print("30대 입니다.")
else :
    print("이제는 중년...")

print(f"나이는 {age}세 입니다.")
'''


#20대에서 성별은 나눈다(성별변수 추가)
# 연령이 20대인 경우 성별이 여이면 "20대 여성입니다"로 출력하고
# 남이면 "20대 남성입니다"로 출력

age = int(input("나이를 입력하세요 : "))

if 0< age < 20 : # 0<= age <20 파이썬만 가능
    print("미성년자 입니다.")
elif age < 30 :
    gender = input("여 or 남으로 입력해주세요 :")
    if gender == "여":
        print("20대 여성입니다.")
    elif gender == "남":  #else : 여도 가능 >>코드는 간결한게 좋음
        print("20대 남성입니다.")
elif age < 40 :
    print("30대 입니다.")
else :
    print("이제는 중년...")

print(f"나이는 {age}세 입니다.")



