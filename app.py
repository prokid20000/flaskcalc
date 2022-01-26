from flask import Flask, request
import operations

app = Flask(__name__)


@app.get("/add")
def add_num():
    """Page showing addition of query params a and b"""
    a = request.args["a"]
    b = request.args["b"]
    num = operations.add(int(a), int(b))
    return f"<html><body>{num}</body></html>"


@app.get("/sub")
def sub_num():
    """Page showing subtraction of query params a and b"""
    a = request.args["a"]
    b = request.args["b"]
    num = operations.sub(int(a), int(b))
    return f"<html><body>{num}</body></html>"


@app.get("/mult")
def mult_num():
    """Page showing multiplication of query params a and b"""

    a = request.args["a"]
    b = request.args["b"]
    num = operations.mult(int(a), int(b))
    return f"<html><body>{num}</body></html>"


@app.get("/div")
def div_num():
    """Page showing division of query params a and b"""

    a = request.args["a"]
    b = request.args["b"]
    num = operations.div(int(a), int(b))
    return f"<html><body>{num}</body></html>"


# TODO: ADD DOCSTRINGS
