from tkinter import *
import tkinter as tk
from tkinter import ttk

from available_sensors import SENSORS


class Ui(tk.Tk):
    def __init__(self):
        super().__init__()

        window = tk.Tk()
        window.title("Rainforest Application")

        tabControl = ttk.Notebook(window)
        tab_environment = ttk.Frame(tabControl)
        tab_animals = ttk.Frame(tabControl)

        tabControl.add(tab_environment, text='Environment')
        tabControl.add(tab_animals, text='Animals')
        tabControl.pack(expand=1, fill="both")

        # Set other parts of UI in another class/method

        ttk.Label(
            tab_environment,
            text="Qui ci metti le hose"
        ).grid(column=0, row=0, padx=30, pady=30)

        ttk.Label(
            tab_animals,
            text="Qui ci metti le altre hose"
        ).grid(column=0, row=0, padx=30, pady=30)

    def update(self):
        self._update_data()
        self.after(2000, self.update)

    def _update_data(self):
        # self.label1.configure(
        #     text=f'User Presence Sensor value {SENSORS[0].value}'
        # )
        # self.label2.configure(
        #     text=f'Water Vaporizer value {SENSORS[1].value}'
        # )
        pass
