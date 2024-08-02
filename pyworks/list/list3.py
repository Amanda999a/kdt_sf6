
my_shop = ["반팔티" 
           "청바지" 
           "이어폰"
           ['무선키보드', '유선키보드']
           ]
# 이어폰을 출력하기
print(my_shop[2])
# '반팔티'를 '긴팔티'로 수정
my_shop[0] = "긴팔티"

print(my_shop[:]) #전체 출력

print(my_shop[3]) #리스트 안의 리스트 출력
print(my_shop[-1]) #리스트 안의 리스트 출력

# 이차원 리스트(행과 열로 구성됨)
print(my_shop[3][0]) # 무선키보드
print(my_shop[3][1]) # 유선키보드

# 여러개 삭제
del my_shop[0:2] #0번과 1번 동시 삭제
print(my_shop)