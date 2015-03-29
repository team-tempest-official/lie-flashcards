import sqlite3

class DatabaseManager(object):

    @classmethod
    def start(cls):
        Deck.start()

    @classmethod
    def shut_down(cls):
        Deck.shut_down()

class Deck(object):
    con = sqlite3.connect('development.sql')

    def __init__(self, name=""):
        self.name=name

    @classmethod
    def create(cls, name):
        cursor = cls.con.cursor()
        try:
            cursor.execute('INSERT INTO DECKS VALUES(?)', (name,))
            cls.con.commit()
            return Deck(name=name)
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error %s" % e.args[0]

    @classmethod
    def get(cls, name):
        cursor = cls.con.cursor()
        try:
            cursor.execute('SELECT * FROM DECKS WHERE NAME = ?', (name,))
            res = cursor.fetchone()
            if res:
                return Deck(res[0])
            else:
                raise(sqlite3.Error(': object does not exist'))
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error %s" % e.args[0]

    @classmethod
    def remove(cls, name):
        cursor = cls.con.cursor()
        try:
            cursor.execute('DELETE FROM DECKS WHERE NAME = ?', (name,))
            cls.con.commit()
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error %s" % e.args[0]

    @classmethod
    def clear(cls):
        cursor = cls.con.cursor()
        try:
            cursor.execute('DELETE FROM DECKS')
            cls.con.commit()
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error %s" % e.args[0]

    @classmethod
    def shut_down(cls):
        if cls.con:
            cls.con.close()

    def update(self, name):
        cursor = Deck.con.cursor()
        try:
            cursor.execute('UPDATE DECKS SET NAME = ? WHERE NAME = ?', (name,self.name))
            Deck.con.commit()
        except sqlite3.Error, e:
            Deck.con.rollback()
            print "Error(update) %s" % e.args[0]


class Card(object):

    def __init__(self, deck, content, type, answers):
        self.deck = deck
        self.type = type
        self.content = content
        self.answers = answers


class Answer(object):

    def __init__(self, card, a_text):
        self.a_text
        self.card = card

