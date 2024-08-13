# 바이너리 파일(binary file) 읽고 쓰기
# mode : 쓰기('wb'), 읽기('rb')
# 바이너리 기계어(0,1)로 변환하는 함수 -> encode() '암호화'
# 기계어를 텍스트로 변환하는 함수 -> decode() '복호화'
with open("./output/data.bin", "wb") as f:
    txt = "드론이 날아간다."
    # f.write(txt) #TypeError. str -> object
    f.write(txt.encode()) #문자를 코드화(기계어) 하는 함수 - encode()

with open("./output/data.bin", "rb") as f2:
    data = f2.read()
    print(data)
    print(data.decode())