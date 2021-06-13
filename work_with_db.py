import psycopg2
from settings import dev_db_settings

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


def select_all_users():
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


def select_all_posts():
    try:
        conn = connect_db(dev_db_settings)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM articles")
        result = cursor.fetchall()
        return result

    except Exception as ex:
        print(f"There is problem with database {ex}")
        
    finally:
        cursor.close()
        conn.close()        


def write_new_post(title, text):
    try:    
        conn = connect_db(dev_db_settings)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO articles (title, text) VALUES('{title}', '{text}')")
        conn.commit()
        return True
    except Exception as ex:
        print(f"There is problem with database {ex}")
        return False
    finally:
        cursor.close()
        conn.close()