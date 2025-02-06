# File System Simulation

File system simulation written in Python. It allows users to navigate through the directory tree, manage files and folders, and perform basic operations on them.

## Design Patterns
The project implements the following design patterns:

- Composite – allows files and directories to be treated uniformly.
- Command – Each operation (e.g., cd, ls, mkdir) is a separate class inheriting from operation.
- Factory Method – Cmd dynamically creates instances of operations based on the user command.

## Available Commands

| Command                  | Description                          |
|--------------------------|--------------------------------------|
| `cd <path>`             | Navigates to the specified directory |
| `ls [path]`            | Displays the contents of a directory |
| `mkdir <name>`         | Creates a new directory              |
| `mv <source> <destination>` | Moves a file or directory         |
| `cp <source> <destination>` | Copies a file or directory        |
| `tree [path]`          | Displays the directory structure     |
| `more <file>`         | Displays the contents of a file      |

## Example Usage

![SSC1](https://github.com/zywczak/FileSystemSimulation/blob/main/console1.png)

![SSC2](https://github.com/zywczak/FileSystemSimulation/blob/main/console2.png)

![SSC3](https://github.com/zywczak/FileSystemSimulation/blob/main/console3.png)