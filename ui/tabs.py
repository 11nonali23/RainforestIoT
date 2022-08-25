from abc import ABC, abstractmethod
from sqlite3 import Row
import tkinter as tk
from tkinter import ttk
from sensors.available_sensors import SENSORS


from ui.components import AnimalInformations, DigitalEntry, SensorRadioOption, Title


class TabUI(ABC):
    def __init__(self, tab: tk.Frame) -> None:
        self.tab = tab
        self._generateUI(tab)

    @abstractmethod
    def _generateUI(self, tab):
        pass

    @abstractmethod
    def update(self):
        pass


class EnvironmentUI(TabUI):
    def __init__(self, tab: tk.Frame) -> None:
        super().__init__(tab)

    def _generateUI(self, tab: tk.Frame):
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

        self.vaporizer_radio = SensorRadioOption(
            self.tab,
            SENSORS[1]
        )
        self.vaporizer_radio.on.place(x=5, y=35)
        self.vaporizer_radio.off.place(x=55, y=35)
        self.vaporizer_radio.auto.place(x=110, y=35)

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
            column=0, row=3, sticky=tk.W,
        )

        self.left_separator = ttk.Separator(
            master=tab,
            style='blue.TSeparator',
            class_=ttk.Separator,
            takefocus=1,
            cursor='plus'
        )
        self.left_separator.grid(row=4, column=0, ipadx=190, pady=10)

        self.irrigator_title = Title(
            tab,
            text="Irrigator"
        )
        self.irrigator_title.label.grid(
            column=0, row=5, sticky=tk.W,
        )

        self.irrigator_radio = SensorRadioOption(
            self.tab,
            SENSORS[3]
        )
        self.irrigator_radio.on.place(x=5, y=190)
        self.irrigator_radio.off.place(x=55, y=190)
        self.irrigator_radio.auto.place(x=110, y=190)

        self.irrigator_label = tk.Label(
            tab,
            text="Irrigator Power"
        ).grid(column=0, row=9, sticky=tk.W,)

        self.irrigator_power = DigitalEntry(
            self.tab,
            value=SENSORS[4].value
        )
        self.irrigator_power.entry.grid(
            column=0, row=10, sticky=tk.W, padx=5, pady=5
        )

    def _build_right_column(self, tab):
        self.presence_title = Title(
            tab,
            text="User Presence"
        )
        self.presence_title.label.grid(
            column=3, row=0, sticky=tk.W, padx=5, pady=5
        )

        self.presence_value = tk.Label(
            tab,
            text="Present" if SENSORS[0].value else "Not Present"
        )
        self.presence_value.grid(column=3, row=1, sticky=tk.W, padx=5, pady=5)

        self.humidity_level = Title(
            tab,
            text="Humidity Level"
        )
        self.humidity_level.label.grid(
            column=3, row=2, sticky=tk.W, padx=5, pady=5
        )

        self.humidity_value = tk.Label(
            tab,
            text=SENSORS[5].value
        )
        self.humidity_value.grid(column=3, row=3, sticky=tk.W,)

        self.right_separator = ttk.Separator(
            master=tab,
            style='blue.TSeparator',
            class_=ttk.Separator,
            takefocus=1,
            cursor='plus'
        )
        self.right_separator.grid(row=4, column=3, ipadx=190, pady=0)

        self.soil_moisture_level = Title(
            tab,
            text="Soil Moisture Level"
        )
        self.soil_moisture_level.label.grid(
            column=3, row=7, sticky=tk.W,
        )

        self.soil_moisture_value = tk.Label(
            tab,
            text=SENSORS[6].value
        )
        self.soil_moisture_value.grid(
            column=3, row=8, sticky=tk.W,
        )

    def update(self):
        self.presence_value.configure(
            text="Present" if SENSORS[0].value else "Not Present"
        )
        self.humidity_value.configure(
            text=SENSORS[5].value,
            bg="red" if SENSORS[16].value else "SystemButtonFace"
        )
        self.soil_moisture_value.configure(
            text=SENSORS[6].value,
            bg="red" if SENSORS[17].value else "SystemButtonFace"
        )
        self.vaporizer_radio.update()
        self.irrigator_radio.update()


class AnimalsUI(TabUI):
    def __init__(self, tab: tk.Frame) -> None:
        super().__init__(tab)

    def _generateUI(self, tab: tk.Frame):
        self.animal_informations = []
        sensors_pos = [7, 8, 9]
        offset = 0
        for index, pos in enumerate(sensors_pos):
            animal_info = AnimalInformations(
                self.tab,
                SENSORS[pos],
                SENSORS[pos + 3],
                index + offset,
                index
            )
            self.animal_informations.append(animal_info)
            offset = offset + 4

    def update(self):
        for animal_info in self.animal_informations:
            animal_info.update()
