#실습1
import random
numbers = []
for i in range(4):
    numbers.append(random.randint(1, 100))
print(numbers)
print()
numbers.sort()
# print(numbers)

'''
numbers = []
for i in range(4):
    n = random.randint(1,100)
    numbers.append(n)

numbers.sort() #오름차순
print(numbers)
'''
print()
print()

#실습2
import random
lotto = []
while len(lotto) < 6: # 0 1 2 3 4 5 까지
    print(len(lotto))
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
'''
for i in range(6):
    print(len(lotto)) # 중복 확인
    n = random.randint(1, 45) # 랜덤요소
    if n not in lotto:  #중복 방지 코드
        lotto.append(n)
'''
lotto.sort() #오름차순
print(lotto)