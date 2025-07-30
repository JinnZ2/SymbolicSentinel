import tkinter as tk
from tkinter import messagebox
import json
from main import run_animal_warning_system

def load_and_run():
    try:
        with open("config.json", "r") as f:
            data = json.load(f)
        run_animal_warning_system(data)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("SymbolicSentinel")

tk.Label(root, text="Symbolic Sentinel - Collapse Warning System", font=("Helvetica", 16)).pack(pady=10)
tk.Button(root, text="Run Analysis", command=load_and_run).pack(pady=10)
tk.Label(root, text="Make sure config.json is set before running.").pack(pady=5)

root.mainloop()
