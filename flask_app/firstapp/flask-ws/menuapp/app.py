from flask import Flask
from flask import render_template
from flask import request

app=Flask("myapp")


@app.route("/")
def home():
    return "i m in home"


@app.route("/menu",methods=["GET"])
def mymenu():
    name=request.args.get('x')  
    sid=request.args.get('y')
    htmlcode=render_template("mymenu.html",myname=name,nname=sid)
    return htmlcode

@app.route("/form")
def myform():
    return render_template("myform.html")



