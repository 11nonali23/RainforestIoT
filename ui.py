from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import update

from available_sensors import SENSORS


class Ui(tk.Tk):
    def __init__(self):
        super().__init__()

        windows = tk.Tk()
        windows.title("My Application")

        self.label = tk.Label(windows, text="Hello World")
        self.label.grid(column=0, row=0)

        self.label1 = tk.Label(windows)
        self.label1.grid(column=0, row=1)

        self.label2 = tk.Label(windows)
        self.label2.grid(column=0, row=2)

    def update(self):
        self._update_data()
        self.after(2000, self.update)

    def _update_data(self):
        self.label1.configure(
            text=f'User Presence Sensor value {SENSORS[0].value}'
        )
        self.label2.configure(
            text=f'Water Vaporizer value {SENSORS[1].value}'
        )
