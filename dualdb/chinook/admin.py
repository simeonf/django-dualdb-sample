from chinook import models as chinook_models
from django.contrib import admin
from django.db.models.base import ModelBase

# Very hacky!
for name, var in chinook_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)

