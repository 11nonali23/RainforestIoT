from sensor import AnalogicalSensor, DigitalSensor, JSONSensor

SENSORS = [
    AnalogicalSensor(_id="1", name="User Presence", value=True),
    AnalogicalSensor(_id="2", name="Water Spout", value=False),
    AnalogicalSensor(_id="3", name="Irrigators", value=False),

    DigitalSensor(_id="4", name="Humidity", value=30),
    DigitalSensor(_id="5", name="Temperature", value=30),
    DigitalSensor(_id="6", name="Soil Moisture", value=5),

    JSONSensor(_id="7", name="Bird1 Health", value={"hb": 35, "body_tem": 35}),
    JSONSensor(_id="8", name="Bird2 Health", value={"hb": 35, "body_tem": 35}),
    JSONSensor(_id="9", name="Bird3 Health", value={"hb": 35, "body_tem": 35}),

    JSONSensor(_id="10", name="Bird1 Coords", value={"lat": 45, "lon": 46}),
    JSONSensor(_id="11", name="Bird2 Coords", value={"lat": 45, "lon": 46}),
    JSONSensor(_id="12", name="Bird3 Coords", value={"lat": 45, "lon": 46}),

    AnalogicalSensor(_id="13", name="HearthBeat Alarm", value=False),
    AnalogicalSensor(_id="14", name="Body Temperature Alarm", value=False),
    AnalogicalSensor(_id="15", name="Boundaries Alarm", value=False),
    AnalogicalSensor(_id="16", name="Humidity Alarm", value=False),
    AnalogicalSensor(_id="17", name="Soil Moisture Alarm", value=False),
]


def exists(sensor_id) -> bool:
    try:
        next(
            sensor for sensor in SENSORS
            if sensor._id == sensor_id
        )
        return True
    except StopIteration:
        return False


def get_sensor(sensor_id):
    return next(
        sensor for sensor in SENSORS
        if sensor._id == sensor_id
    )


def randomize():
    global SENSORS
    for sensor in SENSORS:
        if isinstance(sensor, AnalogicalSensor):
            pass  # randomize bool
        if isinstance(sensor, AnalogicalSensor):
            pass  # randomize value
        if isinstance(sensor, JSONSensor):
            pass  # randomize json
