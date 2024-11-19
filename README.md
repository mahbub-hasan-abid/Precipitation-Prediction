
# Precipitation Prediction Using Milne's Method

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Libraries Used](#libraries-used)
4. [How It Works](#how-it-works)
5. [How to Run the Application](#how-to-run-the-application)
6. [Detailed Explanation of `milnes.py`](#detailed-explanation-of-milnespy)

## Overview

This Python project provides a **Graphical User Interface (GUI)** application that simulates **precipitation prediction** using **Milne's Method**. It allows users to input parameters like **initial precipitation**, **time steps**, **time increment (dt)**, **temperature**, and **humidity** to predict the change in precipitation over time. The program displays the results using a **Matplotlib graph** and a **scrollable iteration table**.

## Features

- **Input Fields** for entering:
   - Initial Precipitation
   - Number of Time Steps
   - Time Increment (dt)
   - Temperature
   - Humidity
   - Model selection (Model 1 or Model 2)

- **Real-Time Graph Update** using **Matplotlib**:
   - A graph is dynamically updated as the user modifies input fields.

- **Scrollable Iteration Table**:
   - Displays the precipitation values at each time step in a scrollable table.

- **Error Handling**:
   - Ensures that the input values are valid numerical entries.

## Libraries Used

- `Tkinter`: Used for creating the GUI application.
- `Matplotlib`: Used for plotting the precipitation prediction.
- `Numpy`: Used for numerical calculations in the simulation.

## How It Works

1. **Precipitation Rate Function**: The precipitation rate is calculated based on the selected model, temperature, and humidity.
      - **Model 1**: Uses a linear formula based on precipitation, temperature, and humidity.
      - **Model 2**: A different linear model with a slightly modified formula.

2. **Milne's Method**: The method iteratively predicts precipitation values over the specified number of time steps:
      - The algorithm first predicts the precipitation at the next time step and then corrects it using a weighted average of the current and predicted rates.

3. **Graph**: Displays the predicted precipitation as a function of time.
      - The x-axis represents time, and the y-axis represents the precipitation value.

4. **Iteration Table**: Shows each time step’s value of time and precipitation, allowing users to see the progression of the simulation.

## How to Run the Application

1. Clone the repository.
2. Install the required libraries:

      ```
      pip install tkinter matplotlib numpy
      ```

3. Run the Python script:

      ```
      python <filename>.py
      ```

4. Enter the desired parameters in the input fields, and the simulation will generate a graph and an iteration table with the results.

## Detailed Explanation of `milnes.py`

The `milnes.py` script is the core of the precipitation prediction application. Here is a detailed breakdown of its components:

### Importing Libraries

```python
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
```

- `tkinter` and `ttk` are used for creating the GUI.
- `matplotlib.pyplot` and `FigureCanvasTkAgg` are used for embedding the Matplotlib graph in the Tkinter window.
- `numpy` is used for numerical calculations.

### Defining the Precipitation Rate Functions

```python
def precipitation_rate_model_1(precipitation, temperature, humidity):
         return 0.1 * precipitation + 0.05 * temperature + 0.02 * humidity

def precipitation_rate_model_2(precipitation, temperature, humidity):
         return 0.08 * precipitation + 0.06 * temperature + 0.03 * humidity
```

- Two models are defined to calculate the precipitation rate based on different linear formulas.

### Milne's Method Implementation

```python
def milnes_method(initial_precipitation, time_steps, dt, temperature, humidity, model):
         precipitation_values = [initial_precipitation]
         for i in range(1, time_steps):
                  if model == 1:
                           rate = precipitation_rate_model_1(precipitation_values[-1], temperature, humidity)
                  else:
                           rate = precipitation_rate_model_2(precipitation_values[-1], temperature, humidity)
                  next_precipitation = precipitation_values[-1] + dt * rate
                  precipitation_values.append(next_precipitation)
         return precipitation_values
```

- This function uses Milne's Method to predict precipitation values over the specified number of time steps.

### Creating the GUI

```python
class PrecipitationPredictionApp:
         def __init__(self, root):
                  self.root = root
                  self.root.title("Precipitation Prediction Using Milne's Method")
                  self.create_widgets()
                  
         def create_widgets(self):
                  # Code to create input fields, buttons, and other GUI components
                  pass
                  
         def update_graph(self):
                  # Code to update the graph based on user input
                  pass
                  
         def update_table(self):
                  # Code to update the iteration table based on user input
                  pass
```

- The `PrecipitationPredictionApp` class initializes the GUI and contains methods to create widgets, update the graph, and update the iteration table.

