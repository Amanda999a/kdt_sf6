#실습1
import random
numbers = []
for i in range(4):
    numbers.append(random.randint(1, 100))
print(numbers)
print()
numbers.sort()
print(numbers)

'''
numbers = []
for i in range(4):
    n = random.randint(1,100)
    numbers.append(n)

numbers.sort() #오름차순
print(numbers)
'''
