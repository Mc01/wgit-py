import json
import os


class File(object):
    Read = 'r'
    Write = 'w'
    NewLine = '\n'

    @staticmethod
    def resolve_path(directory, file_name):
        file_path = os.path.join(directory, file_name)
        file_path = os.path.expanduser(file_path)
        return file_path

    @staticmethod
    def exists(directory, file_name):
        file_path = File.resolve_path(directory, file_name)
        return os.path.exists(file_path)

    @staticmethod
    def get_current():
        return os.getcwd()

    @staticmethod
    def write(directory, file_name, data=None):
        file_path = File.resolve_path(directory, file_name)
        with open(file_path, File.Write) as f:
            if data:
                f.write(json.dumps(
                    data,
                    indent=4,
                    sort_keys=True
                ))
                f.write(File.NewLine)

    @staticmethod
    def read(directory, file_name):
        file_path = File.resolve_path(directory, file_name)
        with open(file_path, File.Read) as f:
            data = json.loads(f.read())
        return data
