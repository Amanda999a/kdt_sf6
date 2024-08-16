# 도서 관리
# 테이블 생성 - book
# 방식 - 동적 바인딩 방식('?' 기호 사용)
# 데이터베이스 레코드(행) 자료형은 튜플구조형(소괄호형)이다
# 요소가 1개일때 (a, ) - 콤마를 찍어야함! 안하면 int로 인식해서 오류발생
import sqlite3

#db 연결. db 없으면 생성되고, 있으면 연결
def getconn():
    conn = sqlite3.connect('./output/bookdb.db')
    return conn

def create_book():
    conn = getconn() #conn을 호출해서 사용 -> getconn() 호출
    cursor = conn.cursor() # 작업객체
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """
    cursor.execute(sql)
    conn.commit()  #파이썬에서 DBL이지만(생성단계) 해줘야함
    conn.close()
def insert_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? - 동적 바인딩 기호.
    sql = "INSERT INTO book (title, author, price) VALUES (?,?,?)"
    cursor.execute(sql, ("점프 투 파이썬", "박응용", "19800"))
    conn.commit()
    conn.close()
def select_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cursor = conn.cursor()
    # '천 개의 파랑' 가격을 15000으로 변경(동적 바인딩 방식. 튜플구조 지키기)
    sql = "UPDATE book SET price = ? WHERE title = ?"
    cursor.execute(sql, ("15000", '천개의 파랑'))
    conn.commit()
    conn.close()

def select_one():
    conn = getconn()
    cursor = conn.cursor()
    # 책 번호가 2번인 도서의 정보 검색(동적으로 검색)
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2,))
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def delete_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql,(1,))
    conn.commit()
    conn.close()

if __name__=="__main__": #외부 호출시 제외되는 문장
    # create_book()
    # insert_book()
    # update_book()
    select_book()
    # select_one()
    # delete_book()

