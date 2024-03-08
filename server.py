from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    #Flask will look for templates in the "templates" folder.
    #All other files like CSS and JS will be looked in "static" folder.
    random_num = random.randint(0, 9)
    NAME = "Madhuri"
    YEAR = datetime.datetime.now().year
    return render_template("index.html", num=random_num, name=NAME, year= YEAR)

if __name__ == '__main__':
    app.run(debug=True)