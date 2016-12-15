from lib.instruments.arguments import Arguments
from lib.instruments.stream import Stream
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
                projects.update({
                    alias: dict(
                        name=name,
                        directory=directory
                    )
                })
                File.write(
                    Wizard.Directory, Wizard.Config,
                    data=data
                )
                Stream.print_output(
                    'Added {name} ({alias}) under directory {directory}.'.format(
                        name=name,
                        alias=alias,
                        directory=directory
                    )
                )
            else:
                Stream.print_output('Alias {alias} is already in projects.'.format(
                    alias=alias
                ))
        else:
            Stream.print_output(
                'Please ensure config exists'
                ' (see: wgit init)'
                ' and try: wgit add {alias} {name}.'
            )
