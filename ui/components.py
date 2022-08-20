import tkinter as tk

from sensors.sensor import Sensor


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

    def _callback(self):
        self._default_callback()

    def _default_callback(self):
        if self.is_on():
            self.switch_button.config(image=self.off_image)
            self.sensor.value = False
        else:
            self.switch_button.config(image=self.on_image)
            self.sensor.value = True


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

    def __init__(self, tab: tk.Frame, health_sensor: Sensor, gps_sensor: Sensor, start_row: int):
        self.tab = tab
        self.health_sensor = health_sensor
        self.gps_sensor = gps_sensor
        self._build(start_row)

    def _build(self, start_row):
        self.title = Title(
            self.tab,
            text="Bird Informations"
        )
        self.title.label.grid(column=0, row=start_row,
                              sticky=tk.W, padx=5, pady=5)

        self.heart_beat = tk.Label(
            self.tab,
            text=f"heart beat: {self.health_sensor.value.get('hb')}"
        )
        self.heart_beat.grid(column=0, row=start_row + 1,
                             sticky=tk.W, padx=5, pady=5)

        self.body_temperature = tk.Label(
            self.tab,
            text=f"body temperature: {self.health_sensor.value.get('body_tem')}"
        )
        self.body_temperature.grid(
            column=0, row=start_row + 2, sticky=tk.W, padx=5, pady=5
        )

        self.location = tk.Label(
            self.tab,
            text=f"location: {self.gps_sensor.value.get('lat')} lat - {self.gps_sensor.value.get('lon')} lon"
        )
        self.location.grid(
            column=0, row=start_row + 3, sticky=tk.W, padx=5, pady=5
        )
