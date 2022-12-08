// Model of Observation that match with the API's Model

class Observation {
    constructor(
      id,
      sensor_name,
      observable_property,
      time_start,
      time_end,
      value_int,
      value_float,
      value_bool,
      value_str
    ) {
      this.id = id
      this.sensor_name = sensor_name
      this.observable_property = observable_property
      this.time_start = time_start
      this.time_end = time_end
      this.value_int = value_int
      this.value_float = value_float
      this.value_bool = value_bool
      this.value_str = value_str
    }
  }
  
  export default Observation