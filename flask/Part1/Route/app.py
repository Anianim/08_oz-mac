from flask import Flask, request , Response



app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Main Page"

#Alt + Shift + 화살표 위/아래 복사됨
@app.route('/about')
def about():
    return "This is about page!!"

# 동적으로 URL 파라미터 값을 받아서 처리해준다 .
# http://127.0.0.1:5000/user/"value"
@app.route('/user/<username>')
def user_profile(username):
    return f'Username : {username}'

@app.route('/number/<int:number>') #지정된 타입만 받을수 있음
def user_number(number):
    return f'number : {number}'

# post 요청 날리는법
# (1) post man (program name)
# (2) requests
import requests # pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***" , request.data)

    return Response("Successfully submitted", status=200)


if __name__ == "__main__":
    print("__name__ : " , __name__)
    app.run()