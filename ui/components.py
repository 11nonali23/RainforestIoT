import tkinter as tk


class OnOffSwtich():

    def __init__(self, tab: tk.Frame, is_on: bool, custom_callback):
        self.tab = tab
        self.is_on = is_on
        self.custom_callback = custom_callback
        self.on_image = tk.PhotoImage(file="ui/images/on.png")
        self.off_image = tk.PhotoImage(file="ui/images/off.png")

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
