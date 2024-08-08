# 반올림 - round(숫자, 자리수)
#  -2:십의자리, -1 - 일의자리, 0 - 정수, 1 - 소수점 첫째, 2 - 소수점 둘째
round_v1 = round(2.547,0) # 3
print(round_v1)
round_v2 = round(2.547,1) # 2.5
print(round_v2)
round_v3 = round(1275,-1) # 1280
print(round_v3)

#eval - 문자열 표현수식을 숫자로 변환. int와 float와는 달리 계산식 자체를 바꾸는 것
eval_v = eval('1+2')
print(eval_v)