import tkinter as tk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("450x600")
        self.root.resizable(False, False)

        self.expression = ""

        self.entry = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=10
        )
        self.entry.pack(fill="both", padx=10, pady=10, ipady=15)

        self.create_buttons()

        self.root.bind("<Key>", self.key_press)

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_display()

    def clear(self):
        self.expression = ""
        self.update_display()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            self.update_display()
        except:
            self.expression = ""
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def key_press(self, event):
        key = event.char

        if key in "0123456789+-*/().":
            self.add_to_expression(key)

        elif event.keysym == "Return":
            self.calculate()

        elif event.keysym == "BackSpace":
            self.backspace()

    def create_buttons(self):

        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")

        buttons = [
            ["7", "8", "9", "/", "sqrt("],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", ".", "^", "+", "="],
            ["sin(", "cos(", "tan(", "log(", "ln("],
            ["pi", "e", "C", "⌫", "**"]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):

                btn = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 16),
                    command=lambda t=text: self.button_click(t)
                )

                btn.grid(
                    row=r,
                    column=c,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)

        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)

    def button_click(self, value):

        if value == "=":
            self.calculate()

        elif value == "C":
            self.clear()

        elif value == "⌫":
            self.backspace()

        elif value == "^":
            self.add_to_expression("**")

        elif value == "pi":
            self.add_to_expression(str(pi))

        elif value == "e":
            self.add_to_expression(str(e))

        elif value == "ln(":
            self.add_to_expression("log(")

        else:
            self.add_to_expression(value)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()