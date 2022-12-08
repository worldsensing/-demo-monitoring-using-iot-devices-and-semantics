import datetime
import enum
from typing import Optional

from sqlmodel import Column, DateTime, Enum, Field, SQLModel


class TypeOfObservations(enum.Enum):
    INTEGER_PROP = "integer"
    FLOAT_PROP = "float"
    BOOLEAN_PROP = "boolean"
    STRING_PROP = "string"
    DICT_PROP = "dict"


class ObservableProperty(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, sa_column_kwargs={"unique": True})
    type_of_observation: TypeOfObservations = Field(sa_column=Column(Enum(TypeOfObservations)))


class Observation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    time_start: Optional[datetime.datetime] = Field(sa_column=Column(DateTime(timezone=True),
                                                                     nullable=False))
    time_end: Optional[datetime.datetime] = Field(sa_column=Column(DateTime(timezone=True),
                                                                   nullable=False))

    value_int: Optional[int]
    value_float: Optional[float]
    value_bool: Optional[bool]
    value_str: Optional[str]

    observable_property: str = Field(nullable=False, foreign_key="observableproperty.name")
    sensor_name: str = Field(nullable=False, foreign_key="sensor.name")
