# -*- coding: utf-8 -*-

import collections


def stub_validator(value):
    pass


class Object(object):
    def __init__(self, *method_names, **methods):
        for name in method_names:
            setattr(self, name, Spy())

        for name, method in methods.items():
            setattr(self, name, method)


class Spy(object):
    def __init__(self, returns=None):
        self.times_called = 0
        self.returns = returns

    def __call__(self):
        self.times_called += 1
        return self.returns


class MyList(collections.MutableSequence):
    def __init__(self, *args):
        self._store = list(args)

    def __getitem__(self, index):
        return self._store[index]

    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass

    def __len__(self):
        pass

    def insert(self, index, value):
        pass
