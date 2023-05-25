from flask import Flask

app = Flask(__name__)

@app.route('/') # 첫 화면

@app.route('/home') # 기본 주소 뒤에 붙는 그거!
def home():
    return 'Hello, World!'

@app.route('/user')
def user():
    return 'hello, user!'

if __name__ == '__main__':
    app.run(debug=True)