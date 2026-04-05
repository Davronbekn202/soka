from handelers.not_found import not_found
from handelers.post_list import list_post
def handle_request(request:bytes,client_socket) -> bytes:
    try:
        text = request.decode("utf-8", errors="ignore")
        line = text.split("\r\n", 1)[0]
        method, path, _ = line.split(" ")
        print(line)
    except Exception:
        method = path = ""
    if method == "GET" and path == "/":
            return list_post(request)
    else:
        return not_found(request)