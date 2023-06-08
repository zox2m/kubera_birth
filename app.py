from flask import Flask,render_template,request,url_for
import birth_attribute
app = Flask(__name__)

@app.route('/') # 첫 화면
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    result= None
    if request.method =='POST':
        month = request.form['month']
        day = request.form['day']
        time = request.form['time']
    result = birth_attribute.cal_rate(month,day,time)
    return render_template('result.html',result)

if __name__ == '__main__':
    app.run(debug=True)


