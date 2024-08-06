# 자료구조 = 딕셔너리(dictionary) ps. 리스트와 연동이 자주 됨
# "치킨" : "닭을 튀긴 요리", key(키):value(값)
# {} 중괄호 사용

#fruits = ['apple', 'banana', 'cherry']
fruits = {
    "apple" : "사과",
    "banana": "바나나",
    "peach" : "복숭아"
}
#접근 = 검색 = 조회
print(fruits["apple"])
#print(frutis["tomato"]) # 검색시에 주의. 에러 발생!!. 해결책 : get

# get()을 이용한 검색
print(fruits.get("banana"))
print(fruits.get("tomato")) #None

# 요소 추가 ps. list는 .append 사용
fruits["strawberry"] = "딸기"
print(fruits)
print(type(fruits)) #dict

# 리스트와 딕셔너리에서는 <생성, 조회, 생성, 삭제> 가능하면 >> 관리

# 요소 수정(변경) update
# 복숭아 > 천도 복숭아로 수정 ; key 여부로 생성과 수정 차이
fruits["peach"] = "천도 복숭아"
print(fruits)

# 요소 삭제 pop
fruits.pop("banana")
print(fruits)

# 키만 반환
print(fruits.keys())

# 값만 반환
print(fruits.values())

# 키와 값 모두 반환
print(fruits.items())

# 키와 값 전체 조회
for key in fruits:
    print(key, ':', fruits[key])

# 딕셔너리 생성
dict1 = {1:'a', 2:'b', 3:'c'}
print(dict1)

# key=4, value='d' 추가
dict1[4] = "d"
print(dict1)

# for문을 사용한 전체 조회(검색) ; 중괄호 말로 값으로 나오는 것
for key in dict1: #dict1.keys()도 가능
    print(f'{key} : {dict1[key]}')

# 요소 수정 - key 3의 값 'k'로 변경
dict1[3] = "k"
print(dict1)

# 요소 삭제 - key 2번 삭제
dict1.pop(2)
print(dict1)

# 빈 딕셔너리 생성
#dict2 = {} #빈 딕셔너리
dict2 = dict()
print(dict2)

dict2["Mike"] = 10
print(dict2)

