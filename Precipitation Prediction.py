import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def precipitation_rate(t, P, temperature, humidity, model):
    if model == 'Model 1':
        return 0.1 * P * (1 - P / 100) + 0.05 * temperature + 0.03 * humidity
    elif model == 'Model 2':
        return 0.2 * P * (1 - P / 150) + 0.07 * temperature + 0.02 * humidity
    return 0.1 * P

def milnes_method(initial_precipitation, time_steps, dt, temperature, humidity, model):
    P = [initial_precipitation]
    for i in range(1, time_steps):
        t = i * dt
        P_pred = P[i - 1] + dt * precipitation_rate(t - dt, P[i - 1], temperature, humidity, model)
        P_corr = P[i - 1] + (dt / 2) * (precipitation_rate(t - dt, P[i - 1], temperature, humidity, model) +
                                        precipitation_rate(t, P_pred, temperature, humidity, model))
        P.append(P_corr)
    return P

def update_plot():
    try:
        initial_precipitation = float(entry_initial.get())
        time_steps = int(entry_steps.get())
        dt = float(entry_dt.get())
        temperature = float(slider_temp.get())
        humidity = float(slider_humidity.get())
        model = combo_model.get()
        P = milnes_method(initial_precipitation, time_steps, dt, temperature, humidity, model)
        ax.clear()
        time_values = np.arange(0, time_steps * dt, dt)
        ax.plot(time_values, P, label='Predicted Precipitation', color='blue', linewidth=2)
        ax.set_title('Precipitation Prediction Using Milne\'s Method', fontsize=12, color='darkblue')
        ax.set_xlabel('Time', fontsize=10)
        ax.set_ylabel('Precipitation', fontsize=10)
        ax.legend()
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        canvas.draw()
        display_textual_info(initial_precipitation, time_steps, dt, temperature, humidity, model, P)
        display_iteration_table(time_steps, dt, P)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def display_textual_info(initial_precipitation, time_steps, dt, temperature, humidity, model, P):
    info = (
        f"Initial Precipitation: {initial_precipitation}\n"
        f"Number of Time Steps: {time_steps}\n"
        f"Time Increment (dt): {dt}\n"
        f"Temperature: {temperature}\n"
        f"Humidity: {humidity}\n"
        f"Selected Model: {model}\n"
        f"Final Predicted Precipitation: {P[-1]:.2f}\n"
    )
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, info)

def display_iteration_table(time_steps, dt, P):
    # Clear the treeview before adding new data
    for row in tree.get_children():
        tree.delete(row)
    
    # Add data to the table
    for i in range(time_steps):
        time_value = i * dt
        precipitation_value = round(P[i], 2)
        tree.insert("", tk.END, values=(round(time_value, 2), precipitation_value))

root = tk.Tk()
root.title("Precipitation Prediction")
root.geometry("1000x700")
root.configure(bg="#f0f8ff")

frame_left = tk.Frame(root, bg="#add8e6", padx=15, pady=15, relief=tk.RIDGE, bd=2)
frame_left.pack(side=tk.LEFT, fill=tk.Y)

frame_right = tk.Frame(root, bg="#f0f8ff", padx=15, pady=15)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(frame_left, text="Initial Precipitation:", bg="#add8e6", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
entry_initial = tk.Entry(frame_left, font=("Arial", 12))
entry_initial.grid(row=0, column=1, pady=5)

tk.Label(frame_left, text="Number of Time Steps:", bg="#add8e6", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
entry_steps = tk.Entry(frame_left, font=("Arial", 12))
entry_steps.grid(row=1, column=1, pady=5)

tk.Label(frame_left, text="Time Increment (dt):", bg="#add8e6", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
entry_dt = tk.Entry(frame_left, font=("Arial", 12))
entry_dt.grid(row=2, column=1, pady=5)

tk.Label(frame_left, text="Select Model:", bg="#add8e6", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, pady=5)
combo_model = ttk.Combobox(frame_left, values=["Model 1", "Model 2"], font=("Arial", 12))
combo_model.set("Model 1")
combo_model.grid(row=3, column=1, pady=5)

tk.Label(frame_left, text="Temperature:", bg="#add8e6", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.W, pady=5)
slider_temp = tk.Scale(frame_left, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda _: update_plot(), bg="#f0f8ff")
slider_temp.grid(row=4, column=1, pady=5)

tk.Label(frame_left, text="Humidity:", bg="#add8e6", font=("Arial", 12)).grid(row=5, column=0, sticky=tk.W, pady=5)
slider_humidity = tk.Scale(frame_left, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda _: update_plot(), bg="#f0f8ff")
slider_humidity.grid(row=5, column=1, pady=5)

fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_right)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

text_output = tk.Text(frame_right, height=10, font=("Arial", 12), bg="#e0ffff", fg="darkblue", wrap=tk.WORD)
text_output.pack(fill=tk.BOTH, expand=True)

# Create a treeview to display iterations in a scrollable table
tree_frame = tk.Frame(frame_right, bg="#f0f8ff")
tree_frame.pack(fill=tk.BOTH, expand=True)

tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(tree_frame, columns=("Time", "Precipitation"), show="headings", yscrollcommand=tree_scroll.set)
tree.heading("Time", text="Time")
tree.heading("Precipitation", text="Precipitation")

tree.column("Time", width=100, anchor=tk.CENTER)
tree.column("Precipitation", width=150, anchor=tk.CENTER)

tree.pack(fill=tk.BOTH, expand=True)
tree_scroll.config(command=tree.yview)

# Bind events to update plot
entry_initial.bind("<KeyRelease>", lambda _: update_plot())
entry_steps.bind("<KeyRelease>", lambda _: update_plot())
entry_dt.bind("<KeyRelease>", lambda _: update_plot())
combo_model.bind("<<ComboboxSelected>>", lambda _: update_plot())

root.mainloop()
