from flask import Flask, session, redirect, url_for, escape, request, render_template,session
import logging
import sys

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route('/',methods=["GET","POST"])
def login():
    
    import sys
    
    print('login page loaded', file=sys.stderr)
    error = ''
    try:
        print('inside try', file=sys.stderr)
        if request.method == "POST":
            print(f"recieved data is {request.form['username']}",file=sys.stderr)
            print(f"recieved data is {request.form['password']}",file=sys.stderr)
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            print(attempted_username,file=sys.stderr)
            #flash(attempted_username)
            #flash(attempted_password)
            if attempted_username == "admin@admin.com" and attempted_password == "password":
                session["user"] = attempted_username
                return redirect(url_for('homepage'))
				
            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("login.html", error = error)  
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('homepage'))
    return flask.render_template('login.html', form=form)
"""
@app.route('/homepage/')
def homepage():
    return render_template('homepage.html')
if __name__ == "__main__":
    
    app.run(debug=True)
