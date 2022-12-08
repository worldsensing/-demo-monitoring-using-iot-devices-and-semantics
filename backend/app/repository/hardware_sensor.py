from sqlmodel import Session

from app.database import engine
from app.schemas.device import HardwareSensor


def get_hardware_sensor(hardware_sensor_name: str):
    with Session(engine) as session:
        return session.query(HardwareSensor) \
            .filter(HardwareSensor.sensor_name == hardware_sensor_name).first()


def get_hardware_sensors(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(HardwareSensor).offset(skip).limit(limit).all()


def get_hardware_sensors_by_sensor(sensor_name: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(HardwareSensor).filter(HardwareSensor.sensor_name == sensor_name) \
            .offset(skip).limit(limit).all()


def get_hardware_sensors_by_node(node_name: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        result = session.query(HardwareSensor).offset(skip).limit(limit).all()

        hardware_sensors = []
        for row in result:
            if node_name in row.node_names:
                hardware_sensors.append(row)
        return hardware_sensors


def create_hardware_sensor(hardware_sensor: HardwareSensor):
    with Session(engine) as session:
        db_hardware_sensor = HardwareSensor(sensor_name=hardware_sensor.sensor_name,
                                            man_id=hardware_sensor.man_id,
                                            man_name=hardware_sensor.man_name,
                                            man_sensor_name=hardware_sensor.man_sensor_name,
                                            fw_version=hardware_sensor.fw_version,
                                            port=hardware_sensor.port,
                                            calibration_date=hardware_sensor.calibration_date,
                                            node_names=hardware_sensor.node_names)
        session.add(db_hardware_sensor)
        session.commit()
        session.refresh(db_hardware_sensor)
        return db_hardware_sensor


def delete_hardware_sensor(hardware_sensor_name: str):
    with Session(engine) as session:
        hardware_sensor = get_hardware_sensor(hardware_sensor_name)
        session.delete(hardware_sensor)
        session.commit()
        return hardware_sensor
