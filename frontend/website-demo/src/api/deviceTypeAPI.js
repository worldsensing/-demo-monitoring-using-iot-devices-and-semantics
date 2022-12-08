import ApiServiceBase from './ApiServiceBase.js'
import Config from '../config.js'

class DeviceTypeAPI extends ApiServiceBase {
  constructor() {
    super()
    this.baseUrl = Config.services.api_device_type.url
  }

  getAllDeviceTypes(priority, callback) {
    this.getFromUrl(
      this.baseUrl,
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

  getDeviceType(name, priority, callback, errorCallback) {
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

  addDeviceType(deviceType, priority, callback, errorCallback) {
    this.postToUrl(
      this.baseUrl,
      deviceType,
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

  updateDeviceType(deviceType, priority, callback, errorCallback) {
    this.putToUrl(
      this.baseUrl + `${deviceType.name}`,
      deviceType,
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

  deleteDeviceType(name, priority, callback, errorCallback) {
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

export default new DeviceTypeAPI()