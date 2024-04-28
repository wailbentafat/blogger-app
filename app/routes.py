from flask_login import current_user, login_user, logout, login_required
from flask import render_template, redirect, url_for, flash
from app import app , db
from app.forms import loginform , editname,editpassword
from app.functions import check
from app.models import user

@app.route('/login', methods=['GET', 'POST'])
def lgin():
    form = loginform()

    if form.validate_on_submit():
        curent_user = user.query.filter_by(username=form.username.data).first()

        if curent_user and curent_user.check_password(form.password.data):
                login_user(curent_user)
                   
                return redirect(url_for('dashboard'))
        else:
                flash('Username or password is incorrect.', 'error')
    
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
      form=editpassword()
      e_form=editname()
      if form.validate_on_submit():
        message , accept=check(form.edited_password.data)
        if accept:
          current_user.password=form.edited_password.data
          db.session.commit()
          redirect(url_for('dashboard'))
        else:
          flash(message,'ereur')
          redirect(url_for('dashboard')) 
          
      if e_form.validate_on_submit():
       current_user.username=form.edited_username.data
       db.session.commit()
       redirect(url_for('dashboard'))
  
      return render_template('dashboard.html',user=current_user)
   


   
@app.route('/', methods=['GET', 'POST'])
def index():
    form = loginform()#we use it to create new user

    if form.validate_on_submit():
         username=form.username.data
         password=form.password.data
         message,accept=check(password)
         if accept:
               new_user=(username,password)
               db.sesssion.add(new_user)
               db.commit()
               login_user(new_user)    
               return redirect(url_for('dashboard'))
         else:
                flash(password, 'error')
    
    return render_template('signup.html', form=form)

