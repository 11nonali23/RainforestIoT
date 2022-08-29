from sensors.available_sensors import exists


AVAILABLE_ACTIONS = ["GET", "SET"]


class Command:
    def __init__(self, data: str):
        self.error_message = "ERRORS: "
        self._parse(data)
        self._validate()

    def _parse(self, data: str):
        data = data.split(" ")
        self.action = data[0]
        self.sensor_id = data[1]
        try:
            self.value = self._parse_value(data[2])
        except IndexError:
            self.value = None

    def _validate(self):
        self.valid = True
        if not self.action in AVAILABLE_ACTIONS:
            self.error_message += f"- invalid action {self.action}"
            self.valid = False
        if not exists(self.sensor_id):
            self.error_message += f"- invalid sensor id {self.sensor_id}"
            self.valid = False

    # For now parsing is needed only on boolean values
    def _parse_value(self, value_str):
        if value_str == "true":
            return True
        return False

    def __str__(self) -> str:
        return f"Command({self.action})"
