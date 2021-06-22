#!/usr/bin/python
from flask import Flask, session, render_template, redirect, request, url_for
from flaskext.mysql import MySQL
from werkzeug.utils import HTMLBuilder
import weather_API
import crawling
import init_data
import save

def guchange(alpha):
    if alpha=="a":
        return str("남구")
    if alpha=="b":
        return str("달서구")
    if alpha=="c":
        return str("동구")
    if alpha=="d":
        return str("북구")   
    if alpha=="e":
        return str("서구")   
    if alpha=="f":
        return str("수성구")   
    if alpha=="g":
        return str("중구")    
    if alpha=="h":
        return str("달성군")                     

mysql = MySQL()
app = Flask(__name__)

#데이터페이스 값을 설정해주는 단계
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
        sql = "SELECT id FROM members WHERE id = %s AND pw = %s" # 실행할 SQL문
        value = (id, pw)
        cursor.execute("set names utf8") # 한글이 정상적으로 출력이 되지 않는 경우를 위해
        cursor.execute(sql, value) # 메소드로 전달해 명령문을 실행
 
        data = cursor.fetchall() # SQL문을 실행한 결과 데이터를 꺼냄
        cursor.close()
        conn.close()
 
        if data:
            session['login_user'] = id # 로그인 된 후 페이지로 데이터를 넘기기 위해 session을 사용함
            return redirect(url_for('home')) # home 페이지로 넘어감 (url_for 메소드를 사용해 reviewboard이라는 페이지로 넘어간다)
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

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/food', methods= ['POST', 'GET'])
def result():
    if request.method == 'POST' :
        result = request.form
        Gu = request.form['gu']
        myGu = guchange(Gu)
        myDong = request.form['dong']
        # myFood = request.form['food']
        list = []
        list = weather_API.get_weather()
        if list[0] == "sunny":
            weather = str("화창합니다")
        elif list[0] == "cloudy":
            weather = str("흐립니다")
        elif list[0] == "rainy":
            weather = str("비가 옵니다")
        else:
            weather = str("눈이 옵니다")
        rank={}
        rank = save.get_info(list[0])
        sourcelist=[]
        sourcelist=rank.get('_source')
        foodlist=[]
        foodlist=sourcelist.get('Food')
        frelist=[]
        frelist=sourcelist.get('Frequency')    
        return render_template('food.html', result=result, myGu=myGu, myDong=myDong, foodlist=foodlist, weather=weather, engw=list[0], temperature=list[1])

@app.route("/storelist", methods = ['POST', 'GET'])
def foodlist():
    if request.method == 'POST':
        result = request.form
        myGu = request.form.get("myGu")
        myDong = request.form.get("myDong")
        list = []
        list = weather_API.get_weather()
        myFood = request.form['food']
        myStoreList = []
        name = []
        rating = []
        link = []
        save.save_data(list[0], myFood)
        i=0
        myStoreList = crawling.crawling(myGu, myDong, myFood)
        if(len(myStoreList)<3):
            for i in range(0,len(myStoreList)):
                name.append(myStoreList[i][0])
                rating.append(myStoreList[i][1])
                link.append(myStoreList[i][2])
        else:        
            name.append(myStoreList[0][0])
            rating.append(myStoreList[0][1])
            link.append(myStoreList[0][2])
            name.append(myStoreList[1][0])
            rating.append(myStoreList[1][1])
            link.append(myStoreList[1][2])
            name.append(myStoreList[2][0])
            rating.append(myStoreList[2][1])
            link.append(myStoreList[2][2])

        
        return render_template("storelist.html", myGu=myGu, myDong=myDong, result=result, myFood=myFood, myWeather=list[0], name = name, link = link, rating = rating)

 # 리뷰 화면
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
            data_list.append(data_dic) # 완성된 딕셔너리를 list에 넣음
 
        cursor.close()
        conn.close()
 
        return render_template('reviewboard.html', error=error, name=id, data_list=data_list) # html을 렌더하며 DB에서 받아온 값들을 넘김
 
    return render_template('reviewboard.html', error=error, name=id)

if __name__ == '__main__':
    app.run(debug = True)
