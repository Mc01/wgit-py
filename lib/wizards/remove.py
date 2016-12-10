from lib.instruments.arguments import Arguments
from lib.wizards.__wizard import Wizard

from lib.instruments.file import File


class Remove(Wizard):
    def call(self, args):
        config = self.assert_config()
        assume = Arguments.assume(args, 1)
        if config and assume:
            alias = args[0]
            data = File.read(
                Wizard.Directory, Wizard.Config
            )
            projects = data.get('projects')
            if alias in projects.keys():
                projects.pop(alias)
                File.write(
                    Wizard.Directory, Wizard.Config,
                    data=data
                )
            else:
                pass
        else:
            pass
