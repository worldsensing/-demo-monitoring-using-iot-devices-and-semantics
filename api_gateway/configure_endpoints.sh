# Register Frontend
sh ./manage.sh "frontend" "http://frontend:80" \
  "frontend-route-a" "/"

# Register Grafana
sh ./manage.sh "grafana-frontend" "http://grafana:3000" \
  "grafana-frontend-route-a" "/grafana"

# Register Backend APIs
## Swagger Docs
sh ./manage.sh "api-docs" "http://backend_api:80/docs" \
  "api-docs-route-a" "/api/docs"
## Graph
sh ./manage.sh "api-graph" "http://backend_api:80/graph/" \
  "api-graph-route-a" "/api/graph"
## Device Type
sh ./manage.sh "api-device-type" "http://backend_api:80/device-types/" \
  "api-device-type-route-a" "/api/device-types"
## Gateway
sh ./manage.sh "api-gateway" "http://backend_api:80/gateways/" \
  "api-device-gateway-route-a" "/api/gateways"
## Node
sh ./manage.sh "api-node" "http://backend_api:80/nodes/" \
  "api-device-node-route-a" "/api/nodes"
## Sensor
sh ./manage.sh "api-sensor" "http://backend_api:80/sensors/" \
  "api-device-sensor-route-a" "/api/sensors"
## Software Sensor
sh ./manage.sh "api-sensor-software" "http://backend_api:80/software-sensors/" \
  "api-sensor-software-route-a" "/api/software-sensors"
## Hardware Sensor
sh ./manage.sh "api-sensor-hardware" "http://backend_api:80/hardware-sensors/" \
  "api-sensor-hardware-route-a" "/api/hardware-sensors"
## Observation
sh ./manage.sh "api-observation" "http://backend_api:80/observations/" \
  "api-observation-route-a" "/api/observations"
## ObservableProperty
sh ./manage.sh "api-observable-property" "http://backend_api:80/observable-properties/" \
  "api-observable-property-route-a" "/api/observable-properties"
## Location
sh ./manage.sh "api-location" "http://backend_api:80/locations/" \
  "api-location-route-a" "/api/locations"

# Examples
#curl -i -X POST --url http://localhost:8001/services/ --data 'name=example-service' --data 'url=http://mockbin.org'
#curl -i -X POST --url http://localhost:8001/services/example-service/routes --data 'name=route-name' --data 'paths[]=/foo&paths[]=/bar'

## Delete
#curl -X DELETE --url http://localhost:8001/services/{service name or id}
#curl -X DELETE --url http://localhost:8001/services/{service name or id}/routes/{route name or id}
