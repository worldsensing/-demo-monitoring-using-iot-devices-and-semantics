// Model of DeviceType that match with the API's Model

class DeviceType {
    constructor(name = 'Sample name', observation_type = 'Sample observation_type') {
      this.name = name
      this.observation_type = observation_type
    }
  }
  
  export default DeviceType