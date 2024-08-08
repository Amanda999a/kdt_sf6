# 재귀함수 - 자기 자신을 호출하는 함수

def sos(n):
    print("Help Me!!")
    if n == 1:
        return ""
    else:
        return sos(n-1)
sos(5)

'''
sos(5)
  n = 5, Help Me!!
sos(4)
  n = 4, Help Me!!
sos(3)
  n = 3, Help Me!!
sos(2)
  n = 2, Help Me!!
sos(1)
  n = 1, Help Me!!
'''

# 팩토리얼 계산할 때 재귀함수 사용 하는 방법
# 종료 조건을 충분히 작아야 함
# 패턴이 있을때 사용가능
def facto(n):
    if n == 1:
        return 1
    else :
        return n * facto(n-1)
print(facto(4)) # 24

'''디버깅
  4!(팩토리얼) =4 * 3 * 2 * 1 
  4! = 4 * (4-1)!  # n! = n * (n-1)!
  3! = 3 * (3-1)!
  2! = 2 * (2-1)!
'''


# 피보나치 수열 1 1 2 3 5 8 13