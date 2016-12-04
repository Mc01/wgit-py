from instruments.arguments import Arguments
from instruments.file import File
from wizards.__wizard import Wizard


class Init(Wizard):
    def call(self, args):
        assume = Arguments.assume(args, 0)
        if assume:
            config = dict(projects=dict())
            File.write(
                Wizard.Directory, Wizard.Config,
                data=config
            )
        else:
            pass
