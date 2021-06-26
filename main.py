from flask import Flask, request, make_response, render_template, redirect
from work_with_db import *

def isautorizate(request):
    return bool(request.cookies.get("email") and request.cookies.get("password"))
    

app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello_world():
    posts = select_all_posts()
    if isautorizate(request):
        email = request.cookies.get("email")
    else:
        email = "Stranger"
    return render_template("home_html.html", email=email, posts=posts)


@app.route("/signup", methods = ["get", "post"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        result_of_write = write_user(email, password)
        if result_of_write:
            return "You sign up successfully"
        else:
            return "You don't sign up. Try one more"
    else:
        return render_template("signup_html.html")


@app.route("/login", methods = ["get", "post"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user_exist = user_exist_in_db(email, password)
        if user_exist:
            resp = make_response(redirect("/cabinet", code=302))#("<h1>Welcome to site</h1><a href='/cabinet'>To cabinet</a>")
            resp.set_cookie("email", email )
            resp.set_cookie("password", password, max_age = 60*60*24)
            return resp
        else:
            if user_exist == None:
                return "There is problem with database"
            return "Such user does not exist"

    else:
        return render_template("login_html.html", isautorizate=isautorizate(request))

@app.route("/cabinet", methods = ["get", "post"])
def cabinet():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        result_post = write_new_post(title, text)
        if result_post:
            return "Your post is added"
        else:
            return "Your post is NOT added"
    else:
        islogin =  isautorizate(request)
        email = request.cookies.get("email")
        return render_template("cabinet_html.html", isautorizate=islogin, email=email)

if __name__ == "__main__":
	app.run(debug=True)
