<template>
  <div class="row pt-1">
    <div class="col-xxl-9 col-lg-9 col-md-12 col-sm-12">
      <IndexChart :inputDataIndex="TodayTepix" class="pb-1"></IndexChart>
      <ChartVol
        :inputDataStatus="highestTvalueData"
        :inputDataImpact="ImpactsData"
        class="pb-2 pt-1"
      ></ChartVol>
      <ChartHH :inputDataHH="HHData" :inputDataQ="QData"></ChartHH>
      <ChartIndustires
        class="pb-2"
        :inpuDataIndustryHH="IndustryHHData"
        :inputDataIndustryImpact="IndustryImpact"
      ></ChartIndustires>
    </div>
    <div class="col-xxl-3 col-lg-3 col-md-12 col-sm-12">
      <div class="row">
        <ChartTradeValue :inputDataTV="AssetTradeValue"></ChartTradeValue>
        <Technical :inputDataTechnical="TechnicalData"></Technical>
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
/* eslint-disable no-unused-vars */
// import MostViewedWidget from "@/view/pages/StockMarket/StockMarketWidgets/MostViewed.vue";
import Technical from "@/view/pages/StockMarket/StockMarketWidgets/TechnicalHighest.vue";
import ChartVol from "@/view/pages/StockMarket/StockMarketWidgets/DashboardChart.vue";
import ChartHH from "@/view/pages/StockMarket/StockMarketWidgets/HH_Q_Chart.vue";
import ChartTradeValue from "@/view/pages/StockMarket/StockMarketWidgets/TradesValueChart.vue";
import ChartIndustires from "@/view/pages/StockMarket/StockMarketWidgets/IndustryChartsForDashboard.vue";
// import IndicesText from "@/view/pages/StockMarket/StockMarketWidgets/DashboardIndicesText.vue";
import IndexChart from "@/view/pages/StockMarket/StockMarketWidgets/IndexChart.vue";
export default {
  name: "Dashboard",
  components: {
    ChartVol,
    ChartHH,
    ChartTradeValue,
    ChartIndustires,
    // // IndicesText,
    IndexChart,
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
      IndustryHHData: [],
      IndustryImpact: [],
      HHData: [],
      QData: [],
      mostviewed: [],
      TechnicalData: [],
      WebsocketRequest: false,
      interval: null
    };
  },
  watch: {
    $route() {
      if (this.$route.name != "Dashboard") {
        clearInterval(this.interval);
        this.WebsocketRequest = false;
      }
    }
  },
  created() {
    document.title = "FinWise - سهام";
    this.loadDataNew();
    // this.loadData();
  },
  mounted() {
    this.liveChecker();
  },
  methods: {
    loadDataNew() {
      const getTepixToday = this.axios.get("/api/getTodayTepix");
      const getTradesAll = this.axios.get("/api/getAllTradesValue");
      const getTechnicalData = this.axios.get(
        "/api/Ticker/TechnicalIndicatorsAll"
      );
      const getImpacts = this.axios.get("/api/ImpactOnIndex");
      const getHHData = this.axios.get("/api/HHMarketDetails");
      const getHighestQ = this.axios.get("/api/HighestQ");
      const getTradesValue = this.axios.get("/api/getHighestValue");
      const getIndustryImpacts = this.axios.get("/api/Indices/Impact");
      const getIndustryHH = this.axios.get("/api/Indices/HH");
      this.axios
        .all([
          getTepixToday,
          getTradesAll,
          getTechnicalData,
          getImpacts,
          getHHData,
          getHighestQ,
          getTradesValue,
          getIndustryImpacts,
          getIndustryHH
        ])
        .then(
          this.axios.spread((...responses) => {
            this.TodayTepix = responses[0].data;
            this.AssetTradeValue = responses[1].data;
            this.TechnicalData = responses[2].data;
            this.ImpactsData = responses[3].data;
            this.HHData = responses[4].data;
            this.QData = responses[5].data;
            this.highestTvalueData = responses[6].data;
            this.IndustryImpact = responses[7].data;
            this.IndustryHHData = responses[8].data;
            // this.loadData2();
            // use/access the results
          })
        )
        .catch(errors => {
          console.error(errors);
          // react on errors.
        });
    },
    loadData() {
      // this.getDashboard();
      this.getTepixToday().then(resp0 => {
        this.getTradesAll().then(resp1 => {
          this.getTechnicalData().then(resp2 => {
            // this.getNews();
            this.loadData2();

            // this.getNews().then(resp3 => {
            // });
          });
        });
      });
    },
    loadData2() {
      this.getImpacts().then(resp4 => {
        this.getHHData().then(resp5 => {
          this.getHighestQ().then(resp6 => {
            this.getTradesValue().then(resp7 => {
              this.getIndustryImpacts().then(resp8 => {
                this.getIndustryHH();
              });
            });
          });
        });
      });
    },
    getImpacts() {
      this.axios
        .get("/api/ImpactOnIndex")
        .then(getImpactsResp => {
          this.ImpactsData = getImpactsResp.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },

    getIndustryImpacts() {
      this.axios
        .get("/api/Indices/Impact")
        .then(getIndustryImpact => {
          this.IndustryImpact = getIndustryImpact.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getIndustryHH() {
      // console.log('Req')
      this.axios
        .get("/api/Indices/HH")
        .then(getIndustryHHData => {
          this.IndustryHHData = getIndustryHHData.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getTradesValue() {
      this.axios
        .get("/api/getHighestValue")
        .then(getTradesValueResp => {
          this.highestTvalueData = getTradesValueResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getTradesAll() {
      this.axios
        .get("/api/getAllTradesValue")
        .then(getTradesAllResp => {
          this.AssetTradeValue = getTradesAllResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getNews() {
      this.axios
        .get("/api/LatestNews")
        .then(getNewsResp => {
          this.News = getNewsResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getTepixToday() {
      this.axios
        .get("/api/getTodayTepix")
        .then(getTepixTodayResp => {
          this.TodayTepix = getTepixTodayResp.data;
        })
        .catch(error => {
          console.error(error);
          // the request has either been canceled due to a network timeout,
          // or because the device is offline
        });
    },
    getHHData() {
      this.axios
        .get("/api/HHMarketDetails")
        .then(getHHDataResp => {
          this.HHData = getHHDataResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getHighestQ() {
      this.axios
        .get("/api/HighestQ")
        .then(getHighestQResp => {
          this.QData = getHighestQResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getTechnicalData() {
      this.axios
        .get("/api/Ticker/TechnicalIndicatorsAll")
        .then(getTechnicalDataResp => {
          this.TechnicalData = getTechnicalDataResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },

    //? %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      this.interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(this.interval._id);
          return;
        }
        // let barier = {
        //   request: "get",
        //   data: {
        //     marketName: this.tableMarketSelected,
        //     marketIndustry: this.tableMarketIndustrySelected
        //   }
        // };
        // this.$socketMarketWatch.send(JSON.stringify(barier));
        this.loadData();
      }, 120000);
    },
    liveChecker() {
      let date = new Date();
      if (
        date.getHours() > 8 &&
        date.getHours() < 14 &&
        date.getDay() != 5 &&
        date.getDay() != 4
      ) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    //? %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    // setActiveTab1(event) {
    //   this.tabIndex = this.setActiveTab(event);
    // },
    // setActiveTab2(event) {
    //   this.tabIndex2 = this.setActiveTab(event);
    // },
    // /**
    //  * Set current active on click
    //  * @param event
    //  */
    // setActiveTab(event) {
    //   // get all tab links
    //   const tab = event.target.closest('[role="tablist"]');
    //   const links = tab.querySelectorAll(".nav-link");
    //   // remove active tab links
    //   for (let i = 0; i < links.length; i++) {
    //     links[i].classList.remove("active");
    //   }

    //   // set current active tab
    //   event.target.classList.add("active");

    //   // set clicked tab index to bootstrap tab
    //   return parseInt(event.target.getAttribute("data-tab"));
    // }
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
