from typing import Optional

from sqlmodel import Field, SQLModel


class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, sa_column_kwargs={"unique": True})
    geo_feature: Optional[str]
    geo_coordinates: Optional[str]  # [ lat, lng ]
