import sqlite3

class Info:
	def __init__(self):
		self.conn =sqlite3.connect("Airways_data.db")
		self.c =self.conn.cursor()

	def create_table(self):
		self.c.execute("""CREATE TABLE IF NOT EXISTS info(
			id INTEGER,
			username varchar(30),
			firstname varchar(30),
			phone_number INTEGER NULL
			)""")

	def users(self, idi):
		self.c.execute("SELECT id, username FROM info")
		data =self.c.fetchall()
		return data

	def check(self, idi):
		self.c.execute(f"SELECT id FROM info WHERE id={idi}")
		data =self.c.fetchone()
		return data

	def check_num(self, idi):
		self.c.execute(f"SELECT phone_number FROM info WHERE id={idi}")
		data =self.c.fetchone()
		return data

	def insert(self, idi, username, firstname):
		self.c.execute("INSERT INTO info VALUES('{}', '{}', '{}', NULL)".format(idi, username, firstname))
		return self.conn.commit()

	def update_num(self, idi, number):
		self.c.execute(f"UPDATE info SET phone_number= {number} WHERE id={idi}")
		return self.conn.commit()

	def user_entry_info(self, idi):
		self.c.execute(f"SELECT * FROM info WHERE id={idi}")
		user_entry_info =self.c.fetchone()
		return user_entry_info

	def users_id(self):
		self.c.execute("SELECT id,username FROM info")
		user_id =self.c.fetchall()
		return user_id

	def user_counter(self, idi):
		self.c.execute(f"SELECT COUNT(id) FROM info")
		user_counter =self.c.fetchall()
		return user_counter
