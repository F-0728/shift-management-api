import ulid

from django.db import models

# Create your models here.

class ULIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 26
        super(ULIDField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(26)'


class Company(models.Model):

    id = ULIDField(
        default=ulid.new,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name
