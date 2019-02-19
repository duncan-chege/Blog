from flask import render_template,redirect,url_for,flash,request
from ..models import Writer
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,login_required,logout_user
from .. import db
from . import auth


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        writer = Writer.query.filter_by(email = login_form.email.data).first()
        if writer is not None and writer.verify_password(login_form.password.data):
            login_user(writer,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.profile', w_id = writer.id))

        # flash('Invalid name or password')

    title='Techie Talk login'
    return render_template('auth/login.html',login_form = login_form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()

    flash('You have been logged out.')
    return redirect(url_for("main.index"))      #redirect url for the main index function

@auth.route('/register',methods = ["GET","POST"])
def register():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        writer = Writer(email = rform.email.data, name = rform.name.data, password = rform.password.data)
        db.session.add(writer)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Writer Account"
    return render_template('auth/register.html',registration_form = rform)