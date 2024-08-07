'''

# 학생 3명의 성적 통계. [리스트] 안에 {딕셔너리}를 이용
student = [
    {"name": "이대한", "kor": 90, "math": 85},
    {"name": "박민국", "kor": 80, "math": 75},
    {"name": "윤지능", "kor": 95, "math": 90}
]

# print(student) 출력이 객체방식
# print(student[0])
# print(student[-1]) #통계 낼때 끝에 값 확인하면 좋다

# 개인별 평균 점수
print("♣ 개인별 평균 점수 ♣")
print(" 이름  국어 수학  평균")
# 문자데이터로 나오게 하려고 해서 for문
for std in student:
    sum_score = std["kor"] + std["math"] #개인별 총점
    avg_score = sum_score / 2
    print(f'{std["name"]}  {std["kor"]}  {std["math"]} {avg_score : .2f}')
print()
'''
# 과목별 총점
score = [
    [90, 85],
    [80, 75],
    [95, 90],
]
kor = []
n = len(score)
for i in range(0, n):
    total = score[i][0]
    kor.append(total)
    print(total / 3)
#print(kor)
sum_subject = [0, 0]
avg_subject = [0.0, 0.0]
for i in range(0, n):
    sum_subject[0] += score[i][0]
    sum_subject[1] += score[i][1]
    avg_subject[0] = sum_subject[0] / n
    avg_subject[1] = sum_subject[1] / n

print("♣ 과목별 총점, 평균 ♣")
print("국어 총점:",sum_subject[0])
print("수학 총점:",sum_subject[1])
print("국어 평균:",avg_subject[0])
print("국어 평균:",avg_subject[0])
print("수학 평균:",avg_subject[1])

