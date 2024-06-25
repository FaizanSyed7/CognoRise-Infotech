import tkinter as tk
from tkinter import messagebox
import threading

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# Global variable to handle timer thread stopping
stop_timer = False

def start_timer():
    global stop_timer
    stop_timer = False
    try:
        # Convert input time to seconds
        total_time = int(hours_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get())
        # Start the countdown in a separate thread
        threading.Thread(target=count_down, args=(total_time,)).start()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def count_down(total_time):
    global stop_timer
    while total_time > 0 and not stop_timer:
        mins, secs = divmod(total_time, 60)
        hours, mins = divmod(mins, 60)
        time_display = f'{hours:02}:{mins:02}:{secs:02}'
        time_label.config(text=time_display)
        time.sleep(1)
        total_time -= 1
    if not stop_timer:
        messagebox.showinfo("Time's up", "Countdown finished")

def reset_timer():
    global stop_timer
    stop_timer = True
    hours_entry.delete(0, tk.END)
    minutes_entry.delete(0, tk.END)
    seconds_entry.delete(0, tk.END)
    time_label.config(text="00:00:00")

# Create the GUI elements
hours_label = tk.Label(root, text="Hours:")
hours_label.grid(row=0, column=0, padx=5, pady=5)
hours_entry = tk.Entry(root, width=5)
hours_entry.grid(row=0, column=1, padx=5, pady=5)

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.grid(row=1, column=0, padx=5, pady=5)
minutes_entry = tk.Entry(root, width=5)
minutes_entry.grid(row=1, column=1, padx=5, pady=5)

seconds_label = tk.Label(root, text="Seconds:")
seconds_label.grid(row=2, column=0, padx=5, pady=5)
seconds_entry = tk.Entry(root, width=5)
seconds_entry.grid(row=2, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.grid(row=3, column=0, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.grid(row=3, column=1, padx=5, pady=5)

time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
time_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
