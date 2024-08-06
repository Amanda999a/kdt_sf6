"""
#중첩 for
for i in range(1,5): #i = 1, 2, 3, 4
    for j in range(1,5): #j = 1, 2, 3, 4
        print("가", end='')
    print() # 행바꿈 일어남
'''
i = 1
  j = 1,     가
  j = 2,     가가
  j = 3,     가가가
  j = 4,     가가가가
i = 2
  j = 1,     가
  j = 2,     가가
  j = 3,     가가가
  j = 4,     가가가가
'''
for i in range(1,5): #i = 1, 2, 3, 4
    for j in range(1,5): #j = 1, 2, 3, 4
        print("*", end='')
    print() # 행바꿈 일어남
'''파이썬은 단일 for, 이중 for 둘다 사용가능. 행은 그대로 열만 변화
*
**
***
****
'''
'''
for i in range(1,5): #i = 1, 2, 3, 4 ; 행
    for j in range(1,i + 1): #j = 1, 2, 3, 4 ; 열
        print("*", end='')
    print() # 행바꿈 일어남
'''
'''
****
***
**
*
'''
'''
for i in range(1,5): #i = 1, 2, 3, 4 ; 행
    for j in range(1, 6-i): #j = 1, 2, 3, 4 ; 열
        print("*", end='')
    print() # 행바꿈 일어남
'''
print("=======================================")
print("=" * 20)

# 파이썬의 단일 for
for i in range(1, 5): #행이 4행까지 나온다
    print("*" * i)

print("=" * 20)
for i in range(1, 5): #행이 4행까지 나온다
    print("*" * 5 - i)
    pass
#
'''
   * - 공백문자3개 별이 1개
  **
 ***
****
'''
for i in range(1, 5): #행이 4행까지 나온다
    print(" " * (4-i) + "*" * i) #1행일 때 공백 3개 별1..????

"""
# 숫자가 연속으로 증가하는 알고리즘
for i in range(0,4):
    for j in range(1, 4+1):
        num = i * 4 +j
        if num > 15: #15까지 나오고 싶으면
            break
        print(num, end=' ')
    print()

''' 오늘 공부 통합본. 4의 배수 + 1~4 더함
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''





