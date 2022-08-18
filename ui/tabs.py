from abc import ABC, abstractmethod
import tkinter as tk

from ui.components import DigitalEntry, OnOffSwtich


class TabUI(ABC):
    def __init__(self, tab: tk.Frame) -> None:
        self.tab = tab
        self._generateUI(tab)

    @abstractmethod
    def _generateUI():
        pass


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
