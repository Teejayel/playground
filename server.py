from flask import Flask, render_template

playground = Flask(__name__)

@playground.route('/')
def welcome():
    return render_template("index.html")

@playground.route('/play')
def boxes():
    return render_template("index.html", times=3)

@playground.route('/play/<int:num>')
def many_boxes(num):
    return render_template("index.html", times=num)

@playground.route('/play/<int:num>/<string:color>')
def custom_boxes(num, color):
    return render_template("index.html", times=num, color=color)

if __name__=="__main__":
    playground.run(debug=True) 