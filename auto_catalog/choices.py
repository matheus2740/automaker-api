# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Choices(object):
    """
    A class to encapsulate handy functionality for lists of choices
    for a Django model field.

    Each argument to ``Choices`` is a choice, represented as a three-tuple.

    When a triple is provided, the first item is the database
    representation, the second a valid Python identifier that can be
    used as a readable label in code, and the third the human-readable
    presentation. This is most useful when the database representation
    must sacrifice readability for some reason: to achieve a specific
    ordering, to use an integer rather than a character field, etc.

    Regardless of what representation of each choice is originally
    given, when iterated over or indexed into, a ``Choices`` object
    behaves as the standard Django choices list of two-tuples.

    the Python identifier names can be accessed as attributes on the
    ``Choices`` object, returning the database representation.

    Option groups can also be used with ``Choices``; in that case each
    argument is a tuple consisting of the option group name and a list
    of options, where each option in the list is a triple as outlined above.
    """

    def __init__(self, *choices):
        self._triples = []  # list of choices expanded to triples - can include optgroups
        self._doubles = []  # list of choices as (db, human-readable) - can include optgroups
        self._display_map = {}  # dictionary mapping db representation to human-readable
        self._identifier_map = {}  # dictionary mapping Python identifier to db representation
        self._db_values = set()  # set of db representations

        self._process(choices)

    def _store(self, triple, triple_collector, double_collector):
        self._identifier_map[triple[1]] = triple[0]
        self._display_map[triple[0]] = triple[2]
        self._db_values.add(triple[0])
        triple_collector.append(triple)
        double_collector.append((triple[0], triple[2]))

    def _process(self, choices, triple_collector=None, double_collector=None):
        if triple_collector is None:
            triple_collector = self._triples

        if double_collector is None:
            double_collector = self._doubles

        for choice in choices:
            if not isinstance(choice, (list, tuple)) or len(choice) != 3:
                raise ValueError('Choices need to be a list of length 3')

            self._store(choice, triple_collector, double_collector)

    def __len__(self):
        return len(self._doubles)

    def __iter__(self):
        return iter(self._doubles)

    def __getattr__(self, attname):
        try:
            return self._identifier_map[attname]
        except KeyError:
            raise AttributeError(attname)

    def __getitem__(self, key):
        return self._display_map[key]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._triples == other._triples
        return False

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__, ', '.join((repr(i) for i in self._triples))
        )

    def __contains__(self, item):
        return item in self._db_values


class ChoicesMeta(type):
    """
        Metaclass to allow for 'class-like' choices.
        You can specify values as 2-tuples or simple values.
        2-tuples are in the form (value, verbose_name : str).

        Examples:
            class SecurityClearance(metaclass=ChoicesMeta):

                NO_CLEARANCE = 1
                BLUE = 2
                GREEN = 3
                YELLOW = 4
                RED = 5
                TOP_SECRET = 6
                STATE_SECRETS = 7

            class SecurityClearance(metaclass=ChoicesMeta):

                NO_CLEARANCE = (1, 'No Clearance')
                BLUE = (2, 'Blue Clearance')
                GREEN = (3, 'Green Clearance')
                YELLOW = (4, 'Yellow Clearance')
                RED = (5, 'Red Clearance')
                TOP_SECRET = (6, 'Top Secret Clearance')
                STATE_SECRETS = (7, 'State Secrets Clearance')

    """
    ALLOWED_TYPES = (int, float, str, bool, tuple)

    def __init__(cls, name, bases, dct):
        super(ChoicesMeta, cls).__init__(name, bases, dct)
        choices = [] if not bases else list(bases[-1].choices._triples)

        for key, val in dct.items():
            if key.startswith('__') or key.startswith(f'_{name}__') or key == 'Meta' or not isinstance(val, ChoicesMeta.ALLOWED_TYPES):
                continue

            db_value = val
            variable = key
            description = key

            if isinstance(val, tuple):
                if len(val) != 2:
                    raise ValueError('Tuple values for Choices must have 2 elements, in the format (db_value, description)')

                db_value, description = val

            choice = (db_value, variable, description)
            choices.append(choice)
            delattr(cls, key)  # __getattr__ Called when an attribute lookup has not found the attribute in the usual places

        cls.choices = Choices(*sorted(choices))

    def __call__(cls):
        return cls.choices

    def __len__(cls):
        return cls.choices.__len__()

    def __iter__(cls):
        return cls.choices.__iter__()

    def __getattr__(cls, name):
        return cls.choices.__getattr__(name)

    def __getitem__(cls, key):
        return cls.choices.__getitem__(key)

    def __eq__(cls, other):
        if isinstance(other, cls.__class__):
            return cls.choices == other.choices
        return False

    def __contains__(cls, item):
        return cls.choices.__contains__(item)

    def __repr__(cls):
        return cls.choices.__repr__()
