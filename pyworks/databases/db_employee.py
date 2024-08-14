# 사원 관리 - 조회(전체, 1건), 삽입, 수정, 삭제
import sqlite3
#설치 되어 있을때 pip install

#함수형
def select_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db') # db에 연결 - conn 객체 생성
    cur = conn.cursor() # 작업 개체 생성
    sql = "SELECT * FROM employee" #데이터 요청
    cur.execute(sql)
    rs = cur.fetchall() #db에 있는 자료를 모두 가져옴 - 자료구조가 리스트가 됨(rs - result set)
    #fetchone ; db에 있는 자료를 한 개 가져옴
    # 요소가 튜플 ; 리스트 안에 튜플(읽기전용)로 되어 있음
    # print(rs)
    # print(rs[0]) #튜플구조로 출력. 리스트 구조라서 인덱싱 가능해짐
    # print(rs[-1]) #최신 자료

# 전체 출력
    for i in rs:
        print(i)
    conn.close()

# 자료 삽입
def insert_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e105', '조대리', 4500000)" #- 두번 실행하면 두번 들어가니까 실행 후 주석처리
    cur.execute(sql)
    conn.commit() # 자료 삽입, 수정, 삭제 후에는 반드시 commit() 명시
    conn.close()

# 자료 수정
def update_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "UPDATE employee SET salary = 2500000 WHERE emp_id = 'e104'"
    cur.execute(sql)
    conn.commit()
    conn.close()

# 자료 삭제 - 이나라 삭제
def delete_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE emp_id = 'e102'"
    cur.execute(sql)
    conn.commit() #무서워서 안넣으면 코드 실행이 안된다..! -> 여기서는 Rollback이 안됨
    conn.close()

# 사원 이름에 '대리'가 포함된 사원의 정보를 검색하시오
def select_one():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE name LIKE '%대리%'"
    cur.execute(sql)
    rs = cur.fetchall()
    print(rs)
    conn.close()

# 사원 이름에 '신입'가 포함된 사원의 정보를 검색하시오
def select_one():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE name LIKE '%신입%'"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)
    conn.close()


# 함수 호출
# update_emp()
# insert_emp()
# select_emp()
# delete_emp()
select_one()



