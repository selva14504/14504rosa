from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello from ROSA Assessment WebApp! ENV: {os.environ.get('APP_ENV')}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
