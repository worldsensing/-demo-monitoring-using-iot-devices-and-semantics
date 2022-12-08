from sqlmodel import Session

from app.database import engine
from app.schemas.device import Node


def get_node(node_name: str):
    with Session(engine) as session:
        return session.query(Node).filter(Node.name == node_name).first()


def get_nodes(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Node).offset(skip).limit(limit).all()


def get_nodes_by_device_type(device_type: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Node).filter(Node.device_type == device_type) \
            .offset(skip).limit(limit).all()


def create_node(node: Node):
    with Session(engine) as session:
        db_node = Node(name=node.name, device_type=node.device_type, location=node.location,
                       info=node.info, active=node.active, lastConnectTime=node.lastConnectTime,
                       lastDisconnectTime=node.lastDisconnectTime,
                       lastActivityTime=node.lastActivityTime,
                       inactivityAlarmTime=node.inactivityAlarmTime,
                       sampling_rate=node.sampling_rate
                       )
        session.add(db_node)
        session.commit()
        session.refresh(db_node)
        return db_node


def delete_node(node_name: str):
    with Session(engine) as session:
        node = get_node(node_name)
        session.delete(node)
        session.commit()
        return node
