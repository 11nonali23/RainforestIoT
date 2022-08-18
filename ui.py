from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

from available_sensors import SENSORS


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
        # self.label1.configure(
        #     text=f'User Presence Sensor value {SENSORS[0].value}'
        # )
        # self.label2.configure(
        #     text=f'Water Vaporizer value {SENSORS[1].value}'
        # )
        pass


class TabUI(ABC):
    def __init__(self, tab: tk.Frame) -> None:
        self.tab = tab
        self._generateUI(tab)

    @abstractmethod
    def _generateUI():
        pass


class OnOffSwtich():

    def __init__(self, tab: tk.Frame, is_on: bool, custom_callback):
        self.tab = tab
        self.is_on = is_on
        self.custom_callback = custom_callback
        self.on_image = tk.PhotoImage(file="images/on.png")
        self.off_image = tk.PhotoImage(file="images/off.png")

        self.switch_button = tk.Button(
            self.tab,
            image=self.on_image if is_on else self.off_image,
            bd=0,
            command=self._callback
        )

    def _callback(self):
        self._default_callback()
        self.custom_callback()

    def _default_callback(self):
        if self.is_on:
            self.switch_button.config(image=self.off_image)
            self.is_on = False
        else:
            self.switch_button.config(image=self.on_image)
            self.is_on = True


# entry should then set the value
class DigitalEntry:

    def __init__(self, tab: tk.Frame, value: float):
        self.tab = tab
        self.value = str(value)

        self.entry = tk.Entry(
            self.tab,
            bd=0
        )
        self.entry.insert(0, value)
        self.entry.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)


# TODO set the values from available sensors and all the callbacks
class EnvironmentUI(TabUI):
    def __init__(self, tab: tk.Frame) -> None:
        super().__init__(tab)

    def _generateUI(self, tab: tk.Frame):
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=1)
        self.vaporize_label = tk.Label(
            tab,
            text="Water Vaporizer"
        )
        self.vaporize_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.vaporizer_switch = OnOffSwtich(
            self.tab,
            is_on=False,
            custom_callback=lambda: None
        )
        self.vaporizer_switch.switch_button.grid(
            column=0, row=1, sticky=tk.W, padx=5, pady=5
        )
        self.vaporize_label = tk.Label(
            tab,
            text="Vaporizer Power"
        ).grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.vaporizer_power = DigitalEntry(
            self.tab,
            value=30.0
        )
        self.vaporizer_power.entry.grid(
            column=0, row=3, sticky=tk.W, padx=5, pady=5
        )

        self.presence_label = tk.Label(
            tab,
            text="User Presence"
        )
        self.presence_label.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        self.presence_value = tk.Label(
            tab,
            text="Present"
        )
        self.presence_value.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        self.humidity_level = tk.Label(
            tab,
            text="Humidity Level"
        )
        self.humidity_level.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        self.humidity_value = tk.Label(
            tab,
            text="30.0"
        )
        self.humidity_value.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        # TODO self.separator = ttk.Separator(self.tab, orient='horizontal')
        #self.separator.grid(row=4, sticky=tk.W, padx=5, pady=5)


class AnimalsUI(TabUI):
    def __init__(self, tab: tk.Frame) -> None:
        super().__init__(tab)

    def _generateUI(self, tab: tk.Frame):
        tk.Label(
            tab,
            text="Qui ci metti le altre hose"
        ).grid(column=0, row=0, padx=30, pady=30)
