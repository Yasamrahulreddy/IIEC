from flask import Flask,request,render_template

app=Flask('myiiec')

@app.route('/form')

def myform():
    return render_template("basic.html")

@app.route('/name/<y>')
def myname(y):
    return y.upper()

@app.route('/data',methods=['POST'])
def mydata():
    if request.method=='POST':
        data=request.form.get("x")
        print(data)
    return data.upper()

app.run(port=5555,debug=True)