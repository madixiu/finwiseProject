import Vue from "vue";
// import store from "../store";

// let vm = this
const WsService = {
  init() {
    try {
      // const option_ws = new WebSocket('localhost:9000/ws/')
      let MostViewed = new WebSocket("ws://45.82.136.21/Top5Views");
      let ImpactOnIndex = new WebSocket("ws://45.82.136.21/ImpactOnIndex");
      let highestVolume = new WebSocket("ws://45.82.136.21/HighestVolume");
      let HighestValue = new WebSocket("ws://45.82.136.21/HighestValues");
      let highestSupply = new WebSocket("ws://45.82.136.21/HighestSupplies");
      let highestDemand = new WebSocket("ws://45.82.136.21/HighestDemands");
      //   let ws2 = new WebSocket("ws://45.82.136.21/marketwatch");
      // const option_ws2 = new WebSocket('ws://localhost/ws/test')
      // const option_ws4 = new WebSocket('ws://localhost:9000/')

      // const index_ws = new WebSocket('ws://45.82.136.21/index_live/')
      //   Vue.prototype.$socket = ws;
      Vue.prototype.$socketMostViewed = MostViewed;
      Vue.prototype.$socketImpactOnIndex = ImpactOnIndex;
      Vue.prototype.$socketMarketHighestDemands = highestDemand;
      Vue.prototype.$socketMarketHighestSupplies = highestSupply;
      Vue.prototype.$socketMarketHighestTVolumes = HighestValue;
      Vue.prototype.$socketMarketHighestTValues = highestVolume;

      // Vue.prototype.$socketIndex = index_ws
      // option_ws.onopen = (event) => console.log('ws connected' + event)

      // define store dispatch here -------------
      // store.dispatch("setSocketOpen");
      // store.dispatch('websocketIndex/setSocketOpen')
    } catch (error) {
      console.log("error in websocket:" + error);
    }
  }
};

export default WsService;
