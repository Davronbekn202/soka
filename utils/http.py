# utils/http.py

def response(body):
    return (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body.encode())}\r\n"   # body uzunligi
        "\r\n"
        + body
    )

