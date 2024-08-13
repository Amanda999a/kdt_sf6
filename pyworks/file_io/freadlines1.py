# readlines() - 데이터를 리스트로 반환

try:
    f = open("./source/season.txt", "r")

    seasons = f.readlines() # 데이터가 seasons 리스트에 저장됨
    print(seasons)
    print(seasons[1]) #리스트 1번 읽기 #여름
    print(seasons[-1]) #리스트 마지막 읽기 #겨울
    print(seasons[1:3]) #슬라이싱 #[여름, 가을] ; 두개 이상이면 리스트로 묶임

    # 전체 출력
    for season in seasons:
        print(season.strip()) #.strip()은 공백이 인자

    f.close()
except FileNotFoundError as msg:
    # print("파일을 찾을 수 없습니다.")

# 내부의 에러 메시지 보고 싶을떄
    print(msg)