from flask import Flask,render_template
app=Flask(__name__)
dec=[{"noureddine":20,"ahmed":22},{"imgharn":20,"ahmed":20}]
@app.route("/")
def hello ():
    return render_template('home.html',dec=dec)
if __name__=="__main__" :
    app.run(debug=True)