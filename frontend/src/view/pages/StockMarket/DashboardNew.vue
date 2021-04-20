<template>
  <div class="row">
    <div class="col-xxl-9 col-lg-9 col-md-12 col-sm-12">
      <IndexChart :inputDataIndex="TodayTepix" class="mb-4"></IndexChart>
      <ChartVol
        :inputDataStatus="highestTvalueData"
        :inputDataImpact="ImpactsData"
        class="mb-4"
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
      dataFetched: false,
      highestTvalueData: null,
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

    // this.make_requests_handler();
  },
  methods: {
    test() {
      let four = "/api/LatestNews";
      let three = "/api/tse/getHighestValue";
      let two = "/api/getAllTradesValue";
      let one = "/api/getTodayTepix";
      let five = "/api/ImpactOnIndex";
      let six = "/api/HHMarketDetails";
      let seven = "/api/HighestQ";
      let eight = "/api/Ticker/TechnicalIndicatorsAll";

      const request1 = this.axios.get(one);
      const request2 = this.axios.get(two);
      const request3 = this.axios.get(three);
      const request4 = this.axios.get(four);

      const request5 = this.axios.get(five);

      const request6 = this.axios.get(six);
      const request7 = this.axios.get(seven);
      const request8 = this.axios.get(eight);

      this.axios
        .all([
          request1,
          request2,
          request3,
          request4,
          request5,
          request6,
          request7,
          request8
        ])
        .then(
          this.axios.spread((...responses) => {
            const response1 = responses[0];
            const response2 = responses[1];
            const response3 = responses[2];
            const response4 = responses[3];
            const response5 = responses[4];
            const response6 = responses[5];
            const response7 = responses[6];
            const response8 = responses[7];

            this.ImpactsData = response5.data;
            this.highestTvalueData = response3.data;
            this.AssetTradeValue = response2.data;
            this.News = response4.data;
            this.HHData = response6.data;
            this.QData = response7.data;
            this.TodayTepix = response1.data;
            this.TechnicalData = response8.data;
            // use/access the results
            console.log(
              response1,
              response2,
              response3,
              response4,
              response5,
              response6,
              response7,
              response8
            );
          })
        )
        .catch(errors => {
          // react on errors.
          console.error(errors);
        });
    },
    // make_requests_handler() {
    //   this.axios.all([this.request_1()]).then(
    //     this.axios.spread(
    //       // (first_response, second_response, third, fourth,fifth,sixth) => {
    //       first_response => {
    //         this.ImpactsData = first_response.data[0];
    //         this.highestTvalueData = first_response.data[1];
    //         this.AssetTradeValue = first_response.data[2];
    //         this.News = first_response.data[3];
    //         this.HHData = first_response.data[4];
    //         this.QData = first_response.data[5];
    //         this.TodayTepix = first_response.data[6];
    //         this.TechnicalData = first_response.data[7];
    //       }
    //     )
    //   );
    // },
    // request_1() {
    //   return this.axios.get("/api/Dashboard");
    // },
    loadData() {
      // this.getDashboard();
      // eslint-disable-next-line no-unused-vars
      this.getTepixToday().then(resp0 => {
        // eslint-disable-next-line no-unused-vars
        this.getTradesAll().then(resp1 => {
          // eslint-disable-next-line no-unused-vars
          this.getTradesValue().then(resp2 => {
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
            this.getTechnicalData();
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
    async getDashboard() {
      await this.axios
        .get("/api/Dashboard")
        .then(first_response => {
          this.ImpactsData = first_response.data[0];
          this.highestTvalueData = first_response.data[1];
          this.AssetTradeValue = first_response.data[2];
          this.News = first_response.data[3];
          this.HHData = first_response.data[4];
          this.QData = first_response.data[5];
          this.TodayTepix = first_response.data[6];
          this.TechnicalData = first_response.data[7];
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getImpacts() {
      if (this.ResponeseTimeout.getImpacts)
        await this.axios
          .get("/api/ImpactOnIndex", { timeout: 2000 })
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
      if (this.ResponeseTimeout.getTradesValue)
        await this.axios
          .get("/api/tse/getHighestValue", { timeout: 2000 })
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
      if (this.ResponeseTimeout.getTradesAll)
        await this.axios
          .get("/api/getAllTradesValue", { timeout: 2000 })
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
      if (this.ResponeseTimeout.getNews)
        await this.axios
          .get("/api/LatestNews", { timeout: 2000 })
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
      if (this.ResponeseTimeout.getTepixToday)
        await this.axios
          .get(
            "/api/getTodayTepix",
            { timeout: 2000 },
            {
              validateStatus: function(status) {
                console.log(status);
                return status < 500; // Resolve only if the status code is less than 500
              }
            }
          )
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
      if (this.ResponeseTimeout.getHHData)
        await this.axios
          .get("/api/HHMarketDetails", { timeout: 2000 })
          .then(getHHDataResp => {
            this.ResponeseTimeout.getHHData = false;

            console.log(getHHDataResp);
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
      if (this.ResponeseTimeout.getHighestQ)
        await this.axios
          .get("/api/HighestQ", { timeout: 2000 })
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
      if (this.ResponeseTimeout.getTechnicalData)
        await this.axios
          .get("/api/Ticker/TechnicalIndicatorsAll", { timeout: 2000 })
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
