from django.db import models


class DeliveryMethod(models.Model):
    name = models.CharField(unique=True, max_length=32)
    description = models.TextField()

    class Meta:
        db_table = 'deliverymethod'

    def __str__(self):
        return self.name


class DurationType(models.Model):
    name = models.CharField(unique=True, max_length=32)
    description = models.TextField()

    class Meta:
        db_table = 'durationtype'

    def __str__(self):
        return self.name


class Effect(models.Model):
    description = models.TextField()

    class Meta:
        db_table = 'effect'

    def __str__(self):
        return self.description


class TargetType(models.Model):
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        db_table = 'targettype'

    def __str__(self):
        return self.name


class Version(models.Model):
    version = models.CharField(unique=True, max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    class Meta:
        db_table = 'version'

    def __str__(self):
        return self.version
