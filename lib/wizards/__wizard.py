from lib.instruments.file import File


class Wizard(object):
    Directory = '~/.wgit'
    Config = '.config.json'

    @staticmethod
    def assert_config():
        return File.exists(Wizard.Directory, Wizard.Config)

    def call(self, args):
        raise NotImplementedError
