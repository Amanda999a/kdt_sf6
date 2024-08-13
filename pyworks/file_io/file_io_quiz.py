# 실습 1 구구단
f = open("c:/pyfile/gugudan.txt", "w")
gugudan = []
for i in range(2,10):
    row = []
    for j in range(1,10):
        row.append(i * j)
        f.write(f'{i} x {j} = {row[j-1]}\n' )
    f.write('\n') #단과 단사이 줄바꿈
f.close()


f = open("c:/pyfile/gugudan.txt", "r")
dan = f.read()
print(dan)

f.close()

