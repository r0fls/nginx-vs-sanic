from sanic import Sanic
from sanic.response import text

app = Sanic()

@app.route("/api1")
async def hello():
    return text("hello1")

@app.route("/api2")
async def hello():
    return text("hello2")

app.run(host="0.0.0.0", port=80)
