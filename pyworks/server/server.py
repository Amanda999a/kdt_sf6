# 출처 : https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
from flask import Flask #Flask는 클래스. 생성자의 인자를 삽입
#Flask 클래스의 app 객체를 생성
app = Flask(__name__)

# 라우터 : 길. 웹페이지의 경로
# 웹페이지의 경로 설정 - 라우팅
# @ at 접두사
@app.route('/') #루트 경로 127.0.0.1:5000/
def index():  #모든 웹사이트 첫페이지 index라고 함. 경로는 루트를 씀
    return "<h1> Hello Flask!</h1>" #루트 페이지에 보내준다
#<h1> : 헤드라인 글자를 제목 크기로 바꿔줌

@app.route('/signup') #루트 경로 127.0.0.1:5000/signup
def signup():
    return "회원가입 페이지입니다."

@app.route('/shopping') #루트 경로 127.0.0.1/shopping
def shop():
    return "쇼핑몰입니다."

if __name__ =='__main__':
    app.run()