import tkinter as tk
from tkinter import messagebox

def compute():
    try:
        choice = choice_var.get()
        x = int(entry_x.get())
        y = int(entry_y.get())

        if choice == 1:
            r = x % y
            result.set(f"Remainder = {r}")

        elif choice == 2:
            a = int(entry_a.get())
            r = pow(x, a, y)
            result.set(f"Remainder = {r}")

        else:
            messagebox.showwarning("Warning", "Please select an option!")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input!\n{e}")


# Main window
root = tk.Tk()
root.title("Modulus Calculator")
root.geometry("350x300")
root.configure(bg="#2E3440")  # dark background

# Title
tk.Label(root, text="🔢 Modulus Calculator",
         font=("Arial", 16, "bold"),
         fg="#88C0D0", bg="#2E3440").pack(pady=10)

# Choice
choice_var = tk.IntVar()
frame_choice = tk.Frame(root, bg="#2E3440")
frame_choice.pack(pady=5)

tk.Label(frame_choice, text="Choose option:",
         font=("Arial", 12), fg="#ECEFF4", bg="#2E3440").grid(row=0, column=0, columnspan=2, pady=5)

tk.Radiobutton(frame_choice, text="1. X mod Y", variable=choice_var, value=1,
               font=("Arial", 11), fg="#D8DEE9", bg="#2E3440", selectcolor="#434C5E").grid(row=1, column=0, padx=10)

tk.Radiobutton(frame_choice, text="2. X^a mod Y", variable=choice_var, value=2,
               font=("Arial", 11), fg="#D8DEE9", bg="#2E3440", selectcolor="#434C5E").grid(row=1, column=1, padx=10)

# Input frame
frame_inputs = tk.Frame(root, bg="#2E3440")
frame_inputs.pack(pady=10)

labels = ["X:", "a (only for option 2):", "Y:"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame_inputs, text=text, font=("Arial", 11), fg="#A3BE8C", bg="#2E3440").grid(row=i, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame_inputs, font=("Arial", 11), bg="#3B4252", fg="#ECEFF4", insertbackground="white")
    entry.grid(row=i, column=1, pady=5, padx=5)
    entries.append(entry)

entry_x, entry_a, entry_y = entries

# Compute button
tk.Button(root, text="⚡ Compute", command=compute,
          font=("Arial", 12, "bold"), bg="#5E81AC", fg="white",
          activebackground="#81A1C1", activeforeground="white",
          relief="flat", padx=10, pady=5).pack(pady=10)

# Result
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14, "bold"),
         fg="#EBCB8B", bg="#2E3440").pack(pady=10)

root.mainloop()
