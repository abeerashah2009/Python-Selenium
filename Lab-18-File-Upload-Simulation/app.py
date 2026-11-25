import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

FORM = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Upload</title>
</head>
<body>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" id="fileInput">
        <button type="submit">Upload</button>
    </form>
</body>
</html>"""

@app.get("/")
def index():
    return FORM

@app.post("/upload")
def upload():
    f = request.files["file"]
    name = secure_filename(f.filename)
    f.save(os.path.join(UPLOAD_DIR, name))
    return "Upload OK: " + name

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
