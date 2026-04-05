# handlers/post_list.py
from db.connect import DBManager
from utils.http import response


def post_list():
    with DBManager() as cur:
        cur.execute(
            """
            SELECT *
            FROM postings
            """
        )
        posts = cur.fetchall()         # natijalarni oling

    body = """
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>Posts</title></head>
    <body>
    <div class="container">
    """

    for p in posts:
        body += f"""
        <div class ="post" >
            <h1> {p[1]} </h1 >
            <p> {p[2]} </p >
        </div>
        """         # har bir post uchun HTML yozing

    body += """
    </div>
    </body>
    </html>
    """
    return response(body)