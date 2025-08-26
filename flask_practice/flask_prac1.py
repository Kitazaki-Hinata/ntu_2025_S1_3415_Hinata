# request 获得用户参数
from flask import Flask, request


app = Flask(__name__)    # create app

# enter url "/", then execute function INDEX
# 默认发送get请求，如果需要post请求就需要再加一个methods
@app.route("/index", methods = ["GET", "POST"])
def index():
    # 当输入这个网址，就会返回值 5001/index?age=180&pwd=123123
    age = request.args.get("age")
    pwd = request.args.get("pwd")
    print(age, pwd)

    # 获取json文件
    # request.json
    return "success"

# 当在端口后面再输入/main代码，就会导入到新的页面
@app.route("/main")
def main():
    return "yesss"

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5001)   # 指定端口
