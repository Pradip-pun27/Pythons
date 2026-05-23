import tkinter as tk

# Function to add two numbers and display the result
def add_numbers():
    num1 = int(entry1.get())  # Get first number from entry
    num2 = int(entry2.get())  # Get second number from entry
    result_var.set(num1 + num2)  # Set the result in the result_var

# Function to subtract two numbers and display the result
def sub_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result_var.set(num1 - num2)

# Function to multiply two numbers and display the result
def mul_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result_var.set(num1 * num2)

# Function to divide two numbers and display the result
# Note: No zero division handling here

def Div_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result_var.set(num1 / num2)

# Create the main application window
window = tk.Tk()
window.title("Add Two Numbers")  # Set window title
window.geometry("400x350")       # Set window size
window.configure(bg="#f0f4f8")  # Set background color

# Header label for the calculator
header = tk.Label(window, text="Simple Calculator", font=("Arial", 18, "bold"), fg="#2d6cdf", bg="#f0f4f8")
header.pack(pady=10)

# Label and entry for the first number
label1 = tk.Label(window, text="First Number:", font=("Arial", 12), bg="#f0f4f8")
label1.pack()
entry1 = tk.Entry(window, font=("Arial", 12), bd=2, relief=tk.GROOVE, justify='center')
entry1.pack(pady=5)

# Label and entry for the second number
label2 = tk.Label(window, text="Second Number:", font=("Arial", 12), bg="#f0f4f8")
label2.pack()
entry2 = tk.Entry(window, font=("Arial", 12), bd=2, relief=tk.GROOVE, justify='center')
entry2.pack(pady=5)

# Result label and readonly entry to display the result
result_var = tk.StringVar()  # Variable to hold the result
result_label = tk.Label(window, text="Result:", font=("Arial", 12), bg="#f0f4f8")
result_label.pack(pady=(10,0))
result_entry = tk.Entry(window, textvariable=result_var, state='readonly', font=("Arial", 12), bd=2, relief=tk.SUNKEN, justify='center', fg="#1a8a34")
result_entry.pack(pady=5)

# Frame to hold the operation buttons side by side
btn_frame = tk.Frame(window, bg="#f0f4f8")
btn_frame.pack(pady=15)

# Button style dictionary for consistent styling
btn_style = {"font": ("Arial", 12, "bold"), "bg": "#2d6cdf", "fg": "white", "activebackground": "#1a4e8a", "activeforeground": "#f0f4f8", "bd": 0, "width": 7, "height": 1}

# Add, Subtract, Multiply, and Divide buttons
btn_add = tk.Button(btn_frame, text="Add", command=add_numbers, **btn_style)
btn_add.pack(side=tk.LEFT, padx=7)
btn_sub = tk.Button(btn_frame, text="Sub", command=sub_numbers, **btn_style)
btn_sub.pack(side=tk.LEFT, padx=7)
btn_mul = tk.Button(btn_frame, text="Mul", command=mul_numbers, **btn_style)
btn_mul.pack(side=tk.LEFT, padx=7)
btn_div = tk.Button(btn_frame, text="Div", command=Div_numbers, **btn_style)
btn_div.pack(side=tk.LEFT, padx=7)

# Start the Tkinter event loop
window.mainloop()