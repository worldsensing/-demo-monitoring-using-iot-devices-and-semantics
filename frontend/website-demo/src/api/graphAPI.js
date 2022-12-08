import ApiServiceBase from './ApiServiceBase.js'
import Config from '../config.js'

class GraphAPI extends ApiServiceBase {
  constructor() {
    super()
    this.baseUrl = Config.services.api_graph.url
  }

  getGraph(priority, callback) {
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
}

export default new GraphAPI()