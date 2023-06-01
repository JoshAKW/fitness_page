from flask import Flask, render_template, url_for, flash, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired,  Email, EqualTo, Length
from wtforms.widgets import TextArea
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, date
from email_validator import EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import os
from f_forms import LoginForm, PostForm, UserForm, AnatomyForm, PasswordForm, SearchForm, WorkoutForm
from flask_ckeditor import CKEditor
# create a flask instance
app = Flask(__name__)  # helps Flask find all the files in the directory

# add ckeditor
ckeditor = CKEditor(app)

# need to create a secret key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySQLPassword!1@localhost/fitness'
# initialize the database

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Flask Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


with app.app_context():
    db.create_all()


# create a route decorator

# Create Admin Page
@app.route('/admin')
@login_required
def admin():
    id = current_user.id
    if id == 1:
        return render_template('admin.html')
    else:
        flash("Sorry you must be the Admin to access this page")
        return redirect(url_for('dashboard'))


# Create Dashboard Page
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = UserForm()
    id = current_user.id
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.username = request.form['username']
        try:
            db.session.commit()  # this one line updates the database
            flash("User Updated Successfully!")
            return render_template("dashboard.html", form=form, name_to_update=name_to_update)
        except:
            flash("Error! Looks like there was a problem. Try again please.")
            return render_template("dashboard.html", form=form, name_to_update=name_to_update)
    else:
        return render_template("dashboard.html", form=form, name_to_update=name_to_update, id=id)


# pass stuff to navbar, context procesor will pass things into our base file.


@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


# create Search Function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    posts = Posts.query
    if form.validate_on_submit():
        # get data from submitted form
        post.searched = form.searched.data
        # query the database
        posts = posts.filter(Posts.content.like('%' + post.searched + '%'))
        posts = posts.order_by(Posts.title).all()
        return render_template("search.html", form=form, searched=post.searched, posts=posts)

# create Login Page


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            # check hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Successful")
                return redirect(url_for('dashboard'))

            else:
                flash("Wrong password, try again please.")
        else:
            flash("User does not exist, try again.")

    return render_template('login.html', form=form)


# Create Logout function
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You are logged out.")
    return redirect(url_for('login'))


# add a forum page
@app.route('/posts')
def posts():

    # grab all the posts from the database
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template("posts.html", posts=posts)


# individual forum pages
@app.route('/posts/<int:id>')
def post(id):
    # this tries to find or passes a 404 if it doesn't exist
    post = Posts.query.get_or_404(id)

    return render_template('post.html', post=post)


# Add a forum Page
@app.route('/add-post', methods=['GET', 'POST'])
# @login_required
def add_post():
    form = PostForm()

    if form.validate_on_submit():
        poster = current_user.id
        post = Posts(title=form.title.data, content=form.content.data,
                     poster_id=poster, slug=form.slug.data)
        # clear the form
        form.title.data = ''
        form.content.data = ''
        # form.author.data = ''
        form.slug.data = ''
        # add post data to database
        db.session.add(post)
        db.session.commit()
        flash("Forum Post Submitted Successfully")

    # Redirect to the webpage
    # form equals form redirects back to the orignal form in the funtion
    return render_template("add_post.html", form=form)

# Add an edit post page


@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Posts.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():  # this mean we clicked the form, we want to validate submission
        post.title = form.title.data
        # post.author = form.author.data
        post.slug = form.slug.data
        post.content = form.content.data
        # update database
        db.session.add(post)
        db.session.commit()
        flash("Post has been edited.")
        return redirect(url_for('post', id=post.id))

    if current_user.id == post.poster.id:
        form.title.data = post.title
        # form.author.data = post.author
        form.slug.data = post.slug
        form.content.data = post.content
        return render_template('edit_post.html', form=form)

    else:
        flash("You are not authorized to edit this post")
        return render_template('post.html', post=post)

# delete Discussion Posts


