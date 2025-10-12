from flask import Flask,render_template
from forms import registreform,loginfrom
app=Flask(__name__)
app.config['SECRET_KEY']='e861d5ca3a8eee5ac533994b07c0f983c6cdb33ba3fc6eccb09c12a683b8ac36'
@app.route("/")
def hello ():
    return render_template('home.html')
@app.route("/registre")
def registre ():
    form=registreform()
    return render_template('registre.html',form=form)
@app.route("/login")
def login ():
    form=loginfrom()
    return render_template('login.html',form=form)
if __name__=="__main__" :
    app.run(debug=True)
