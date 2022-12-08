import enum
from typing import List, Optional

from sqlmodel import Column, Enum, JSON, Field, SQLModel


class TypeOfSensors(enum.Enum):
    SOFTWARE_SENSOR = "softwaresensor"
    HARDWARE_SENSOR = "hardwaresensor"


class Gateway(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, sa_column_kwargs={"unique": True})
    device_type: str = Field(foreign_key="devicetype.name")
    location: Optional[str] = Field(default=None, foreign_key="location.name")
    info: Optional[str]
    active: bool = Field(default=False)
    lastConnectTime: Optional[str]
    lastDisconnectTime: Optional[str]
    lastActivityTime: Optional[str]
    inactivityAlarmTime: Optional[str]
    installation_picture: Optional[str]
    power_type: Optional[str]
    connectivity: Optional[str]
    modem_signal: Optional[str]
    power_supply: Optional[str]


class Node(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, sa_column_kwargs={"unique": True})
    device_type: str = Field(foreign_key="devicetype.name")
    location: Optional[str] = Field(default=None, foreign_key="location.name")
    info: Optional[str]
    active: bool = Field(default=False)
    lastConnectTime: Optional[str]
    lastDisconnectTime: Optional[str]
    lastActivityTime: Optional[str]
    inactivityAlarmTime: Optional[str]
    sampling_rate: Optional[str]


class Sensor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, sa_column_kwargs={"unique": True})
    device_type: str = Field(foreign_key="devicetype.name")
    type: TypeOfSensors = Field(sa_column=Column(Enum(TypeOfSensors)))
    observable_property: str = Field(foreign_key="observableproperty.name")
    location: Optional[str] = Field(default=None, foreign_key="location.name")
    info: Optional[str]
    active: bool = Field(default=False)
    lastConnectTime: Optional[str]
    lastDisconnectTime: Optional[str]
    lastActivityTime: Optional[str]
    inactivityAlarmTime: Optional[str]


class SoftwareSensor(SQLModel, table=True):
    sensor_name: Optional[str] = Field(default=None, foreign_key="sensor.name", primary_key=True)

    status: bool = Field(default=False)
    # Has to be inside a Gateway or a Node
    gateway_name: Optional[str] = Field(default=None, foreign_key="gateway.name")
    node_name: Optional[str] = Field(default=None, foreign_key="node.name")


class HardwareSensor(SQLModel, table=True):
    sensor_name: Optional[str] = Field(default=None, foreign_key="sensor.name", primary_key=True)

    man_id: Optional[str]
    man_name: Optional[str]
    man_sensor_name: Optional[str]
    fw_version: Optional[str]
    port: Optional[str]
    calibration_date: Optional[str]
    node_names: List[str] = Field(sa_column=Column(JSON))

    # TODO Add Gateway info, update graph
