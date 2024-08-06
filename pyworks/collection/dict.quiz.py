# 실습 1
score = {}
score = {
    "Alice" : 80,
    "Bob" : 90,
    "Charile" : 95,
}
print(score)

score["David"] = 80
print(score)

score["Alice"] = 88
print(score)

score.pop("Bob")
print(score)

for key in score:
    print(f'{key} : {score[key]}')

'''
마지막 권장 답변
for key in scores.keys():
print(f'{key}의 점수는 {scores.get(key)}')
'''
