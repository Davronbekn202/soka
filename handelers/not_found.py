from utils.http import response
def not_found():
    body = "<h1>404 ERROR </h1>"
    return response(body)


