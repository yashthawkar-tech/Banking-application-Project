from flask import Flask,render_template #it will consider all files in template folder
app=Flask(__name__) #object Named as App

@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)