import enum
from typing import Dict

from fastapi import APIRouter

from app.repository import gateway as gateway_repo, node as node_repo, sensor as sensor_repo, \
    software_sensor as software_sensor_repo, hardware_sensor as hardware_sensor_repo, device_type \
    as device_type_repo, location as location_repo, observable_property as \
    observable_property_repo, observation as observation_repo

router = APIRouter(prefix="/graph")

X_DISPLACEMENT = 175


class ID_TYPES(enum.Enum):
    DEVICE_TYPE = "DEVICE_TYPE|"
    LOCATION = "LOCATION|"
    OBSERVABLE_PROPERTY = "OBSERVABLE_PROPERTY|"
    OBSERVATION = "OBSERVATION|"
    GATEWAY = "GATEWAY|"
    NODE = "NODE|"
    SENSOR = "SENSOR|"
    SOFTWARE_SENSOR = "SOFTWARE_SENSOR|"
    HARDWARE_SENSOR = "HARDWARE_SENSOR|"


@router.get("/", response_model=Dict)
def get_graph(skip: int = 0, limit: int = 100):
    device_types = device_type_repo.get_device_types(skip=skip, limit=limit)
    locations = location_repo.get_locations(skip=skip, limit=limit)
    observable_properties = observable_property_repo.get_observable_properties(skip=skip,
                                                                               limit=limit)
    observations = observation_repo.get_observations(skip=skip, limit=limit)
    gateways = gateway_repo.get_gateways(skip=skip, limit=limit)
    nodes = node_repo.get_nodes(skip=skip, limit=limit)
    sensors = sensor_repo.get_sensors(skip=skip, limit=limit)
    software_sensors = software_sensor_repo.get_software_sensors(skip=skip, limit=limit)
    hardware_sensors = hardware_sensor_repo.get_hardware_sensors(skip=skip, limit=limit)

    graph_nodes = []
    graph_edges = []

    # Create all NODES

    y_count = 1
    for device_type in device_types:
        graph_nodes.append({
            "id": ID_TYPES.DEVICE_TYPE.value + device_type.name,
            "position": {"x": 0 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "DeviceType: " + device_type.name}
        })
        y_count += 1

    y_count = 1
    for location in locations:
        graph_nodes.append({
            "id": ID_TYPES.LOCATION.value + location.name,
            "position": {"x": 1 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "Location: " + location.name}
        })
        y_count += 1

    y_count = 1
    for gateway in gateways:
        graph_nodes.append({
            "id": ID_TYPES.GATEWAY.value + gateway.name,
            "position": {"x": 2 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "Gateway: " + gateway.name}
        })
        y_count += 1

    y_count = 1
    for node in nodes:
        graph_nodes.append({
            "id": ID_TYPES.NODE.value + node.name,
            "position": {"x": 3 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "Node: " + node.name}
        })
        y_count += 1

    y_count = 1
    for sensor in sensors:
        graph_nodes.append({
            "id": ID_TYPES.SENSOR.value + sensor.name,
            "position": {"x": 4 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "Sensor: " + sensor.name}
        })
        y_count += 1

    y_count = 1
    for software_sensor in software_sensors:
        graph_nodes.append({
            "id": ID_TYPES.SOFTWARE_SENSOR.value + software_sensor.sensor_name,
            "position": {"x": 5 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "SoftSens: " + software_sensor.sensor_name}
        })
        y_count += 1

    y_count = 1
    for hardware_sensor in hardware_sensors:
        graph_nodes.append({
            "id": ID_TYPES.HARDWARE_SENSOR.value + hardware_sensor.sensor_name,
            "position": {"x": 6 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "HardSens: " + hardware_sensor.sensor_name}
        })
        y_count += 1

    y_count = 1
    for observable_property in observable_properties:
        graph_nodes.append({
            "id": ID_TYPES.OBSERVABLE_PROPERTY.value + observable_property.name,
            "position": {"x": 7 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "ObservableProperty: " + observable_property.name}
        })
        y_count += 1

    y_count = 1
    for observation in observations:
        graph_nodes.append({
            "id": ID_TYPES.OBSERVATION.value + str(observation.id),
            "position": {"x": 8 * X_DISPLACEMENT, "y": y_count * 100},
            "data": {"label": "Observation: " + str(observation.id)}
        })
        y_count += 1

    # Create all EDGES
    for device_type in device_types:
        for gateway in gateways:
            if gateway.device_type in device_type.name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.DEVICE_TYPE.value + device_type.name +
                          "e" + ID_TYPES.GATEWAY.value + gateway.name,
                    "source": ID_TYPES.DEVICE_TYPE.value + device_type.name,
                    "target": ID_TYPES.GATEWAY.value + gateway.name,
                })
        for node in nodes:
            if node.device_type in device_type.name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.DEVICE_TYPE.value + device_type.name +
                          "e" + ID_TYPES.NODE.value + node.name,
                    "source": ID_TYPES.DEVICE_TYPE.value + device_type.name,
                    "target": ID_TYPES.NODE.value + node.name,
                })
        for sensor in sensors:
            if sensor.device_type in device_type.name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.DEVICE_TYPE.value + device_type.name +
                          "e" + ID_TYPES.SENSOR.value + sensor.name,
                    "source": ID_TYPES.DEVICE_TYPE.value + device_type.name,
                    "target": ID_TYPES.SENSOR.value + sensor.name,
                })
    for location in locations:
        for gateway in gateways:
            if gateway.location in location.name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.GATEWAY.value + gateway.name +
                          "e" + ID_TYPES.LOCATION.value + location.name,
                    "source": ID_TYPES.GATEWAY.value + gateway.name,
                    "target": ID_TYPES.LOCATION.value + location.name
                })
        for node in nodes:
            if node.location in location.name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.NODE.value + node.name +
                          "e" + ID_TYPES.LOCATION.value + location.name,
                    "source": ID_TYPES.NODE.value + node.name,
                    "target": ID_TYPES.LOCATION.value + location.name
                })
        for sensor in sensors:
            if sensor.location in location.name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.SENSOR.value + sensor.name +
                          "e" + ID_TYPES.LOCATION.value + location.name,
                    "source": ID_TYPES.SENSOR.value + sensor.name,
                    "target": ID_TYPES.LOCATION.value + location.name
                })
    for observation in observations:
        for observable_property in observable_properties:
            if observable_property.name in observation.observable_property:
                graph_edges.append({
                    "id": "e" + ID_TYPES.OBSERVABLE_PROPERTY.value + observable_property.name +
                          "e" + ID_TYPES.OBSERVATION.value + str(observation.id),
                    "source": ID_TYPES.OBSERVABLE_PROPERTY.value + observable_property.name,
                    "target": ID_TYPES.OBSERVATION.value + str(observation.id)
                })
        for sensor in sensors:
            if sensor.name in observation.sensor_name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.SENSOR.value + sensor.name +
                          "e" + ID_TYPES.OBSERVATION.value + str(observation.id),
                    "source": ID_TYPES.SENSOR.value + sensor.name,
                    "target": ID_TYPES.OBSERVATION.value + str(observation.id)
                })
    for sensor in sensors:
        for observable_property in observable_properties:
            if observable_property.name in sensor.observable_property:
                graph_edges.append({
                    "id": "e" + ID_TYPES.OBSERVABLE_PROPERTY.value + observable_property.name +
                          "e" + ID_TYPES.SENSOR.value + sensor.name,
                    "source": ID_TYPES.OBSERVABLE_PROPERTY.value + observable_property.name,
                    "target": ID_TYPES.SENSOR.value + sensor.name
                })
    for software_sensor in software_sensors:
        for gateway in gateways:
            if gateway.name == software_sensor.gateway_name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.GATEWAY.value + gateway.name +
                          "e" + ID_TYPES.SOFTWARE_SENSOR.value + software_sensor.sensor_name,
                    "source": ID_TYPES.GATEWAY.value + gateway.name,
                    "target": ID_TYPES.SOFTWARE_SENSOR.value + software_sensor.sensor_name
                })
                break
        for node in nodes:
            if node.name == software_sensor.node_name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.NODE.value + node.name +
                          "e" + ID_TYPES.SOFTWARE_SENSOR.value + software_sensor.sensor_name,
                    "source": ID_TYPES.NODE.value + node.name,
                    "target": ID_TYPES.SOFTWARE_SENSOR.value + software_sensor.sensor_name
                })
                break
        for sensor in sensors:
            if sensor.name in software_sensor.sensor_name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.SENSOR.value + sensor.name +
                          "e" + ID_TYPES.SOFTWARE_SENSOR.value + software_sensor.sensor_name,
                    "source": ID_TYPES.SENSOR.value + sensor.name,
                    "target": ID_TYPES.SOFTWARE_SENSOR.value + software_sensor.sensor_name
                })

    for hardware_sensor in hardware_sensors:
        for node in nodes:
            if node.name in hardware_sensor.node_names:
                graph_edges.append({
                    "id": "e" + ID_TYPES.NODE.value + node.name +
                          "e" + ID_TYPES.HARDWARE_SENSOR.value + hardware_sensor.sensor_name,
                    "source": ID_TYPES.NODE.value + node.name,
                    "target": ID_TYPES.HARDWARE_SENSOR.value + hardware_sensor.sensor_name
                })
        for sensor in sensors:
            if sensor.name in hardware_sensor.sensor_name:
                graph_edges.append({
                    "id": "e" + ID_TYPES.SENSOR.value + sensor.name +
                          "e" + ID_TYPES.HARDWARE_SENSOR.value + hardware_sensor.sensor_name,
                    "source": ID_TYPES.SENSOR.value + sensor.name,
                    "target": ID_TYPES.HARDWARE_SENSOR.value + hardware_sensor.sensor_name
                })

    return {
        "graph_nodes": graph_nodes,
        "graph_edges": graph_edges
    }
