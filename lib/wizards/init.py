from lib.instruments.arguments import Arguments
from lib.wizards.__wizard import Wizard

from lib.instruments.file import File


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
