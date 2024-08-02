# 리스트 함수

# 추가 - 리스트 .append(), 리스트 .insert()
# 삭제 - 리스트 .pop(), 리스트 .remove()
# 정렬 - 리스트 .sort(), 뒤집기(내림차순 아님) - reverse()
lower = ['b', 'd', 'a', 'c']
# 정렬(오름차순)
lower.sort()
print(lower)

lower.reverse()
print(lower)

'''
# e를 추가하고 싶다  # append 맨 뒤 인덱스로 추가된다
lower.append('e')
print(lower)

# e를 삭제하고 싶다
lower.pop()
print(lower)

# b와 c 사이에 'e' 넣고 싶다
lower.insert(2, 'e')
print(lower)

# c 삭제
lower.remove("c")
print(lower)
'''