@app.route('/posts/delete<int:id>')
@login_required
def delete_post(id):
    post_to_delete = Posts.query.get_or_404(id)
    id = current_user.id

    if id == post_to_delete.poster.id or id == 1:

        try:
            db.session.delete(post_to_delete)
            db.session.commit()

            # return a message
            flash("Forum post was deleted")

            posts = Posts.query.order_by(Posts.date_posted)
            return render_template("posts.html", posts=posts)

        except:
            # Return an error message
            flash("Whoops! There was a problem deleting post, try again.")
            posts = Posts.query.order_by(Posts.date_posted)
            return render_template("posts.html", posts=posts)

    else:
        # return a message
        flash("You are not authorized to delete that post")

        posts = Posts.query.order_by(Posts.date_posted)
        return render_template("posts.html", posts=posts)


@app.route('/delete<int:id>')
@login_required
def delete(id):
    if id == current_user.id:
        user_to_delete = Users.query.get_or_404(id)
        name = None
        form = UserForm()

        try:
            db.session.delete(user_to_delete)
            db.session.commit()
            flash("User deleted successfully.")

            our_users = Users.query.order_by(Users.date_add)
            return render_template("add_user.html", form=form, name=name, our_users=our_users)

        except:
            flash("Whoops problem deleting user, try again please.")
            return render_template("add_user.html", form=form, name=name, our_users=our_users)

    else:
        flash("Sorry, you can't delete that user.")
        return redirect(url_for('dashboard'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.username = request.form['username']
        try:
            db.session.commit()  # this one line updates the database
            flash("User Updated Successfully!")
            return render_template("update.html", form=form, name_to_update=name_to_update)
        except:
            flash("Error! Looks like there was a problem. Try again please.")
            return render_template("update.html", form=form, name_to_update=name_to_update)
    else:
        return render_template("update.html", form=form, name_to_update=name_to_update, id=id)


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            # Hash the Password
            hashed_pw = generate_password_hash(
                form.password_hash.data, "sha256")
            user = Users(username=form.username.data, name=form.name.data, email=form.email.data,
                         password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.username.data = ''
        form.email.data = ''
        form.password_hash = ''
        flash("User added successfully")
    our_users = Users.query.order_by(Users.date_add)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)


@app.route('/')
def home():
    
    text = "This is <strong> Bold</strong> Text"
    return render_template('home.html', text=text)


# create custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

# create name page


@app.route('/anatomy', methods=['GET', 'POST'])
def anatomy():
    name = None
    form = AnatomyForm()
    # validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Successful Retrieval")
    return render_template("anatomy.html", name=name, form=form)


@app.route('/posts')
# add a workout page
@app.route('/workouts')
def workouts():
    # grab all the workouts from the database
    workouts = Workouts.query.order_by(Workouts.date_posted)
    return render_template("workouts.html", workouts=workouts)


# individual workout pages
@app.route('/workouts/<int:id>')
def workout(id):
    # this tries to find or passes a 404 if it doesn't exist
    workout = Workouts.query.get_or_404(id)

    return render_template('workout.html', workout=workout)


# Add a Workout Page
@app.route('/add_workout', methods=['GET', 'POST'])
# @login_required
def add_workout():
    form = WorkoutForm()

    if form.validate_on_submit():
        worker = current_user.id
        workout = Workouts(title=form.title.data, exercise1=form.exercise1.data,
                           exercise2=form.exercise2.data,
                           exercise3=form.exercise3.data,
                           exercise4=form.exercise4.data,
                           exercise5=form.exercise5.data,
                           exercise6=form.exercise6.data,
                           exercise7=form.exercise7.data,
                           exercise8=form.exercise8.data,
                           exercise9=form.exercise9.data,
                           exercise10=form.exercise10.data,
                           exercise11=form.exercise11.data,
                           exercise12=form.exercise12.data,
                           worker_id=worker)
        # clear the form
        form.title.data = ''
        form.exercise1.data = ''
        form.exercise2.data = ''
        form.exercise3.data = ''
        form.exercise4.data = ''
        form.exercise5.data = ''
        form.exercise6.data = ''
        form.exercise7.data = ''
        form.exercise8.data = ''
        form.exercise9.data = ''
        form.exercise10.data = ''
        form.exercise11.data = ''
        form.exercise12.data = ''

        # add workout data to database
        db.session.add(workout)
        db.session.commit()
        flash("Workout ready to go!")

    # Redirect to the webpage
    # form equals form redirects back to the orignal form in the funtion
    return render_template("add_workout.html", form=form)

# Add an edit workout page


@app.route('/workouts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_workout(id):
    workout = Workouts.query.get_or_404(id)
    form = WorkoutForm()

    if form.validate_on_submit():  # this mean we clicked the form, we want to validate submission
        workout.title = form.title.data
        workout.exercise1 = form.exercise1.data
        workout.exercise2 = form.exercise2.data
        workout.exercise3 = form.exercise3.data
        workout.exercise4 = form.exercise4.data
        workout.exercise5 = form.exercise5.data
        workout.exercise6 = form.exercise6.data
        workout.exercise7 = form.exercise7.data
        workout.exercise8 = form.exercise8.data
        workout.exercise9 = form.exercise9.data
        workout.exercise10 = form.exercise10.data
        workout.exercise11 = form.exercise11.data
        workout.exercise12 = form.exercise12.data
        # update database
        db.session.add(workout)
        db.session.commit()
        flash("workout has been edited.")
        return redirect(url_for('workout', id=workout.id))

    if current_user.id == workout.worker.id:
        form.title.data = workout.title
        form.exercise1.data = workout.exercise1
        form.exercise2.data = workout.exercise2
        form.exercise3.data = workout.exercise3
        form.exercise4.data = workout.exercise4
        form.exercise5.data = workout.exercise5
        form.exercise6.data = workout.exercise6
        form.exercise7.data = workout.exercise7
        form.exercise8.data = workout.exercise8
        form.exercise9.data = workout.exercise9
        form.exercise10.data = workout.exercise10
        form.exercise11.data = workout.exercise11
        form.exercise12.data = workout.exercise12
        return render_template('edit_workout.html', form=form)

    else:
        flash("You can't edit this, only the creator can.")
        return render_template('workout.html', workout=workout)

# delete Forum Posts


@app.route('/workouts/delete<int:id>')
@login_required
def delete_workout(id):
    workout_to_delete = Workouts.query.get_or_404(id)
    id = current_user.id

    if id == workout_to_delete.worker.id or id == 1:

        try:
            db.session.delete(workout_to_delete)
            db.session.commit()

            # return a message
            flash("Workout was deleted")

            workouts = Workouts.query.order_by(workouts.date_posted)
            return render_template("workouts.html", workouts=workouts)

        except:
            # Return an error message
            flash("It didn't work, try again.")
            workouts = Workouts.query.order_by(workouts.date_posted)
            return render_template("workouts.html", workouts=workouts)

    else:
        # return a message
        flash("You can't edit this, only the creator can.")

        workouts = Workouts.query.order_by(workouts.date_posted)
        return render_template("workouts.html", workouts=workouts)

# models


class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    exercise1 = db.Column(db.String(250))
    exercise2 = db.Column(db.String(250))
    exercise3 = db.Column(db.String(250))
    exercise4 = db.Column(db.String(250))
    exercise5 = db.Column(db.String(250))
    exercise6 = db.Column(db.String(250))
    exercise7 = db.Column(db.String(250))
    exercise8 = db.Column(db.String(250))
    exercise9 = db.Column(db.String(250))
    exercise10 = db.Column(db.String(250))
    exercise11 = db.Column(db.String(250))
    exercise12 = db.Column(db.String(250))

    # Foreign Key to link users (refer to primary key of users)
    worker_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    # author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(255))  # this allows for a post address.
    # Foreign Key to link users (refer to primary key of users)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# Create Model
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)
    # User can have many posts
    posts = db.relationship('Posts', backref='poster')
    workouts = db.relationship('Workouts', backref='worker')
    # Create a String  this will put name on the screen if we want to return it.
    # now do password stuff
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        # this causes a error to flash if needed
        raise AttributeError('Password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Name %r>' % self.name

# app.run(debug=True)
