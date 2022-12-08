from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import device_type as device_type_repo, gateway as gateway_repo, \
    node as node_repo, sensor as sensor_repo
from app.schemas.device_type import DeviceType

router = APIRouter(prefix="/device-types")


@router.get("/", response_model=List[DeviceType])
def get_device_types(skip: int = 0, limit: int = 100):
    device_types = device_type_repo.get_device_types(skip=skip, limit=limit)
    return device_types


@router.post("/", response_model=DeviceType)
def post_device_type(device_type: DeviceType):
    db_device_type = device_type_repo.get_device_type(device_type_name=device_type.name)
    if db_device_type:
        raise HTTPException(status_code=400, detail="DeviceType name already registered")
    return device_type_repo.create_device_type(device_type=device_type)


@router.get("/{device_type_name}/", response_model=DeviceType)
def get_device_type(device_type_name: str):
    db_device_type = device_type_repo.get_device_type(device_type_name=device_type_name)
    return db_device_type


@router.delete("/{device_type_name}/", response_model=DeviceType)
def delete_device_type(device_type_name: str):
    db_device_type = device_type_repo.get_device_type(device_type_name=device_type_name)
    if not db_device_type:
        raise HTTPException(status_code=400, detail="The DeviceType does not exist.")

    db_gateway = gateway_repo.get_gateways_by_device_type(device_type_name)
    if db_gateway:
        raise HTTPException(status_code=400, detail="A Gateway is using this DeviceType, "
                                                    "remove it first.")
    db_node = node_repo.get_nodes_by_device_type(device_type_name)
    if db_node:
        raise HTTPException(status_code=400, detail="A Node is using this DeviceType, "
                                                    "remove it first.")
    db_sensor = sensor_repo.get_sensors_by_device_type(device_type_name)
    if db_sensor:
        raise HTTPException(status_code=400, detail="A Sensor is using this DeviceType, "
                                                    "remove it first.")
    db_device_type = device_type_repo.delete_device_type(device_type_name=device_type_name)
    return db_device_type
