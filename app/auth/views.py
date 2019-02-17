from flask import render_template,redirect,url_for,flash,request
from ..models import Writer
from .forms import LoginForm
from flask_login import login_user,login_required
from .. import db
from . import auth


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        writer = Writer.query.filter_by(email = login_form.email.data).first()
        if writer is not None and writer.verify_password(login_form.password.data):
            login_user(writer,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid name or password')

    title='Techie Talk login'
    return render_template('auth/login.html',login_form = login_form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

