import sys
import collections


class Arguments(object):
    @staticmethod
    def get():
        arguments = sys.argv
        return collections.deque(arguments[1:])

    @staticmethod
    def splice(arguments):
        command = arguments.popleft()
        return command, list(arguments)

    @staticmethod
    def assume(arguments, length):
        return len(arguments) == length
