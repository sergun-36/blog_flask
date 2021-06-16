import dotenv
import os

try:
	dotenv.load_dotenv(".env")

	dbname = os.environ["DBNAME"]
	user = os.environ["USER_DB"]
	password = os.environ["PASSWORD"]
	host = os.environ["HOST"]

	dev_db_settings = {'dbname': dbname,
						'user': user,
						'password': password,
						'host': host}
except Exception as ex:
	raise Exception("File .env is not found")