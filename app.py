from instruments.arguments import Arguments
from instruments.attributes import Attributes
from instruments.stream import Stream
from wizards.add import Add
from wizards.go import Go
from wizards.init import Init
from wizards.list import List


class WatchGit:
    @staticmethod
    def __list_attributes(attributes):
        return '\n'.join(['-> %s' % a for a in attributes])

    def __init__(self):
        attributes = Attributes.describe(WatchGit)
        arguments = Arguments.get()
        if arguments:
            command, arguments = Arguments.splice(arguments)
            if hasattr(self, command):
                getattr(self, command)(arguments)
            else:
                Stream.output(
                    'You have provided an invalid argument.\n'
                    'Please use one of:\n'
                    '{attributes}'.format(
                        attributes=self.__list_attributes(attributes)
                    )
                )
        else:
            Stream.output(
                'You have not provided any argument.\n'
                'Please use one of:\n'
                '{attributes}'.format(
                    attributes=self.__list_attributes(attributes)
                )
            )

    @staticmethod
    def init(args):
        wizard = Init()
        wizard.call(args)

    @staticmethod
    def add(args):
        wizard = Add()
        wizard.call(args)

    @staticmethod
    def list(args):
        wizard = List()
        wizard.call(args)

    @staticmethod
    def go(args):
        wizard = Go()
        wizard.call(args)


if __name__ == '__main__':
    app = WatchGit()
