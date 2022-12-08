from typing import Optional

from sqlmodel import Field, SQLModel


class DeviceType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, sa_column_kwargs={"unique": True})
    observation_type: Optional[str]
