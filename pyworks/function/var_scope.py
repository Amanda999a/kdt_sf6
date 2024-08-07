# def 만들때 변수의 유효 범위를 설정해야한다.
# 변수의 유효범위(생명주기)
# 전역변수 - 전체에 영향을 미침, 프로그램 종료되면 메모리 소멸
# 지역변수 - 함수나 제어문(if, 반복문) 내에서만 생성되고 소멸

# 상품 가격 = 단위당 가격 * 수량
def get_price():
    price = 4000 * quantity
    return price
#함수는 모아놔야함
def one_up():
    x = 0 # 지역변수, 값을 호출시 반환하고 소멸
    x += 1 # x = x+1
    return x

print(one_up()) #1
# print(one_up()) #초기화가 되서 값이 변하지 않고 1로 계속 산출됨



quantity = 2 # 수량변수에 2 값이 저장 ; 전역변수 - 지역변수에 값을 줌
order_price = get_price()

print(f'{quantity}개에 {order_price}원 입니다.')
# print(price) #선언되지 않는 값이다, 정의되지 않았다 인터프리터인데 알려주니까 컴파일 오류


