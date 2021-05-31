import Vue from "vue";
// import store from "../store";

// let vm = this
let URI = "wss://finwise.ir";
// let URI = "ws://localhost:8000";

// let URI = "wss://171.22.25.73";

const WsService = {
  init() {
    try {
      // let MostViewed = new WebSocket("ws://" + URI + "/ws/Top5Views");
      // let ImpactOnIndex = new WebSocket("ws://" + URI + "/ws/ImpactOnIndex");
      // let HighestValue = new WebSocket("ws://" + URI + "/ws/HighestValues");
      // let highestSupply = new WebSocket("ws://" + URI + "/ws/HighestSupplies");
      // let highestDemand = new WebSocket("ws://" + URI + "/ws/HighestDemands");

      // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      let highestVolume = new WebSocket(URI + "/ws/HighestVolume");
      let marketWatch = new WebSocket(URI + "/ws/marketwatch");
      let Optoins = new WebSocket(URI + "/ws/options");
      let marketMap = new WebSocket(URI + "/ws/marketmap");
      let LiveTickerData = new WebSocket(URI + "/ws/liveTickerData");
      let Sandoq = new WebSocket(URI + "/ws/funds");
      let Oraq = new WebSocket(URI + "/ws/oraq");
      let HaghTaghadom = new WebSocket(URI + "/ws/taghadom");
      let Crypto = new WebSocket(URI + "/ws/Crypto");
      // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

      // Vue.prototype.$socketMostViewed = MostViewed;
      // Vue.prototype.$socketImpactOnIndex = ImpactOnIndex;
      // Vue.prototype.$socketMarketHighestDemands = highestDemand;
      // Vue.prototype.$socketMarketHighestSupplies = highestSupply;
      // Vue.prototype.$socketMarketHighestTVolumes = HighestValue;

      // %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

      Vue.prototype.$socketMarketHighestTValues = highestVolume;
      Vue.prototype.$socketMarketWatch = marketWatch;
      Vue.prototype.$socketMarketMap = marketMap;
      Vue.prototype.$socketLiveTickerData = LiveTickerData;
      Vue.prototype.$socketOptions = Optoins;
      Vue.prototype.$socketSandoq = Sandoq;
      Vue.prototype.$socketOraq = Oraq;
      Vue.prototype.$socketCrypto = Crypto;
      Vue.prototype.$socketTaqadom = HaghTaghadom;
    } catch (error) {
      console.error("error in websocket:" + error);
    }
  }
};

export default WsService;
