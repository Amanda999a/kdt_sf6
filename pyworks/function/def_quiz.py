'''
#실습1
def mul(x, y):
    return x + y
su_v = mul(2,3)

def mul(x, y):
    return x * y
sq_v = mul(2, 2)

print("결과(합)", su_v)
print("결과(곱)", sq_v)

# 권장 답변
def a(x, y):
    if x==y:
        return x * y
    else:
        return x + y
value1 = a(2,2)
print(f'결과(곱): {value1}')

value2 = a(2,3)
print(f'결과(합): {value2}')

'''

# 실습2
'''
def get_price(x, y):
    if x * y < 20000 :
        return (x * y) + 2500
    else :
        return x * y
get_price1 = get_price(10000, 3)
get_price2 = get_price(5000,3)

print(f'상품1 가격: {get_price1}원')
print(f'상품2 가격: {get_price2}원')


def get_price(price, quantitiy):
    order_price = price * quantitiy
    fee = 2500 #배송비
    if order_price < 20000:
        order_price += fee
    else :
        order_price
    return order_price

price1 = get_price(15000,2)
price2 = get_price(5000,3)

# print(f'상품1 가격 : {price1}원')
print(f'상품1 가격  : {format(price1, ',d')}원')
print(f'상품2 가격  : {format(price2, ',d')}원')
'''
'''
def get_price(a):
    if a < 20000:
        return a + 2500
    else:
        return a
print(f'상품1 가격: {get_price(30000)}원')
print(f'상품2 가격: {get_price(15000)}원')
'''
#실습4

'''
def times(v):
    v =
    for i in a range(1,31):
        i * 3
    v2 = []

print(times)

'''
'''
# \n - 줄바꿈, \t- 탭
def get_times(x):
   count = 0
   for i in range(1,31):
    if i % x == 0:
        print(i, end=' ')
        count += 1
   print(f'\n3의 배수의 개수: {count}')

get_times(3)
'''

#실습 3
vending_machine = ['게토레이', '레쓰비', '생수', '게토레이', '이프로', '생수']
def check_machine():  # 남은 음료수를 출력하는 함수
    print("남은 음료수: ", vending_machine)
def is_drink(): # 음료수가 있는지 확인하는 함수
    if drink in vending_machine:
        return True
def add_drink(): # 음료수를 추가하는 함수
    vending_machine.append(drink) # 입력된 drink 추가

def remove_drink(drink): #음료수를 제거하는 함수
    vending_machine.remove(drink)

while True :
    who = input("사용자 종류를 입력하세요: \n1. 소비자 \n2. 주인\n")
    if who =='1':
        drink = input("마시고 싶은 음료?")
        if is_drink():
            print(drink, "드릴께요.")
            remove_drink()
            check_machine()
        else:
            print(f"{drink}는 지금 없네요.")
    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        if todo == '1':
            check_machine()
            drink = input("추가할 음료수? ") 
            add_drink()
            vending_machine.sort()
            print("추가 완료")
            check_machine()
        elif todo == '2':
            print("남은 음료는", vending_machine)
            drink = input("삭제할 음료수? ") #remove_drink
            if is_drink():
                print("삭제완료")
                check_machine()
            else:
                print("음료 없음")
