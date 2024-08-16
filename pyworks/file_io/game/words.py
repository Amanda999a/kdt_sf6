import random
#영어 단어장 만들기
# 경로 - game 폴더에 위치함
# word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'mountain', 'garlic', 'onion', 'potato']

with open("words.txt", 'w') as f:
    words = ['icecream', 'chocolate', 'cake', 'water', 'cup', 'coffee', 'juice','soda']
    for i in words:
        f.write(i + ' ')

# 단어 일기
with open("words.txt", 'r') as f:
    # print(f.read())
    data = f.read().split() #.split(0) : 공백 문자로 구분 -> 리스트로 반환하는 매서드
    # print(data)
    print(random.choice(data))
