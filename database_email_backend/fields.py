#-*- coding: utf-8 -*-
import base64
from django.db import models

# Stolen from http://djangosnippets.org/snippets/1669/
class Base64Field(models.TextField):

    def contribute_to_class(self, cls, name):
        if self.db_column is None:
            self.db_column = name
        self.field_name = name + '_base64'
        super(Base64Field, self).contribute_to_class(cls, self.field_name)
        setattr(cls, name, property(self.get_data, self.set_data))

    def get_data(self, obj):
        return base64.decodestring(getattr(obj, self.field_name))

    def set_data(self, obj, data):
        setattr(obj, self.field_name, base64.encodestring(data))

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules(
        [([Base64Field],[],{})],
        ["^database_email_backend\.fields\.Base64Field"]
    )
except ImportError:
    pass