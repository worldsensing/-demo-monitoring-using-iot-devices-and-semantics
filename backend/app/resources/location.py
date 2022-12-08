from typing import List

from fastapi import HTTPException, APIRouter

from app.repository import location as location_repo
from app.schemas.location import Location

router = APIRouter(prefix="/locations")


@router.get("/", response_model=List[Location])
def get_locations(skip: int = 0, limit: int = 100):
    locations = location_repo.get_locations(skip=skip, limit=limit)
    return locations


@router.post("/", response_model=Location)
def post_location(location: Location):
    db_location = location_repo.get_location(location_name=location.name)
    if db_location:
        raise HTTPException(status_code=400, detail="Location name already registered")
    return location_repo.create_location(location=location)


@router.get("/{location_name}/", response_model=Location)
def get_location(location_name: str):
    db_location = location_repo.get_location(location_name=location_name)
    return db_location


@router.delete("/{location_name}/", response_model=Location)
def delete_location(location_name: str):
    # TODO Checks before deleting
    db_location = location_repo.delete_location(location_name=location_name)
    return db_location
