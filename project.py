
import ast
import math
import operator
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox


# ==========================================
# MATHEMATICAL FUNCTIONS
# ==========================================

def calculate(num1, operator_symbol, num2):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,
        "%": operator.mod
    }

    if operator_symbol not in operations:
        raise ValueError("Invalid operator.")

    if operator_symbol in ["/", "%"] and num2 == 0:
        raise ValueError("Cannot divide by zero.")

    result = operations[operator_symbol](num1, num2)

    if isinstance(result, complex) or not math.isfinite(result):
        raise ValueError("Invalid mathematical result.")

    return result


def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


def calculate_percentage(number, percentage):
    return number * percentage / 100


def calculate_average(numbers):
    if not numbers:
        raise ValueError("Number list cannot be empty.")
    return sum(numbers) / len(numbers)


# ==========================================
# SAFE EXPRESSION EVALUATOR
# ==========================================

def evaluate_expression(expression):

    binary_operations = {
        ast.Add: lambda a, b: calculate(a, "+", b),
        ast.Sub: lambda a, b: calculate(a, "-", b),
        ast.Mult: lambda a, b: calculate(a, "*", b),
        ast.Div: lambda a, b: calculate(a, "/", b),
        ast.Pow: lambda a, b: calculate(a, "**", b),
        ast.Mod: lambda a, b: calculate(a, "%", b)
    }

    unary_operations = {
        ast.UAdd: lambda a: a,
        ast.USub: lambda a: -a
    }

    functions = {
        "sqrt": square_root,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log10,
        "ln": math.log,
        "abs": abs
    }

    constants = {
        "pi": math.pi,
        "e": math.e
    }

    def evaluate(node):

        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) not in (int, float):
                raise ValueError("Only numbers are allowed.")
            return node.value

        if isinstance(node, ast.Name):
            if node.id not in constants:
                raise ValueError("Unknown constant.")
            return constants[node.id]

        if isinstance(node, ast.BinOp):
            operation_type = type(node.op)

            if operation_type not in binary_operations:
                raise ValueError("Unsupported operation.")

            left = evaluate(node.left)
            right = evaluate(node.right)

            if operation_type == ast.Pow and abs(right) > 1000:
                raise ValueError("Exponent is too large.")

            return binary_operations[operation_type](left, right)

        if isinstance(node, ast.UnaryOp):
            operation_type = type(node.op)

            if operation_type not in unary_operations:
                raise ValueError("Unsupported operation.")

            return unary_operations[operation_type](
                evaluate(node.operand)
            )

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Invalid function.")

            name = node.func.id

            if name not in functions or len(node.args) != 1:
                raise ValueError("Unsupported function.")

            return functions[name](evaluate(node.args[0]))

        raise ValueError("Invalid expression.")

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree)

        if isinstance(result, complex) or not math.isfinite(result):
            raise ValueError("Invalid mathematical result.")

        return result

    except (SyntaxError, TypeError, OverflowError) as error:
        raise ValueError("Invalid mathematical expression.") from error


# ==========================================
# HISTORY MANAGEMENT
# ==========================================

def save_history(calculation):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(calculation + "\n")


def get_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def clear_history():
    with open("history.txt", "w", encoding="utf-8") as file:
        file.write("")


def view_history():
    history = get_history()

    if not history:
        print("No calculation history found.")
        return

    for item in history:
        print(item.strip())


# ==========================================
# SMART CALCULATOR GUI
# ==========================================

