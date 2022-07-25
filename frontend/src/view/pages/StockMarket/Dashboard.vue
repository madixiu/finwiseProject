<template>
  <div class="row pt-1">
    <div class="col-xxl-9 col-lg-9 col-md-12 col-sm-12">
      <IndexChart
        :inputDataIndex="TodayTepix"
        :inputDataNetHH="TodayNetHaghighi"
        class="pb-1"
      ></IndexChart>
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
        <AdvancingWidgetTotal :inputData="advancing"></AdvancingWidgetTotal>
        <ChartTradeValue :inputDataTV="AssetTradeValue"></ChartTradeValue>
        <Technical :inputDataTechnical="TechnicalData"></Technical>
        <WinnerLosers :inputWinLose="WinLose"></WinnerLosers>
        <AdvancingWidget
          :inputDataInd="advancingInd"
          class="pb-7"
        ></AdvancingWidget>
      </div>
    </div>
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
import WinnerLosers from "@/view/pages/StockMarket/StockMarketWidgets/WinnerLosersWidget.vue";
// import IndicesText from "@/view/pages/StockMarket/StockMarketWidgets/DashboardIndicesText.vue";
import IndexChart from "@/view/pages/StockMarket/StockMarketWidgets/IndexChart.vue";
import AdvancingWidget from "@/view/pages/StockMarket/StockMarketWidgets/AdvancingWidget.vue";
import AdvancingWidgetTotal from "@/view/pages/StockMarket/StockMarketWidgets/AdvancingWidgetTotal.vue";
export default {
  name: "Dashboard",
  components: {
    ChartVol,
    ChartHH,
    ChartTradeValue,
    ChartIndustires,
    WinnerLosers,
    // // IndicesText,
    IndexChart,
    Technical,
    AdvancingWidget,
    AdvancingWidgetTotal
    // HighestSupply
  },
  data() {
    return {
      highestTvalueData: [],
      AssetTradeValue: [],
      TodayTepix: [],
      TodayNetHaghighi: [],
      News: [],
      ImpactsData: [],
      IndustryHHData: [],
      IndustryImpact: [],
      HHData: [],
      QData: [],
      mostviewed: [],
      TechnicalData: [],
      WebsocketRequest: false,
      interval: null,
      WinLose: [],
      advancingInd: [],
      advancing: []
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
    // this.loadDataNew();
    this.loadData();

    // this.getTepixToday().then(resp0 => {

    // });
  },
  mounted() {
    // this.loadData();
    this.liveChecker();
  },
  methods: {
    // loadDataNew() {
    //   const getTepixToday = this.axios.get("/api/getTodayTepix");
    //   const getNetHaghighiToday = this.axios.get("/api/getTodayNetHaghighi");
    //   const getTradesAll = this.axios.get("/api/getAllTradesValue");
    //   const getTechnicalData = this.axios.get(
    //     "/api/Ticker/TechnicalIndicatorsAll"
    //   );
    //   const getImpacts = this.axios.get("/api/ImpactOnIndex");
    //   const getHHData = this.axios.get("/api/HHMarketDetails");
    //   const getHighestQ = this.axios.get("/api/HighestQ");
    //   const getTradesValue = this.axios.get("/api/getHighestValue");
    //   const getIndustryImpacts = this.axios.get("/api/Indices/Impact");
    //   const getIndustryHH = this.axios.get("/api/Indices/HH");
    //   // this.axios
    //   //   .all([
    //   //     getTepixToday,
    //   //     getNetHaghighiToday,
    //   //     // getTradesAll,
    //   //     // getTechnicalData,
    //   //     // getImpacts,
    //   //     // getHHData,
    //   //     // getHighestQ,
    //   //     // getTradesValue,
    //   //     // getIndustryImpacts,
    //   //     // getIndustryHH
    //   //   ])
    //   //   .then(
    //   //     this.axios.spread((...responses) => {
    //   //       this.TodayTepix = responses[0].data;
    //   //       this.TodayNetHaghighi = responses[1].data;
    //   //       // this.AssetTradeValue = responses[3].data;
    //   //       // this.TechnicalData = responses[4].data;
    //   //       // this.ImpactsData = responses[4].data;
    //   //       // this.HHData = responses[5].data;
    //   //       // this.QData = responses[6].data;
    //   //       // this.highestTvalueData = responses[7].data;
    //   //       // this.IndustryImpact = responses[8].data;
    //   //       // this.IndustryHHData = responses[9].data;
    //   //       // this.loadData2();
    //   //       // use/access the results
    //   //     })
    //   //   )
    //   //   .catch(errors => {
    //   //     console.error(errors);
    //   //     // react on errors.
    //   //   });
    // },
    loadData() {
      this.getTepixToday().then(resp0 => {
        this.getTodayAdvancingDescending().then(resp1 => {
          this.getTradesAll().then(resp2 => {
            this.getTechnicalData().then(respX => {
              this.loadData2();
            });
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
                this.getIndustryHH().then(resp9 => {
                  this.getNetHH().then(resp9 => {
                    this.loadData3();
                  });
                });
              });
            });
          });
        });
      });
    },

    loadData3() {
      this.getWinnersLosers().then(resp10 => {
        this.getTodayAdvancingDescendingIndustries();
      });
    },
    async getImpacts() {
      await this.axios
        .get("/api/ImpactOnIndex")
        .then(getImpactsResp => {
          this.ImpactsData = getImpactsResp.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getWinnersLosers() {
      await this.axios
        .get("/api/getTodayWinnersLosers")
        .then(getWLData => {
          this.WinLose = getWLData.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getNetHH() {
      await this.axios
        .get("/api/getTodayNetHaghighi")
        .then(getNetHD => {
          this.TodayNetHaghighi = getNetHD.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTodayAdvancingDescending() {
      await this.axios
        .get("/api/getTodayAdvancingDescending")
        .then(getAd => {
          this.advancing = getAd.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },

    async getTodayAdvancingDescendingIndustries() {
      await this.axios
        .get("/api/getTodayAdvancingDescendingIndustries")
        .then(getAdInd => {
          this.advancingInd = getAdInd.data;
          return true;
        })
        .catch(error => {
          console.error(error);
        });
    },

    async getIndustryImpacts() {
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
    async getIndustryHH() {
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
    async getTradesValue() {
      this.axios
        .get("/api/getHighestValue")
        .then(getTradesValueResp => {
          this.highestTvalueData = getTradesValueResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTradesAll() {
      this.axios
        .get("/api/getAllTradesValue")
        .then(getTradesAllResp => {
          this.AssetTradeValue = getTradesAllResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getNews() {
      this.axios
        .get("/api/LatestNews")
        .then(getNewsResp => {
          this.News = getNewsResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTepixToday() {
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
    async getHHData() {
      this.axios
        .get("/api/HHMarketDetails")
        .then(getHHDataResp => {
          this.HHData = getHHDataResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getHighestQ() {
      this.axios
        .get("/api/HighestQ")
        .then(getHighestQResp => {
          this.QData = getHighestQResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTechnicalData() {
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
