def response(body):
    return (
        "HTTP/1.1 200 ok\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-length: {len(body.encode())}\r\n"
        "\r\n"
        + body
    )

def redirect(path):
    return (
        "HTTP/1.1 303 See Other\r\n"
        f"Location: {path}\r\n"
        "\r\n"
    )
