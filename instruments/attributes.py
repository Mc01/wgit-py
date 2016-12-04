class Attributes(object):
    @staticmethod
    def describe(cls):
        attributes = dir(cls)
        attributes = [
            a for a in attributes
            if '__' not in a
        ]
        return attributes
