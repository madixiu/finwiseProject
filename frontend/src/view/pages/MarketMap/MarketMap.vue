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
      height: null
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
    console.log(this.width);
    console.log(this.height);
    this.loadData();
    console.log(this.map);
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
    }
  }
};
</script>
<style scoped>
#mapparent {
  display: contents;
}
</style>
