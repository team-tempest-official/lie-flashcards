import sqlite3
from information import Information
from attribute import Attribute
from card import Card
from deck import Deck
from answer import Answer
from question import Question
from eum import Enum

PATH = "../database.sqlite3"

class LoadMethod(Enum):
	LAZY = 1
	EAGER = 2

class Sqlite3Implementation(object):

	def __init__(self, method):
		self.connection = sqlite3.connect(PATH) 
		self.cursor = self.connection.cursor()

		self.decks = list()
		self.cards = list()
		self.answers = list()
		self.qas = list()
		self.information = list()
		self.attributes = list()

		self.method = method

	def __del__(self):
		self.connection.close()

	def add_deck(self):
		deck = Deck(list(), list())
		try:
			self.cursor.execute("insert into decks values()");
			self.cursor.execute("select id from decks order by id desc limit 1")
			deck._id = int(self.cursor.fetchone())
		except sqlite3.Error, e:
			print e

		self.decks.append(deck)	

		return deck	
	
