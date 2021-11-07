from flask import Flask, render_template

app = Flask(__name__) #naš objekt - predstavlja našo spletno aplikacijo

@app.route("/") # "/" prva oz. glavna stran aplikacije - tako lahko dodaš več strani
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__': # na objektu zaženemo funkcijo run
    app.run(use_reloader=True, debug=True)