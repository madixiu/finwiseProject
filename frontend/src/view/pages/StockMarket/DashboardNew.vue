<template>
  <div class="row" style="padding-top:5px">
    <div class="col-xxl-9 col-lg-9 col-md-12 col-sm-12">
      <IndexChart :inputDataIndex="TodayTepix" class="mb-4"></IndexChart>
      <ChartVol
        :inputDataStatus="highestTvalueData"
        :inputDataImpact="ImpactsData"
        class="pb-2 pt-1"
      ></ChartVol>
      <ChartHH :inputDataHH="HHData" :inputDataQ="QData"></ChartHH>
    </div>
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm-12">
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
      highestTvalueData: [],
      AssetTradeValue: [],
      TodayTepix: [],
      News: [],
      ImpactsData: [],
      HHData: [],
      QData: [],
      mostviewed: [],
      TechnicalData: [],
      ResponeseTimeout: {
        getImpacts: true,
        TradesValue: true,
        getTradesAll: true,
        getNews: true,
        getTepixToday: true,
        getHHData: true,
        getHighestQ: true,
        getTechnicalData: true
      }
    };
  },
  created() {
    document.title = "FinWise - سهام";
  },
  mounted() {
    // this.test();
    this.ResponeseTimeout = {
      getImpacts: true,
      TradesValue: true,
      getTradesAll: true,
      getNews: true,
      getTepixToday: true,
      getHHData: true,
      getHighestQ: true,
      getTechnicalData: true
    };
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "Dashboard" }]);

    this.loadData();
    // eslint-disable-next-line no-unused-vars
    let interval = setInterval(() => {
      this.loadData();
    }, 300000);

    // this.make_requests_handler();
  },
  methods: {
    loadData() {
      // this.getDashboard();
      // eslint-disable-next-line no-unused-vars
      this.getTepixToday().then(resp0 => {
        // eslint-disable-next-line no-unused-vars
        this.getTradesAll().then(resp1 => {
          // eslint-disable-next-line no-unused-vars
          this.getTechnicalData().then(resp2 => {
            // this.getNews();
            // eslint-disable-next-line no-unused-vars
            this.getNews().then(resp3 => {
              this.loadData2();
            });
          });
        });
      });
    },
    loadData2() {
      // eslint-disable-next-line no-unused-vars
      this.getImpacts().then(resp4 => {
        // eslint-disable-next-line no-unused-vars
        this.getHHData().then(resp5 => {
          // eslint-disable-next-line no-unused-vars
          this.getHighestQ().then(resp6 => {
            // eslint-disable-next-line no-unused-vars
            this.getTradesValue();
            //   let TimeoutList = Object.values(this.ResponeseTimeout);
            //   for (let item of TimeoutList) {
            //     if (item == true) {
            //       setTimeout(() => {
            //         this.loadData();
            //       }, 5000);
            //     }
            //   }
            // });
          });
        });
      });
    },
    async getImpacts() {
      await this.axios
        .get("/api/ImpactOnIndex")
        .then(getImpactsResp => {
          this.ResponeseTimeout.getImpacts = false;

          this.ImpactsData = getImpactsResp.data;
          return true;
        })
        .catch(error => {
          // if (error.code == "ECONNABORTED") setTimeout(this.getImpacts(), 1000);
          // else console.error(error);
          if (error.code == "ECONNABORTED") {
            this.ResponeseTimeout.getImpacts = true;
            // return false
          } else console.error(error);
        });
    },
    async getTradesValue() {
      await this.axios
        .get("/api/getHighestValue")
        .then(getTradesValueResp => {
          this.ResponeseTimeout.getTradesValue = false;

          this.highestTvalueData = getTradesValueResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            // setTimeout(this.getTradesValue(), 1000);
            this.ResponeseTimeout.getTradesValue = true;
          else console.error(error);
        });
    },
    async getTradesAll() {
      await this.axios
        .get("/api/getAllTradesValue")
        .then(getTradesAllResp => {
          this.ResponeseTimeout.getTradesAll = false;

          this.AssetTradeValue = getTradesAllResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            // setTimeout(this.getTradesAll(), 1000);
            this.ResponeseTimeout.getTradesAll = true;
          else console.error(error);
        });
    },
    async getNews() {
      await this.axios
        .get("/api/LatestNews")
        .then(getNewsResp => {
          this.ResponeseTimeout.getNews = false;

          this.News = getNewsResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            // setTimeout(this.getNews(), 1000);
            this.ResponeseTimeout.getNews = true;
          else {
            console.error(error);
            this.ResponeseTimeout.getNews = false;
          }
        });
    },
    async getTepixToday() {
      await this.axios
        .get("/api/getTodayTepix")
        .then(getTepixTodayResp => {
          this.ResponeseTimeout.getTepixToday = false;
          this.TodayTepix = getTepixTodayResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            // setTimeout(this.getTepixToday(), 1000);
            this.ResponeseTimeout.getTepixToday = true;
          else console.error(error);
          // the request has either been canceled due to a network timeout,
          // or because the device is offline
        });
    },
    async getHHData() {
      await this.axios
        .get("/api/HHMarketDetails")
        .then(getHHDataResp => {
          this.ResponeseTimeout.getHHData = false;

          // console.log(getHHDataResp);
          this.HHData = getHHDataResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            // setTimeout(this.getHHData(), 1000);
            this.ResponeseTimeout.getHHData = true;
          else console.error(error);
        });
    },
    async getHighestQ() {
      await this.axios
        .get("/api/HighestQ")
        .then(getHighestQResp => {
          this.ResponeseTimeout.getHighestQ = false;
          this.QData = getHighestQResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            this.ResponeseTimeout.getHighestQ = true;
          // setTimeout(this.getHighestQ(), 1000);
          else console.error(error);
        });
    },
    async getTechnicalData() {
      await this.axios
        .get("/api/Ticker/TechnicalIndicatorsAll")
        .then(getTechnicalDataResp => {
          this.ResponeseTimeout.getTechnicalData = false;
          this.TechnicalData = getTechnicalDataResp.data;
        })
        .catch(error => {
          if (error.code == "ECONNABORTED")
            this.ResponeseTimeout.getTechnicalData = true;
          // setTimeout(this.getTechnicalData(), 1000);
          else console.error(error);
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
<style>
.rtl_centerd {
  font-size: 1em;
  direction: rtl;
  text-align: center;
}
</style>
