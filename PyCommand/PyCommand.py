import PyConsole
import PyError
from PyError import PyErrorMeta
import inspect

class PyCommand:
    def __init__(self):
        self.commandList = {}

    def AddCommand(self, name, function, destription=""):
        i = len(self.commandList) + 1
        self.commandList[i] = [i, name, function, destription]

    def Run(self, i, *args, **kwargs):
        if i in self.commandList:
            cmd = self.commandList[i][2]
            PyError.BindMetadeta(i, cmd, *args, **kwargs)
            cmd(*args, **kwargs)