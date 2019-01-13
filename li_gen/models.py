from peewee import *


db = SqliteDatabase('licenses.db')


class License(Model):
    name = CharField()
    text = TextField()

    class Meta:
        database = db
