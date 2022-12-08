import React, { Component } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'
import DeviceTab from '../pages/device.js'
import ObservationTab from '../pages/observation.js'
import GrafanaTab from '../pages/grafana.js'
import Flow from '../pages/map.js'

import '../App.css'

class Main extends Component {
  render() {
    return (
      <div className="app-content">
        <Routes>
          <Route path="/devices" element={<DeviceTab />} />
          <Route path="/observations" element={<ObservationTab />} />
          <Route path="/grafana" element={<GrafanaTab />} />
          <Route path="/map" element={<Flow />} />
          <Route
                exact
                path="/"
                render={() => {
                    return (
                      <Navigate to="/devices" />
                    )
                }}
              />
        </Routes>
      </div>
    )
  }
}

export default Main