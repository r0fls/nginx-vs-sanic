from sanic import Sanic
from sanic.response import text

app = Sanic()

@app.route("/api1", host="example.com")
async def hello():
    return text("hello1")

@app.route("/api2", host="sub.example.com")
async def hello():
    return text("hello2")

app.run(host="0.0.0.0", port=80)
