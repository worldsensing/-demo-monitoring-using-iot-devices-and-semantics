import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import database
from app.config import Settings
from app.resources import device_type, gateway, node, sensor, hardware_sensor, software_sensor, \
    observable_property, observation, location, graph

app = FastAPI()
app.include_router(device_type.router)
app.include_router(gateway.router)
app.include_router(node.router)
app.include_router(sensor.router)
app.include_router(hardware_sensor.router)
app.include_router(software_sensor.router)
app.include_router(observable_property.router)
app.include_router(observation.router)
app.include_router(location.router)
app.include_router(graph.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    database.create_db_and_tables()


@app.get("/")
def read_health():
    return {"status": "UP"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
