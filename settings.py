import dotenv
import os

dotenv.load_dotenv(".env")

dbname = os.environ["DBNAME"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]

dev_db_settings = {'dbname': dbname,
					'user': user,
					'password': password,
					'host': host}