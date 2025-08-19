from flask import Flask, request, render_template

print("start flask ...")

# easy web framework
# based on: Web Server Gateway interface,WSGI
app = Flask(__name__)

# @app.route("/")
# def hello():
#     # create hello world html
#     print("Hello")
#     return "Hello World"

@app.route(      "/",
    methods=["GET", "POST"])
    # route是路由，将URL: / 映射到home函数（默认）
    # @app.route('/about')   这个是映射到about函数上

def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, port = 5001)

