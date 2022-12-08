from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import hardware_sensor as hardware_sensor_repo, node as node_repo, sensor as \
    sensor_repo
from app.schemas.device import HardwareSensor

router = APIRouter(prefix="/hardware-sensors")


@router.get("/", response_model=List[HardwareSensor])
def get_hardware_sensors(skip: int = 0, limit: int = 100):
    hardware_sensors = hardware_sensor_repo.get_hardware_sensors(skip=skip, limit=limit)
    return hardware_sensors


@router.post("/", response_model=HardwareSensor)
def post_hardware_sensor(hardware_sensor: HardwareSensor):
    db_hardware_sensor = hardware_sensor_repo.get_hardware_sensor(
        hardware_sensor_name=hardware_sensor.sensor_name)
    if db_hardware_sensor:
        raise HTTPException(status_code=400, detail="Hardware Sensor with that name does exist")

    db_sensor = sensor_repo.get_sensor(sensor_name=hardware_sensor.sensor_name)
    if not db_sensor:
        raise HTTPException(status_code=400, detail="Sensor name does not exist")

    if not hardware_sensor.node_names:
        raise HTTPException(status_code=400, detail="At least one valid NodeName has to be "
                                                    "provided.")
    for node_name in hardware_sensor.node_names:
        db_node = node_repo.get_node(node_name=node_name)
        if not db_node:
            raise HTTPException(status_code=400, detail="Provided Node name does not exist")

    return hardware_sensor_repo.create_hardware_sensor(hardware_sensor=hardware_sensor)


@router.get("/{hardware_sensor_name}/", response_model=HardwareSensor)
def get_hardware_sensor(hardware_sensor_name: str):
    db_hardware_sensor = hardware_sensor_repo.get_hardware_sensor(
        hardware_sensor_name=hardware_sensor_name)
    return db_hardware_sensor


@router.delete("/{hardware_sensor_name}/", response_model=HardwareSensor)
def delete_hardware_sensor(hardware_sensor_name: str):
    db_hardware_sensor = hardware_sensor_repo.get_hardware_sensor(
        hardware_sensor_name=hardware_sensor_name)
    if not db_hardware_sensor:
        raise HTTPException(status_code=400, detail="Hardware Sensor does not exist")

    db_hardware_sensor = hardware_sensor_repo.delete_hardware_sensor(
        hardware_sensor_name=hardware_sensor_name)
    return db_hardware_sensor
