from flask import Flask, render_template
import os
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/browse")
def browse():
    path = "C:\\"
    p = Path(path)

    dirs = []
    files = []

    for item in p.iterdir():
        if item.is_dir():
            dirs.append(item)
        elif item.is_file():
            files.append(item)

    return render_template(
        "dashboard.html",
        dirs=dirs,
        files=files,
        current_path=str(p)
    )
@app.route('/notes')
def notes():
    return render_template("notes.html")
if __name__ == "__main__":
    app.run(debug=True)
