# with open(파일경로, 모드) ~ as 파일객체(클래스에서 배운 개념) 구문
# 자원 누수 방지를 위해 f.close()를 사용하지 않음

try:
    with open("./source/data.txt", "w") as f1:
        f1.write("Hello, World!\n")
        f1.write("폭염이 극성입니다.\n")
        num = "1KB는 %d이다" % 1024
        f1.write(num)

    # 파일 읽기
    with open("./source/data.txt", "r") as f2:
        data = f2.read()
        print(data)
except FileNotFoundError:
    print("File not found")


