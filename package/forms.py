from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
class registreform(FlaskForm) :
    fname=StringField("first name",validators=[DataRequired(),Length(min=5,max=20) ])
    lname=StringField("last name",validators=[DataRequired(),Length(min=5,max=20) ])
    username=StringField("first name",validators=[DataRequired(),Length(min=5,max=20) ])
    email=StringField("EMAIL",validators=[DataRequired(),Email() ])
    password=PasswordField("password",validators=[DataRequired(),Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', message="Le mot de passe doit contenir au moins 8 caractères, une lettre et un chiffre")])
    confirm_password=PasswordField("confirm_pasword",validators=[DataRequired(),EqualTo("password")])  
    submit=SubmitField("signeup")  
class loginfrom(FlaskForm):
    
    email=StringField("EMAIL",validators=[DataRequired(),Email() ])
    password=PasswordField("password",validators=[DataRequired()])
    remembre=BooleanField("Remember me")
    submit=SubmitField("signeup") 
