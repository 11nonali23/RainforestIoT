from sensors.sensor import AnalogicalSensor, DigitalSensor, GPSSensor, HealthSensor

SENSORS = [
    AnalogicalSensor(_id="1", name="User Presence", value=True),
    AnalogicalSensor(_id="2", name="Water Vaporizer", value=True),
    DigitalSensor(_id="3", name="Vaporizer Power", value=30),
    AnalogicalSensor(_id="4", name="Irrigators", value=False),
    DigitalSensor(_id="5", name="Irrigator Power", value=30),

    DigitalSensor(_id="6", name="Humidity", value=80),
    DigitalSensor(_id="7", name="Soil Moisture", value=80),

    # ibis, trumpeter, honeycreeper
    HealthSensor(_id="8", name="Bird1",
                 value={"hb": 290, "body_tem": 40, "name": "Bird1"}),
    HealthSensor(_id="9", name="Bird2",
                 value={"hb": 290, "body_tem": 40, "name": "Bird2"}),
    HealthSensor(_id="10", name="Bird3",
                 value={"hb": 290, "body_tem": 40, "name": "Bird3"}),

    GPSSensor(_id="11", name="Bird1", value={
              "lat": 45, "lon": 46, "name": "Bird1"}),
    GPSSensor(_id="12", name="Bird2", value={
              "lat": 45, "lon": 46, "name": "Bird2"}),
    GPSSensor(_id="13", name="Bird3", value={
              "lat": 45, "lon": 46, "name": "Bird3"}),

    AnalogicalSensor(_id="14", name="Humidity Alarm", value=False),
    AnalogicalSensor(_id="15", name="Soil Moisture Alarm", value=False),
    AnalogicalSensor(_id="16", name="Bird1 HearthBeat Alarm", value=False),
    AnalogicalSensor(_id="17", name="Bird2 HearthBeat Alarm", value=False),
    AnalogicalSensor(_id="18", name="Bird3 HearthBeat Alarm", value=False),
    AnalogicalSensor(_id="19", name="Bird1 Temperature Alarm", value=False),
    AnalogicalSensor(_id="20", name="Bird2 Temperature Alarm", value=False),
    AnalogicalSensor(_id="21", name="Bird3 Temperature Alarm", value=False),
    AnalogicalSensor(_id="22", name="Bird1 Boundaries Alarm", value=False),
    AnalogicalSensor(_id="23", name="Bird2 Boundaries Alarm", value=False),
    AnalogicalSensor(_id="24", name="Bird3 Boundaries Alarm", value=False),
]


RANDOMIZE_RULES = [
    {
        "index": 0,
        "range": 5
    },

    {
        "index": 5,
        "range": (72, 93)
    },
    {
        "index": 6,
        "range": (72, 93)
    },

    {
        "index": 7,
        "hb": (280, 310),
        "body_tem": (37, 45)
    },
    {
        "index": 8,
        "hb": (280, 310),
        "body_tem": (37, 45)
    },
    {
        "index": 9,
        "hb": (280, 310),
        "body_tem": (37, 45)
    },

    {
        "index": 10,
        "lat": (38, 52),
        "lon": (38, 52)
    },
    {
        "index": 11,
        "lat": (38, 52),
        "lon": (38, 52)
    },
    {
        "index": 12,
        "lat": (38, 52),
        "lon": (38, 52)
    }
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
    for rule in RANDOMIZE_RULES:
        index = rule["index"]
        SENSORS[index].randomize(rule)
