import sqlite3
import string

DB_PATH = "/tmp/data.db"

class PinBoardPost:
	def __init__(self, id=None):
		if id is not None:
			self.id = id

	def setAuthor(self, author):
		self.author = author

	def setPost(self, post):
		self.post = post

	def save(self):
		if self.author != None and self.post != None:
			db = sqlite3.connect(DB_PATH)
			cur = db.cursor() 
			cur.execute("INSERT INTO pinboard (\"author\", \"post\") VALUES (?, ?)", (self.author, self.post)) 
			db.commit()
			return True
		return False

	def delete(self):
			db = sqlite3.connect(DB_PATH)
			cur = db.cursor() 
			cur.execute("DELETE FROM pinboard WHERE id=?", (self.id, )) 
			db.commit()

def pinboard(phenny, input):
	args = input.group(2)

	if args == None:
		db = sqlite3.connect(DB_PATH)
		cur = db.cursor()    
		cur.execute("SELECT * FROM pinboard")
		rows = cur.fetchall()

		phenny.say("Pinboard content:")
		for row in rows:
			phenny.say("[ %d ][ %s ][ %s ]" % (row[0], row[1], row[2]))
		return

	args = args.split()

	if args[0] != "add" and args[0] != "delete" and args[0] != "del":
		phenny.say("Bad command. I understand \"add\", \"del\" and \"delete\" commands, try again!") 
		return

	if args[0] == "add":
		newPost = PinBoardPost()
		newPost.author = input.nick
		newPost.post = " ".join(args[1:])
		newPost.save()
		phenny.say("%s added message to the pinboard!" % input.nick)
		return

	if args[0] == "del" or args[0] == "delete":
		newPost = PinBoardPost(" ".join(args[1:]))
		newPost.delete()
		phenny.say("%s deleted message from the pinboard!" % input.nick)
		return

pinboard.commands = ["pb", "pinboard", "pin"]
pinboard.example = ".pb [add | del | delete [msg]]"
pinboard.priority = "low"
