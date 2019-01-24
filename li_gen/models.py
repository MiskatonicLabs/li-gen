from functools import total_ordering

from peewee import CharField, Model, TextField

from .config import Config


@total_ordering
class License(Model):
    name = CharField()
    text = TextField()

    class Meta:
        database = Config.db

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return self.name
