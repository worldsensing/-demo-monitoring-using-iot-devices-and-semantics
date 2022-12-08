from sqlmodel import Session

from app.database import engine
from app.schemas.device import Sensor


def get_sensor(sensor_name: str):
    with Session(engine) as session:
        return session.query(Sensor) \
            .filter(Sensor.name == sensor_name).first()


def get_sensors(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Sensor).offset(skip).limit(limit).all()


def get_sensors_by_device_type(device_type: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Sensor).filter(Sensor.device_type == device_type) \
            .offset(skip).limit(limit).all()


def get_sensors_by_observable_property(observable_property: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Sensor).filter(Sensor.observable_property == observable_property) \
            .offset(skip).limit(limit).all()


def create_sensor(sensor: Sensor):
    with Session(engine) as session:
        db__sensor = Sensor(name=sensor.name, device_type=sensor.device_type, type=sensor.type,
                            observable_property=sensor.observable_property,
                            location=sensor.location, info=sensor.info, active=sensor.active,
                            lastConnectTime=sensor.lastConnectTime,
                            lastDisconnectTime=sensor.lastDisconnectTime,
                            lastActivityTime=sensor.lastActivityTime,
                            inactivityAlarmTime=sensor.inactivityAlarmTime)
        session.add(db__sensor)
        session.commit()
        session.refresh(db__sensor)
        return db__sensor


def delete_sensor(sensor_name: str):
    with Session(engine) as session:
        sensor = get_sensor(sensor_name)
        session.delete(sensor)
        session.commit()
        return sensor
