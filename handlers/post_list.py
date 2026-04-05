from db.connect import DBManager
from utils.http import response


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Postlar</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        :root {{
            --bg:        #0d0d0f;
            --surface:   #16161a;
            --border:    #2a2a30;
            --accent:    #c8a96e;
            --accent-dim:#7a6240;
            --text-main: #e8e4db;
            --text-muted:#7a7880;
            --danger:    #e05555;
            --radius:    14px;
        }}

        body {{
            font-family: 'DM Sans', sans-serif;
            background: var(--bg);
            color: var(--text-main);
            min-height: 100vh;
            padding: 60px 20px;
        }}

        .page {{
            max-width: 740px;
            margin: 0 auto;
        }}

        .page-header {{
            display: flex;
            align-items: baseline;
            gap: 12px;
            margin-bottom: 48px;
        }}
        .page-header h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 2.4rem;
            color: var(--text-main);
            letter-spacing: -0.5px;
        }}
        .page-header .counter {{
            font-size: 0.85rem;
            color: var(--text-muted);
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 3px 10px;
            border-radius: 20px;
        }}

        .card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 28px 32px;
            margin-bottom: 40px;
        }}
        .card-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.05rem;
            color: var(--accent);
            margin-bottom: 20px;
            letter-spacing: 0.5px;
        }}

        .field {{ margin-bottom: 16px; }}
        .field label {{
            display: block;
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--text-muted);
            margin-bottom: 7px;
        }}
        .field input,
        .field textarea {{
            width: 100%;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 9px;
            padding: 11px 14px;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.95rem;
            color: var(--text-main);
            transition: border-color .2s, box-shadow .2s;
            resize: vertical;
        }}
        .field input::placeholder,
        .field textarea::placeholder {{ color: var(--text-muted); }}
        .field input:focus,
        .field textarea:focus {{
            outline: none;
            border-color: var(--accent-dim);
            box-shadow: 0 0 0 3px rgba(200,169,110,.10);
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-family: 'DM Sans', sans-serif;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 11px 26px;
            border: none;
            border-radius: 40px;
            cursor: pointer;
            letter-spacing: 0.3px;
            text-decoration: none;
            transition: background .2s, transform .15s;
        }}
        .btn:active {{ transform: scale(.97); }}
        .btn-primary {{ background: var(--accent); color: #0d0d0f; }}
        .btn-primary:hover {{ background: #d9bc85; }}
        .btn-edit {{
            background: transparent;
            color: var(--text-muted);
            border: 1px solid var(--border);
            font-size: 0.82rem;
            padding: 7px 16px;
        }}
        .btn-edit:hover {{
            color: var(--accent);
            border-color: var(--accent-dim);
        }}

        .divider {{
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 32px;
        }}
        .divider span {{
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            white-space: nowrap;
        }}
        .divider::before,
        .divider::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: var(--border);
        }}

        .post {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 26px 30px;
            margin-bottom: 18px;
            position: relative;
            transition: border-color .2s, transform .2s;
            animation: fadeUp .4s ease both;
        }}
        .post:hover {{
            border-color: var(--accent-dim);
            transform: translateY(-2px);
        }}
        .post-index {{
            position: absolute;
            top: 26px;
            right: 30px;
            font-size: 0.75rem;
            color: var(--text-muted);
        }}
        .post h2 {{
            font-family: 'Playfair Display', serif;
            font-size: 1.25rem;
            color: var(--text-main);
            margin-bottom: 10px;
            padding-right: 40px;
            line-height: 1.35;
        }}
        .post p {{
            font-size: 0.95rem;
            color: #a8a4b0;
            line-height: 1.7;
            margin-bottom: 18px;
        }}
        .post-actions {{
            display: flex;
            gap: 10px;
        }}

        .empty {{
            text-align: center;
            padding: 60px 20px;
            color: var(--text-muted);
        }}
        .empty-icon {{
            font-size: 2.5rem;
            margin-bottom: 14px;
            opacity: .5;
        }}

        @keyframes fadeUp {{
            from {{ opacity: 0; transform: translateY(16px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body>
<div class="page">

    <header class="page-header">
        <h1>Postlar</h1>
        <span class="counter">{post_count} ta yozuv</span>
    </header>

    <div class="card">
        <p class="card-title">✦ Yangi post</p>
        <form method="post" action="/">
            <div class="field">
                <label>Sarlavha</label>
                <input type="text" name="title" placeholder="Post sarlavhasini kiriting…" required>
            </div>
            <div class="field">
                <label>Matn</label>
                <textarea name="content" rows="4" placeholder="Post matnini kiriting…" required></textarea>
            </div>
            <button class="btn btn-primary" type="submit">&#10003; Saqlash</button>
        </form>
    </div>

    <div class="divider"><span>Barcha postlar</span></div>

    {posts_html}

</div>
</body>
</html>"""


POST_CARD_TEMPLATE = """
    <article class="post" style="animation-delay:{delay}s">
        <span class="post-index">#{index}</span>
        <h2>{title}</h2>
        <p>{content}</p>
        <div class="post-actions">
            <a class="btn btn-edit" href="/edit?id={post_id}">✏️ Tahrirlash</a>
        </div>
    </article>"""

EMPTY_STATE = """
    <div class="empty">
        <div class="empty-icon">📭</div>
        <p>Hozircha postlar yo'q. Birinchi postni yarating!</p>
    </div>"""


def _render_posts(posts: list) -> str:
    if not posts:
        return EMPTY_STATE
    return "".join(
        POST_CARD_TEMPLATE.format(
            index=i + 1,
            delay=round(i * 0.07, 2),
            post_id=p[0],
            title=p[1],
            content=p[2],
        )
        for i, p in enumerate(posts)
    )


def post_list():
    with DBManager() as cur:
        cur.execute("SELECT * FROM postings")
        posts = cur.fetchall()

    posts_html = _render_posts(posts)
    body = HTML_TEMPLATE.format(
        post_count=len(posts),
        posts_html=posts_html,
    )
    return response(body)
