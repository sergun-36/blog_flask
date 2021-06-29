from flask import Flask, request, make_response, render_template, redirect
from work_with_db import *
from models import User, Post, DeclarativeBase, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
#posts = select_all_posts()

posts_query = session.query(User).all()

def isautorizate(request):
    return bool(request.cookies.get("email") and request.cookies.get("password"))
    

app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello_world():
    session = Session()
    posts_query = session.query(Post).all()

    #posts = [post.__dict__ for post in posts_query]

    if isautorizate(request):
        email = request.cookies.get("email")
        name_query = session.query(User).filter(User.email==email).one()
        name = name_query.name
    else:
        name = "Stranger"
    return render_template("home_html.html", email=name, posts=posts_query)


@app.route("/signup", methods = ["get", "post"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        new_user = User(email = email, password = password, name=name)
        session = Session()


        try:
            user_exist = session.query(User).filter(User.email == email).one()# TO DO oNE
        except exc.NoResultFound as ex:
            user_exist = False        

        if not user_exist:
            session.add(new_user)
            session.commit()
            resp = make_response(redirect("/login", 302))
            return resp
        else:
            return render_template("signup_html.html", user_exist=user_exist)

    else:
        return render_template("signup_html.html", user_exist=False)


@app.route("/login", methods = ["get", "post"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        session = Session()
        
        try:
            user_exist = session.query(User).filter(User.email == email, User.password == password).one()# TO DO oNE
        except exc.NoResultFound as ex:
            user_exist = False
        
        
        if user_exist:
            resp = make_response(redirect("/cabinet", code=302))#("<h1>Welcome to site</h1><a href='/cabinet'>To cabinet</a>")
            resp.set_cookie("email", email )
            resp.set_cookie("password", password, max_age = 60*60*24)
            return resp
        else:
            return "Such user does not exist"

    else:
        return render_template("login_html.html", isautorizate=isautorizate(request))

@app.route("/cabinet", methods = ["get", "post"])
def cabinet():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        email = request.cookies.get("email")
        session = Session()
        try:
            user_query = session.query(User).filter(User.email == email).one()
            author = user_query.id
            new_post = Post(title = title, text = text, author = user_query.id)
            session.add(new_post)
            session.commit()
        except exc.NoResultFound as ex:
            return "Your post is NOT added"

        else:
            return "Your post is added"

    else:
        islogin =  isautorizate(request)
        email = request.cookies.get("email")
        session = Session()
        try:
            name = session.query(User).filter(User.email == email).one().name
        except exc.NoResultFound as ex:
            name = "Who are you?"
        return render_template("cabinet_html.html", isautorizate=islogin, name=name)

