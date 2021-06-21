import dotenv
import os

try:
	dotenv.load_dotenv(".env")

	dev_db_settings = {'dbname': os.environ["DBNAME"],
						'user': os.environ["USER_DB"],
						'password': os.environ["PASSWORD"],
						'host': os.environ["HOST"]}

except Exception as ex:
	raise Exception("File .env is not found")