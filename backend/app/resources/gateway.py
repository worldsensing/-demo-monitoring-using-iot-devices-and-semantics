from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import gateway as gateway_repo, device_type as device_type_repo, location as \
    location_repo, software_sensor as software_sensor_repo
from app.schemas.device import Gateway

router = APIRouter(prefix="/gateways")


@router.get("/", response_model=List[Gateway])
def get_gateways(skip: int = 0, limit: int = 100):
    gateways = gateway_repo.get_gateways(skip=skip, limit=limit)
    return gateways


@router.post("/", response_model=Gateway)
def post_gateway(gateway: Gateway):
    db_gateway = gateway_repo.get_gateway(gateway_name=gateway.name)
    if db_gateway:
        raise HTTPException(status_code=400, detail="Gateway name already registered")

    db_device_type = device_type_repo.get_device_type(device_type_name=gateway.device_type)
    if not db_device_type:
        raise HTTPException(status_code=400, detail="DeviceType does not exist")

    if gateway.location:
        db_location = location_repo.get_location(location_name=gateway.location)
        if not db_location:
            raise HTTPException(status_code=400, detail="Location name does not exist")

    return gateway_repo.create_gateway(gateway=gateway)


@router.get("/{gateway_name}/", response_model=Gateway)
def get_gateway(gateway_name: str):
    db_gateway = gateway_repo.get_gateway(gateway_name=gateway_name)
    return db_gateway


@router.delete("/{gateway_name}/", response_model=Gateway)
def delete_gateway(gateway_name: str):
    db_gateway = gateway_repo.get_gateway(gateway_name=gateway_name)
    if not db_gateway:
        raise HTTPException(status_code=400, detail="Gateway name does not exist.")

    db_software_sensor = software_sensor_repo.get_software_sensors_by_gateway(gateway_name)
    if db_software_sensor:
        raise HTTPException(status_code=400, detail="A SoftwareSensor is using this Gateway, "
                                                    "remove it first.")

    db_gateway = gateway_repo.delete_gateway(gateway_name=gateway_name)
    return db_gateway
