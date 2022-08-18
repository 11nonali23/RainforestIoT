import tkinter as tk

window = tk.Tk()

# DIGITAL
digital = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5)

title_dig = tk.Label(master=digital, text="Digital Devices")

temp_label = tk.Label(master=digital, text="Temperature")
temp_entry = tk.Entry(master=digital)

cleaner_label = tk.Label(master=digital, text="Cleaner")
cleaner_entry = tk.Entry(master=digital)

# ANALOGICAL
analogical = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5)

title_analog = tk.Label(master=analogical, text="Analogical Devices")


# PACKING
digital.pack(side=tk.LEFT)
analogical.pack(side=tk.LEFT)

title_dig.pack()
temp_label.pack()
temp_entry.pack()
cleaner_label.pack()
cleaner_entry.pack()

title_analog.pack()


window.mainloop()
