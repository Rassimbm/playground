from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/play")
def level_1():
    return render_template("home.html", color = "aqua", num = 3)

@app.route("/play/<int:num>")
def level_2(num):
    return render_template("home.html", color = "aqua", num=num)

@app.route("/play/<int:num>/<string:color>")
def level_3(num,color):
    return render_template("home.html", num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)