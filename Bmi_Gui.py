# ---------------------------------------------
# GUI Version of BMI Calculator (Tkinter)
#
# This script was developed with external help,
# including AI-generated suggestions and online
# resources, as part of learning how to build GUIs
# in Python. While the logic was based on my own
# CLI BMI calculator, the GUI structure and syntax
# were adapted with assistance.
# ---------------------------------------------

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError
        bmi = round(weight / (height ** 2), 2)
        result_label.config(text=f"Your BMI is: {bmi}")
        check_button.config(state="normal")  # Enable category check
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers for weight and height.")

def check_category():
    try:
        bmi_text = result_label.cget("text")
        if "BMI is:" not in bmi_text:
            raise ValueError
        bmi = float(bmi_text.split(":")[1].strip())
        category = get_bmi_category(bmi)
        messagebox.showinfo("BMI Category", f"According to WHO:\n{category}")
    except:
        messagebox.showerror("Error", "Could not determine BMI category.")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obesity Class I"
    elif 35 <= bmi < 40:
        return "Obesity Class II"
    else:
        return "Obesity Class III"

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    check_button.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")

tk.Label(root, text="Enter Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Enter Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

check_button = tk.Button(root, text="Check BMI Category", command=check_category, state="disabled")
check_button.pack(pady=5)

tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
