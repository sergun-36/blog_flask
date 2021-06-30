import dotenv
import os

try:
	dotenv.load_dotenv(".env")

	dev_db_settings = {'database': os.environ["DBNAME"],
						'username': os.environ["USER_DB"],
						'password': os.environ["PASSWORD"],
						'host': os.environ["HOST"],
						'drivername': 'postgresql+psycopg2'}

except Exception as ex:
	raise Exception("File .env is not found")