import tkinter as tk
from tkinter import *

def calculate_bmi():
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    bmi = weight / (height ** 2)
    result = f"Your BMI is: {bmi:.2f}"
    label_result.config(text=result)

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place the height label and entry
label_height = tk.Label(root, text="Height (m):")
label_height.grid(row=0, column=0, padx=10, pady=10)

entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1, padx=10, pady=10)

# Create and place the weight label and entry
label_weight = tk.Label(root, text="Weight (kg):")
label_weight.grid(row=1, column=0, padx=10, pady=10)

entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and place the result label
label_result = tk.Label(root, text="Your BMI will be displayed here")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()