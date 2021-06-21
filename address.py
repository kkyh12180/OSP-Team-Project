#!/usr/bin/python
from flask import Flask, render_template, request
from werkzeug.utils import HTMLBuilder
import weather_API
import crawling

def guchange(alpha):
    if alpha=="a":
        return str("남구")
    if alpha=="b":
        return str("달성군")
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

app = Flask(__name__)

@app.route('/')
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
            icon = str("{{url_for(static,filename=images/sunny.png)}}")
        elif list[0] == "cloudy":
            weather = str("흐립니다")
            # icon = str("{{url_for('static',filename='images/cloudy.png')}}")
        elif list[0] == "rainy":
            weather = str("비가 옵니다")
            # icon = str("{{url_for('static',filename='images/rainy.png')}}")
        else:
            weather = str("눈이 옵니다")
            # icon = str("{{url_for('static',filename='images/snowy.png')}}")
        return render_template('food.html', result=result, myGu=myGu, myDong=myDong, weather=weather, icon = icon, engw=list[0], temperature=list[1])

@app.route("/storelist", methods = ['POST', 'GET'])
def foodlist():
    if request.method == 'POST':
        result = request.form
        myGu = request.form.get("myGu")
        myDong = request.form.get("myDong")
        list = []
        list = weather_API.get_weather()
        myFood = request.form['food']
        myStoreList = crawling.crawling(myGu, myDong, myFood)
        return render_template("storelist.html", result=result, myFood=myFood, myWeather=list[0], myStoreList=myStoreList)


if __name__ == '__main__':
    app.run(debug = True)