import Vue from "vue";
// import store from "../store";

// let vm = this
let URI = "localhost:8000";
// let URI = "45.82.136.21"

const WsService = {
  init() {
    try {
      // let MostViewed = new WebSocket("ws://" + URI + "/ws/Top5Views");
      // let ImpactOnIndex = new WebSocket("ws://" + URI + "/ws/ImpactOnIndex");
      let highestVolume = new WebSocket("ws://" + URI + "/ws/HighestVolume");
      // let HighestValue = new WebSocket("ws://" + URI + "/ws/HighestValues");
      // let highestSupply = new WebSocket("ws://" + URI + "/ws/HighestSupplies");
      // let highestDemand = new WebSocket("ws://" + URI + "/ws/HighestDemands");
      let marketWatch = new WebSocket("ws://" + URI + "/ws/marketwatch");
      let Optoins = new WebSocket("ws://" + URI + "/ws/options");
      let marketMap = new WebSocket("ws://" + URI + "/ws/marketmap");
      let LiveTickerData = new WebSocket("ws://" + URI + "/ws/liveTickerData");
      let Sandoq = new WebSocket("ws://" + URI + "/ws/funds");
      let Oraq = new WebSocket("ws://" + URI + "/ws/oraq");
      let HaghTaghadom = new WebSocket("ws://" + URI + "/ws/taghadom");

      // const option_ws2 = new WebSocket('ws://45.82.136.21/ws/test')
      // Vue.prototype.$socketMostViewed = MostViewed;
      // Vue.prototype.$socketImpactOnIndex = ImpactOnIndex;
      // Vue.prototype.$socketMarketHighestDemands = highestDemand;
      // Vue.prototype.$socketMarketHighestSupplies = highestSupply;
      // Vue.prototype.$socketMarketHighestTVolumes = HighestValue;
      Vue.prototype.$socketMarketHighestTValues = highestVolume;
      Vue.prototype.$socketMarketWatch = marketWatch;
      Vue.prototype.$socketMarketMap = marketMap;
      Vue.prototype.$socketLiveTickerData = LiveTickerData;
      Vue.prototype.$socketOptions = Optoins;
      Vue.prototype.$socketSandoq = Sandoq;
      Vue.prototype.$socketOraq = Oraq;
      Vue.prototype.$socketTaqadom = HaghTaghadom;

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
