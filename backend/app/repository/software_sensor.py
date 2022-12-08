from sqlmodel import Session

from app.database import engine
from app.schemas.device import SoftwareSensor


def get_software_sensor(software_sensor_name: str):
    with Session(engine) as session:
        return session.query(SoftwareSensor) \
            .filter(SoftwareSensor.sensor_name == software_sensor_name).first()


def get_software_sensors(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(SoftwareSensor).offset(skip).limit(limit).all()


def get_software_sensors_by_sensor(sensor_name: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(SoftwareSensor).filter(SoftwareSensor.sensor_name == sensor_name) \
            .offset(skip).limit(limit).all()


def get_software_sensors_by_gateway(gateway_name: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(SoftwareSensor).filter(SoftwareSensor.gateway_name == gateway_name) \
            .offset(skip).limit(limit).all()


def get_software_sensors_by_node(node_name: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(SoftwareSensor).filter(SoftwareSensor.node_name == node_name) \
            .offset(skip).limit(limit).all()


def create_software_sensor(software_sensor: SoftwareSensor):
    with Session(engine) as session:
        db_software_sensor = SoftwareSensor(sensor_name=software_sensor.sensor_name,
                                            status=software_sensor.status,
                                            gateway_name=software_sensor.gateway_name,
                                            node_name=software_sensor.node_name
                                            )
        session.add(db_software_sensor)
        session.commit()
        session.refresh(db_software_sensor)
        return db_software_sensor


def delete_software_sensor(software_sensor_name: str):
    with Session(engine) as session:
        software_sensor = get_software_sensor(software_sensor_name)
        session.delete(software_sensor)
        session.commit()
        return software_sensor