class SmartCalculator(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Smart Python Calculator")
        self.geometry("1050x720")
        self.minsize(850, 620)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.expression = tk.StringVar()

        self.bg = "#111827"
        self.panel = "#1F2937"
        self.accent = "#3B82F6"
        self.button_color = "#293548"

        self.configure(fg_color=self.bg)

        self.create_interface()
        self.refresh_history()

        self.bind("<Return>", self.keyboard_enter)
        self.bind("<Escape>", self.keyboard_clear)

    # ======================================
    # INTERFACE
    # ======================================

    def create_interface(self):

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(
            row=0, column=0, columnspan=2,
            sticky="ew", padx=25, pady=20
        )

        ctk.CTkLabel(
            header,
            text="SMART CALCULATOR",
            font=("Segoe UI", 26, "bold")
        ).pack(side="left")

        ctk.CTkLabel(
            header,
            text="PYTHON EDITION",
            text_color=self.accent,
            font=("Segoe UI", 12, "bold")
        ).pack(side="left", padx=15)

        self.theme_switch = ctk.CTkSwitch(
            header,
            text="Light mode",
            command=self.toggle_theme
        )
        self.theme_switch.pack(side="right")

        # Calculator panel
        calculator = ctk.CTkFrame(
            self, fg_color=self.panel, corner_radius=20
        )
        calculator.grid(
            row=1, column=0,
            sticky="nsew", padx=(25, 10), pady=10
        )

        calculator.grid_columnconfigure((0, 1, 2, 3), weight=1)
        calculator.grid_rowconfigure(2, weight=1)

        # Display
        display_frame = ctk.CTkFrame(
            calculator, fg_color="#182233", corner_radius=15
        )
        display_frame.grid(
            row=0, column=0, columnspan=4,
            sticky="ew", padx=18, pady=18
        )

        ctk.CTkLabel(
            display_frame,
            text="CALCULATION DISPLAY",
            text_color="#94A3B8",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", padx=15, pady=(12, 0))

        self.display = ctk.CTkEntry(
            display_frame,
            textvariable=self.expression,
            font=("Segoe UI", 30),
            height=75,
            fg_color="transparent",
            border_width=0,
            justify="right"
        )
        self.display.pack(fill="x", padx=12, pady=10)
        self.display.focus_set()

        # Scientific operations
        scientific = ctk.CTkFrame(
            calculator, fg_color="transparent"
        )
        scientific.grid(
            row=1, column=0, columnspan=4,
            sticky="ew", padx=12
        )

        scientific_buttons = [
            "sin", "cos", "tan", "log",
            "ln", "π", "e", "abs"
        ]

        for i, value in enumerate(scientific_buttons):
            scientific.grid_columnconfigure(i, weight=1)

            ctk.CTkButton(
                scientific,
                text=value,
                height=38,
                corner_radius=9,
                fg_color="#344766",
                hover_color="#45618C",
                command=lambda v=value: self.scientific_click(v)
            ).grid(row=0, column=i, padx=3, pady=8, sticky="ew")

        # Number buttons
        buttons_frame = ctk.CTkFrame(
            calculator, fg_color="transparent"
        )
        buttons_frame.grid(
            row=2, column=0, columnspan=4,
            sticky="nsew", padx=12, pady=12
        )

        buttons = [
            ["C", "DEL", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["0", ".", "%", "+"],
            ["√", "x²", "^", "="]
        ]

        for r in range(6):
            buttons_frame.grid_rowconfigure(r, weight=1)

        for c in range(4):
            buttons_frame.grid_columnconfigure(c, weight=1)

        for r, row in enumerate(buttons):
            for c, value in enumerate(row):
                self.create_button(buttons_frame, value, r, c)

        # History panel
        self.create_history_panel()

    # ======================================
    # BUTTON DESIGN
    # ======================================

    def create_button(self, parent, value, row, column):

        if value == "=":
            color = "#2563EB"
            hover = "#1D4ED8"
        elif value in ["C", "DEL"]:
            color = "#8B3545"
            hover = "#A94456"
        elif value in ["÷", "×", "−", "+", "%", "^"]:
            color = "#344766"
            hover = "#45618C"
        else:
            color = self.button_color
            hover = "#3B4960"

        ctk.CTkButton(
            parent,
            text=value,
            height=58,
            corner_radius=13,
            font=("Segoe UI", 18, "bold"),
            fg_color=color,
            hover_color=hover,
            command=lambda: self.button_click(value)
        ).grid(
            row=row, column=column,
            padx=5, pady=5, sticky="nsew"
        )

    # ======================================
    # HISTORY PANEL
    # ======================================

    def create_history_panel(self):

        panel = ctk.CTkFrame(
            self, fg_color=self.panel, corner_radius=20
        )
        panel.grid(
            row=1, column=1,
            sticky="nsew", padx=(10, 25), pady=10
        )

        panel.grid_columnconfigure(0, weight=1)
        panel.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            panel,
            text="HISTORY",
            font=("Segoe UI", 20, "bold")
        ).grid(row=0, column=0, padx=15, pady=20)

        self.history_list = ctk.CTkScrollableFrame(
            panel, fg_color="#182233", corner_radius=12
        )
        self.history_list.grid(
            row=1, column=0,
            sticky="nsew", padx=12, pady=5
        )

        self.history_count = ctk.CTkLabel(
            panel,
            text="0 calculations",
            text_color="#94A3B8"
        )
        self.history_count.grid(row=2, column=0, pady=10)

        ctk.CTkButton(
            panel,
            text="CLEAR HISTORY",
            fg_color="#8B3545",
            hover_color="#A94456",
            height=42,
            command=self.clear_gui_history
        ).grid(
            row=3, column=0,
            sticky="ew", padx=12, pady=(5, 15)
        )

    # ======================================
    # BUTTON ACTIONS
    # ======================================

    def button_click(self, value):

        if value == "C":
            self.clear()
            return

        if value == "DEL":
            self.expression.set(self.expression.get()[:-1])
            return

        if value == "=":
            self.calculate_result()
            return

        current = self.expression.get()

        if value == "√":
            if current:
                self.expression.set(f"sqrt({current})")
            return

        if value == "x²":
            if current:
                self.expression.set(f"({current})**2")
            return

        symbols = {
            "÷": "/",
            "×": "*",
            "−": "-",
            "^": "**"
        }

        self.expression.set(current + symbols.get(value, value))

    # ======================================
    # SCIENTIFIC FUNCTIONS
    # ======================================

    def scientific_click(self, value):

        current = self.expression.get()

        if value == "π":
            self.expression.set(current + "pi")
        elif value == "e":
            self.expression.set(current + "e")
        else:
            self.expression.set(current + value + "(")

    # ======================================
    # CALCULATIONS
    # ======================================

    def calculate_result(self):

        expression = self.expression.get().strip()

        if not expression:
            return

        try:
            result = evaluate_expression(expression)

            save_history(f"{expression} = {result}")

            self.expression.set(str(result))
            self.refresh_history()

        except (ValueError, ZeroDivisionError) as error:
            messagebox.showerror(
                "Calculation Error",
                str(error),
                parent=self
            )

    # ======================================
    # HISTORY
    # ======================================

    def refresh_history(self):

        for widget in self.history_list.winfo_children():
            widget.destroy()

        history = get_history()

        for item in reversed(history):
            calculation = item.strip()

            if calculation:
                ctk.CTkButton(
                    self.history_list,
                    text=calculation,
                    anchor="w",
                    fg_color="#293548",
                    hover_color="#3B4960",
                    height=42,
                    command=lambda v=calculation: self.load_history(v)
                ).pack(fill="x", padx=4, pady=4)

        self.history_count.configure(
            text=f"{len(history)} calculations"
        )

    def load_history(self, calculation):

        if " = " in calculation:
            self.expression.set(
                calculation.rsplit(" = ", 1)[0]
            )

    def clear_gui_history(self):

        if messagebox.askyesno(
            "Clear History",
            "Delete all calculation history?",
            parent=self
        ):
            clear_history()
            self.refresh_history()

    # ======================================
    # THEME
    # ======================================

    def toggle_theme(self):

        mode = "light" if self.theme_switch.get() else "dark"
        ctk.set_appearance_mode(mode)

    # ======================================
    # KEYBOARD
    # ======================================

    def keyboard_enter(self, event=None):
        self.calculate_result()

    def keyboard_clear(self, event=None):
        self.clear()

    def clear(self):
        self.expression.set("")


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():
    app = SmartCalculator()
    app.mainloop()


if __name__ == "__main__":
    main()