from handlers.not_found import not_found
from handlers.post_list import post_list


def handel_request(request: bytes) -> str:
    try:
        text = request.decode("utf-8", errors="ignore")
        line = text.split(          )[0]
        method, path, _ = line.split(" ")

    except Exception:
        return not_found()

    if method == "GET" and path == "/":
        return post_list(request)
    else:
        return not_found(request)