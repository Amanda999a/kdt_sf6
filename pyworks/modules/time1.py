# time 모듈
# time.time() - 1970.1.1 자정 이후부터 초로 반환(유닉스 컴퓨터 생성일)
import time
import math
print(time.time()) # 파이썬은 17억초
# 일로 환산
day = math.floor(time.time() / (24 * 60 * 60)) # 24시간 * 60분 * 60초
print(day)
# 년으로 환산
year = math.floor(time.time() / (365* 24 * 60 * 60))
print(year)
print()
# time.sleep() IOT에서 많이 사용됨. time.sleep(1) -> 1초 간격으로 단위. 파이썬만 1초가 기준

# for i in range(1,10):
#     print(i) # 1~9까지 출력
#     time.sleep(0.5) #0.5초에 한번씩 출력

# 수행(실행)시간을 측정 - time.time
start = time.time() # 시작시간 17억초
# print(start)
for i in range(1,1000000):
    print(i)
    # time.sleep(1)

end = time.time() # 끝나는 시간
print("수행시간 : " + str(end - start) + "초") # str이 큰 쪽이니까 붙여줌