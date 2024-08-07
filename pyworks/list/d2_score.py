# 학생 5명의 국어, 수학의 총점과 평균 > 5행 2열
score = [
    [80, 70],
    [70, 95],
    [60, 90],
    [50, 75],
    [75, 60]
]

# 개인별 총점과 평균
# 개인별 총점을 저장
# total = 0 #토탈을 주석처리해도 계산 가능 ; 계산식에 포함이 되지 않으니까
students = []
n = len(score) #행이니까 변수에 담을 수 있다
print("총점 평균")
for i in range(0, n):
    # 총점 = 국어점수 + 수학점수
    # total(지역변수)은 필요할 곳(코드블럭)에서 선언(생성)해서 사용
    # 지역변수는 코드블럭을 빠져나올떄 소멸. 전역변수는 해당없음
    total = score[i][0] + score[i][1]
    students.append(total)
    # print(total)
    print(total / 2)

print(students)
# 반 전체 과목별 총점과 평균
# 국어 총점, 수학 총점, 국어 평균, 수학 평균 이 필요 ; 4개의 값이 필요
sum_subject = [0, 0] #국어 총점, 수학 총점 #리스트를 초기화함..?>
avg_subject = [0.0, 0.0] # 국어 평균, 수학 평균
'''아래와 같으나 한줄로 요약해서 리스트로 초기화한다
    sum_kor = 0
    sum_math = 0
    avg_kor = 0.0 # 0으로 해도 가능
    avg_math = 0.0
'''

for i in range(0, n): #0~5까지 돈다
    # sum_subject[0] = sum_subject[0] + score[i][0]
    sum_subject[0] += score[i][0] #국어 총점
    sum_subject[1] += score[i][1] #수학 총점

print("국어 총점:",sum_subject[0])
print("수학 총점:",sum_subject[1])

print()

# 평균 계산
avg_subject[0] = sum_subject[0] / n #국어 평균
avg_subject[1] = sum_subject[1] / n #수학 평균

print("국어 평균:",avg_subject[0])
print("수학 평균:",avg_subject[1])