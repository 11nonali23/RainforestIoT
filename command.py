AVAILABLE_ACTIONS = ["GET", "SET"]


class Command:
    def __init__(self, data: str, sensors):
        self._parse(data)
        self._validate(sensors)

    def _parse(self, data: str):
        data = data.split(" ")
        self.action = data[0]
        self.sensor_id = data[1]
        self.value = data[2] if 2 < len(data) else None

    def _validate(self, sensors):
        sensor_exists = any(sensor._id == self.sensor_id for sensor in sensors)
        # do something for the value
        self.valid = sensor_exists and self.action in AVAILABLE_ACTIONS

    def __str__(self) -> str:
        return f"Command({self.action}, {self.sensor_id})"
