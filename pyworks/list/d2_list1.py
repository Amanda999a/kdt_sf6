# 이차원 리스트 - 리스트 내부에 리스트 있음
# matrix - 행, 열로 이루어짐
d = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(d)
print(type(d))

#인덱싱 - 요소 접근(조회)
print(d[0][0]) #10
print(d[0][1]) #20
print(d[1][0]) #30
print(d[1][1])
print(d[2][0])
print(d[2][1])

# 요소 추가 - 1차원일 경우 extend 2차원은 append로 해도 상관 없음
d.append([70, 80])
print(d)

# 요소 수정
d[0][0] = 90
d[0][1] = 100
print(d)

#요소 삭제 - .pop을 이용하고 행을 찾은 다음 열을 삭제
#

# 리스트의 크기
# a = [1, 2, 3]
# print(len(a))
# for i in range(len(a)): #range일때 a[i]
#     print(a[i])
# 전체 조회(이중 for문 사용해야함)
print(len(d)) #4개 ; [[90, 100], [30], [50, 60], [70, 80]]
print("리스트의 크기(행):", len(d))
print("리스트의 크기(열):", len(d[0]))
print("리스트의 크기(열):", len(d[1]))

# for i in range(len(d)):
#     for j in range (len(d[i])):
#         print(d[i][j], end=" ")
#     print()

# for in 리스트
# 주의 - 요소의 구조(값)가 일치해야한다. 갯수가 맞아야함
for x, y in d:
    print(x, y)
