import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
root = tk.Tk()
root.configure(bg="#1E1E2E")
root.title("Simple Calculator")
root.geometry("340x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🧮 Calculator",
    font=("Segoe UI", 22, "bold"),
    bg="#1E1E2E",
    fg="white"
)
title.pack(pady=10)

entry = tk.Entry(
    root,
    font=("Segoe UI", 24, "bold"),
    justify="right",
    bg="#313244",
    fg="white",
    insertbackground="white",
    bd=0
)
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:

    if button == "=":
        cmd = calculate
    else:
        cmd = lambda x=button: click(x)

    tk.Button(
        frame,
        text=button,
        width=5,
        height=2,
        font=("Arial", 16),
        command=cmd
    ).grid(row=row, column=col)

    col += 1

    if col > 3:
        col = 0
        row += 1

button_frame = tk.Frame(root)
button_frame.pack(fill="x", padx=10, pady=10)

tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 16),
    command=clear
).pack(side="left", expand=True, fill="x")

tk.Button(
    button_frame,
    text="⌫",
    font=("Arial", 16),
    command=backspace
).pack(side="right", expand=True, fill="x")

credit = tk.Label(
    root,
    text="Made by Jiya Baghel ❤️",
    font=("Segoe UI", 9),
    bg="#1E1E2E",
    fg="white"
)
credit.pack(pady=5)

root.mainloop()