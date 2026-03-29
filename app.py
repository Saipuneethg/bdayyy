from flask import Flask, render_template
import os

app = Flask(__name__)

# --- CONFIGURATION ---
HER_NAME = "Laddu"
UNLOCK_TIME_STR = "2026-04-03 00:00:00"

@app.route("/")
def home():
    return render_template("index.html", name=HER_NAME)

@app.route("/cringe.html")
def cringe():
    return render_template("cringe.html")

if __name__ == "__main__":
    # REQUIRED for deployment: Run on 0.0.0.0 and use heroku/render port
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
