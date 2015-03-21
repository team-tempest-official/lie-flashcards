import sqlite3
from model.attribute import Attribute
from model.card import Card
from model.deck import Deck
from model.answer import Answer
from model.question import Question

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

	def populate(self):
		pass

	def get_deck(self, _id):
		if self.mode == LAZY:
			populate()

		for d in self.decks:
			if d._id == _id:
				return d

	def remove_deck(self, _id):
		for it in length(self.decks):
			if self.decks[it]._id == _id:
				try:
					self.cursor.execute("delete from deck_card_relation where d_id = ?", (_id,))
					self.cursor.execute("delete from decks where id = ?", (_id, ))
					del self.decks[it]
				except sqlite3.Error, e:
					pass

