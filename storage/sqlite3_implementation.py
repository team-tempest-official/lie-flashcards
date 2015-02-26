import sqlite3
from information import Information
from attribute import Attribute
from card import Card
from deck import Deck
from answer import Answer
from question import Question

PATH = "../database.sqlite3"

class Sqlite3Implementation(object):

	def __init__(self):
		self.connection = sqlite3.connect(PATH) 

	def __del__(self):
		self.connection.close()

	
