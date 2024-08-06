'''
# 다중 if 실습
score = float(input(f'점수 입력 :'))
if score >= 90 and score <= 100 :
    print('A 등급입니다.')
elif score >= 80 and score < 90 :
    print('B 등급입니다.')
elif score >= 70 and score < 80 :
    print('C 등급입니다.')
elif score >= 60 and score < 70 :
    print('D 등급입니다.')
else :
    print('E 등급입니다.')
print(f'당신의 점수는 {score}점입니다.')
'''
# else : score >= 0 and score <60 : 는 왜 안되는지 궁금합니다!

#권장 답안
# 점수가 마이너스일 경우 "올바른 점수를 입력해주세요"
score = int(input(f'점수 입력 :'))
grade = '' # 빈 문자열 ; 문자를 넣겠다
if score >= 90 and score <= 100 :
    grade = 'A'
elif score >= 80 and score < 90 :
    grade = 'B'
elif score >= 70 and score < 80 :
    grade = 'C'
elif score >= 60 and score < 70 :
    grade = 'D'
elif score >= 0 and score < 60:
    grade = 'E'
else :
    print('올바른 점수를 입력해주세요')
print(f' {grade} 등급입니다.')


'''
if score > 0 :
    if score >= 90 and score <= 100 :
    grade = 'A'
    elif score >= 80 :
    grade = 'B'
    elif score >= 70 :
    grade = 'C'
    elif score >= 60 :
    grade = 'D'
    else :
    grade = 'E'
    print(f' {grade} 등급입니다.')
else :
    grade = 'E'
    print('올바른 점수를 입력해주세요')
    
    
#다른거
if score < 0:
    print("올바른 점수를 입력해주세요")
else:
    if score >= 90 and score <= 100 :
    grade = 'A'
    elif score >= 80 :
    grade = 'B'
    elif score >= 70 :
    grade = 'C'
    elif score >= 60 :
    grade = 'D'
    else :
    grade = 'E'
    print(f' {grade} 등급입니다.')
'''
