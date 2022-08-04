from flask import Flask,render_template
import random
import datetime
import requests
app = Flask(__name__)
time = datetime.datetime.now()

URL = "https://api.agify.io"
para = {
    "name":"Shresth"
}


@app.route('/')
def home():
    year = time.year
    random_num = random.randint(1,10)
    return render_template("index.html", num=random_num, year=year)

@app.route('/guess/<name>')
def guess_name(name):
    para["name"] = name
    response = requests.get(url=URL, params=para).json()
    gender = requests.get(url=f'https://api.genderize.io?name=shresth').json()['gender']
    return render_template("guess.html", name=response['name'], gender=gender, age=response['age'])


if __name__ == '__main__':
    app.run(debug=True)