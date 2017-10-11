# ASE---toy system----CALCULATOR

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/results")
def members():
    return "Members"

#basic display - printing a string
@app.route("/members/<string:name>/")
def getMember(name):
    return name
if __name__ == "__main__":
    app.run()
    

#addition operation - e.g /add/7+3
@app.route("/add/<string:nums>/")
def add(nums):
    v=nums.split('+')
    v[0]=int(v[0])
    v[1]=int(v[1])
    return str(v[0]+v[1])

#subtraction operation - e.g. /sub/13-2
@app.route("/sub/<string:nums>/")
def sub(nums):
    v=nums.split('-')
    v[0]=int(v[0])
    v[1]=int(v[1])
    return str(v[0]-v[1])

#multiplication operation - e.g. /mul/12*5
@app.route("/mul/<string:nums>/")
def mul(nums):
    v=nums.split('*')
    v[0]=int(v[0])
    v[1]=int(v[1])
    return str(v[0]*v[1])

#division operation - e.g. /div/8div2
@app.route("/div/<string:nums>/")
def div(nums):
    v=nums.split('div')
    v[0]=int(v[0])
    v[1]=int(v[1])
    return str(v[0]/v[1])
