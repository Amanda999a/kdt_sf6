
score = [10, 20, 30, 40, 80]
# 인덱싱 : 특정한 한 개 요소에 접근
print(score[2])

# 슬라이싱 : 여러개 요소에 접근(콜론(:)을 사용하고, 최종값-1한 인덱스가 출력)
print(score[0:3]) #처음부터 2번 인덱스 까지 접근
print(score[:3])
print(score[3:]) #3번 인덱스 부터 끝까지 접근
print(score[:]) #전 요소 접근



'''
# 요소를 수정하는 방법
score[1] = 50 # 20 > 50
# 요소 삭제하는 방법
del score[2]

print(score) #전체 출력
'''