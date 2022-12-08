from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import software_sensor as software_sensor_repo, node as node_repo, \
    gateway as gateway_repo, sensor as sensor_repo
from app.schemas.device import SoftwareSensor, TypeOfSensors

router = APIRouter(prefix="/software-sensors")


@router.get("/", response_model=List[SoftwareSensor])
def get_software_sensors(skip: int = 0, limit: int = 100):
    software_sensors = software_sensor_repo.get_software_sensors(skip=skip, limit=limit)
    return software_sensors


@router.post("/", response_model=SoftwareSensor)
def post_software_sensor(software_sensor: SoftwareSensor):
    db_software_sensor = software_sensor_repo.get_software_sensor(
        software_sensor_name=software_sensor.sensor_name)
    if db_software_sensor:
        raise HTTPException(status_code=400, detail="Software Sensor with that name does exist")

    db_sensor = sensor_repo.get_sensor(sensor_name=software_sensor.sensor_name)
    if not db_sensor:
        raise HTTPException(status_code=400, detail="Sensor name does not exist")

    if db_sensor.type is not TypeOfSensors.SOFTWARE_SENSOR:
        raise HTTPException(status_code=400, detail="Sensor is not a Software Sensor")

    if software_sensor.node_name:
        db_node = node_repo.get_node(node_name=software_sensor.node_name)
        if not db_node:
            raise HTTPException(status_code=400, detail="Provided Node name does not exist")

    if software_sensor.gateway_name:
        db_gateway = gateway_repo.get_gateway(gateway_name=software_sensor.gateway_name)
        if not db_gateway:
            raise HTTPException(status_code=400, detail="Provided Gateway name does not exist")

    return software_sensor_repo.create_software_sensor(software_sensor=software_sensor)


@router.get("/{software_sensor_name}/", response_model=SoftwareSensor)
def get_software_sensor(software_sensor_name: str):
    db_software_sensor = software_sensor_repo.get_software_sensor(
        software_sensor_name=software_sensor_name)
    return db_software_sensor


@router.delete("/{software_sensor_name}/", response_model=SoftwareSensor)
def delete_software_sensor(software_sensor_name: str):
    db_software_sensor = software_sensor_repo.get_software_sensor(
        software_sensor_name=software_sensor_name)
    if not db_software_sensor:
        raise HTTPException(status_code=400, detail="Software Sensor with that name does not "
                                                    "exist.")

    db_software_sensor = software_sensor_repo.delete_software_sensor(
        software_sensor_name=software_sensor_name)
    return db_software_sensor
