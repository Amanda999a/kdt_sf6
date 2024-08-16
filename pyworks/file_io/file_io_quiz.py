# 실습 1 구구단
# f = open("c:/pyfile/gugudan.txt", "w")
# gugudan = []
# for i in range(2,10):
#     row = []
#     for j in range(1,10):
#         row.append(i * j)
#         f.write(f'{i} x {j} = {row[j-1]}\n' )
#     f.write('\n') #단과 단사이 줄바꿈
# f.close()
#
#
# f = open("c:/pyfile/gugudan.txt", "r")
# dan = f.read()
# print(dan)
#
# f.close()

# 실습 2

try :
    with open("./source/member.txt", 'w') as f:
        for i in range(3):
            name = input("이름 : ")
            password = input("비밀번호 :")
            f.write(f'{name} {password}\n')

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
'''

try:
    with open("./source/member.txt", "r") as f:
        member = f.read()
        print(member)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
'''

# 실습 3
# 로그인
name = input('이름 입력 : ')
pw = input('비밀번호 입력 : ')
user = name + " " + pw + "\n"

with open("./source/member.txt", "r") as f:
    member_list = f.readlines()
    #print(member_list)

    #상태 변수 - True/False(ex.토글키)
    sw = False # 상태 초기화 False임 #boolan 가장 작은 자료형을 초기화로 둠
    for member in member_list: #리스트를 순회하면서
        # 파일에 있는 member의 name, pw와 입력한 user의 name, pw가 일치하면
        if member == user:
            sw = True

    if sw : #sw == True:
        print("로그인 성공!")
    else:
        print("로그인 실패!")

