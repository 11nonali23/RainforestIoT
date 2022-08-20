from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

from sensors.available_sensors import SENSORS
from ui.tabs import AnimalsUI, EnvironmentUI


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        window = tk.Toplevel()
        window.title("Rainforest Application")
        window.geometry("1300x700")

        tabControl = ttk.Notebook(window)
        tab_environment = tk.Frame(tabControl)
        tab_animals = tk.Frame(tabControl)

        tabControl.add(tab_environment, text='Environment')
        tabControl.add(tab_animals, text='Animals')
        tabControl.pack(expand=1, fill="both")

        # Set other parts of UI in another class/method
        # I should use dependency injection......
        self.environmentUI = EnvironmentUI(tab_environment)
        self.animalsUI = AnimalsUI(tab_animals)

    def update(self):
        self._update_data()
        self.after(2000, self.update)

    def _update_data(self):
        self.environmentUI.presence_value.configure(
            text="Present" if SENSORS[0].value else "Not Present"
        )
