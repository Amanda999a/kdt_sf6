# 파일쓰기 = 파일을 생성
# 파일 열기(open()) -> 파일 쓰기(write()) -> 파일 종료(close())
# 절대경로(c:/디렉토리/파일) vs 상대경로
# 모드(mode) - 쓰기모드('w'), 읽기모드('r'), 추가모드('a')
# 경로와 모드를 꼭 써줘야함
# 문자(글자)를 쓰기(저장)
# 어떤 내용을 쓰거나 수정할 경우 전에 것은 초기화됨.
f = open("c:/pyfile/file1.txt", "w")

f.write("Hello~ Python\n") #\n은 줄 바꿈
f.write("너무 더워!!\n")
f.write("音樂\n")
# 숫자 저장
# f.write(100)  #TypeError ; 숫자를 바로 넣으면 에러. 문자화 시켜야함
# 계산 결과 변수를 쓰면 저장됨
num = 4 + 5
f.write(f'{num}\n')
f.write(str(num) + '\n')
f.write("100\n")
f.write("10.45")


f.close()



