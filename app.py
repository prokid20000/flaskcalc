from flask import Flask, request
import operations
app = Flask(__name__)

@app.get("/add")
def add_num():
    a = request.args["a"]
    b = request.args["b"]
    num = operations.add(int(a),int(b))
    return f"<html><body>{num}</body></html>"

