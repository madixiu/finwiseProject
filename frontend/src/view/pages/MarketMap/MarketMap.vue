<template>
  <div
    class="row"
    id="MapRoot"
    style="padding-top:0px;padding-left:0px;padding-right:0px;margin-top:-20px"
  >
    <!-- <v-btn @click="forceUpdate()">change</v-btn> -->
    <!-- <div id="MarketMapID" class="MarketMapContainer" width="100%" height="100%"> -->

    <treemap
      v-if="dataFetched && width != null"
      :key="mapKey"
      :inputData="map"
      :inputWidth="width"
      :inputHeight="height"
    ></treemap>
    <!-- </div> -->
  </div>
</template>
<script>
import treemap from "@/view/content/d3/treemap.vue";
export default {
  name: "marketmap",
  components: {
    treemap
  },
  data() {
    return {
      mapKey: 0,
      interval: null,
      dataFetched: false,
      map: null,
      width: null,
      height: null,
      WebsocketRequest: false
    };
  },
  watch: {
    $route() {
      if (this.$route.name != "marketmap") {
        clearInterval(this.interval);
        this.WebsocketRequest = false;
      }
    }
  },
  created() {
    document.title = "Finwise - نقشه بازار";

    // let chartDiv = document.getElementsByClassName("container-fluid");
    // console.log(chartDiv);
    // // this.height = (chartDiv[1].clientHeight);
    // this.width = (chartDiv[1].clientWidth) ;
    //  let headerHeight = document.getElementById("kt_header").clientHeight
    // this.height = (window.innerHeight - headerHeight);
  },

  mounted() {
    let headerWidth = document.getElementById("MapRoot").clientWidth;
    // console.log(headerHeight);
    // let chartDiv = document.getElementsByClassName("container-fluid");
    this.height = (window.screen.height * 73) / 100;
    this.height = window.innerHeight - 65;

    // this.width = (chartDiv[0].clientWidth * 98) / 100;
    // this.width = (chartDiv[0].clientWidth * 98) / 100;
    this.width = headerWidth;
    this.width = window.innerWidth - 10;
    // console.log(this.width);
    this.loadData();

    // this.height = chartDiv[0].clientHeight;
    // this.width = chartDiv.width;

    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    // this.$socketMarketMap.send(JSON.stringify({ request: "get" }));
    this.liveChecker();
    // this.liveData()
    // this.$socketMarketMap.onmessage = data => {
    //   // this.$store.dispatch("setMarketWatchItems", JSON.parse(data.data));
    //   if (
    //     (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) &&
    //     this.dataFetched == true
    //   )
    //     this.map = JSON.parse(data.data);

    // };
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
    forceUpdate() {
      this.mapKey += 1;
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      this.interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(this.interval_id);
          return;
        }
        // let barier = { request: "get" };
        // this.$socketMarketMap.send(JSON.stringify(barier));
        this.loadData();
      }, 3000);
    },
    liveChecker() {
      let date = new Date();
      if (
        date.getHours() > 8 &&
        date.getHours() < 13 &&
        date.getDay() != 5 &&
        date.getDay() != 4
      ) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  beforeDestroy() {
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketMarketWatch.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  }
};
</script>
<style scoped>
/* div#MarketMapID.MarketMapContainer {
  background-color: #252830 !important;
  padding-left: 0px !important;
} */
</style>
