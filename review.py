from flask import Flask, session, render_template, redirect, request, url_for
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
 
#데이터페이스 값을 설정해주는 단계
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'yellow2090*'
app.config['MYSQL_DATABASE_DB'] = 'reviewdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = "ABCDEFG"
mysql.init_app(app)
 
 # 로그인 화면
@app.route('/', methods=['GET', 'POST'])
def main():
    error = None
 
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
 
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT id FROM members WHERE id = %s AND pw = %s" # 실행할 SQL문
        value = (id, pw)
        cursor.execute("set names utf8") # 한글이 정상적으로 출력이 되지 않는 경우를 위해
        cursor.execute(sql, value) # 메소드로 전달해 명령문을 실행
 
        data = cursor.fetchall() # SQL문을 실행한 결과 데이터를 꺼냄
        cursor.close()
        conn.close()
 
        if data:
            session['login_user'] = id # 로그인 된 후 페이지로 데이터를 넘기기 위해 session을 사용함
            return redirect(url_for('reviewboard')) # reviewboard 페이지로 넘어감 (url_for 메소드를 사용해 reviewboard이라는 페이지로 넘어간다)
        else:
            error = 'invalid input data detected !' # 에러가 발생한 경우
 
    return render_template('login.html', error = error)
 
 # 회원가입 화면
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        
        id = request.form['regi_id']
        pw = request.form['regi_pw']
 
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO members VALUES ('%s', '%s')" % (id, pw)
        cursor.execute(sql)
        data = cursor.fetchall()
 
        if not data:
            conn.commit()
            return redirect(url_for('main'))
 
        else:
            conn.rollback()
            return "Register Failed"
 
        cursor.close()
        conn.close()
 
    return render_template('register.html', error=error)
 
 # 로그인 된 후 홈 화면
@app.route('/reviewboard.html', methods=['GET', 'POST'])
def reviewboard():
    error = None
    id = session['login_user']
 
     # 게시판에 글 등록하기
    if request.method == 'POST':
        #print("WRITE TEST")
        store = request.form['store']
        review = request.form['review']
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO reviewlist (store, id, review) VALUES ('%s', '%s', '%s')" % (store, id, review)  # 실행할 SQL문
        cursor.execute(sql)
        new_data = cursor.fetchall()

        if not new_data:
            conn.commit()
            return redirect(url_for("reviewboard"))
 
        else:
            conn.rollback()
            return "Register Failed"
 
        cursor.close()
        conn.close()
 
    elif request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT num, store, id, review, times FROM reviewlist ORDER BY times desc"
        cursor.execute(sql)
        data = cursor.fetchall()
 
        data_list = []
 
        for obj in data:
            data_dic = {
                'number': obj[0],
                'restaruant': obj[1],
                'writer': obj[2],
                'con': obj[3],
                'time':obj[4]
            }
            data_list.append(data_dic) # 완성된 딕셔너리를 list에 넣음
 
        cursor.close()
        conn.close()
 
        return render_template('reviewboard.html', error=error, name=id, data_list=data_list) # html을 렌더하며 DB에서 받아온 값들을 넘김
 
    return render_template('reviewboard.html', error=error, name=id)
 
if __name__ == '__main__':
    app.run()