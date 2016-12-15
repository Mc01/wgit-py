from lib.instruments.arguments import Arguments
from lib.instruments.file import File
from lib.instruments.stream import Stream
from lib.wizards.__wizard import Wizard


class Go(Wizard):
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
                project = projects.get(alias)
                directory = project.get('dir')
                Stream.print_output(directory)
            else:
                Stream.print_output('Alias {alias} is not in projects.'.format(
                    alias=alias
                ))
        else:
            Stream.print_output(
                'Please ensure config exists'
                ' (see: wgit init)'
                ' and try: wgit add {alias} {name}.'
            )
