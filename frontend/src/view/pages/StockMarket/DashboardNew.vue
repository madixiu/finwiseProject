<template>
  <div class="row">
    <div class="col-xxl-9 col-lg-9 col-md-12 col-sm 12" id="ChartOneDiv">
      <ChartVol
        :inputData="highestTvalueData"
        :inputWidth="width"
        :inputHeight="height"
        v-if="dataFetched"
      ></ChartVol>
    </div>
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm 12">
      <div class="row">
        <ChartTradeValue
          :inputData="AssetTradeValue"
          :inputWidth="width"
          :inputHeight="height"
          v-if="dataFetched"
        ></ChartTradeValue>
        <NewsW :inputDataNews="News"></NewsW>
      </div>
    </div>
    <div class="col-xxl-3 col-lg-3">
      <!-- <IndicesText :inputData="AssetTradeValue"></IndicesText> -->
    </div>
    <div class="col-xxl-3 col-lg-3">
      <!-- <IndexChart
          :inputData="TodayTepix"
          :inputWidth="width"
          :inputHeight="height"
          v-if="dataFetched"
        ></IndexChart> -->
    </div>

    <!-- <div class="col-xxl-2 col-lg-4">
        <Impacts></Impacts>
      </div> -->
    <div class="col-xxl-4 col-lg-5">
      <HighestTradeValue></HighestTradeValue>
    </div>
    <!-- <div class="col-xxl-4"></div> -->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import MostViewedWidget from "@/view/pages/StockMarket/StockMarketWidgets/MostViewed.vue";
import HighestTradeValue from "@/view/pages/StockMarket/StockMarketWidgets/HighestTradeValues.vue";
import ChartVol from "@/view/pages/StockMarket/StockMarketWidgets/DashboardChart.vue";
import ChartTradeValue from "@/view/pages/StockMarket/StockMarketWidgets/TradesValueChart.vue";
// import IndicesText from "@/view/pages/StockMarket/StockMarketWidgets/DashboardIndicesText.vue";
// import IndexChart from "@/view/pages/StockMarket/StockMarketWidgets/IndexChart.vue";
import NewsW from "@/view/pages/StockMarket/StockMarketWidgets/NewsWidget.vue";
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
    ChartTradeValue,
    // IndicesText,
    // IndexChart,
    NewsW
    // HighestDemand,
    // HighestSupply
  },
  data() {
    return {
      dataFetched: false,
      highestTvalueData: null,
      AssetTradeValue: {},
      TodayTepix: [],
      News: [],
      width: null,
      height: null,
      mostviewed: []
    };
  },
  mounted() {
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "Dashboard" }]);
    // let chartDiv = document.getElementsByClassName("container-fluid");
    let chartDiv = document.getElementsByClassName("container-fluid");
    // this.width = window.screen.width;
    this.height = (window.screen.height * 73) / 100;
    this.width = (chartDiv[0].clientWidth * 98) / 100;
    // this.width = 200
    // this.height = 200
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
          if (data != "noData") this.highestTvalueData = data;
          // eslint-disable-next-line no-unused-vars
          this.getTradesAll().then(response => {
            // eslint-disable-next-line no-unused-vars
            this.getTepixToday().then(response2 => {
              // eslint-disable-next-line no-unused-vars
              this.getNews().then(response2 => {
                this.dataFetched = true;
              });
            });
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
    async getNews() {
      await this.axios
        .get("/api/LatestNews")
        .then(response1 => {
          this.News = response1.data;
          // console.log(response1.data);
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getTepixToday() {
      await this.axios
        .get("/api/getTodayTepix")
        .then(response3 => {
          this.TodayTepix = response3.data;
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
