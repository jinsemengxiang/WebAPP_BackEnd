from functools import wraps
from flask import jsonify, make_response


def json_response(code=200):
    """
        统一返回json形式
    :param code: 状态码
        如果正常返回，code默认为200，如果异常返回，code为异常状态码
    :return:
        json形式的数据
        {
            'code': 200,
            'message': 'success',
            'data': {
                'message': '你好'
            }
        }
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                response = {
                    'code': code,
                    'message': 'success',
                    'data': result
                }
                return make_response(jsonify(response))
            except Exception as e:
                response = {
                    'code': code,
                    'message': str(e) + '，请联系管理员',
                    'data': None
                }
                return make_response(jsonify(response))

        return wrapper

    return decorator
