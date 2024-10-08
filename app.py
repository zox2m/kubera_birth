from flask import Flask,render_template,request,url_for
import birth_attribute
app = Flask(__name__)

@app.route('/') # 첫 화면
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    print("hello")
    if request.method =='POST':
        month = int(request.form['month'])
        day = int(request.form['day'])
        time = int(request.form['time'])
    
    return render_template('result.html',result = birth_attribute.cal_all(month,day,time))

if __name__ == '__main__':
    app.run(debug=True)


