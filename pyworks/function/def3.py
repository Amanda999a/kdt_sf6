#1부터 n까지 곱하는 함수
def gob_n(n):
    gob_v = 1 #합계와 다르게 초기값이 1이어야한다
    for i in range(1, n + 1): #n + 1 해줘야함
        # gob_v = gob_v * i
        gob_v *= i
    return gob_v

'''디버깅
  i = 1  1 = 1 * 1
  i = 2  2 = 1 * 1
  i = 3  6 = 2 * 3
  i = 3  24 = 6 * 4
  
  4!(팩토리얼) =4 * 3 * 2 * 1 
  4! = 4 * 3! #n! = n * (n-1)!
  3! = 3 * 2!
  
'''
# print("결과값 :", gob_v)

print(gob_n(10))
