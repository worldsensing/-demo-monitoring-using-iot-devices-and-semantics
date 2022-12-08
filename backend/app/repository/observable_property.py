from sqlmodel import Session

from app.database import engine
from app.schemas.observation import ObservableProperty


def get_observable_property(observable_property_name: str):
    with Session(engine) as session:
        return session.query(ObservableProperty) \
            .filter(ObservableProperty.name == observable_property_name).first()


def get_observable_properties(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        return session.query(ObservableProperty).offset(skip).limit(limit).all()


def create_observable_property(observable_property: ObservableProperty):
    with Session(engine) as session:
        db_observable_property = ObservableProperty(name=observable_property.name,
                                                    type_of_observation=observable_property.type_of_observation)
        session.add(db_observable_property)
        session.commit()
        session.refresh(db_observable_property)
        return db_observable_property


def delete_observable_property(observable_property_name: str):
    with Session(engine) as session:
        observable_property = get_observable_property(observable_property_name)
        session.delete(observable_property)
        session.commit()
        return observable_property
