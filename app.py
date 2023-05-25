from flask import Flask,render_template,request
import birth_attribute
app = Flask(__name__)

@app.route('/',methods=['GET','POST']) # 첫 화면
def index():
    month=None
    day=None
    time=None
    
    if request.method =='POST':
        month = request.form['month']
        day = request.form['day']
        time = request.form['time']

    return render_template('result.html',month=month, day=day,time=time)



if __name__ == '__main__':
    app.run(debug=True)