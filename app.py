#Vamika Arya
from flask import Flask, redirect, url_for, request
import csv
file=open("form.csv","w")
app=Flask(__name__)
#First Binding for greeting the user
@app.route("/<user>")
def greet(user):
    return f'<html><body><h1><style="color:pink">Welcome {user}</h1></body></html>'
#Second Binding for handling the requests
@app.route('/store data',methods=["POST","GET"])
def handling_data():
    if request.method=="POST":
        user_name=request.form["user"]
        writer=csv.writer(file)
        writer.writerows(user_name)
        return redirect(url_for('greet',user=user_name))
    else:
        user=request.args.get["user"]
        return redirect(url_for(greet,user=user))
if (__name__=="__main__"):
    app.run(debug=True)


        
    