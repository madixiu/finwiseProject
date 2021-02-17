<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-8 col-lg-8">
        aaaa
      </div>
      <div class="col-xxl-4 col-lg-4">
        <ChartTradeValue
          :inputData="AssetTradeValue"
          :inputWidth="width"
          :inputHeight="height"
          v-if="dataFetched"
        ></ChartTradeValue>
      </div>
      <div class="col-xxl-10 col-lg-10" id="ChartOneDiv">
        <ChartVol
          :inputData="highestTvalueData"
          :inputWidth="width"
          :inputHeight="height"
          v-if="dataFetched"
        ></ChartVol>
      </div>
      <!-- <div class="col-xxl-2 col-lg-4">
        <Impacts></Impacts>
      </div> -->
      <div class="col-xxl-4 col-lg-5">
        <HighestTradeValue></HighestTradeValue>
      </div>
      <!-- <div class="col-xxl-4"></div> -->
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import MostViewedWidget from "@/view/pages/StockMarket/StockMarketWidgets/MostViewed.vue";
import HighestTradeValue from "@/view/pages/StockMarket/StockMarketWidgets/HighestTradeValues.vue";
import ChartVol from "@/view/pages/StockMarket/StockMarketWidgets/DashboardChart.vue";
import ChartTradeValue from "@/view/pages/StockMarket/StockMarketWidgets/TradesValueChart.vue";
// import HighestDemand from "@/view/pages/StockMarket/StockMarketWidgets/HighestDemand.vue";
// import HighestSupply from "@/view/pages/StockMarket/StockMarketWidgets/HighestSupply.vue";
// import Impacts from "@/view/pages/StockMarket/StockMarketWidgets/ImpactOnIndex.vue";
// import axios from "axios";
export default {
  name: "Dashboard",
  components: {
    // MostViewedWidget,
    // Impacts,
    HighestTradeValue,
    ChartVol,
    ChartTradeValue
    // HighestDemand,
    // HighestSupply
  },
  data() {
    return {
      dataFetched: false,
      highestTvalueData: null,
      AssetTradeValue: {},
      width: null,
      height: null,
      mostviewed: []
    };
  },
  mounted() {
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "Dashboard" }]);
    // let chartDiv = document.getElementsByClassName("container-fluid");

    this.width = document.getElementById("ChartOneDiv").clientWidth;
    this.height = (window.screen.height * 50) / 100;
    console.log(this.width);
    // console.log(this.height);
    this.loadData();
  },
  methods: {
    loadData() {
      this.axios
        .get("/api/tse/getHighestValue/")
        .then(response => {
          let data = response.data;
          // let tickerNames = [];
          console.log(data);
          if (data != "noData") this.highestTvalueData = data;
          // eslint-disable-next-line no-unused-vars
          this.getTradesAll().then(response => {
            this.dataFetched = true;
          });

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
    async getTradesAll() {
      await this.axios
        .get("/api/getAllTradesValue")
        .then(response2 => {
          this.AssetTradeValue = response2.data;
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    setActiveTab1(event) {
      this.tabIndex = this.setActiveTab(event);
    },
    setActiveTab2(event) {
      this.tabIndex2 = this.setActiveTab(event);
    },
    /**
     * Set current active on click
     * @param event
     */
    setActiveTab(event) {
      // get all tab links
      const tab = event.target.closest('[role="tablist"]');
      const links = tab.querySelectorAll(".nav-link");
      // remove active tab links
      for (let i = 0; i < links.length; i++) {
        links[i].classList.remove("active");
      }

      // set current active tab
      event.target.classList.add("active");

      // set clicked tab index to bootstrap tab
      return parseInt(event.target.getAttribute("data-tab"));
    }
  }
};
</script>
