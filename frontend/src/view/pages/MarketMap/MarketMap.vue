<template>
  <!-- <div id="mapparent" class="container-fluid"> -->
  <div width="100%" height="100%">
    <treemap
      :inputData="map"
      :inputWidth="width"
      :inputHeight="height"
      v-if="dataFetched"
    ></treemap>
  </div>
  <!-- <treemap></treemap> -->
  <!-- </div> -->
</template>
<script>
import treemap from "@/view/content/d3/treemap.vue";

// import ErrorMine from "@/view/pages/error/Error-6.vue";
export default {
  name: "marketmap",
  components: {
    // Error,
    treemap

    // ErrorMine
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

  created() {},
  mounted() {
    let chartDiv = document.getElementsByClassName("container-fluid");
    // this.width = window.screen.width;
    this.height = (window.screen.height * 73) / 100;
    this.width = (chartDiv[0].clientWidth * 98) / 100;
    // this.height = chartDiv[0].clientHeight;
    // this.width = chartDiv.width;
    // console.log(this.width);
    // console.log(this.height);
    this.loadData();

    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    // this.$socketMarketMap.send(JSON.stringify({ request: "get" }));
    this.liveChecker();
    this.$socketMarketMap.onmessage = data => {
      // this.$store.dispatch("setMarketWatchItems", JSON.parse(data.data));
      // console.log(!!this.DataItems.length);
      if (
        (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) &&
        this.dataFetched == true
      )
        this.map = JSON.parse(data.data);

      // this.loading = false;
    };
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    // console.log(this.map);
  },
  methods: {
    loadData() {
      this.axios
        .get("/api/Map")
        .then(response => {
          let data = response.data;
          // let tickerNames = [];
          console.log(data);
          if (data != "noData") this.map = data;
          this.dataFetched = true;

          // for (let item of data) {
          //   tickerNames.append(item.ticker);
          // }
          // console.log(tickerNames);
          // this.states = tickerNames;
        })
        .catch(error => {
          console.log(error);
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
        // console.log(this.WebsocketRequest);
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
#mapparent {
  display: contents;
}
</style>
