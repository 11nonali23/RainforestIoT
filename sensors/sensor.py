from abc import ABC, abstractmethod
from dataclasses import dataclass
import json
from random import randrange


@dataclass
class Sensor(ABC):
    _id: str
    name: str

    def get_value_str(self) -> str:
        return str(self.value)

    def set_value(self, value: bool) -> str:
        # I have to do some validation
        self.value = value
        return f"SET {self._id} to {value} OK"

    def do(self, command):
        if command.action == "GET":
            return self.get_value_str()
        if command.action == "SET":
            return self.set_value(command.value)
        return "ERROR - invalid message"

    @abstractmethod
    def randomize(self, rule):
        pass


@dataclass
class AnalogicalSensor(Sensor):
    value: bool

    def randomize(self, rule):
        self.set_value(
            randrange(rule["range"]) == 0
        )


@dataclass
class DigitalSensor(Sensor):
    value: float

    def randomize(self, rule):
        ranges = rule["range"]
        self.set_value(randrange(ranges[0], ranges[1]))


@dataclass
class JSONSensor(Sensor):
    value: dict

    def get_value_str(self) -> str:
        return json.dumps(self.value)


class HealthSensor(JSONSensor):

    def randomize(self, rule):
        hb_range = rule["hb"]
        body_tem_range = rule["body_tem"]
        self.value["hb"] = randrange(hb_range[0], hb_range[1])
        self.value["body_tem"] = randrange(
            body_tem_range[0], body_tem_range[1]
        )


class GPSSensor(JSONSensor):

    def randomize(self, rule):
        lat_range = rule["lat"]
        lon_range = rule["lon"]
        self.value["lat"] = randrange(lat_range[0], lat_range[1])
        self.value["lon"] = randrange(lon_range[0], lon_range[1])
