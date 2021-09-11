<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 col-lg-12 col-md-12 pt-3 pb-1">
        <SubHeaderWidget
          :tickerdata="subheaders"
          :ComponentData="componentdata"
        ></SubHeaderWidget>
      </div>
      <div class="col-xxl-12 col-lg-12 col-md-12" style="padding-top:0px">
        <liveWidget2
          :liveData="livedata"
          :Indicators="techdata"
          :FundamentalRobot="FundamentalRobot"
          :priceHistory="priceHistory"
        ></liveWidget2>
      </div>
      <!-- <div class="col-xxl-12 col-lg-12 col-md-12" style="padding-top:0px">
        <liveWidget
          :statistics="stats"
          :hh="hhdata"
          :liveData="livedata"
        ></liveWidget>
      </div> -->
      <!-- <div class="col-xxl-4 col-lg-4 col-md-4">
        <FundamentalRobotWidget
          :liveData="livedata"
          :FundamentalRobot="FundamentalRobot"
        ></FundamentalRobotWidget>
      </div> -->
      <!-- <div class="col-xxl-4 col-lg-4 col-md-4">
        <FundamentalRobotWidget></FundamentalRobotWidget>
      </div> -->
      <div class="col-xxl-12 col-lg-12 col-md-12" style="padding-top:0px">
        <v-row no-gutters class="d-flex flex-row justify-content-between">
          <v-col cols="4" class="flex-grow-1 flex-shrink-0 pl-1">
            <FSWidget :RatioData="ratiodata"></FSWidget>
            <v-col class="px-0">
              <DivWidget :RatioData="ratiodata"></DivWidget>
            </v-col>
            <v-col class="px-0">
              <ReturnWidget :RatioData="FundamentalRobot" :liveData="livedata"></ReturnWidget>
            </v-col>
          </v-col>
          <v-col cols="4" class="flex-grow-1 flex-shrink-0 pl-1">
            <VWidget
              :LiveData="livedata"
              :RatioData="ratiodata"
              :ComponentData="componentdata"
            ></VWidget>

            <v-col class="px-0">
              <PWidget :RatioData="ratiodata"></PWidget>
            </v-col>
          </v-col>
          <v-col cols="4" class="flex-grow-1 flex-shrink-0 pl-1">
            <AIWidget
              :PredictionData="predictiondata"
              :priceHistory="priceHistory"
            ></AIWidget>
          </v-col>
        </v-row>
      </div>

      <!-- <div class="col-xxl-4 col-lg-4 col-md-4">
        <MoreStatisticsWidget></MoreStatisticsWidget>
      </div>
      <div class="col-xxl-8 col-lg-8 col-md-8">
        <AnalystWidget></AnalystWidget>
      </div> -->
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
/* eslint-disable no-unused-vars */
import {
  SET_BREADCRUMB,
  ADD_BREADCRUMB,
  SET_BREADCRUMB_TITLE
} from "@/core/services/store/breadcrumbs.module";
// import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import liveWidget from "@/view/pages/Ticker/Rankers/liveWidget.vue";
import liveWidget2 from "@/view/pages/Ticker/TickerWidgets/liveWidget2.vue";
// import TechnicalWidget from "@/view/pages/Ticker/TickerWidgets/TechnicalIndicators.vue";
import FSWidget from "@/view/pages/Ticker/Rankers/FinStrengthWidget.vue";
import VWidget from "@/view/pages/Ticker/Rankers/ValuationWidget.vue";
import PWidget from "@/view/pages/Ticker/Rankers/ProfitabilityWidget.vue";
import ReturnWidget from "@/view/pages/Ticker/Rankers/ValuationReturnWidget.vue";
import DivWidget from "@/view/pages/Ticker/Rankers/DividendReturnWidget.vue";
import AIWidget from "@/view/pages/Ticker/TickerWidgets/OneWeekPredictionWidget.vue";
// import FundamentalRobotWidget from "@/view/pages/Ticker/TickerWidgets/FundamentalRobotWidget.vue";

// import AnalystWidget from "@/view/pages/Ticker/Rankers/AnalystWidget.vue";
// import MoreStatisticsWidget from "@/view/pages/Ticker/Rankers/MoreInfoWidget.vue";
// import SubHeaderWidget from "@/view/pages/Ticker/TickerWidgets/subHeaderWidget.vue";

import SubHeaderWidget from "@/view/pages/Ticker/TickerWidgets/subHeaderWidget.vue";

