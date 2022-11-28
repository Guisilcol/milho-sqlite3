import subprocess

class Subprocess:

    @staticmethod
    def call_subprocess(commands: str):
        return subprocess.call(commands, shell=True)