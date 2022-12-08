from sqlmodel import Session

from app.database import engine
from app.schemas.device_type import DeviceType


def get_device_type(device_type_name: str):
    with Session(engine) as session:
        return session.query(DeviceType) \
            .filter(DeviceType.name == device_type_name).first()


def get_device_types(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(DeviceType).offset(skip).limit(limit).all()


def create_device_type(device_type: DeviceType):
    with Session(engine) as session:
        db_device_type = DeviceType(name=device_type.name,
                                    observation_type=device_type.observation_type)
        session.add(db_device_type)
        session.commit()
        session.refresh(db_device_type)
        return db_device_type


def delete_device_type(device_type_name: str):
    with Session(engine) as session:
        device_type = get_device_type(device_type_name)
        session.delete(device_type)
        session.commit()
        return device_type
