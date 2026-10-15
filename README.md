# mindows

A fast, simple system information tool for Windows, written in Python. It prints a small ASCII logo next to your host name, Windows version, total memory, and total disk size.

> **Windows only.** On other systems the OS line will say your OS is not Windows.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [termcolor](https://pypi.org/project/termcolor/)
- [psutil](https://pypi.org/project/psutil/)
- [colorama](https://pypi.org/project/colorama/)

Install the Python packages:

```
pip install termcolor psutil colorama
```

## Usage

Run the program directly from the source:

```
python mindows.py
```

Or, after building the compiled version (see below), run:

```
python run.py
```

## Commands

| Command | Description |
|---|---|
| `--help`, `-h` | Show the help message |
| `--issue` | Show how to contact the author about a problem |

## Building the compiled version (optional)

`mindows.py` runs fine on its own. Building compiles it into a `.pyd` file with Cython, which is useful if you want a compiled module instead of the script.

Extra requirements:

- Cython and setuptools: `pip install cython setuptools`
- A C compiler: install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with the **Desktop development with C++** workload.

Build from the project folder:

```
python setup.py build_ext --inplace
```

This creates `mindows.cpXY-win_amd64.pyd`, where `XY` is your Python version (for example, `cp315` for Python 3.15). The file only works with that Python version on 64-bit Windows. Then run:

```
python run.py
```

`run.py` exists because a compiled module doesn't run the `if __name__ == "__main__"` block, so the launcher calls `mindows.main()` directly.

The build also creates `mindows.c` and a `build/` folder. You can delete them after building.

## Running on startup (optional)

To run mindows every time you open PowerShell, add this line to your profile. Open it with `notepad $PROFILE` (create it first if it doesn't exist):

```
python "C:\path\to\mindows\run.py"
```

## Project structure

```
mindows/
├── mindows.py   main program
├── setup.py     Cython build script
├── run.py       launcher for the compiled build
└── .gitignore
```

## Screenshots

### V1.0
### Python
<img width="529" height="129" alt="mindowsfetch_picture" src="https://github.com/user-attachments/assets/92343545-bc1c-46f6-b659-fd2b0d03caaa" />
<img width="974" height="131" alt="mindowsfetch-help" src="https://github.com/user-attachments/assets/31de0e6a-0a3d-4766-bb90-2c6e84cd2fba" />
<img width="505" height="72" alt="mindowsfetch-issue" src="https://github.com/user-attachments/assets/5ec57dcc-2d8a-499b-acdc-9b212a691710" />

### V1.1
### Python
<img width="524" height="98" alt="v1 1" src="https://github.com/user-attachments/assets/6bd277a6-ed93-4db8-9b5d-fec68e79e442" />

### V1.2
### CPython
<img width="298" height="88" alt="v1 2" src="https://github.com/user-attachments/assets/6439c6df-3d93-47b1-9c59-d9a97aba7fbd" />

## Issues

Found a bug or have a suggestion? Open an issue at https://github.com/akettunen/mindows/issues or run `python run.py --issue`.

## Credits

Originally created by [akx25](https://github.com/akx25/mindows).
