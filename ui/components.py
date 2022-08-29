from abc import ABC
import tkinter as tk
from sensors.available_sensors import SENSORS

from sensors.sensor import Sensor


class TabComponent(ABC):
    # Here I can define a hierarchy for every component, 'cause they need similar things
    pass


class Title:

    def __init__(self, tab: tk.Frame, text: str):
        self.tab = tab
        self.text = text
        self._build()

    def _build(self):
        self.label = tk.Label(
            self.tab,
            text=self.text,
            font=("Arial", 17)
        )


class OnOffSwtich:

    def __init__(self, tab: tk.Frame, sensor: Sensor):
        self.tab = tab
        self.sensor = sensor
        self.on_image = tk.PhotoImage(file="ui/images/on.png")
        self.off_image = tk.PhotoImage(file="ui/images/off.png")

        self.switch_button = tk.Button(
            self.tab,
            image=self.on_image if self.is_on() else self.off_image,
            bd=0,
            command=self._callback
        )

    def is_on(self):
        return self.sensor.value

    def update(self):
        if self.is_on():
            self.switch_button.config(image=self.on_image)
        else:
            self.switch_button.config(image=self.off_image)

    def _callback(self):
        if self.is_on():
            self.switch_button.config(image=self.off_image)
            self.sensor.value = False
        else:
            self.switch_button.config(image=self.on_image)
            self.sensor.value = True


class SensorRadioOption:

    def __init__(self, tab, sensor: Sensor) -> None:
        self.tab = tab
        self.sensor = sensor
        self.currentOption = tk.IntVar()
        self.currentOption.set(3)
        self._build()

    def _build(self):
        self.off = tk.Radiobutton(
            self.tab,
            text="Off",
            variable=self.currentOption,
            value=1,
            command=self.handleSelection
        )

        self.on = tk.Radiobutton(
            self.tab,
            text="On",
            variable=self.currentOption,
            value=2,
            command=self.handleSelection
        )

        self.auto = tk.Radiobutton(
            self.tab,
            text="Auto" if self.sensor.locked else f"Auto (now {self.sensor.value})",
            variable=self.currentOption,
            value=3,
            command=self.handleSelection
        )

    def handleSelection(self):
        choice = self.currentOption.get()

        if choice == 1:
            self.sensor.locked = False
            self.sensor.set_value(False)
            self.sensor.locked = True
        elif choice == 2:
            self.sensor.locked = False
            self.sensor.set_value(True)
            self.sensor.locked = True
        elif choice == 3:
            self.sensor.locked = False

    def update(self):
        self.auto.configure(
            text="Auto" if self.sensor.locked else f"Auto (now {self.sensor.value})",
        )


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


class AnimalInformations:

    def __init__(self, tab: tk.Frame, health_sensor: Sensor, gps_sensor: Sensor, start_row: int, bird_num: int):
        self.tab = tab
        self.health_sensor = health_sensor
        self.gps_sensor = gps_sensor
        self.bird_num = bird_num
        self._build(start_row)

    def _build(self, start_row):
        self.title = Title(
            self.tab,
            text=f"Bird{self.bird_num + 1} Informations"
        )
        self.title.label.grid(column=0, row=start_row,
                              sticky=tk.W, padx=5, pady=5)

        self.heart_beat = tk.Label(
            self.tab,
            text=f"heart beat: {self.health_sensor.value.get('hb')}",
        )
        self.heart_beat.grid(column=0, row=start_row + 1,
                             sticky=tk.W, padx=5, pady=5)

        self.body_temperature = tk.Label(
            self.tab,
            text=f"body temperature: {self.health_sensor.value.get('body_tem')}",
        )
        self.body_temperature.grid(
            column=0, row=start_row + 2, sticky=tk.W, padx=5, pady=5
        )

        self.location = tk.Label(
            self.tab,
            text=f"location: {self.gps_sensor.value.get('lat')} lat - {self.gps_sensor.value.get('lon')} lon",
        )
        self.location.grid(
            column=0, row=start_row + 3, sticky=tk.W, padx=5, pady=5
        )

    def update(self):
        self.heart_beat.configure(
            text=f"heart beat: {self.health_sensor.value.get('hb')}",
            bg="red" if SENSORS[15 +
                                self.bird_num].value else "#ECECEC"
        )
        self.body_temperature.configure(
            text=f"body temperature: {self.health_sensor.value.get('body_tem')}",
            bg="red" if SENSORS[18 +
                                self.bird_num].value else "#ECECEC"
        )
        self.location.configure(
            text=f"location: {self.gps_sensor.value.get('lat')} lat - {self.gps_sensor.value.get('lon')} lon",
            bg="red" if SENSORS[21 +
                                self.bird_num].value else "#ECECEC"
        )
