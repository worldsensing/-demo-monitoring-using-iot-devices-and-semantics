from sqlmodel import Session

from app.database import engine
from app.schemas.device import Gateway


def get_gateway(gateway_name: str):
    with Session(engine) as session:
        return session.query(Gateway).filter(Gateway.name == gateway_name).first()


def get_gateways(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Gateway).offset(skip).limit(limit).all()


def get_gateways_by_device_type(device_type: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Gateway).filter(Gateway.device_type == device_type) \
            .offset(skip).limit(limit).all()


def create_gateway(gateway: Gateway):
    with Session(engine) as session:
        db_gateway = Gateway(name=gateway.name, device_type=gateway.device_type,
                             location=gateway.location, info=gateway.info, active=gateway.active,
                             lastConnectTime=gateway.lastConnectTime,
                             lastDisconnectTime=gateway.lastDisconnectTime,
                             lastActivityTime=gateway.lastActivityTime,
                             inactivityAlarmTime=gateway.inactivityAlarmTime,
                             installation_picture=gateway.installation_picture,
                             power_type=gateway.power_type, connectivity=gateway.connectivity,
                             modem_signal=gateway.modem_signal, power_supply=gateway.power_supply
                             )
        session.add(db_gateway)
        session.commit()
        session.refresh(db_gateway)
        return db_gateway


def delete_gateway(gateway_name: str):
    with Session(engine) as session:
        gateway = get_gateway(gateway_name)
        session.delete(gateway)
        session.commit()
        return gateway
