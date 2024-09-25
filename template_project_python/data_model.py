import datetime

from peewee import SqliteDatabase, Model, Database, PrimaryKeyField, CharField, DateTimeField, IntegerField, AutoField


class BaseModel(Model):
    pass


class Shelf(BaseModel):
    shelf_id = AutoField()
    description = CharField()
    creation_timestamp = DateTimeField(default=datetime.datetime.now)


class Item(BaseModel):
    item_id = AutoField()
    name = CharField()
    amount = IntegerField()
    modification_timestamp = DateTimeField()

    def save(self, *args, **kwargs):
        self.modification_timestampd = datetime.datetime.now()
        return super(Item, self).save(*args, **kwargs)