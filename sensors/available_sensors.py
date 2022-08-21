from operator import index
from sensors.sensor import AnalogicalSensor, DigitalSensor, GPSSensor, HealthSensor, JSONSensor

SENSORS = [
    AnalogicalSensor(_id="1", name="User Presence", value=True),
    AnalogicalSensor(_id="2", name="Water Vaporizer", value=True),
    DigitalSensor(_id="3", name="Vaporizer Power", value=30),
    AnalogicalSensor(_id="4", name="Irrigators", value=False),
    DigitalSensor(_id="5", name="Irrigator Power", value=30),

    DigitalSensor(_id="6", name="Humidity", value=30),
    DigitalSensor(_id="7", name="Soil Moisture", value=50),

    HealthSensor(_id="8", name="Bird1 Health",
                 value={"hb": 35, "body_tem": 35}),
    HealthSensor(_id="9", name="Bird2 Health",
                 value={"hb": 35, "body_tem": 35}),
    HealthSensor(_id="10", name="Bird3 Healt",
                 value={"hb": 35, "body_tem": 35}),

    GPSSensor(_id="11", name="Bird1 Coords", value={"lat": 45, "lon": 46}),
    GPSSensor(_id="12", name="Bird2 Coords", value={"lat": 45, "lon": 46}),
    GPSSensor(_id="13", name="Bird3 Coords", value={"lat": 45, "lon": 46}),

    AnalogicalSensor(_id="14", name="HearthBeat Alarm", value=False),
    AnalogicalSensor(_id="15", name="Body Temperature Alarm", value=False),
    AnalogicalSensor(_id="16", name="Boundaries Alarm", value=False),
    AnalogicalSensor(_id="17", name="Humidity Alarm", value=False),
    AnalogicalSensor(_id="18", name="Soil Moisture Alarm", value=False),
]


RANDOMIZE_RULES = [
    {
        "index": 0,
        "range": 5
    },

    {
        "index": 5,
        "range": (10, 90)
    },
    {
        "index": 6,
        "range": (10, 90)
    },

    {
        "index": 7,
        "hb": (10, 90),
        "body_tem": (10, 90)
    },
    {
        "index": 8,
        "hb": (10, 90),
        "body_tem": (10, 90)
    },
    {
        "index": 9,
        "hb": (10, 90),
        "body_tem": (10, 90)
    },

    {
        "index": 10,
        "lat": (10, 90),
        "lon": (10, 90)
    },
    {
        "index": 11,
        "lat": (10, 90),
        "lon": (10, 90)
    },
    {
        "index": 12,
        "lat": (10, 90),
        "lon": (10, 90)
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

        # vaporizer on only if user is present or humidity is < 30
        # humidty set alarm if value is < 30
        if index == 5:
            SENSORS[1].value = SENSORS[0].value == True or SENSORS[5].value < 30
            SENSORS[16].value = SENSORS[5].value < 30

        # irrigators should be on only when soil moisture is < 30
        # soil moisture set alarm if value is < 30
        if index == 6:
            SENSORS[3].value = SENSORS[6].value < 30
            SENSORS[17].value = SENSORS[6].value < 30

        # TODO set alarms also foor coordinates and birds health
        # ...
