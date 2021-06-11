from django.db import models


class CharClass(models.Model):
    name = models.CharField(unique=True, max_length=32)
    base_body = models.IntegerField()
    max_armour = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'class'

    def __str__(self):
        return self.name
