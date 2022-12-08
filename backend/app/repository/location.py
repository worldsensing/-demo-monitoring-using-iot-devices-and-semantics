from sqlmodel import Session

from app.database import engine
from app.schemas.location import Location


def get_location(location_name: str):
    with Session(engine) as session:
        return session.query(Location) \
            .filter(Location.name == location_name).first()


def get_locations(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(Location).offset(skip).limit(limit).all()


def create_location(location: Location):
    with Session(engine) as session:
        db_location = Location(name=location.name, geo_feature=location.geo_feature,
                               geo_coordinates=location.geo_coordinates)
        session.add(db_location)
        session.commit()
        session.refresh(db_location)
        return db_location


def delete_location(location_name: str):
    with Session(engine) as session:
        location = get_location(location_name)
        session.delete(location)
        session.commit()
        return location
