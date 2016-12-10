from __future__ import print_function

from termcolor import colored


class Stream(object):
    class Color(object):
        Blue = 'blue'
        Green = 'green'
        Yellow = 'red'

    @staticmethod
    def print_output(string):
        print(string)

    @staticmethod
    def colorize(string, color):
        return colored(string, color=color)
