# 실습 1
# 합계를 응용. 1부터 사용자가 입력한 수까지 합계

num = int(input("어디까지 계산할까요?:"))
for i in range(1, num):
        # total = total + i
    num += i
    print(num)

#권장 답안
# 조건 : 홀수의 합계
num = int(input("몇까지의 합을 계산할까요? "))
total = 0
for i in range(1, num + 1):
if i % 2 != 0: #홀수인 것만 1,3,5로 더한다
    total += i
print(f'1부터 {num}까지의 합 : {total}')


#실습2
count = int(input('몇 초? :'))
while True:
    count = count - 1
    if count < 1:
        break
    print(count + 1, end=" ")  # 결과값이 가로로
print("발사!!")

#권장 답안
n = int(input('몇 초? :'))
for i in range(n, 0, -1):
        print(i, end=' ')  # 결과값이 가로로
    print('발사!!')


