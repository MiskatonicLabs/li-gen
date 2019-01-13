from peewee import CharField, Model, SqliteDatabase, TextField

db = SqliteDatabase('licenses.db')


class License(Model):
    name = CharField()
    text = TextField()

    class Meta:
        database = db
