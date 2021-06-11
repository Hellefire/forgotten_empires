# -*- coding: utf-8 -*-
# from https://bitbucket.org/roam/django-stdfields

from django.db import models


class EnumIntegerField(models.PositiveIntegerField):
    """
    Extension of a standard Django ``PositiveIntegerField`` that takes an
    optional ``enum`` argument which should point to an implementation of
    ``stdfields.models.Enumeration``.

    The results of the implementation's ``all`` method will be used as the
    possible choices.
    """

    description = "An enumeration of integer values"

    def __init__(self, *args, **kwargs):
        if 'enum' in kwargs:
            self.enum = kwargs.pop('enum')
            kwargs['choices'] = self.enum.all()
        super(EnumIntegerField, self).__init__(*args, **kwargs)


class EnumCharField(models.CharField):
    """
    Extension of a standard Django ``CharField`` that takes an optional
    ``enum`` argument which should point to an implementation of
    ``stdfields.models.Enumeration``.

    The results of the implementation's ``all`` method will be used as the
    possible choices.
    """

    description = "An enumeration of character values"

    def __init__(self, *args, **kwargs):
        if 'enum' in kwargs:
            self.enum = kwargs.pop('enum')
            choices = self.enum.all()
            kwargs['choices'] = choices
        else:
            choices = kwargs.get('choices', [])
        super(EnumCharField, self).__init__(*args, **kwargs)
