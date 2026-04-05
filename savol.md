# 📝 Oy Yakuni Amaliyot

**⏱ Vaqt:** 40–50 min  
**🎯 Maqsad:** Raw socket server + PostgreSQL bilan ishlashni mustahkamlash  
**📚 Mavzu:** Python Socket, HTTP, psycopg2, Context Manager

---

## 📦 1. Database sozlash

### 📌 Migration fayli yaratish

`db/migrations/001_create_posting_table.sql` faylini yarating:

| Maydon | Turi |
|--------|------|
| `id` | `SERIAL PRIMARY KEY` |
| `title` | `VARCHAR(255)` |
| `content` | `TEXT` |

```sql
-- 001_create_posting_table.sql
CREATE TABLE IF NOT EXISTS postings
(
    id      ,
    title   ,
    content
);
```

---

### 📌 DBManager klassi yaratish

`db/connect.py` faylini yarating.  
`DBManager` — context manager bo'lishi kerak (`with` bilan ishlashi uchun).

```python
# db/connect.py
import psycopg2


class DBManager:
    def __init__(self, host="localhost", user="", password="", database="", port=5432):
        self.conn = psycopg2.connect(
            database=,
            user=,
            password=,
            host=,
            port=,
        )

    def __enter__(self):
        return               # cursor qaytarish kerak

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            self.conn.          # xatolikda rollback
            self.conn.close()
            raise

        if self.conn:
            self.conn.          # muvaffaqiyatda commit
            self.conn.close()
```

### ⚠ Migration ishga tushirish

```bash
python db/migrate.py
```

---

## 🌐 2. Socket server yaratish

### 📌 HTTP javob yozuvchisi

`utils/http.py` faylini yarating:

```python
# utils/http.py

def response(body):
    return (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {}\r\n"   # body uzunligi
        "\r\n"
        +
    )
```

---

### 📌 Server yaratish

`socket_server/server.py` faylini yarating:

```python
# socket_server/server.py
import socket
from socket_server.router import handel_request

HOST = "127.0.0.1"
PORT = 8010


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((    ,     ))
    server_socket.listen(5)

    print(f"Server running on http://{HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.          # ulanishni qabul qilish
        
        request = client_socket.recv(4096)
        response = handel_request(request)
        client_socket.sendall(response.encode())
        client_socket.         # ulanishni yopish


if __name__ == '__main__':
    start_server()
```

---

## 🧠 3. Handler va Router yozish

### 📌 Post List handler

`handlers/post_list.py` faylini yarating.  
Bazadan barcha postlarni olib, HTML ko'rinishida qaytarsin.

```python
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
        posts =              # natijalarni oling

    body = """
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>Posts</title></head>
    <body>
    <div class="container">
    """

    for p in posts:
        body +=              # har bir post uchun HTML yozing

    body += """
    </div>
    </body>
    </html>
    """
    return response(body)
```

---

### 📌 Not Found handler

`handlers/not_found.py` faylini yarating:

```python
# handlers/not_found.py
from utils.http import response


def not_found():
    body = "<h1>404 - Sahifa topilmadi</h1>"
    return response(body)
```

---

### 📌 Router yozish

`socket_server/router.py` faylini yarating.  
So'rovdan `method` va `path` ni ajratib, to'g'ri handlerga yo'naltirsin.

```python
# socket_server/router.py
from handlers.not_found import not_found
from handlers.post_list import post_list


def handel_request(request: bytes) -> str:
    try:
        text = request.decode("utf-8", errors="ignore")
        line = text.split(          )[0]      # birinchi qatorni oling
        method, path, _ = line.split(" ")

    except Exception:
        return not_found()

    if method == "GET" and path == "/":
        return
    else:
        return
```

---

## 🎨 4. Serverni ishga tushirish

```bash
python socket_server/server.py
```

Brauzerda `http://127.0.0.1:8010` ga kiring.

---

## 🧠 Muhim tushunchalar

### 🔹 Context Manager
```python
# __enter__ va __exit__ metodlari with bloki uchun kerak
with DBManager() as cur:
    cur.execute(...)      # __enter__ cursor qaytaradi
                          # __exit__ commit yoki rollback qiladi
```

### 🔹 HTTP So'rov Tuzilishi
```
GET / HTTP/1.1\r\n
Host: 127.0.0.1:8010\r\n
\r\n
```

### 🔹 HTTP Javob Tuzilishi
```
HTTP/1.1 200 OK\r\n
Content-Type: text/html; charset=utf-8\r\n
Content-Length: 123\r\n
\r\n
<html>...</html>
```

### 🔹 SQL — Barcha postlarni olish
```sql
SELECT * FROM postings;
```

---

## 🎯 Talabadan kutiladigan natija

- ✅ `postings` jadvalini yaratuvchi migration fayli
- ✅ `DBManager` context manager ishlaydi
- ✅ Socket server `127.0.0.1:8010` da ishga tushadi
- ✅ `GET /` so'rovida postlar ro'yxati HTML da chiqadi
- ✅ Noto'g'ri URL da `404` xabari chiqadi
