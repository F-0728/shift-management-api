import ulid

from django.db import models

# Create your models here.

class ULIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 26
        super(ULIDField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(26)'


class Shift(models.Model):

    id = ULIDField(
        default=ulid.new,
        primary_key=True,
        editable=False
    )
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    break_time = models.IntegerField()
    salary = models.IntegerField()
    transportation_fee = models.IntegerField()
    company_id = models.ForeignKey('companies.Company', on_delete=models.PROTECT)
