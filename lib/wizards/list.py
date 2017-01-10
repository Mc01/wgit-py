from lib.instruments.arguments import Arguments
from lib.instruments.file import File
from lib.instruments.stream import Stream
from lib.wizards.__wizard import Wizard

from lib.instruments.git import Git


class List(Wizard):
    def call(self, args):
        config = self.assert_config()
        assume = Arguments.assume(args, 0)
        if config and assume:
            data = File.read(
                Wizard.Directory, Wizard.Config
            )
            projects = sorted(data.get('projects').items())
            if projects:
                for alias, project in projects:
                    name = project.get('name')
                    directory = project.get('directory')
                    branch = Git.get_branch(directory)
                    changes = Git.get_changes(directory)
                    Stream.print_output(
                        '{name} {alias} {branch} {changes}'.format(
                            name=Stream.colorize(
                                name, Stream.Color.Blue
                            ),
                            alias=Stream.colorize(
                                '(%s)' % alias, Stream.Color.Green
                            ),
                            branch=Stream.colorize(
                                branch, Stream.Color.Red
                            ),
                            changes=Stream.colorize(
                                changes, Stream.Color.Yellow
                            )
                        )
                    )
            else:
                Stream.print_output(
                    'No projects in config.'
                    ' Please try: wgit add {alias} {name}.'
                )
        else:
            Stream.print_output(
                'Please ensure config exists'
                ' (see: wgit init)'
                ' and try: wgit list.'
            )
