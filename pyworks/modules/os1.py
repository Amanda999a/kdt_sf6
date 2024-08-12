# os 모듈 - 디렉터리, 파일 등의 자원을 제어하는 모드
import os

file_path = os.chdir("c:/KDT_SF6/pyworks/modules") # 디렉터리 경로(외부 라이브러리 연결할때 사용함)

dir = os.popen('dir') # 'dir' 명령으로 열기
print(dir.read())

print(os.listdir(file_path)) #파일들을 리스트로 저장함