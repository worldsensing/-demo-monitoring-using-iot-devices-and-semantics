console.log('Running in mode: ' + process.env.REACT_APP_MODE)

const dev_url = "http://localhost"
const prod_url = "http://localhost"

const dev = {
  services: {
    api_device: {
      url_gateway: dev_url + ':5000/gateways/',
      url_node: dev_url + ':5000/nodes/',
      url_sensor: dev_url + ':5000/sensors/'
    },
    api_device_type: {
      url: dev_url + ':5000/device-types/'
    },
    api_observation: {
      url: dev_url + ':5000/observations/'
    },
    api_graph: {
      url: dev_url + ':5000/graph/'
    },
    grafana: {
      url: dev_url + ':3001'
    }
  }
}

const prod = {
  services: {
    api_device: {
      url_gateway: prod_url + ':8000/api/gateways/',
      url_node: prod_url + ':8000/api/nodes/',
      url_sensor: prod_url + ':8000/api/sensors/'
    },
    api_device_type: {
      url: prod_url + ':8000/api/device-types/'
    },
    api_observation: {
      url: prod_url + ':8000/api/observations/'
    },
    api_graph: {
      url: prod_url + ':8000/api/graph/'
    },
    grafana: {
      url: prod_url + ':8000/grafana'
    }
  }
}

const config = process.env.REACT_APP_MODE === 'production' ? prod : dev

export default config