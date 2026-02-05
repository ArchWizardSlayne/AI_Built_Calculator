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

## Installation

Choose your operating system below for specific setup instructions.

### Windows

1. **Clone the repository:**
   ```cmd
   git clone https://github.com/ArchWizardSlayne/AI_Built_Calculator.git
   ```

2. **Install Python 3.8+**
   - Download from [python.org](https://www.python.org/downloads/)
   - Run the installer and check "Add Python to PATH"
   - tk/tkinter is included by default

3. **Create and activate a virtual environment:**
   ```cmd
   cd AI_Built_Calculator
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Install customtkinter:**
   ```cmd
   pip install customtkinter
   ```

5. **Install pyinstaller (optional, for building executables):**
   ```cmd
   pip install pyinstaller
   ```

6. **Building an Executable (Optional)**

   ```cmd
   pyinstaller --onefile --windowed --name "Calculator" main.py
   ```

   The executable will be created in the `dist/` folder and can be run without Python or any dependencies installed.

7. **Run the calculator:**
   ```cmd
   python main.py
   ```

### macOS

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArchWizardSlayne/AI_Built_Calculator.git
   ```

2. **Install Python 3.8+**
   - Using Homebrew:
   ```bash
   brew install python@3.11
   ```
   - tk is included with the Python installation

3. **Create and activate a virtual environment:**
   ```bash
   cd AI_Built_Calculator
   python -m venv .venv
   source .venv/bin/activate
   ```

4. **Install customtkinter:**
   ```bash
   pip install customtkinter
   ```

5. **Install pyinstaller (optional, for building executables):**
   ```bash
   pip install pyinstaller
   ```

6. **Building an Executable (Optional)**

   ```bash
   pyinstaller --onefile --windowed --name "Calculator" main.py
   ```

   The executable will be created in the `dist/` folder and can be run without Python or any dependencies installed.

7. **Run the calculator:**
   ```bash
   python main.py
   ```

### Linux (Ubuntu/Debian)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArchWizardSlayne/AI_Built_Calculator.git
   ```

2. **Install Python and tk:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   ```

3. **Create and activate a virtual environment:**
   ```bash
   cd AI_Built_Calculator
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install customtkinter:**
   ```bash
   pip install customtkinter
   ```

5. **Install pyinstaller (optional, for building executables):**
   ```bash
   pip install pyinstaller
   ```

6. **Building an Executable (Optional)**

   ```bash
   pyinstaller --onefile --windowed --name "Calculator" main.py
   ```

   The executable will be created in the `dist/` folder and can be run without Python or any dependencies installed.

7. **Run the calculator:**
   ```bash
   python3 main.py
   ```

### Arch

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArchWizardSlayne/AI_Built_Calculator.git
   ```

2. **Install Python and tk:**
   ```bash
   sudo pacman -Syu python python-pip tk
   ```

3. **Create and activate a virtual environment:**
   ```bash
   cd AI_Built_Calculator
   python -m venv .venv
   source .venv/bin/activate
   ```

4. **Install customtkinter:**
   ```bash
   pip install customtkinter
   ```

5. **Install pyinstaller (optional, for building executables):**
   ```bash
   pip install pyinstaller
   ```

6. **Building an Executable (Optional)**

   ```bash
   pyinstaller --onefile --windowed --name "Calculator" main.py
   ```

   The executable will be created in the `dist/` folder and can be run without Python or any dependencies installed.

7. **Run the calculator:**
   ```bash
   python main.py
   ```

### Linux (Fedora/RHEL)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArchWizardSlayne/AI_Built_Calculator.git
   ```

2. **Install Python and tk:**
   ```bash
   sudo dnf install python3 python3-pip tk
   ```

3. **Create and activate a virtual environment:**
   ```bash
   cd AI_Built_Calculator
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install customtkinter:**
   ```bash
   pip install customtkinter
   ```

5. **Install pyinstaller (optional, for building executables):**
   ```bash
   pip install pyinstaller
   ```

6. **Building an Executable (Optional)**

   ```bash
   pyinstaller --onefile --windowed --name "Calculator" main.py
   ```

   The executable will be created in the `dist/` folder and can be run without Python or any dependencies installed.

7. **Run the calculator:**
   ```bash
   python3 main.py
   ```

## How to Use

- Click number buttons or type on your keyboard to enter expressions
- Press `=` or `Enter` to evaluate
- Use `Backspace` to delete the last character, `Escape` to clear all
- Press `Up`/`Down` arrows to navigate through expression history
- Click the theme dropdown in the top-right to switch between Light and Dark modes

The calculator uses Python's `ast` module to safely parse and evaluate user-provided mathematical expressions. Only whitelisted operators are allowed, preventing malicious code execution. Expressions are recursively evaluated through an Abstract Syntax Tree, supporting nested operations like `(2 + 3) * (5 - 1)`.



