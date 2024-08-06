# for in 리스트
'''
shop = ['반팔티', '바지', '이어폰', '키보드']

print('바지' in shop) #True
print('손수건' in shop) #False
print('양말' not in shop) #True

#리스트에 마우스 요소 추가
shop.append('마우스')
print(shop[:])

for i in shop:
    print(i)

#리스트에 이어폰 삭제
shop.remove('이어폰')
print(shop[:]) # print(shop[0:])

# 여러개 요소 추가 - 커피, 비스켓 추가
shop.extend(['커피', '비스켓'])
print(shop[:])

for i in shop:
    print(i)


# 리스트의 연산
# 개수(len.) 합계(total+i), 평균(합계/개수), 최대값, 최소값 ; 기본적인 통계
score = [70, 80, 60, 90, 40]

print(f'개수 : {len(score)}')
print(f'합계 : {sum(score)}')
print(f'평균 : {sum(score) / len(score)}')
print(f'최대값 : {max(score)}')
print(f'최소값 : {min(score)}')

# 합계
sum_v = 0
for i in score:
    sum_v += i
print(f'합계 : {sum_v}')

# 최대값
max_v = score[0] #아주 적은 수나 처음 값을 리스트 내에서 설정해줘도 됨 ; 처음값으로 초기화
n = len(score)
for i in range(1, n): #n+1이 아닌 n. 인덱스니까!
    if score[i] > max_v: #값
        max_v = score[i]  #80으로 값이 바뀜 True일때 값이 바뀜
디버깅
i=1 80 > 70, max_v = 80
i=2 60 > 80, max_v = 80(유지)
i=3 90 > 80, max_v = 90
i=4 40 > 90, max_v = 90(유지)

print(f'최대값 : {max_v}')
'''

#최소값
score = [70, 80, 60, 90, 40]
min_v = -99 #매우 작은 값으로 초기화
for i in score: # i - 리스트의 요소
    if i > min_v:
        min_v = i
print(f'최소값 : {min_v}')