export default {
  name: "TickerOverall",
  components: {
    // liveWidget,
    liveWidget2,
    FSWidget,
    VWidget,
    PWidget,
    ReturnWidget,
    DivWidget,
    AIWidget,
    // FundamentalRobotWidget,

    // AnalystWidget,
    // MoreSMtatisticsWidget,
    // TechnicalWidget,
    // SubHeaderWidget,
    SubHeaderWidget
  },
  data() {
    return {
      subheaders: {},
      stats: [],
      hhdata: [],
      livedata: [],
      techdata: [],
      ratiodata: [],
      componentdata: [],
      FundamentalRobot: [],
      predictiondata: [],
      priceHistory: [],
      interval: null
    };
  },
  created() {
    document.title = "Finwise - سهم";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "خلاصه سهم" }]);
    this.loadData();
  },
  mounted() {
    this.liveChecker();
    // this.$socketLiveTickerData.onmessage = data => {

    //   if (JSON.parse(data.data) != "noData" || !!JSON.parse(data.data).length) {
    //     this.subheaders = JSON.parse(data.data)[0][0];
    //     this.livedata = JSON.parse(data.data)[0];
    //     this.hhdata = JSON.parse(data.data)[1];
    //   }

    //   // this.loading = false;
    // };
  },
  watch: {
    $route() {
      if (this.$route.name != "TickerOverall") {
        clearInterval(this.interval);
        this.WebsocketRequest = false;
      }
    },
    "$route.params": {
      handler(newValue, oldValue) {
        if (newValue != oldValue && oldValue != undefined) {
          this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
          this.$store.dispatch(ADD_BREADCRUMB, [{ title: "خلاصه سهم" }]);
          this.subheaders = {};
          this.stats = [];
          this.hhdata = [];
          this.livedata = [];
          this.techdata = [];
          this.ratiodata = [];
          this.componentdata = [];
          this.FundamentalRobot = [];
          this.predictiondata = [];
          this.priceHistory = [];
          this.loadData();
        }
      },
      immediate: true
    }
  },
  methods: {
    loadData() {
      this.getLiveTickerData().then(getLiveTickerDataresponse => {
        // this.getTickerStats().then(responx1 => {
        // this.getHH().then(responx2 => {
        this.getPriceHistory().then(getPriceHistoryresponse => {
          this.getTechnical().then(getTechnicalresponse => {
            this.getBonyadi().then(getBonyadiRespose => {
              this.getRatios().then(getRatioRespnse => {
                this.getPredictionData().then(getRatioRespnse => {
                  this.getComponentData();
                });
              });
            });
          });
        });
        // });
        // });
      });
    },
    async getPriceHistory() {
      await this.axios
        .get("/api/AdjustedPricesCodal/" + this.$route.params.id + "/")
        .then(responsePrice => {
          this.priceHistory = responsePrice.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getBonyadi() {
      await this.axios
        .get("/api/Fundamental/ValuationRatio/" + this.$route.params.id + "/")
        .then(getBonyadiResp => {
          this.FundamentalRobot = getBonyadiResp.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getHH() {
      await this.axios
        .get("/api/LiveHHTicker/" + this.$route.params.id + "/")
        .then(response3 => {
          this.hhdata = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },

    async getTickerStats() {
      await this.axios
        .get("/api/StatsTicker/" + this.$route.params.id + "/")
        .then(response2 => {
          this.stats = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getTechnical() {
      await this.axios
        .get("/api/Ticker/TechnicalIndicators/" + this.$route.params.id + "/")
        .then(responsetech => {
          this.techdata = responsetech.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getRatios() {
      await this.axios
        .get(
          "/api/Fundamental/Ratios/RatioToDisplay/" +
            this.$route.params.id +
            "/"
        )
        .then(responseratio => {
          this.ratiodata = responseratio.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getLiveTickerData() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id + "/")
        .then(LiveTickerResponse => {
          this.subheaders = LiveTickerResponse.data[0];
          this.livedata = LiveTickerResponse.data;
          this.$store.dispatch("SetLiveTickerData", this.subheaders);
          this.$store.dispatch("SetLiveTickerID", this.subheaders.ID);
          this.$store.dispatch(SET_BREADCRUMB_TITLE, this.subheaders.ticker);
        })
        .catch(error => {
          console.error(error);
        });
    },

    async getComponentData() {
      await this.axios
        .get(
          "/api/Fundamental/Ratios/LatestComponents/" +
            this.$route.params.id +
            "/"
        )
        .then(responsec => {
          this.componentdata = responsec.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getPredictionData() {
      await this.axios
        .get("/api/AI/OneWeekStockPrediction/" + this.$route.params.id + "/")
        .then(responsep => {
          this.predictiondata = responsep.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        // let barier = { request: "get", id: this.$route.params.id };
        // this.$socketLiveTickerData.send(JSON.stringify(barier));
        this.getLiveTickerData();
      }, 6000);
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
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketMarketWatch.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
    clearInterval(this.interval);
  }
};
</script>
