# 구구단 프로그램 구현 - 리스트(이전엔 변수로 출력해봤음)

dan = 2
gugu = [] #구구단의 결과값 저장(2,4...)
for i in range(1,10):
    gugu.append(dan * i)
    print(f'{dan} x {i} = {gugu[i-1]}')
# print(gugu)

print("=" * 20)
# 반복문 구구단(변수에 출력된 for 문)
# for i in range(1,10):
#     print(f'{dan} x {i} = {dan * 1}')

# 구구단 전체 출력
gugudan = []
for i in range(2,10):
    row = []
    for j in range(1,10):
        row.append(i * j)
        print(f'{i} x {j} = {row[j-1]}') #0번 인덱스를 접근(j-1)
    # print(row)
    print() # 한 줄 넣는 것 = 한줄 바꿈
