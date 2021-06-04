from flask import Flask, render_template
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

import weather_API
import crawling


@app.route("/")
def main():
    myWeather = weather_API.outputWeather
    myFood = crawling.crawling()
    return render_template("home.html", one=myWeather, list=myFood)

if __name__ == "__main__":
    app.run(debug=True)
