import tkinter as tk


class TemperatureDisplayBar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.temperature = tk.DoubleVar()
        self.init_ui()

    def init_ui(self):
        self.master.title("Temperature Display (Bar)")
        self.pack(fill=tk.BOTH, expand=True)

        self.temperature.set(25.0)  # Initial temperature value

        tk.Label(self, text="Indoor Temperature").pack(pady=5)

        # Additional information
        tk.Label(self, text="Units: °C").pack()
        tk.Label(self, text="Low Value: 10°C").pack()
        tk.Label(self, text="Normal Range: 10°C - 30°C").pack()
        tk.Label(self, text="High Value: 30°C").pack()

        self.temperature_bar = tk.Canvas(self, bg='white', height=30)
        self.temperature_bar.pack(fill=tk.X, padx=10)
        self.update_temperature_bar()

        tk.Label(self, text="Set Temperature:").pack(pady=5)
        self.temperature_entry = tk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.pack(pady=5)

        tk.Button(self, text="Update", command=self.update_temperature_bar).pack()

    def update_temperature_bar(self):
        self.temperature_bar.delete("all")
        temperature_value = self.temperature.get()

        # Cap temperature value at maximum allowed value (30°C)
        temperature_value = min(temperature_value, 30)

        width = (temperature_value - 10) * 10  # Adjusting width for better visualization
        self.temperature_bar.create_rectangle(0, 0, width, 30, fill='lightblue', outline='blue')

        # Displaying temperature value along the bar line
        self.temperature_bar.create_text(width, 15, text=f"{temperature_value}°C", anchor=tk.W)


def main():
    root = tk.Tk()
    TemperatureDisplayBar(root)
    root.mainloop()


if __name__ == "__main__":
    main()
