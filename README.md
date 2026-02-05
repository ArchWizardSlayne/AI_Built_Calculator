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

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   ```

   - **Windows**: `.venv\Scripts\activate`
   - **macOS/Linux**: `source .venv/bin/activate`

2. **Install customtkinter:**

   ```bash
   pip install customtkinter
   ```

3. **Install pyinstaller (optional, for building executables):**

   ```bash
   pip install pyinstaller
   ```

4. **Run the calculator:**

   ```bash
   python main.py
   ```

## Building an Executable with PyInstaller

Create a standalone executable:

```bash
pyinstaller --onefile --windowed --name "Calculator" main.py
```

**Options:**
- `--onefile`: Single executable file
- `--windowed`: No console window
- `--name "Calculator"`: Executable name

The executable will be in the `dist/` folder.


## How it works
- Click number buttons or type on your keyboard to enter expressions
- Press `=` or `Enter` to evaluate
- Use `Backspace` to delete, `Escape` to clear
- Press `Up`/`Down` arrows to navigate history
- Click the dropdown menu to switch themes

The calculator uses Python's `ast` module to safely parse and evaluate user-provided mathematical expressions. Only whitelisted operators are allowed, preventing malicious code execution. Expressions are recursively evaluated through an Abstract Syntax Tree, supporting nested operations like `(2 + 3) * (5 - 1)`.

