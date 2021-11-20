from flask import Blueprint,render_template,request,flash,redirect,url_for
from website.models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,login_user,logout_user,current_user

from website import db

auth=Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():

    if request.method =='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Successfully logged in!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Email does not exist', category='error')

    return render_template('login.html', user=current_user) #Passing values to templates. We can pass multiple variables as well.  {% if boolean==True %} Yes it is correct {% elif %} It depends {% else %} No, it is false {% endif %} 


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password=request.form.get('password')
        confirmedPassword=request.form.get('confirmedPassword')

        user=User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists:', category='error')

        elif len(email) <4:
            flash('Email must be greater than 3 characters.', category='error')

        elif len(firstName) <10:
            flash('First Name must be greater than 9 characters.', category='error')

        elif password != confirmedPassword:
            flash('Passwords does not match', category='error')

        else:
            # Adding the user to the database

            # Creating a new user.
            new_user=User(email=email,firstName=firstName,password=generate_password_hash(password,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)

            flash('Accounted successfully created', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html',user=current_user)