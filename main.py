from flask import Flask, redirect, url_for, render_template, request 
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/passed/<int:score>')
def passed(score):
    return render_template("passed.html",result = score)

@app.route('/failed/<int:score>')
def failed(score):
    return render_template("failed.html",result = score)

#Result checker by submit html page and using http verbs like get and post
@app.route('/submit', methods = ['GET','POST'])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])   #it should match with what has been written in index html file under name
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    res = ""
    if total_score >= 30:
        res = "passed"
    else:
        res = 'failed'
    return redirect(url_for(res,score = total_score))





if __name__ == '__main__': 
    app.run(debug = True)