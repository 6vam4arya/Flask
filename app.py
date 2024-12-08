from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/storedata',methods=['POST'])
def store_data():
    if request.method=='POST':
        form_dict=request.form
        return render_template('store_data_app.html',dict=form_dict)

if __name__=="__main__":
    app.run(debug=True)
