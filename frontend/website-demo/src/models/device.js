// Model of Device that match with the API's Model

class Device {
  constructor(name = 'Sample name', type = 'Sample Type', device_type = 'Sample type', location = '', info = '', active = '') {
    this.name = name
    this.type = type
    this.device_type = device_type
    this.location = location
    this.info = info
    this.active = active
  }
}

class Gateway extends Device {
  constructor(name = 'Sample name', type = 'Sample Type', device_type = 'Sample type', location = '', info = '', active = '',
   power_type = '', connectivity = '', modem_signal = '', power_supply = '') {
    super(name, type, device_type, location, info, active)
    this.power_type = power_type
    this.connectivity = connectivity
    this.modem_signal = modem_signal
    this.power_supply = power_supply
  }
}

class Node extends Device {
  constructor(name = 'Sample name', type = 'Sample Type', device_type = 'Sample type', location = '', info = '', active = '',
   sampling_rate = '') {
    super(name, type, device_type, location, info, active)
    this.sampling_rate = sampling_rate
  }
}

class Sensor extends Device {
  constructor(name = 'Sample name', type = 'Sample Type', device_type = 'Sample type', location = '', info = '', active = '') {
    super(name, type, device_type, location, info, active)
  }
}
  
export { Device, Gateway, Node, Sensor }