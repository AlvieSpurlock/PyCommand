import PyConsole

class PyCommand:
    def __init__(self):
        self.commandList = {}

    def AddCommand(self, name, function, destription=""):
        i = len(self.commandList) + 1
        self.commandList[i] = [i, name, function, destription]

    def Run(self, i, *args, **kwargs):
        if i in self.commandList:
           cmd = self.commandList[i][2]
           cmd(*args, **kwargs)
        else:
            print("Invalid Index")
    def ShowCommands(self):
        PyConsole.PrintHeader("Available Commands")
        cmdList = []
        for cmd in self.commandList:
            cmdList.append(self.commandList[cmd][1])
        PyConsole.PrintNumberedList(cmdList)