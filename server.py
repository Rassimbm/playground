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

if __name__ == "__main__":
    app.run(debug=True)