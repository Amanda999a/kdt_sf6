# 파일 읽기 - 기존의 파일의 내용 읽기
# 파일 열기(open()) -> 파일 읽기(read()) -> 파일 종료(close())
# 바로 출력 가능. 변수에 담아서 출력도 가능
f = open("c:/pyfile/file1.txt", "r")

data = f.read()
print(data)

f.close()