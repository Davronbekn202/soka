from db.connect import DBManager
from utils.http import response
def list_post():
    with DBManager() as cur:
        cur.execute("SELECT * FROM posting")
        posts = cur.fetchall()
    body = """
        <html>
        <head>
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e7f9f4;
            margin: 20px;
            color: #333;
        }

        .card {
            background-color: #fff8e7;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        h1 {
            color: #2c3e50;
            font-size: 24px;
            margin-bottom: 10px;
        }

        p {
            font-size: 16px;
            line-height: 1.6;
        }

        form {
            background: #2c3e50;
            padding: 25px;
            border-radius: 12px;
            width: 300px;
            margin: 30px auto;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }

        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            outline: none;
            margin-bottom: 15px;
            transition: 0.3s;
        }

        input:focus {
            border-color: #c8a97e;
            box-shadow: 0 0 5px rgba(200,169,126,0.5);
        }

        button {
            width: 100%;
            padding: 10px;
            background: #c8a97e;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background: #a8895f;
            transform: scale(1.05);
        }

        .posts-container {
            max-width: 600px;
            margin: 20px auto;
        }
        </style>
        </head>

        <body>

        <form method="post">
            <input type="text" name="title" id="">
            <input type="text" name="content" id"">
            <button>Submit</button>
        </form>

        <div class="posts-container">
        """

    for p in posts:
        body += f"""
            <div class="card">
                <h1>{p[1]}</h1>
                <p>{p[2]}</p>
            </div>
            """

    body += """
        </div>

        </body>
        </html>
        """

    return response(body)