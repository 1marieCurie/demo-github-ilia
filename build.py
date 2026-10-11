from bonjour import saluer
from pathlib import Path

message = saluer("ILIA")

html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Démo GitHub Pages</title>
    <style>
        body {{
            background: #171923;
            color: #f7fafc;
            font-family: Arial, sans-serif;
            display: grid;
            place-items: center;
            min-height: 100vh;
            margin: 0;
        }}
        h1 {{ font-size: 2.5rem; }}
    </style>
</head>
<body>
    <h1>{message}</h1>
</body>
</html>
"""

Path("index.html").write_text(html, encoding="utf-8")
