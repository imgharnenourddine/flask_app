from package import app
from flask import render_template,url_for,redirect,flash
from forms import registreform,loginfrom
@app.route("/")
@app.route("/home")
def home ():
    return render_template('home.html')
@app.route("/registre", methods=['GET', 'POST'])
def registre():
    form = registreform()

    

    if form.validate_on_submit():
        
        flash(f"Vous avez créé votre compte avec succès {form.fname.data} {form.lname.data}", "success")
        return redirect(url_for('login'))

    return render_template('registre.html', form=form)
@app.route("/login",methods=['GET','POST'])
def login ():
    form=loginfrom()
    if form.validate_on_submit() :
        if form.email.data=="imgharnenourddine3@gmail.com" and form.password.data=="noureddine188" :
            flash (f"vous avez connecter a votre compte avec succes","succes")
            return redirect(url_for('home'))  
        else :
            flash (f" votre login est echouer vouller entrer vous donnees correct","danger")
            return redirect(url_for('login'))
        
    return render_template('login.html',form=form)