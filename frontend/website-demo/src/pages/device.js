import React from 'react'
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'

import EnhancedTable from '../components/table/EnhancedTable.js'
import DeviceAPI from '../api/deviceAPI.js'
import { Gateway, Node, Sensor } from '../models/device.js'

import { combineArrayNoDuplication } from '../toolbox/utils.js'

function createData(name, type, device_type, location, info, active, extra_info) {
  return { name, type, device_type, location, info, active, extra_info}
}

export class DeviceTab extends React.Component {
  constructor(props) {
    super(props)

    this.randomIDToForceRefresh = 0
    this.state = {
      selectedDeviceName: '',
      devices: [],
      devicesRows: [],
      filterValues: []
    }
  }

  // TODO Z This function is called twice
  componentDidMount() {
    DeviceAPI.getAllGateways(false, (response) => {
      var gatewaysFromApi = response.message.map((gateway) => {
        return new Gateway(gateway.name, gateway.type, gateway.device_type, gateway.location, gateway.info, gateway.active, 
          gateway.power_type, gateway.connectivity, gateway.modem_signal, gateway.power_supply)
      })
      var resultRows = gatewaysFromApi.map((device) => {
        let extra_info = ""

        if (device.power_type) {
          extra_info += "Power Type: " + device.power_type + ", "
        }
        if (device.connectivity) {
          extra_info += "Connectivity: " + device.connectivity + ", "
        }
        if (device.modem_signal) {
          extra_info += "Modem Signal: " + device.modem_signal + ", "
        }
        if (device.power_supply) {
          extra_info += "Power Supply: " + device.power_supply + ", "
        }

        return createData(
          device.name,
          "Gateway",
          device.device_type,
          device.location,
          device.info,
          device.active ? "Yes" : "No",
          extra_info
        )
      })
      
      // TODO CombineArray can be removed once TODO Z is solved
      this.setState(prevState => ({
        devices: [...prevState.devices, ...combineArrayNoDuplication(gatewaysFromApi, prevState.devices)],
        devicesRows: [...prevState.devicesRows, ...combineArrayNoDuplication(resultRows, prevState.devicesRows)],
      }))
    })
    DeviceAPI.getAllNodes(false, (response) => {
      var nodesFromApi = response.message.map((node) => {
        return new Node(node.name, node.type, node.device_type, node.location, node.info, node.active, node.sampling_rate)
      })
      var resultRows = nodesFromApi.map((device) => {
        return createData(
          device.name,
          "Node",
          device.device_type,
          device.location,
          device.info,
          device.active ? "Yes" : "No",
          device.sampling_rate ? "Sampling Rate: " + device.sampling_rate : ""
        )
      })

      // TODO CombineArray can be removed once TODO Z is solved
      this.setState(prevState => ({
        devices: [...prevState.devices, ...combineArrayNoDuplication(nodesFromApi, prevState.devices)],
        devicesRows: [...prevState.devicesRows, ...combineArrayNoDuplication(resultRows, prevState.devicesRows)],
      }))
    })
    DeviceAPI.getAllSensors(false, (response) => {
      var sensorsFromApi = response.message.map((sensor) => {
        return new Sensor(sensor.name, sensor.type, sensor.device_type, sensor.location, sensor.info, sensor.active)
      })
      var resultRows = sensorsFromApi.map((device) => {
        return createData(
          device.name,
          "Sensor",
          device.device_type,
          device.location,
          device.info,
          device.active ? "Yes" : "No",
          ''
        )
      })

      // TODO CombineArray can be removed once TODO Z is solved
      this.setState(prevState => ({
        devices: [...prevState.devices, ...combineArrayNoDuplication(sensorsFromApi, prevState.devices)],
        devicesRows: [...prevState.devicesRows, ...combineArrayNoDuplication(resultRows, prevState.devicesRows)],
      }))
    })
  }

  render() {
    const columns = [
      {
        id: 'name',
        label: 'Name'
      },
      {
        id: 'type',
        label: 'Type'
      },
      {
        id: 'device_type',
        label: 'Device Type'
      },
      {
        id: 'location',
        label: 'Location'
      },
      {
        id: 'info',
        label: 'Info'
      },
      {
        id: 'active',
        label: 'Active'
      },
      {
        id: 'extra_info',
        label: 'Extra Information'
      }
    ]

    this.randomIDToForceRefresh++

    return (
      <Grid
        container
        spacing={2}
        justifyContent="center"
        alignItems="flex-start"
        style={{ marginTop: '20px' }}
      >
        <Grid item xs={8}>
          <Paper key={this.randomIDToForceRefresh}>
            <EnhancedTable
              toolbarTitle={'Devices'}
              filterValues={this.state.filterValues}
              dataColumns={columns}
              dataRows={this.state.devicesRows}
            />
          </Paper>
        </Grid>
      </Grid>
    )
  }
}

export default DeviceTab