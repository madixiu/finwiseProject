<template>
  <div class="row">
    <div class="col-xxl-9 col-lg-9 col-md-12 col-sm 12">
      <IndexChart :inputDataIndex="TodayTepix"></IndexChart>
      <ChartVol
        :inputDataStatus="highestTvalueData"
        :inputDataImpact="ImpactsData"
      ></ChartVol>
      <ChartHH :inputDataHH="HHData" :inputDataQ="QData"></ChartHH>
    </div>
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm 12">
      <div class="row">
        <ChartTradeValue :inputDataTV="AssetTradeValue"></ChartTradeValue>
        <Technical :inputDataTechnical="TechnicalData"></Technical>
        <NewsW :inputDataNews="News"></NewsW>
      </div>
    </div>
    <!-- <div class="col-xxl-3 col-lg-3"> -->
    <!-- <IndicesText :inputData="AssetTradeValue"></IndicesText> -->
    <!-- </div> -->
    <!-- <div class="col-xxl-3 col-lg-3"> -->
    <!-- 
     </div> -->

    <!-- <div class="col-xxl-2 col-lg-4">
        <Impacts></Impacts>
      </div> -->
    <!-- <div class="col-xxl-4 col-lg-5">
      <HighestTradeValue></HighestTradeValue>
    </div> -->
    <!-- <div class="col-xxl-4"></div> -->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import MostViewedWidget from "@/view/pages/StockMarket/StockMarketWidgets/MostViewed.vue";
import Technical from "@/view/pages/StockMarket/StockMarketWidgets/TechnicalHighest.vue";
import ChartVol from "@/view/pages/StockMarket/StockMarketWidgets/DashboardChart.vue";
import ChartHH from "@/view/pages/StockMarket/StockMarketWidgets/HH_Q_Chart.vue";
import ChartTradeValue from "@/view/pages/StockMarket/StockMarketWidgets/TradesValueChart.vue";
// import IndicesText from "@/view/pages/StockMarket/StockMarketWidgets/DashboardIndicesText.vue";
import IndexChart from "@/view/pages/StockMarket/StockMarketWidgets/IndexChart.vue";
import NewsW from "@/view/pages/StockMarket/StockMarketWidgets/NewsWidget.vue";
// import axios from "axios";
export default {
  name: "Dashboard",
  components: {
    ChartVol,
    ChartHH,
    ChartTradeValue,
    // // IndicesText,
    IndexChart,
    NewsW,
    Technical
    // HighestSupply
  },
  data() {
    return {
      dataFetched: false,
      highestTvalueData: null,
      AssetTradeValue: [],
      TodayTepix: [],
      News: [],
      ImpactsData: [],
      HHData: [],
      QData: [],
      mostviewed: [],
      TechnicalData: []
    };
  },
  mounted() {
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "Dashboard" }]);
    this.loadData();

    // this.make_requests_handler();
  },
  methods: {
    make_requests_handler() {
      this.axios.all([this.request_1()]).then(
        this.axios.spread(
          // (first_response, second_response, third, fourth,fifth,sixth) => {
          first_response => {
            this.ImpactsData = first_response.data[0];
            this.highestTvalueData = first_response.data[1];
            this.AssetTradeValue = first_response.data[2];
            this.News = first_response.data[3];
            this.HHData = first_response.data[4];
            this.QData = first_response.data[5];
            this.TodayTepix = first_response.data[6];
            this.TechnicalData = first_response.data[7];
          }
        )
      );
    },
    request_1() {
      return this.axios.get("/api/Dashboard");
    },
    loadData() {
      this.getDashboard()
        // eslint-disable-next-line no-unused-vars
        .then(r1 => {
          // eslint-disable-next-line no-unused-vars
          // this.getImpacts().then(r5 => {
          //   // eslint-disable-next-line no-unused-vars
          //   this.getTradesAll().then(r2 => {
          //     // eslint-disable-next-line no-unused-vars
          //     this.getTepixToday().then(r3 => {
          //       // eslint-disable-next-line no-unused-vars
          //       this.getNews().then(r4 => {
          //         this.dataFetched = true;
          //       });
          //     });
          //   });
          // });
        })

        // for (let item of data) {
        //   tickerNames.append(item.ticker);
        // }
        // console.log(tickerNames);
        // this.states = tickerNames;
        .catch(error => {
          console.log(error);
        });
    },
    async getDashboard() {
      await this.axios
        .get("/api/Dashboard")
        .then(first_response => {
          console.log("here");
          console.log(first_response);
          this.ImpactsData = first_response.data[0];
          this.highestTvalueData = first_response.data[1];
          this.AssetTradeValue = first_response.data[2];
          this.News = first_response.data[3];
          this.HHData = first_response.data[4];
          this.QData = first_response.data[5];
          this.TodayTepix = first_response.data[6];
          this.TechnicalData = first_response.data[7]; // console.log(respoey.data)
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getImpacts() {
      await this.axios
        .get("/api/ImpactOnIndex")
        .then(respoey => {
          this.ImpactsData = respoey.data;
          // console.log(respoey.data)
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getTradesValue() {
      await this.axios
        .get("/api/tse/getHighestValue/")
        .then(respoex => {
          this.highestTvalueData = respoex.data;
          // console.log(respoex)
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
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
