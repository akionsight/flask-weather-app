# Weather App using Flask

## imports 
import secrets
import main
import requests
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

no_internet = False
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)

## initalisation
@app.route('/', methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        city = request.form["city"]
        try:
            wee = main.get_weather_final(city)
        except requests.exceptions.ConnectionError:
            no_internet = True
            return redirect(url_for('no_internet'))
        session['city'] = wee['for_city']
        session['temp_faren'] = wee['temp_faren']
        session['temp_celcius'] = wee['temp_celcius']
        session['humidity'] = wee['humidity']
        return redirect(url_for("give_weather"))
    return render_template("main.html")


@app.route('/weather/')      
def give_weather():
    try:
        return render_template('weather.html', city=session['city'], temp_faren=session['temp_faren'], temp_celcius=session['temp_celcius'], humidity=session['humidity'])
    except KeyError:
        return redirect(url_for('main_page'))
@app.route('/no_internet/')
def no_internet():
    if no_internet == True:
        return render_template('please_check_connection.html')
    else:
        return redirect(url_for('main_page'))
        pass
        
if __name__ == "__main__":
    app.run(debug=True)