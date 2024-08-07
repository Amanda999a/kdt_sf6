# return이 있는 함수(반환값이 있음)

# 매개변수 1개 있는 경우
# 자기 자신을 곱하는 함수 - square (제곱수 함수)
def square(x):
    return x * x

#절대값(absolute) - 어떤 수(정수)를 양수로 만드는 함수
def myabs(x):
    if x < 0:
        return -x
    else :
        return x

def mul(x,y):
    return x * y



value = square(6) # return이 준 반환값을 value에 저장
print(value)
# print(square(7)) # value에 저장하지 않아도 값 도출은 가능

print(myabs(-10))



# 파이썬의 절대값 구하는 함수 - abs()
# print(abs(-10)) #10
# print(abs(10)) #10

# 매개변수 2개 호출
value2 = mul(5,2)
print(value2) # print(mul(5,2))




