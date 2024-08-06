#실습 5
input_num = input("숫자 입력:").split(" ")  #문자니까 스플릿 가능
numbers = [] # 숫자를 저장할 리스트
for i in input_num:
    numbers.append(int(i))
print(numbers)
max_v = max(numbers)
print("가장 큰 값:", max_v)
min_v = min(numbers)
print("가장 작은 값:", min_v)
avg = sum(numbers) / len(numbers)
print("나머지 값의 평균:", avg)
'''
# 권장 답안
max_v = max(numbers)
print("가장 큰 값:", max_val)

min_v = min(numbers)
print("가장 작은 값:", min_val
# 3 나머지 값의 평균 구하기
numbers.remove(max_v)
numbers.remove(min_v)
#평균 = 합계 / 개수
avg = sum(numbers) / len(numbers)
print("나머지 값의 평균:", avg)
'''

'''
# sum()
print(sum([1, 2, 3])) #6

# max()
print(max([1, 2, 3])) #3
'''


