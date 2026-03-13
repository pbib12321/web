from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello! Your Python website is working 🚀</h1>"

@app.route("/about")
def about():
    return "<h2>This site is running on Flask.</h2>"

if __name__ == "__main__":
    app.run()
