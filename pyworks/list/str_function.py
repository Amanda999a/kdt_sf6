'''
유용한 문자열 함수
전체 개수 - len(), 특정한 문자 개수 - 문자열.count(),
대문자 변환 - 문자열.upper(), 소문자 변환 - 문자열.lower()
문자열을 잘라서 리스트로 반환 - 문자열.split(구분기호)
특정한 문자를 변경 - replace(old, new)
'''

f = "바나나"
print(len(f))
print(len("banana"))

print("banana".count("a")) #"대상" .count("특정한 문자")

upper_case = "Hello".upper()
print(upper_case)
lower_case = "Hello" .lower()
print(lower_case)
print(upper_case, lower_case)

friends = "존 루나 제리"
a = friends.split(" ")
print(a) #구분문자 - 공백 문자

#입력 받아서 리스트 만들기
input_num = input("숫자 입력:").split(" ")  #문자니까 스플릿 가능
numbers = [] # 숫자를 저장할 리스트
for i in input(input_num):
    numbers.append(int(i))1
print(numbers)

print("=" * 20 )

alpha = "a:b:c:d"
print(alpha.split(":"))

email = "codingOn@spreatics.com"
print(email.split("@"))

# replace()
msg = "Hello Python"
print(msg.replace("Python","C++"))