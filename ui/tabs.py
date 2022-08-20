from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
from sensors.available_sensors import SENSORS


from ui.components import AnimalInformations, DigitalEntry, OnOffSwtich, Title


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
        self._build_left_column(tab)
        self._build_right_column(tab)

    def _build_left_column(self, tab):
        self.vaporize_title = Title(
            tab,
            text="Water Vaporizer"
        )
        self.vaporize_title.label.grid(
            column=0, row=0, sticky=tk.W, padx=5, pady=5
        )

        self.vaporizer_switch = OnOffSwtich(
            self.tab,
            SENSORS[1]
        )
        self.vaporizer_switch.switch_button.grid(
            column=0, row=1, sticky=tk.W, padx=5, pady=5
        )
        self.vaporize_power_label = tk.Label(
            tab,
            text="Vaporizer Power"
        )
        self.vaporize_power_label.grid(
            column=0, row=2, sticky=tk.W, padx=5, pady=5
        )

        # TODO digital entry callbacks
        self.vaporizer_power = DigitalEntry(
            self.tab,
            value=SENSORS[2].value
        )
        self.vaporizer_power.entry.grid(
            column=0, row=3, sticky=tk.W, padx=5, pady=5
        )

        self.left_separator = ttk.Separator(
            master=tab,
            style='blue.TSeparator',
            class_=ttk.Separator,
            takefocus=1,
            cursor='plus'
        )
        self.left_separator.grid(row=5, column=0, ipadx=200, pady=10)

        self.irrigator_title = Title(
            tab,
            text="Irrigator"
        )
        self.irrigator_title.label.grid(
            column=0, row=6, sticky=tk.W, padx=5, pady=5
        )

        self.irrigator_switch = OnOffSwtich(
            self.tab,
            SENSORS[3]
        )
        self.irrigator_switch.switch_button.grid(
            column=0, row=7, sticky=tk.W, padx=5, pady=5
        )
        self.irrigator_label = tk.Label(
            tab,
            text="Irrigator Power"
        ).grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)

        self.irrigator_power = DigitalEntry(
            self.tab,
            value=SENSORS[4].value
        )
        self.irrigator_power.entry.grid(
            column=0, row=9, sticky=tk.W, padx=5, pady=5
        )

    def _build_right_column(self, tab):
        self.presence_title = Title(
            tab,
            text="User Presence"
        )
        self.presence_title.label.grid(
            column=1, row=0, sticky=tk.W, padx=5, pady=5
        )

        self.presence_value = tk.Label(
            tab,
            text="Present" if SENSORS[0].value else "Not Present"
        )
        self.presence_value.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        self.humidity_level = Title(
            tab,
            text="Humidity Level"
        )
        self.humidity_level.label.grid(
            column=1, row=2, sticky=tk.W, padx=5, pady=5
        )

        self.humidity_value = tk.Label(
            tab,
            text=SENSORS[5].value
        )
        self.humidity_value.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        self.right_separator = ttk.Separator(
            master=tab,
            style='blue.TSeparator',
            class_=ttk.Separator,
            takefocus=1,
            cursor='plus'
        )
        self.right_separator.grid(row=5, column=1, ipadx=200, pady=0)

        self.soil_moisture_level = Title(
            tab,
            text="Soil Moisture Level"
        )
        self.soil_moisture_level.label.grid(
            column=1, row=7, sticky=tk.W, padx=5, pady=5
        )

        self.soil_moisture_value = tk.Label(
            tab,
            text=SENSORS[6].value
        )
        self.soil_moisture_value.grid(
            column=1, row=8, sticky=tk.W, padx=5, pady=5
        )


class AnimalsUI(TabUI):
    def __init__(self, tab: tk.Frame) -> None:
        super().__init__(tab)

    def _generateUI(self, tab: tk.Frame):
        sensors_pos = [7, 8, 9]
        # TODO find a more elgant way
        offset = 0
        for index, pos in enumerate(sensors_pos):
            AnimalInformations(
                self.tab,
                SENSORS[pos],
                SENSORS[pos + 3],
                index + offset,
                index
            )
            offset = offset + 4
