import tkinter as tk

def calculate_average():
    try:
        score1 = float(entry1.get())
        score2 = float(entry2.get())
        score3 = float(entry3.get())
        average = (score1 + score2 + score3) / 3
        result_label.config(text=f"Average: {average:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid scores.")

# Create the main window
root = tk.Tk()
root.title("Test Average Calculator")

# Create Entry widgets
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# Create a Label to display the result
result_label = tk.Label(root, text="Average: ")

# Create a Button to calculate the average
calculate_button = tk.Button(root, text="Calculate Average", command=calculate_average)

# Grid layout
entry1.grid(row=0, column=0)
entry2.grid(row=1, column=0)
entry3.grid(row=2, column=0)
calculate_button.grid(row=3, column=0)
result_label.grid(row=4, column=0)

# Run the application
root.mainloop()

