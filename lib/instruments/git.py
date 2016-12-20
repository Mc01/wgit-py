import subprocess


class Git(object):
    @staticmethod
    def get_branch(directory):
        return subprocess.check_output(
            'git -c {directory} rev-parse --abbrev-ref HEAD'.format(
                directory=directory
            ), shell=True
        ).strip()

    @staticmethod
    def get_changes(directory):
        return subprocess.check_output(
            'git -c {directory} diff --shortstat'.format(
                directory=directory
            ), shell=True
        ).strip()
