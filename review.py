#!/usr/bin/python
from flask import Flask, session, render_template, redirect, request, url_for
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
 
#DB 값 설정
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ospteamproject9'
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
        sql = "SELECT id FROM members WHERE id = %s AND pw = %s"
        value = (id, pw)
        cursor.execute("set names utf8")
        cursor.execute(sql, value)
 
        data = cursor.fetchall()
        cursor.close()
        conn.close()
 
        if data:
            session['login_user'] = id
            return redirect(url_for('reviewboard'))
        else:
            error = 'invalid input data detected !'
 
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
            data_list.append(data_dic)
 
        cursor.close()
        conn.close()
 
        return render_template('reviewboard.html', error=error, name=id, data_list=data_list) # html을 렌더하며 DB에서 받아온 값들을 넘김
 
    return render_template('reviewboard.html', error=error, name=id)
 
if __name__ == '__main__':
    app.run()
