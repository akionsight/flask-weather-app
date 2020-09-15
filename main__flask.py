# Weather App using Flask

## imports 
import random
import main
import string
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
app = Flask(__name__)
secret_key = ''
for i in range(5):
    letter = random.choice(list(string.ascii_letters))
    secret_key = secret_key + letter
app.secret_key = secret_key
## initalisation
@app.route('/', methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        city = request.form["city"]
        wee = main.get_weather_final(city)
        session['city'] = wee['for_city']
        session['temp_faren'] = wee['temp_faren']
        session['temp_celcius'] = wee['temp_celcius']
        session['humidity'] = wee['humidity']
        return redirect(url_for("give_weather"))
    return render_template("main.html")


@app.route('/weather/')      
def give_weather():
    return render_template('weather.html', city=session['city'], temp_faren=session['temp_faren'], temp_celcius=session['temp_celcius'], humidity=session['humidity'])



if __name__ == "__main__":
    app.run(debug=True)