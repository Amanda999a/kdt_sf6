import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
        'mountain', 'garlic', 'onion', 'potato']

# test 랜덤으로 나오는가
# text = random.choice(word)
# print(text)

n = 1 # 문제 번호(1~10)
input("[타자 게임] 준비되면 엔터!")
start = time.time() # 게임 시작 시간
while n < 11:
    print("문제",n)
    question = random.choice(word)
    print(question) # 단어가 출제
    user = input() # input괄호 안이 비면 유저가 단어를 입력한 값이 적용
    if user == question:
        print("통과!!")
        n += 1 #다음 문제 출제
    else:
        print("오타~, 다시 도전!")
end = time.time() # 게임 종료 시간
et = end - start
print("프로그램 종료되었습니다.")
print(f'타자 시간 : {et : .2f}초')

