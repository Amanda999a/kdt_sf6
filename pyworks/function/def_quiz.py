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


# 실습2

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
def get_price(a):
    if a < 20000:
        return a + 2500
    else:
        return a
print(f'상품1 가격: {get_price(30000)}원')
print(f'상품2 가격: {get_price(15000)}원')
'''

