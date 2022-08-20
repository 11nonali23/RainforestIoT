from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

from sensors.available_sensors import SENSORS
from ui.tabs import AnimalsUI, EnvironmentUI


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.window = tk.Toplevel()
        self.window.title("Rainforest Application")
        self.window.geometry("1300x700")

        self.tabControl = ttk.Notebook(self.window)
        self.tab_environment = tk.Frame(self.tabControl)
        self.tabControl.add(self.tab_environment, text='Environment')
        self.tab_animals = tk.Frame(self.tabControl)
        self.tabControl.add(self.tab_animals, text='Animals')
        self.tabControl.pack(expand=1, fill="both")

        # Set other parts of UI in another class/method
        # I should use dependency injection......
        self.environmentUI = EnvironmentUI(self.tab_environment)
        self.animalsUI = AnimalsUI(self.tab_animals)

    def update(self):
        self._update_data()
        self.after(2000, self.update)

    def _update_data(self):
        self.environmentUI.presence_value.configure(
            text="Present" if SENSORS[0].value else "Not Present"
        )
