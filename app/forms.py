from Flask_wtf import FlaskForm   # type: ignore
from wtforms import StringField, PasswordField, SubmitField  # type: ignore
from wtforms.validators import DataRequired   # type: ignore

class loginform(FlaskForm ) :
    username =StringField("username",validators=DataRequired())
    password=StringField("password",validators=DataRequired())
    submit=SubmitField("sign in ")
class editname(FlaskForm ) :
    edited_username =StringField("username",validators=DataRequired())
    e_submit=SubmitField("update")

class editpassword(FlaskForm):
 edited_password=StringField("password",validators=DataRequired())
 e_submit=SubmitField("update")
 class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Search')
