# handlers/not_found.py
from utils.http import response


def not_found():
    body = "<h1>404 - Sahifa topilmadi</h1>"
    return response(body)