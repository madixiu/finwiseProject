<template>
  <div id="MarketMapID" class="MarketMapContainer" width="100%" height="100%">
    <treemap
      :inputData="map"
      :inputWidth="width"
      :inputHeight="height"
      v-if="dataFetched"
    ></treemap>
  </div>
</template>
<script>
import treemap from "@/view/content/d3/treemap.vue";

// import ErrorMine from "@/view/pages/error/Error-6.vue";
export default {
  name: "marketmap",
  components: {
    treemap
  },
  data() {
    return {
      dataFetched: false,
      map: null,
      width: null,
      height: null,
      WebsocketRequest: false
    };
  },

  created() {
    // let chartDiv = document.getElementsByClassName("container-fluid");
    // console.log(chartDiv);
    // // this.height = (chartDiv[1].clientHeight);
    // this.width = (chartDiv[1].clientWidth) ;
    //  let headerHeight = document.getElementById("kt_header").clientHeight
    // this.height = (window.innerHeight - headerHeight);
  },
  mounted() {
    // let headerHeight = document.getElementById("kt_header").clientHeight
    // console.log(headerHeight);
    let chartDiv = document.getElementsByClassName("container-fluid");

    this.height = (window.screen.height * 73) / 100;
    this.width = (chartDiv[0].clientWidth * 98) / 100;
    // this.height = chartDiv[0].clientHeight;
    // this.width = chartDiv.width;
    this.loadData();

    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    // this.$socketMarketMap.send(JSON.stringify({ request: "get" }));
    this.liveChecker();
    this.$socketMarketMap.onmessage = data => {
      // this.$store.dispatch("setMarketWatchItems", JSON.parse(data.data));
      if (
        (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) &&
        this.dataFetched == true
      )
        this.map = JSON.parse(data.data);

      // this.loading = false;
    };
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  methods: {
    loadData() {
      this.axios
        .get("/api/Map")
        .then(response => {
          let data = response.data;
          // let tickerNames = [];
          if (data != "noData") this.map = data;
          this.dataFetched = true;

          // for (let item of data) {
          //   tickerNames.append(item.ticker);
          // }
          // this.states = tickerNames;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketMarketMap.send(JSON.stringify(barier));
      }, 30000);
    },
    liveChecker() {
      let date = new Date();
      if (date.getHours() > 8 && date.getHours() < 15) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$socketMarketMap.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style scoped>
/* div#MarketMapID.MarketMapContainer {
  background-color: #252830 !important;
  padding-left: 0px !important;
} */
</style>
