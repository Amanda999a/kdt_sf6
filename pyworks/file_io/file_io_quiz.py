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
            f.write(f'{name}, {password}')
            f.write('\n')

    except:
    print("파일을 찾을 수 없습니다.")

try:
    with open("./source/member.txt", 'r') as f:
        print(f.read())
except:
    print("파일을 찾을 수 없습니다.")
