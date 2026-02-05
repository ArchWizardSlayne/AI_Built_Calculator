# Python Modern Calculator

A modern calculator built with Python and `customtkinter`. Supports basic arithmetic with a clean, responsive UI and keyboard controls.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, division, modulo, and exponentiation with full parentheses support
- **Decimal Support**: Full floating-point arithmetic with clean integer display when applicable
- **Sign Toggle**: Negate expressions with the +/- button
- **Modern UI**: Built with customtkinter for a sleek, contemporary look
- **Resizable Window**: Buttons and layout scale smoothly when window is resized
- **Theme Switcher**: Toggle between Light and Dark themes via dropdown menu in the top-right corner
- **Keyboard Input**: Type numbers and operators directly from your keyboard
- **Keyboard Shortcuts**:
  - `Enter` or `=` to evaluate
  - `Backspace` to delete the last character
  - `Escape` to clear the entire expression
  - `Up Arrow` to navigate previous expressions in history
  - `Down Arrow` to return to recent expressions
  - `^` to enter exponentiation (converts to `**`)
- **Expression History**: Automatically saves evaluated expressions; navigate with Up/Down arrows
- **Safe Evaluation**: Uses Python's AST module to safely evaluate expressions without allowing arbitrary code execution

## Requirements

- Python 3.8+
- `tk` / `tkinter` (usually included with Python)
- `customtkinter` package

## Installation



### Virtual Environment (Recommended)

For any operating system, use a virtual environment to keep dependencies isolated:

```bash
python -m venv .venv
```

Activate the virtual environment:

- **Windows**: `.venv\Scripts\activate`
- **macOS/Linux**: `source .venv/bin/activate`

Install customtkinter:

```bash
pip install customtkinter
```

Run the calculator:

```bash
python main.py
```


### Windows

1. Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. Ensure "Add Python to PATH" is checked during installation
3. Open Command Prompt and install customtkinter:

```cmd
pip install customtkinter
```

4. Run the calculator:

```cmd
python main.py
```

### macOS

1. Install Python 3.8+ using Homebrew:

```bash
brew install python@3.11
```

2. Install customtkinter:

```bash
pip install customtkinter
```

3. Run the calculator:

```bash
python main.py
```

### Linux (Ubuntu/Debian)

1. Install Python and required dependencies:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

2. Install customtkinter:

```bash
pip install customtkinter
```

3. Run the calculator:

```bash
python3 main.py
```

### Linux (Arch)

1. Install Python and required dependencies:

```bash
sudo pacman -Syu python python-pip tk
```

2. Install customtkinter:

```bash
pip install customtkinter
```

3. Run the calculator:

```bash
python main.py
```

### Linux (Fedora/RHEL)

1. Install Python and required dependencies:

```bash
sudo dnf install python3 python3-pip tk
```

2. Install customtkinter:

```bash
pip install customtkinter
```

3. Run the calculator:

```bash
python3 main.py
```


## How it works
- Click number buttons or type on your keyboard to enter expressions
- Press `=` or `Enter` to evaluate
- Use `Backspace` to delete, `Escape` to clear
- Press `Up`/`Down` arrows to navigate history
- Click the dropdown menu to switch themes

The calculator uses Python's `ast` module to safely parse and evaluate user-provided mathematical expressions. Only whitelisted operators are allowed, preventing malicious code execution. Expressions are recursively evaluated through an Abstract Syntax Tree, supporting nested operations like `(2 + 3) * (5 - 1)`.

