# Diary CLI

A simple command-line diary application written in Python.

Diary started as a small file-handling project and is being developed into a proper installable terminal application.

## Features

* Create diary entries for specific dates
* Read previously saved diary entries
* Handle missing diary entries without crashing
* Store entries locally as `.txt` files
* Hide diary files on Linux and other Unix-like systems
* Keep diary files out of Git using `.gitignore`
* Install the application as a global `Diary` command using `pipx`

## Requirements

* Python 3.10 or newer
* `pipx`

Diary currently uses only Python's standard library.

## Installation

Clone the repository:

```bash
git clone git@github.com:Narla7/Diary-CLI.git
cd Diary-CLI
```

Install Diary with `pipx`:

```bash
pipx install .
```

After installation, the application can be launched from any directory with:

```bash
Diary
```

## Usage

Run:

```bash
Diary
```

The program will ask whether you want to write or read a diary entry.

### Write an Entry

Choose:

```text
write
```

or:

```text
w
```

Then enter the date of the entry:

```text
Enter today's date (dd.mm.yy): 19.08.26
```

Enter your diary entry when prompted.

The entry is saved locally as a hidden `.txt` file, for example:

```text
.19.08.26.txt
```

### Read an Entry

Choose:

```text
read
```

or:

```text
r
```

Then enter the date of the entry you want to read.

If the entry exists, its contents are displayed.

If it does not exist, Diary displays an error message instead of crashing.

## File Storage

Diary entries are stored as plain-text `.txt` files in the directory from which Diary is run.

On Linux and other Unix-like systems, Diary prefixes filenames with `.` so that they are hidden by default.

For example:

```text
.19.08.26.txt
```

Diary entries are ignored by Git so that personal diary contents are not uploaded to the repository.

To view hidden files on Linux:

```bash
ls -a
```

## Project Structure

```text
Diary-CLI/
├── pyproject.toml
├── README.md
├── .gitignore
└── src/
    └── diary/
        ├── __init__.py
        └── main.py
```

## Development

Diary is currently being developed as a learning project while exploring:

* Python file handling
* Functions
* Exceptions
* Context managers
* Git and GitHub
* Python packaging
* Command-line applications

The project is intentionally simple at its current stage.

## Future Plans

* Build a full terminal user interface (TUI)
* Add keyboard navigation
* Browse diary entries interactively
* Create and edit entries from the TUI
* Improve input validation
* Improve diary entry management
* Publish Diary as a Python package for easier installation

## Version

**0.1.0**

## License

No license has been added to this project yet.

