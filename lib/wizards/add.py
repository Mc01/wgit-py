from lib.instruments.arguments import Arguments
from lib.wizards.__wizard import Wizard

from lib.instruments.file import File


class Add(Wizard):
    def call(self, args):
        config = self.assert_config()
        assume = Arguments.assume(args, 2)
        if config and assume:
            alias = args[0]
            name = args[1]
            data = File.read(
                Wizard.Directory, Wizard.Config
            )
            projects = data.get('projects')
            if alias not in projects.keys():
                directory = File.get_current()
                print directory
                projects.update({
                    alias: dict(
                        name=name,
                        dir=directory
                    )
                })
                File.write(
                    Wizard.Directory, Wizard.Config,
                    data=data
                )
            else:
                pass
        else:
            pass
