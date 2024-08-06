# 자리 배치도
# 고객 수 - customer, 좌석 열 - column, 행 - row
# "나머지"가 0일때 행의 수, 0이 아닐때 행의 수 분기 > if 문
customer = int(input("고객 수 입력:"))  #나머지가 있어서 행이 하나 더 늘어나야함
column = int(input("좌석 열 수 입력:"))

if customer % column == 0:
    row = customer // column #몫
else:
    row = customer // column + 1

print(row)

for i in range(0, row):
    for j in range(1, column + 1):
        num = i * column + j
        if num > customer: #15까지 나오고 싶으면
            break
        print(num, end=' ')
    print()