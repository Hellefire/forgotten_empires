from django.db import models


class Race(models.Model):
    name = models.CharField(unique=True, max_length=32)
    attribute_points = models.PositiveSmallIntegerField()
    description = models.TextField()
    costume_req = models.TextField(blank=True, null=True)
    costume_sugg = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'race'

    def __str__(self):
        return self.name


class SubRace(models.Model):
    name = models.CharField(unique=True, max_length=32)
    race = models.ForeignKey(Race, models.RESTRICT)
    attribute_points = models.PositiveSmallIntegerField()
    description = models.TextField()
    costume_req = models.TextField()
    costume_sugg = models.TextField()

    class Meta:
        db_table = 'subrace'

    def __str__(self):
        return '{} {}'.format(self.name, str(self.race))
