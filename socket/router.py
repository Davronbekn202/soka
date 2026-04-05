
from handlers.not_found import not_found
from handlers.post_list import post_list

def handel_request(request: bytes) -> bytes:
    try:
        text = request.decode("utf-8", errors="ignore")
        line =text.split("\r\n",1)[0]
        method, path, _ =line.split(" ")

    except Exception as e:
        print(f"Error parsing request: {e}")
        return not_found()

    if method == "GET" and path == "/":
        return post_list()
    else:
        return not_found()