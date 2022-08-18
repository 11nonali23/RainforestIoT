from sensors.available_sensors import exists


AVAILABLE_ACTIONS = ["GET", "SET"]


class Command:
    def __init__(self, data: str, sensors):
        self.error_message = "ERRORS: "
        self._parse(data)
        self._validate(sensors)

    def _parse(self, data: str):
        data = data.split(" ")
        self.action = data[0]
        self.sensor_id = data[1]
        self.value = data[2] if 2 < len(data) else None

    def _validate(self, sensors):
        self.valid = True
        if not self.action in AVAILABLE_ACTIONS:
            self.error_message += "- invalid action "
            self.valid = False
        if not exists(self.sensor_id):
            self.error_message += "- invalid sensor id"
            self.valid = False

    def __str__(self) -> str:
        return f"Command({self.action}, {self.sensor_id})"
