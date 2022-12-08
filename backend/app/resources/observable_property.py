from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import observable_property as observable_property_repo, sensor as \
    sensor_repo, observation as observation_repo
from app.schemas.observation import ObservableProperty

router = APIRouter(prefix="/observable-properties")


@router.get("/", response_model=List[ObservableProperty])
def get_observable_properties(skip: int = 0, limit: int = 100):
    observable_property = observable_property_repo.get_observable_properties(skip=skip, limit=limit)
    return observable_property


@router.post("/", response_model=ObservableProperty)
def post_observable_property(observable_property: ObservableProperty):
    db_observable_property = observable_property_repo.get_observable_property(
        observable_property_name=observable_property.name)
    if db_observable_property:
        raise HTTPException(status_code=400, detail="ObservableProperty name already registered")

    return observable_property_repo.create_observable_property(
        observable_property=observable_property)


@router.delete("/{observable_property_name}/", response_model=ObservableProperty)
def delete_observable_property(observable_property_name: str):
    db_observable_property = observable_property_repo.get_observable_property(
        observable_property_name=observable_property_name)
    if not db_observable_property:
        raise HTTPException(status_code=400, detail="ObservableProperty does not exist.")

    db_sensor = sensor_repo.get_sensors_by_observable_property(observable_property_name)
    if db_sensor:
        raise HTTPException(status_code=400, detail="A Sensor is using this ObservableProperty, "
                                                    "remove it first.")

    db_observations_sensor = observation_repo.get_observations_sensor(observable_property_name)
    if db_observations_sensor:
        raise HTTPException(status_code=400,
                            detail="An Observation is using this ObservableProperty, "
                                   "remove it first.")

    db_observable_property = observable_property_repo.delete_observable_property(
        observable_property_name=observable_property_name)
    return db_observable_property
