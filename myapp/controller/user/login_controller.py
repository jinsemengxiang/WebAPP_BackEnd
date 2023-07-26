from flask import request

from myapp.common.R.json_response import json_response
from myapp.controller.user import user


@user.route('/login', methods=['POST'])
@json_response(200)
def login():
    """
    登录接口
    :return:
    登录成功返回'登录成功'
    登录失败返回'用户名或密码错误'
    """
    json = request.json
    username = json['username']
    password = json['password']
    print(username + '===' + password)
    if username == 'tcw' and password == '123456':
        return '登录成功'
    return '用户名或密码错误'
