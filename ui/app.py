import tkinter as tk
from tkinter import ttk

from sensors.available_sensors import randomize
from ui.tabs import AnimalsUI, EnvironmentUI


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rainforest Application")
        self.geometry("800x500")

        self.tabControl = ttk.Notebook(self)
        self.tab_environment = tk.Frame(self.tabControl)
        self.tabControl.add(self.tab_environment, text='Environment')
        self.tab_animals = tk.Frame(self.tabControl)
        self.tabControl.add(self.tab_animals, text='Birds')
        self.tabControl.pack(expand=1, fill="both")

        # I should use dependency injection
        self.environmentUI = EnvironmentUI(self.tab_environment)
        self.animalsUI = AnimalsUI(self.tab_animals)

    def update(self):
        self._update_ui()
        self.after(1000, self.update)

    def randomize(self):
        randomize()
        self.after(10000, self.randomize)

    def _update_ui(self):
        self.environmentUI.update()
        self.animalsUI.update()
