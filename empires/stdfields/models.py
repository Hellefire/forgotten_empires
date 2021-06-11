# -*- coding: utf-8 -*-
# from https://bitbucket.org/roam/django-stdfields

from django.utils.encoding import smart_str


class Enumeration(object):
    """
    Simple enumeration object - subclasses should implement ``all``,
    mapping keys to values.
    """

    @classmethod
    def as_dict(cls):
        """
        Returns the key-label pairs of the enumeration.
        """
        return dict((k, v) for (k, v) in cls.all())

    @classmethod
    def as_list(cls):
        """
        Returns a list of the key-label pairs of the enumeration.
        """
        item_list = []
        item_dicts = dict((x, y) for x, y in cls.all())
        for key, label in item_dicts.items():
            if key:
                temp = {"key": key, "label": label}
                item_list.append(temp)
        return item_list

    @classmethod
    def as_display(cls, key):
        """Returns the label or display value of the key."""
        return cls.as_dict().get(key, None)

    @classmethod
    def all(cls):
        """
        Returns all key-label pairs as a list of tuples.

        Useful to pass on to a field as the possible choices. Will be used
        internally by the customer enum fields. Should be *implemented* by 
        subclasses if they provide no value for the ``enumeration`` field.
        """
        return cls.enumeration

    @classmethod
    def filter(cls, allowed_values):
        """
        Filters and returns all key-label pairs as a list of tuples for values
        that match the allowed_values.
        """
        filtered_list = []
        for value in cls.all():
            if value[0] in allowed_values:
                filtered_list.append(value)

        return filtered_list

    @classmethod
    def max_length(cls):
        """
        Calculates the maximum length of the key.

        You can set the ``max_length`` value of a ``CharField`` or
        ``EnumCharField`` to the result of this method. That way South will be
        able to pick up any changes to the maximum key length automatically.
        """
        keys = [smart_str(x[0]) for x in cls.all()]
        value = max(keys, key=lambda x: len(x))
        return 1 if not value else len(value)


class EnumValue(object):
    """
    An EnumValue is basically a wrapper for tuples, adding a counter that 
    allows us to keep them in the order they were defined.
    """
    creation_counter = 0

    def __init__(self, key, label):
        self.key = key
        self.label = label
        # Use the same trick Django uses to keep the order
        self.creation_counter = EnumValue.creation_counter
        EnumValue.creation_counter += 1

    def as_tuple(self):
        return (self.key, self.label)


class EnumMetaclass(type):
    """
    Metaclass for Enum that will turn an Enum with EnumValue fields into an 
    Enumeration instance.
    """

    def __new__(cls, name, bases, attrs):
        enum_values = [(name, value) for name, value in attrs.items()
                            if isinstance(value, EnumValue)]
        enum_values.sort(key=lambda x: x[1].creation_counter)
        for (name, value) in enum_values:
            attrs[name] = value.key
        tuples = [e[1].as_tuple() for e in enum_values]
        previous_enumerations = []
        for base in bases[::1]:
            if hasattr(base, 'enumeration'):
                previous_enumerations = [x for x in base.enumeration]
        attrs['enumeration'] = previous_enumerations + tuples
        for (name, value) in enum_values:
            attrs['%s_display' % (name)] = value.label
        return super(EnumMetaclass, cls).__new__(cls, name, bases, attrs)


class Enum(Enumeration, metaclass=EnumMetaclass):
    """
    An easier to use version of ``Enumeration``, which will grab the possible
    values from the defined ``EnumValue`` fields::

        class Color(Enum):
            RED = EnumValue('R', 'Red')
            GREEN = EnumValue('G', 'Green')
            BLUE = EnumValue('B', 'Blue')

        class Pencil(models.Model):
            color = EnumCharField(choices=Color.all())

        Pencil.objects.filter(color=Color.RED)

    This is the equivalent of::

        class Color(Enumeration):
            enumeration = [
                ('R', 'Red'),
                ('G', 'Green'),
                ('B', 'Blue')
            ]

        class Pencil(models.Model):
            color = EnumCharField(choices=Color.all())

        Pencil.objects.filter(color=Color.RED)

    But ``Enum`` also provides a ``FIELD_display`` field for each value::

        Color.RED_display == 'Red'
        Color.BLUE_display == 'Blue'
    """
