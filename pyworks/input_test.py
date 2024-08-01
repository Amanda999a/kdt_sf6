'''
#실습 1
name = input(f'이름을 입력하세요:')
age = input(f'나이를 입력하세요:')
print(f"안녕하세요! {name}님 ({age})세")
'''

#실습 2
name = input(f'이름을 입력하세요.')
birth = input(f'태어난 년도를 입력하세요.')
year = input(f'올해 년도를 입력하세요.')
age = int(year) - int(birth)

print(f"올해는 {year}년, {name}님의 나이는 {age}세 입니다.")

'''
try:
    name = input("이름ㅇ르 입력하세요."
    bith_year = int(input("태어난 연도를 입력하세요.")
    current_year = int(input("올해 연도를 입력하세요.")
    age = current_year - birth_year
    print(f'올해는 {current_year}
except ValueError:
    print("숫자로 꼭 입력해주세요")
'''
