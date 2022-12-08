console.log('Running in mode: ' + process.env.REACT_APP_MODE)

const dev = {
  services: {
    api_device: {
      url_gateway: 'http://localhost:5000/gateways/',
      url_node: 'http://localhost:5000/nodes/',
      url_sensor: 'http://localhost:5000/sensors/'
    },
    api_device_type: {
      url: 'http://localhost:5000/device-types/'
    },
    api_observation: {
      url: 'http://localhost:5000/observations/'
    },
    api_graph: {
      url: 'http://localhost:5000/graph/'
    },
    grafana: {
      url: 'http://localhost:3001'
    }
  }
}

const prod = {
  services: {
    api_device: {
      url_gateway: 'http://localhost:8000/api/gateways/',
      url_node: 'http://localhost:8000/api/nodes/',
      url_sensor: 'http://localhost:8000/api/sensors/'
    },
    api_device_type: {
      url: 'http://localhost:8000/api/device-types/'
    },
    api_observation: {
      url: 'http://localhost:8000/api/observations/'
    },
    api_graph: {
      url: 'http://localhost:8000/api/graph/'
    },
    grafana: {
      url: 'http://localhost:8000/grafana'
    }
  }
}

const config = process.env.REACT_APP_MODE === 'production' ? prod : dev

export default config