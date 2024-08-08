# 리스트를 매개변수로 사용하는 함수

def times(a):   #times()안의 글자는 달라도 괜찮음 times : 배수. a = [1,2,3,4]
    # a2 = [] #배수를 저장할 빈 리스트(배열) 생성(선언)
    # for i in a:
    #     a2.append(i * 3)
    a2 = [i * 3 for i in a] #리스트 내포
    return a2

v= [1, 2, 3, 4] #정수형 리스트
v2 = times(v) #호출(3의 배수
print(v2)