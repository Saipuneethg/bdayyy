from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# --- CONFIGURATION ---

# 1. Her Name
HER_NAME = "Bestie"

# 2. Time the website unlocks
# Format: "YYYY-MM-DD HH:MM:SS"
# Example: Midnight of March 14th, 2026 -> "2026-03-14 00:00:00"
UNLOCK_TIME_STR = "2026-03-14 00:00:00"

@app.route("/")
def home():
    # TEMPORARY: Unlocking the website immediately for testing!
    return render_template("index.html", name=HER_NAME)

if __name__ == "__main__":
    print("-" * 50)
    print(f"Birthday Server Starting!")
    print(f"Make sure you place 11 photos named 1.jpg to 11.jpg inside 'static/photos/'")
    print("-" * 50)
    app.run(debug=True, port=5000)
