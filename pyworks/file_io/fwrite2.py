#입력 받아서 파일 쓰기 - 추가모드를 사용한다

f = open("c:/pyfile/input.txt", "a")

text = input("글자입력 : ")
f.write(text)
f.write('\n')

f.close()