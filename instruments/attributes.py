class Attributes(object):
    @staticmethod
    def get_docstring(cls, attr):
        return getattr(cls, attr).__doc__

    @staticmethod
    def describe(cls):
        attributes = dir(cls)
        attributes = [
            (
                a, Attributes.get_docstring(cls, a)
            ) for a in attributes
            if '__' not in a
        ]
        return attributes
