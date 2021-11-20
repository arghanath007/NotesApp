from flask import Blueprint,render_template

auth=Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html') #Passing values to templates. We can pass multiple variables as well.  {% if boolean==True %} Yes it is correct {% elif %} It depends {% else %} No, it is false {% endif %} 


@auth.route('/logout')
def logout():
    return "<p>Logout Page</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')