from sqlmodel import Session

from app.database import engine
from app.schemas.observation import Observation


def get_observations(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Observation).offset(skip).limit(limit).all()


def get_observations_id(observation_id: int):
    with Session(engine) as session:
        return session.query(Observation) \
            .filter(Observation.id == observation_id) \
            .first()


def get_observations_sensor(sensor_name: str, skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Observation) \
            .filter(Observation.sensor_name == sensor_name) \
            .offset(skip).limit(limit).all()


def create_observation(observation: Observation):
    with Session(engine) as session:
        db_observation = Observation(value_int=observation.value_int,
                                     value_float=observation.value_float,
                                     value_str=observation.value_str,
                                     value_bool=observation.value_bool,
                                     time_start=observation.time_start,
                                     time_end=observation.time_end,
                                     observable_property=observation.observable_property,
                                     sensor_name=observation.sensor_name)  # TODO Complete
        session.add(db_observation)
        session.commit()
        session.refresh(db_observation)
        return db_observation


def delete_observations_sensor(sensor_name: str):
    with Session(engine) as session:
        observations_sensor = get_observations_sensor(sensor_name)
        for observation_sensor in observations_sensor:
            session.delete(observation_sensor)
            session.commit()
        return observations_sensor


def delete_observation_id(observation_id: int):
    with Session(engine) as session:
        observation_sensor = get_observations_id(observation_id)
        session.delete(observation_sensor)
        session.commit()
        return observation_sensor
