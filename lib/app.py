from lib.instruments.arguments import Arguments
from lib.instruments.attributes import Attributes
from lib.instruments.stream import Stream
from lib.wizards.add import Add
from lib.wizards.go import Go
from lib.wizards.init import Init
from lib.wizards.list import List

from lib.wizards.remove import Remove


class WatchGit:
    @staticmethod
    def __list_attributes(attributes):
        return '\n'.join([
            '-> {0:16} {1}'.format(a[0], a[1])
            for a in attributes
        ])

    def __init__(self):
        attributes = Attributes.describe(WatchGit)
        arguments = Arguments.get()
        if arguments:
            command, arguments = Arguments.splice(arguments)
            if hasattr(self, command):
                getattr(self, command)(arguments)
            else:
                Stream.print_output(
                    'You have provided an invalid argument.\n'
                    'Please use one of:\n'
                    '{attributes}'.format(
                        attributes=self.__list_attributes(attributes)
                    )
                )
        else:
            Stream.print_output(
                'You have not provided any argument.\n'
                'Please use one of:\n'
                '{attributes}'.format(
                    attributes=self.__list_attributes(attributes)
                )
            )

    @staticmethod
    def init(args):
        """Create new config."""
        Init().call(args)

    @staticmethod
    def add(args):
        """Add current directory as project."""
        Add().call(args)

    @staticmethod
    def remove(args):
        """Remove current directory from projects."""
        Remove().call(args)

    @staticmethod
    def list(args):
        """List all projects."""
        List().call(args)

    @staticmethod
    def go(args):
        """Jump to project."""
        Go().call(args)


if __name__ == '__main__':
    app = WatchGit()
