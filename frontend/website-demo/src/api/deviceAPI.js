import ApiServiceBase from './ApiServiceBase.js'
import Config from '../config.js'

class DeviceAPI extends ApiServiceBase {
  constructor() {
    super()
    this.baseUrlGateways = Config.services.api_device.url_gateway
    this.baseUrlNodes = Config.services.api_device.url_node
    this.baseUrlSensors = Config.services.api_device.url_sensor
  }

  getAllGateways(priority, callback) {
    this.getFromUrl(
      this.baseUrlGateways,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      priority
    )
  }

  getAllNodes(priority, callback) {
    this.getFromUrl(
      this.baseUrlNodes,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      priority
    )
  }

  getAllSensors(priority, callback) {
    this.getFromUrl(
      this.baseUrlSensors,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      priority
    )
  }

  getDevice(name, priority, callback, errorCallback) {
    this.getFromUrl(
      this.baseUrl + `${name}`,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  addDevice(device, priority, callback, errorCallback) {
    this.postToUrl(
      this.baseUrl,
      device,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  updateDevice(device, priority, callback, errorCallback) {
    this.putToUrl(
      this.baseUrl + `${device.name}`,
      device,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  deleteDevice(name, priority, callback, errorCallback) {
    this.deleteToUrl(
      this.baseUrl + `${name}`,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }
}

export default new DeviceAPI()