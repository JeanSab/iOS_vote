import db_tools


class DbUser:
	 
	def __init__(self):
		self.db = db_tools.getDB()
		self.cur = self.db.cursor()
		self.polls = []

	def getUserInfo(self, login):
		try:
			self.cur.execute("SELECT * FROM user WHERE login = %s", (login))
			return self.cur.fetchall()[0]
		except:
			self.db.rollback()
			
		


	def userInDb(self, login):
		self.cur.execute("SELECT count(1) FROM user WHERE login = %s", (login))
		return self.cur.fetchall()[0]["count(1)"] == 1



	def getToken(self, login):
		self.cur.execute("SELECT token FROM user WHERE login = %s", (login))
		return self.cur.fetchall()[0]
	

	def getAttempts(self, login):
		self.cur.execute("SELECT attempts FROM user WHERE login = %s", (login))
		return self.cur.fetchall()[0]


	def getId(self, login):
		self.cur.execute("SELECT id FROM user WHERE login = %s", (login))
		return self.cur.fetchall()[0]

	def changeToken(self, token, login, validity=0):
		try:
			self.cur.execute('UPDATE user SET token = %s, token_validity = %s WHERE login = %s;', (token, validity ,login))
			self.db.commit()
		except:
			self.db.rollback()


	def updateBanDate(self, login, banDate=0):

		#if banDate is None:
		#	banDate = "NULL"
		try:
			print("ban date-" + str(banDate))
			self.cur.execute('UPDATE user SET ban_date = %s WHERE login = %s;', (banDate ,login))
			self.db.commit()
		except:
			self.db.rollback()

	def getBanDate(self, login):
		self.cur.execute("SELECT ban_date FROM user WHERE login = %s", (login))
		return self.cur.fetchall()[0]

	def updateFailedAttempts(self, nbAttempts, login):
		self.cur.execute("UPDATE user SET attempts = %s WHERE login = %s;", (nbAttempts, login))
		self.db.commit()

	
	def updateTokenValidity(self, validity, login):
		self.cur.execute("UPDATE user SET token_validity = %s WHERE login = %s;", (validity, login))
		self.db.commit()
		

	def getFailedAttemps(self, login):
		self.cur.execute("SELECT attempts FROM user WHERE login = %s", (login))
		return self.cur.fetchall()[0]

	def insertUser(self, login, pwd, salt, token):
		#token = 123
		try:
			self.cur.execute("""INSERT INTO user (login, salted_pwd, salt, token) VALUES (%s, %s, %s, %s) """, (login, pwd, salt, token))
			self.db.commit()
		except:
			self.db.rollback()

