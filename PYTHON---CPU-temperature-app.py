import psutil
import tkinter as tk
from tkinter import Label
import time


def update_temperature():
    temp_data = psutil.sensors_temperatures()
    cpu_temp = temp_data.get("coretemp", None)
    if cpu_temp:
        current_temp = cpu_temp[0].current  # Get current CPU temperature
        label.config(text=f"CPU Temperature: {current_temp}°C")
    else:
        label.config(text="Temperature data not available.")
    root.after(1000, update_temperature)  # Update every second


# Create GUI
root = tk.Tk()
root.title("CPU Temperature Monitor")
label = Label(root, font=("Helvetica", 16))
label.pack(pady=20)

update_temperature()
root.mainloop()
