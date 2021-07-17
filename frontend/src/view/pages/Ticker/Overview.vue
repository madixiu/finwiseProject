<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 col-lg-12 col-md-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12 col-lg-12 col-md-12" style="padding-top:0px">
        <liveWidget
          :statistics="stats"
          :hh="hhdata"
          :liveData="livedata"
        ></liveWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <TechnicalWidget :Indicators="techdata"></TechnicalWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <FundamentalRobotWidget></FundamentalRobotWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <FSWidget></FSWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <VWidget></VWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <PWidget></PWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <ReturnWidget></ReturnWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <DivWidget></DivWidget>
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
import {
  SET_BREADCRUMB,
  ADD_BREADCRUMB,
  SET_BREADCRUMB_TITLE
} from "@/core/services/store/breadcrumbs.module";
// import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import liveWidget from "@/view/pages/Ticker/Rankers/liveWidget.vue";
import TechnicalWidget from "@/view/pages/Ticker/TickerWidgets/TechnicalIndicators.vue";
import FSWidget from "@/view/pages/Ticker/Rankers/FinStrengthWidget.vue";
import VWidget from "@/view/pages/Ticker/Rankers/ValuationWidget.vue";
import PWidget from "@/view/pages/Ticker/Rankers/ProfitabilityWidget.vue";
import ReturnWidget from "@/view/pages/Ticker/Rankers/ValuationReturnWidget.vue";
import DivWidget from "@/view/pages/Ticker/Rankers/DividendReturnWidget.vue";
import FundamentalRobotWidget from "@/view/pages/Ticker/Rankers/FundamentalRobotWidget.vue";
// import AnalystWidget from "@/view/pages/Ticker/Rankers/AnalystWidget.vue";
// import MoreStatisticsWidget from "@/view/pages/Ticker/Rankers/MoreInfoWidget.vue";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";

export default {
  name: "dashboard",
  components: {
    liveWidget,
    FSWidget,
    VWidget,
    PWidget,
    ReturnWidget,
    DivWidget,
    FundamentalRobotWidget,
    // AnalystWidget,
    // MoreSMtatisticsWidget,
    TechnicalWidget,
    SubHeaderWidget
  },
  data() {
    return {
      search: "",
      subheaders: {},
      // allowed: [],
      stats: [],
      hhdata: [],
      livedata: [],
      techdata: []
    };
  },
  created() {
    document.title = "Finwise - سهم";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "خلاصه سهم" }]);
  },
  mounted() {
    this.loadData();
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
    "$route.params": {
      handler(newValue, oldValue) {
        if (newValue != oldValue && oldValue != undefined) {
          this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
          this.$store.dispatch(ADD_BREADCRUMB, [{ title: "خلاصه سهم" }]);
          this.loadData();
        }
      },
      immediate: true
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(responx => {
        // eslint-disable-next-line no-unused-vars
        this.getTwo().then(responx1 => {
          // eslint-disable-next-line no-unused-vars
          this.getHH().then(responx2 => {
            // eslint-disable-next-line no-unused-vars
            this.getTechnical();
          });
        });
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
    async getTwo() {
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
    async getOne() {
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
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        // let barier = { request: "get", id: this.$route.params.id };
        // this.$socketLiveTickerData.send(JSON.stringify(barier));
      }, 3000);
    },
    liveChecker() {
      let date = new Date();
      if (date.getHours() > 8 && date.getHours() < 14) {
        this.WebsocketRequest = true;
        // this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketLiveTickerData.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
