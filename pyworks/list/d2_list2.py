# 1차원 리스트의 합계와 평균
'''
a = [1, 2, 3, 4]
total = 0
for i in a:
    # total = total + i
    total += i
print("합계:", total)
print("평균:", total / len(a))
'''

# 2차원 리스트의 합계와 평균
# 옆으로 써도 됨 d = [[1], [2, 3], [4, 5, 6]
d = [
      [1],
      [2, 3],
      [4, 5, 6]
]

# sum_v = 0
# print(len(d)) #행의 개수 이차원은 열 갯수까지해야한다!!!
count = 0
for i in range(len(d)): #행
    for j in range(len(d[i])): #열
        sum_v += sum_v + d[i][j]
        count += 1

'''
  1 = 0 + 1 -- [0][0] count = 1
  3 = 1 + 2 -- [1][0] count = 2
  6 = 3 + 3 -- [1][1] count = 3
'''
print("요소의 개수:", count) #6
print("합계:", sum_v) #21
print("평균:", sum_v / count) #3.5