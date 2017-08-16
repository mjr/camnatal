import re

from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def index():
    URL_BASE = "http://transito.gtrans.com.br/sttunatal/index.php/portal/cameras"
    html = urlopen(URL_BASE)
    soup = BeautifulSoup(html, "html.parser")
    lis = soup.find("ul", attrs={"data-role": "listview"}).findAll("li")

    cameras = []
    for index, li in enumerate(lis):
        cameras.append({'id': index, 'description': li.find("p").get_text().lower(), 'url': li.find("img")["rel"]})

    return render_template('index.html', cameras=cameras)


@app.route("/map")
def map():
    return render_template('map.html')

app.run(debug=True, use_reloader=True)
