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

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    #database
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    q = float(request.form.get("q"))
    return(render_template("dbs.html",r=(-50.6*q)+90.2))

if __name__ == "__main__":
    app.run(port = 5001)


