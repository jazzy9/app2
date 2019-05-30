
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
import tweepy


app = Flask(__name__)

#secret key that can prevent cybreattacks and information theft
app.config['SECRET_KEY'] = 'HSj5QhqDYETstW49L9GMOOhHwP52eYlW'

#posts contained within a list
posts = [{'author': 'Londonder 1',
            'title': 'Cahoots review',
            'content': 'Glamorous coctail bar',
            'date_posted': 'April, 2019'},
 { 'author': 'Londoner 2',
 'title': 'Candeligth Club - review ',
 'content': 'A dazzling, clandestine pop-up cocktail bar with a 1920s speakeasy flavour in a secret den lit entirely by candles',
 'date_posted': 'May, 2019'}]

#--  decorators --#

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title=about)


@app.route("/quiz")
def quiz():
    return render_template('quiz.html', title=quiz)

@app.route("/tweets")
def quiz():
    return render_template('tweets.html', title=tweets)



@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    #return render_template('register.html', title ='Register', form = form)
    if form.validate_on_submit():
            flash('Account created ', 'success')
            #return redirect(url_for('home'))
            return ('Account created successfully', 'success')
    return render_template('register.html', title ='Register', form = form)


@app.route("/login", methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')

            return redirect(url_for('home'))

        else:
            flash('Login unsuccessful. Please check your username and password', 'danger')

    return render_template('login.html', title ='Login', form = form)




#@app.route("/home")
#def home():
    #return render_template('home.html', posts=posts)


#@app.route("/about")
#def about():
    #return render_template('about.html', title='About')



#@app.route("/register")
#def register():
        #form = RegistrationForm()
        #return render_template('register.html', title='Register', form = form)


#@app.route("/login")
#def register():
        #form = RegistrationForm()
        #return render_template('register.html', title='Register', form = form)





if __name__ == '__main__':
    app.run(debug=True)
