from lib.instruments.arguments import Arguments
from lib.instruments.stream import Stream
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
                project = projects.pop(alias)
                File.write(
                    Wizard.Directory, Wizard.Config,
                    data=data
                )
                Stream.print_output(
                    'Removed {name} ({alias}) under directory {directory}.'.format(
                        name=project.get('name'),
                        alias=alias,
                        directory=project.get('directory')
                    )
                )
            else:
                Stream.print_output('Alias {alias} is not in projects.'.format(
                    alias=alias
                ))
        else:
            Stream.print_output(
                'Please ensure config exists'
                ' (see: wgit init)'
                ' and try: wgit remove {alias}.'
            )
