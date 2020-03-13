from flask import request, abort, g
from functools import wraps


def has_body(req):
    request_json = req.get_json(force=True)

    if not request_json:
        abort(400)

    g.text = request_json["text"]
    return


def request_handler_factory():
    def request_handler(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            has_body(request)
            return function(*args, **kwargs)

        return wrapper
    return request_handler
