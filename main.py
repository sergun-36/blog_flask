from flask import Flask, request
import psycopg2
from html_pages import login_html, signup_html
from settings import dev_db_settings


app = Flask(__name__)


def connect_db(db_data):
    conn = psycopg2.connect(**db_data)
    return conn


def write_user(email, password):
    try:    
        conn = connect_db(dev_db_settings)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (email, password) VALUES('{email}', '{password}')")
        conn.commit()
        return True
    except Exception as ex:
        print(f"There is problem with database {ex}")
        return False
    finally:
        cursor.close()
        conn.close()
    


def user_exist_in_db(email, password):
    try:
        conn = connect_db(dev_db_settings)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE email='{email}' and password='{password}'")
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False

    except Exception as ex:
        print(f"There is problem with database {ex}")

    finally:
        cursor.close()
        conn.close()


def select_all():
    try:
        conn = connect_db(dev_db_settings)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users")
        result = cursor.fetchall()
        return result

    except Exception as ex:
        print(f"There is problem with database {ex}")
        
    finally:
        cursor.close()
        conn.close()

@app.route("/")
def hello_world():
    return """
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
            return "<h1>Welcome to site</h1>"
        else:
            if user_exist == None:
                return "There is problem with database"
            return "Such user does not exist"

    else:
        return login_html

if __name__ == "__main__":
	app.run(debug=True)
