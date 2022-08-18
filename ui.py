from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import update

from pip import main
from server import Server


class Ui(tk.Tk):
    def __init__(self):
        super().__init__()

        windows = tk.Tk()
        windows.title("My Application")

        self.label = tk.Label(windows, text="Hello World")
        self.label.grid(column=0, row=0)

        self.label1 = tk.Label(windows)
        self.label1.grid(column=0, row=1)

        self.custom_button = ttk.Button(
            windows,
            text="Click on me",
            command=self._clicked
        )
        self.custom_button.grid(column=1, row=0)

    def update(self, server):
        self._update_data(server.count)
        self.after(2000, self.update, server)

    def _update_data(self, data):
        self.count = data
        self.label1.configure(text=f'Button was clicked {self.count} times!!!')

    def _clicked(self):
        self.count = self.count + 1
        self.label1.configure(text=f'Button was clicked {self.count} times!!!')
