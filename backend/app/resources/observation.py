from typing import List

from fastapi import APIRouter, HTTPException

from app.repository import observation as observation_repo, observable_property as \
    observable_property_repo, sensor as sensor_repo
from app.schemas.observation import Observation
from app.utils import time

router = APIRouter(prefix="/observations")


@router.get("/", response_model=List[Observation])
def get_observations(skip: int = 0, limit: int = 100):
    observations = observation_repo.get_observations(skip=skip, limit=limit)
    return observations


@router.post("/", response_model=Observation)
def post_observations(observation: Observation):
    if not observation.time_start:
        observation.time_start = time.get_current_datetime()

    db_observable_property = observable_property_repo.get_observable_property(
        observable_property_name=observation.observable_property)
    if not db_observable_property:
        raise HTTPException(status_code=400, detail="ObservableProperty does not exist")

    # TODO Check comparing that if the observable_property states that the data comes via
    #  Integer, there is where information should be

    db_sensor = sensor_repo.get_sensor(sensor_name=observation.sensor_name)
    if not db_sensor:
        raise HTTPException(status_code=400, detail="Sensor name does not exist.")

    if not observation.time_end:
        observation.time_end = time.get_current_datetime()

    return observation_repo.create_observation(observation=observation)


@router.delete("/{observation_id}/", response_model=Observation)
def delete_observations(observation_id: int):
    db_observation = observation_repo.delete_observation_id(observation_id=observation_id)
    return db_observation


@router.delete("/{sensor_name}/", response_model=list)
def delete_observations(sensor_name: str):
    db_observations = observation_repo.delete_observations_sensor(sensor_name=sensor_name)
    return db_observations
