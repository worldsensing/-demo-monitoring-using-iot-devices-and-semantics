from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import node as node_repo, device_type as device_type_repo, location as \
    location_repo, software_sensor as software_sensor_repo, hardware_sensor as hardware_sensor_repo
from app.schemas.device import Node

router = APIRouter(prefix="/nodes")


@router.get("/", response_model=List[Node])
def get_nodes(skip: int = 0, limit: int = 100):
    nodes = node_repo.get_nodes(skip=skip, limit=limit)
    return nodes


@router.post("/", response_model=Node)
def post_node(node: Node):
    db_node = node_repo.get_node(node_name=node.name)
    if db_node:
        raise HTTPException(status_code=400, detail="Node name already registered")

    db_device_type = device_type_repo.get_device_type(device_type_name=node.device_type)
    if not db_device_type:
        raise HTTPException(status_code=400, detail="DeviceType does not exist")

    if node.location:
        db_location = location_repo.get_location(location_name=node.location)
        if not db_location:
            raise HTTPException(status_code=400, detail="Location name does not exist")

    return node_repo.create_node(node=node)


@router.get("/{node_name}/", response_model=Node)
def get_node(node_name: str):
    db_node = node_repo.get_node(node_name=node_name)
    return db_node


@router.delete("/{node_name}/", response_model=Node)
def delete_node(node_name: str):
    db_node = node_repo.get_node(node_name=node_name)
    if not db_node:
        raise HTTPException(status_code=400, detail="Node does not exist.")

    db_software_sensor = software_sensor_repo.get_software_sensors_by_node(node_name)
    if db_software_sensor:
        raise HTTPException(status_code=400, detail="A SoftwareSensor is using this Node, "
                                                    "remove it first.")

    db_hardware_sensors = hardware_sensor_repo.get_hardware_sensors_by_node(node_name)
    if db_hardware_sensors:
        raise HTTPException(status_code=400, detail="At least one HardwareSensor is using this "
                                                    "Node, remove it first.")

    db_node = node_repo.delete_node(node_name=node_name)
    return db_node
