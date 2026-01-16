# PyCommand

PyCommand is a lightweight command‑routing engine designed to register, organize, and execute functions by index. It integrates seamlessly with PyError to provide automatic metadata binding and clean, contextualized error reporting. This makes PyCommand ideal for CLI tools, menu systems, debugging utilities, and any environment where user‑triggered actions need to be mapped to callable functions.

## Overview

PyCommand stores commands internally as indexed entries, each containing:

- A unique command index

- A command name

- A function reference

- An optional description

### When a command is executed, PyCommand automatically:

- Looks up the function by index

- Binds argument metadata to PyError for debugging

- Executes the function with the provided arguments

This keeps your command logic clean, modular, and easy to extend.

## Why PyCommand?

Most CLI or menu‑driven systems eventually need a way to map user choices to functions. PyCommand solves this cleanly by providing:

- A predictable, index‑based command registry

- Automatic argument tracking for PyError

- A simple API for adding and running commands

- Zero boilerplate — just register and execute

Instead of writing repetitive lookup logic or manual error handling, PyCommand centralizes the entire command‑execution pipeline.

## Core Features

### Command Registration

Register commands with a name, function, and optional description:

- Commands are automatically assigned an index

- Stored internally in a clean, predictable structure

- Easy to extend or modify

### Automatic Error Metadata Binding

Before executing a command, PyCommand calls:

- PyError.BindMetadeta(i, cmd, *args, **kwargs)

#### This captures:

- The command index

- Required arguments

- Given arguments

PyError then uses this information to produce detailed, contextual error messages.

### Simple Command Execution

Running a command is as simple as:

- PyCommand.Run(index, *args, **kwargs)

If the index exists, the function is executed with the provided arguments.

### Modular Design

PyCommand is intentionally small and focused:

- Command storage

- Metadata binding

- Function execution

Everything else — formatting, error handling, menus — is delegated to other tools in your ecosystem.

## Example

```python
from PyCommand import PyCommand

def Greet(name: str):
    print(f"Hello, {name}!")

cmd = PyCommand()
cmd.AddCommand("Greet User", Greet)

cmd.Run(1, "Alvie")
```

### Output:

```txt
Hello, Alvie!
```

If incorrect arguments are passed, PyError will automatically generate a clean, contextual error message.

## Class Structure

```python
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
```

(Full implementation included in repository.)

## Summary

PyCommand provides a clean, minimal, and extensible command‑routing system for Python applications. With automatic PyError integration and a simple API, it’s an ideal foundation for CLI tools, menu systems, debugging utilities, and text‑based engines.

Requires: Python 3.x, PyError, PyConsole
