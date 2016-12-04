from instruments.arguments import Arguments
from instruments.file import File
from wizards.__wizard import Wizard


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
