from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from config import BaseConfig
from myapp.common.R.json_response import json_response
from myapp.controller.user import user as user_blueprint

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(user_blueprint)

app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 如果是GET请求，直接下面这样写，默认methods=['GET']
@app.route('/test')
def test():
    # 这种就是在url后面添加的参数，例如：http://localhost:127.0.0.1/test?q=123456,那么query的值就是123456
    # 可以接收多个参数，例如：http://localhost:127.0.0.1/test?username=tcw&password=123456,然后用request.args.get('username')和request.args.get('password')获取
    username = request.args.get('username')
    password = request.args.get('password')
    # 获取到数据后可以做逻辑判断，比如将username和password与数据库当中的做比对，然后正确的话，返回true，然后前端得到true就让他成狗跳转界面，错误的话返回false，前端让他重新输入
    print(username + '===' + password)
    data = {'message': '你好'}
    return jsonify(data)


# 如果是POST请求，并且传入的数据是JSON形式，按下面这样写
@app.route('/postTest', methods=['POST'])
@json_response(200)
def post_test():
    json = request.json
    username = json['username']
    password = json['password']
    print(username + '===' + password)
    raise Exception('测试异常')
    data = {'message': '你好'}
    return data


with app.app_context():
    with db.engine.connect() as conn:
        result = db.session.execute(text("show databases"))
        for row in result:
            print(row)

if __name__ == '__main__':
    app.run()
