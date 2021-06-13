from flask import Flask, request, make_response, redirect
from html_pages import login_html, signup_html, cabinet_html
from work_with_db import *

def create_list_html(posts):
    text_post = ""
    for post in posts:
        text_post+=f"<li><b>{post[0]}</b><br/>{post[1]}</li>"
    return text_post

app = Flask(__name__)


@app.route("/")
def hello_world():
    posts = select_all_posts()
    text_posts = create_list_html(posts)
    return f"""
        <ul>{text_posts}</ul>
        <p>
            <a href="http://127.0.0.1:5000/signup">Sign up</a>
        </p>
        <p>
            <a href="http://127.0.0.1:5000/login">Log in</a>
        </p>"""


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
        return signup_html


@app.route("/login", methods = ["get", "post"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user_exist = user_exist_in_db(email, password)
        if user_exist:
            resp = make_response("<h1>Welcome to site</h1>")
            resp.set_cookie("email", email )
            resp.set_cookie("password", password, max_age = 60*60*24)
            return resp
        else:
            if user_exist == None:
                return "There is problem with database"
            return "Such user does not exist"

    else:
        return login_html

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
        if request.cookies.get("email") and request.cookies.get("password"):
            return cabinet_html
        else:
            return redirect("/login", code=302)

if __name__ == "__main__":
	app.run(debug=True)
