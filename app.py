from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to flask homepage"

@app.route('/learn')
def learn():
    return "learn flask well and in depth.You can do it."

@app.route('/passed/<int:score>')
def passed(score):
    return "The person is passed with "+str(score)+" marks."

@app.route('/failed/<int:score>')
def failed(score):
    return "The person is failed with "+str(score)+" marks."

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks <30:
        result = "failed"
    else:
        result = "passed"
    return redirect(url_for(result,score = marks))



if __name__ == '__main__': 
    app.run(debug = True)