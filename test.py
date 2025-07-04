from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def welcome():
    return 'welocome to flask course why'
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/foam',methods=['GET','POST'])
def foam():
    if request.method=='POST':
        name=request.form['name']
        return f"Helo {name}"
    return render_template('foam.html')
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"Helo {name}"
    return render_template('foam.html')

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score > 50:
        res="PASS"
    else:
        res="Failed"
    return render_template('results.html',result=res)


if  __name__=='__main__':
    app.run(debug=True)