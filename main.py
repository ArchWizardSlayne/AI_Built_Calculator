import ast
import operator as op
import customtkinter as ctk


# Safe evaluator for basic arithmetic expressions
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
    ast.Mod: op.mod,
}


def safe_eval(expr: str):
    """Evaluate a math expression safely (supports + - * / % ** and parentheses)."""
    try:
        node = ast.parse(expr, mode="eval").body
    except Exception:
        raise ValueError("Invalid expression")

    def _eval(n):
        if isinstance(n, ast.Num):
            return n.n
        if isinstance(n, ast.Constant):
            if isinstance(n.value, (int, float)):
                return n.value
            raise ValueError("Unsupported constant")
        if isinstance(n, ast.BinOp):
            left = _eval(n.left)
            right = _eval(n.right)
            op_type = type(n.op)
            if op_type in ALLOWED_OPERATORS:
                return ALLOWED_OPERATORS[op_type](left, right)
            raise ValueError("Unsupported binary operator")
        if isinstance(n, ast.UnaryOp):
            operand = _eval(n.operand)
            op_type = type(n.op)
            if op_type in ALLOWED_OPERATORS:
                return ALLOWED_OPERATORS[op_type](operand)
            raise ValueError("Unsupported unary operator")
        raise ValueError("Unsupported expression")

    return _eval(node)


class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("360x520")
        # allow window to be resized
        self.resizable(True, True)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.expression = ctk.StringVar()
        self.history: list[str] = []
        self.history_index: int | None = None
        self.current_theme = "dark"
        self.buttons: list[ctk.CTkButton] = []

        self._create_widgets()

        # keyboard bindings
        # capture all key presses so the UI stays readonly but keyboard works
        self.bind_all("<Key>", self._on_key)
        # ensure window has focus to receive keys
        self.after(100, lambda: self.focus_force())

    def _create_widgets(self):
        # configure grid to expand/contract with window
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=0)  # theme menu row
        self.grid_rowconfigure(1, weight=0)  # entry row stays fixed height
        self.grid_rowconfigure(2, weight=1)  # button rows expand
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)

        # theme menu button at top-right
        theme_menu = ctk.CTkOptionMenu(
            self,
            values=["Light", "Dark"],
            command=self._switch_theme,
            fg_color=("#2b2b2b"),
        )
        theme_menu.grid(row=0, column=3, padx=12, pady=8, sticky="e")
        theme_menu.set("Dark")

        entry = ctk.CTkEntry(self, textvariable=self.expression, height=60, font=("Roboto", 20))
        entry.grid(row=1, column=0, columnspan=4, padx=12, pady=(20, 10), sticky="nsew")
        entry.configure(state="readonly")

        buttons = [
            ["C", "<-", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
        ]

        for r, row in enumerate(buttons, start=2):
            for c, label in enumerate(row):
                btn = ctk.CTkButton(self, text=label, fg_color=("#2b2b2b"), text_color="white", command=lambda l=label: self._on_button(l))
                # remove fixed size; let button fill the grid cell
                btn.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")
                self.buttons.append(btn)

    def _switch_theme(self, theme: str):
        """Switch between light and dark themes."""
        self.current_theme = theme.lower()
        ctk.set_appearance_mode(self.current_theme)

        # update button colors based on theme
        if self.current_theme == "light":
            for btn in self.buttons:
                btn.configure(fg_color="#d0d0d0", text_color="black")
        else:  # dark
            for btn in self.buttons:
                btn.configure(fg_color="#2b2b2b", text_color="white")

    def _on_button(self, label: str):
        if label == "C":
            self.expression.set("")
            return
        if label == "<-":
            self.expression.set(self.expression.get()[:-1])
            return
        if label == "=":
            self._evaluate_expression()
            return
        if label == "+/-":
            cur = self.expression.get()
            if not cur:
                return
            # toggle sign for last number: simple approach
            try:
                # attempt to evaluate entire expression and negate
                val = safe_eval(cur)
                self.expression.set(str(-val))
            except Exception:
                # fallback: prepend minus
                if cur.startswith("-"):
                    self.expression.set(cur[1:])
                else:
                    self.expression.set("-" + cur)
            return

        # append digit/operator
        # reset history navigation when user types
        self.history_index = None
        self.expression.set(self.expression.get() + label)

    def _evaluate_expression(self):
        expr = self.expression.get()
        if not expr:
            return
        try:
            result = safe_eval(expr)
            # Format result: drop .0 for integers
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            # save expression to history (store the expression, not result)
            self.history.append(expr)
            self.history_index = None
            self.expression.set(str(result))
        except Exception:
            self.expression.set("Error")

    def _navigate_history(self, direction: int):
        # direction: -1 for up (older), +1 for down (newer)
        if not self.history:
            return
        if self.history_index is None:
            # start from the most recent
            if direction == -1:
                self.history_index = len(self.history) - 1
            else:
                return
        else:
            self.history_index += direction
            if self.history_index < 0:
                self.history_index = 0
            if self.history_index >= len(self.history):
                # past latest -> clear and reset
                self.history_index = None
                self.expression.set("")
                return

        if self.history_index is not None:
            self.expression.set(self.history[self.history_index])

    def _on_key(self, event):
        # handle keyboard input (works even when entry is readonly)
        ks = event.keysym
        ch = event.char

        if ks in ("Return", "KP_Enter"):
            self._evaluate_expression()
            return "break"
        if ks == "BackSpace":
            cur = self.expression.get()
            self.expression.set(cur[:-1])
            self.history_index = None
            return "break"
        if ks == "Escape":
            self.expression.set("")
            self.history_index = None
            return "break"
        if ks == "Up":
            self._navigate_history(-1)
            return "break"
        if ks == "Down":
            self._navigate_history(1)
            return "break"

        # allow direct '=' key to evaluate
        if ch == "=":
            self._evaluate_expression()
            return "break"

        # map ^ to ** for exponent shorthand
        if ch == "^":
            self.history_index = None
            self.expression.set(self.expression.get() + "**")
            return "break"

        # append allowed chars
        allowed = "0123456789+-*/%.()"
        if ch and ch in allowed:
            # replace 'Error' on new input
            if self.expression.get() == "Error":
                self.expression.set(ch)
            else:
                self.expression.set(self.expression.get() + ch)
            self.history_index = None
            return "break"


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
