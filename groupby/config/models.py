# -*- coding: utf-8 -*-
#
# created by Kim

from mongoengine import Document
from mongoengine import EmbeddedDocument

from mongoengine import BooleanField
from mongoengine import EmbeddedDocumentField
from mongoengine import IntField
from mongoengine import StringField


class Mysql(EmbeddedDocument):
    host = StringField(required=True)
    user = StringField(required=True)
    password = StringField(required=True)
    port = IntField(required=True)
    dbname = StringField(required=True)
    pool_size = IntField(required=True)


class AppConfig(Document):
    mysql = EmbeddedDocumentField(Mysql, required=True)
    debug = BooleanField(required=True)
