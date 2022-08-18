from abc import ABC
from dataclasses import dataclass
import json


@dataclass
class Sensor(ABC):
    _id: str
    name: str

    def get_value(self) -> str:
        return str(self.value)

    def set_value(self, value: bool) -> str:
        # I have to do some validation
        self.value = value
        return f"SET {self._id} to {value} OK"

    def do(self, command):
        if command.action == "GET":
            return self.get_value()
        if command.action == "SET":
            return self.set_value(command.value)
        return "ERROR - invalid message"


@dataclass
class AnalogicalSensor(Sensor):
    value: bool


@dataclass
class DigitalSensor(Sensor):
    value: float


@dataclass
class JSONSensor(Sensor):
    value: dict

    def get_value(self) -> str:
        return json.dumps(self.value)
