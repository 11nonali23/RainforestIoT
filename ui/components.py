import tkinter as tk

from sensors.sensor import Sensor


class OnOffSwtich():

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
