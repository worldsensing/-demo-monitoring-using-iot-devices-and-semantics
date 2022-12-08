from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import sensor as sensor_repo, device_type as \
    device_type_repo, location as location_repo, hardware_sensor as hardware_sensor_repo, \
    software_sensor as software_sensor_repo, observable_property as observable_property_repo, \
    observation as observation_repo
from app.schemas.device import Sensor

router = APIRouter(prefix="/sensors")


@router.get("/", response_model=List[Sensor])
def get_sensors(skip: int = 0, limit: int = 100):
    sensors = sensor_repo.get_sensors(skip=skip, limit=limit)
    return sensors


@router.post("/", response_model=Sensor)
def post_sensor(sensor: Sensor):
    db_sensor = sensor_repo.get_sensor(sensor_name=sensor.name)
    if db_sensor:
        raise HTTPException(status_code=400, detail="Sensor name already registered")

    db_device_type = device_type_repo.get_device_type(device_type_name=sensor.device_type)
    if not db_device_type:
        raise HTTPException(status_code=400, detail="DeviceType does not exist")

    db_observable_property = observable_property_repo.get_observable_property(
        observable_property_name=sensor.observable_property)
    if not db_observable_property:
        raise HTTPException(status_code=400, detail="ObservableProperty does not exist")

    if sensor.location:
        db_location = location_repo.get_location(location_name=sensor.location)
        if not db_location:
            raise HTTPException(status_code=400, detail="Location name does not exist")

    return sensor_repo.create_sensor(sensor=sensor)


@router.get("/{sensor_name}/", response_model=Sensor)
def get_sensor(sensor_name: str):
    db_sensor = sensor_repo.get_sensor(
        sensor_name=sensor_name)
    return db_sensor


@router.delete("/{sensor_name}/", response_model=Sensor)
def delete_sensor(sensor_name: str):
    db_sensor = sensor_repo.get_sensor(sensor_name=sensor_name)
    if not db_sensor:
        raise HTTPException(status_code=400, detail="Sensor name does not exist.")

    db_hardware_sensor = hardware_sensor_repo.get_hardware_sensors_by_sensor(sensor_name)
    if db_hardware_sensor:
        raise HTTPException(status_code=400, detail="A HardwareSensor is using this Sensor, "
                                                    "remove it first.")
    db_software_sensor = software_sensor_repo.get_software_sensors_by_sensor(sensor_name)
    if db_software_sensor:
        raise HTTPException(status_code=400, detail="A SoftwareSensor is using this Sensor, "
                                                    "remove it first.")

    db_observations_sensor = observation_repo.get_observations_sensor(sensor_name)
    if db_observations_sensor:
        raise HTTPException(status_code=400, detail="An Observation is using this Sensor, "
                                                    "remove it first.")

    db_sensor = sensor_repo.delete_sensor(sensor_name=sensor_name)
    return db_sensor
