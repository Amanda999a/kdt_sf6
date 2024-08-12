# random 모듈
import random
import math

# 랜덤수 출력 - 무작위. (0.0 <= r < 1)
# print(random.random()) # 출력할때마다 다른 값

# 주사위(dice) - 방법 1 매서드 활용하기 파이썬에서만 가능
dice = random.randint(1,6) # 1 ~ 6 사이값
print(dice)

# 주사위 - 방법2 math 필요
dice2 = math.floor(random.random() * 6) + 1 # 0~5.999...에서 나옴 + 0값이 나오기 때문에 임의로 1을 더함
print(dice2)
print()
# 주사위 5번 던지기 - 반복문
for i in range(5): #i가 5번일때 반복해보는 for 구분
    dice = random.randint(1, 6)
    print(dice)
print()
# 랜덤하게 단어 추출하기
words = ['여름', '꽃', '나비', '벌', '나무']
# 방법1 only 파이썬
print(random.choice(words))

# 방법2 인덱스필요. 주의! 리스트이므로 0부터 시작함
idx = math.floor(random.random() * len(words))  # 인덱스되어서 리스트니까 1을 더할 필요 없음
print(idx) #0~5사이에서 값이 추출
print(words[idx])
