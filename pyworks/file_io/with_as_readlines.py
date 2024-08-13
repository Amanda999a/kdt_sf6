
with open('./source/city.txt', 'r') as f:
    #data = f.readlines()
    #data = f.readline().split() # 여러개 중에 서울만 보임(['서울']). 1차원 리스트
    #print(data)

    a = [] # 2차원 빈 리스트
    for i in range(6):
        data = f.readline().split() #.split() 구분기호로 공백을 이용해 요소분리
        a.append(data)
    print(a) #6행 1열 형태

    # 리스트의 요소 출력
    print(a[0]) # ['서울']
    print(a[-1]) # ['대구']
    print(a[0][0]) # 0행0열 #서울
    print(a[-1][0]) # 6행0열 #대구

    #전체 출력
    for i in a:
        print(i)
