<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12 col-lg-12 col-md-12" style="padding-bottom:0px">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12 col-lg-12 col-md-12" style="padding-top:5px">
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
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
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
        if (newValue != oldValue) {
          this.loadData();
          this.$store.dispatch(SET_BREADCRUMB, [{ title: "خلاصه سهم" }]);
        }
      },
      immediate: true
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      // this.getAllowed().then(response => {
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
      // });
    },
    // async getAllowed() {
    //   await this.axios
    //     .get("/api/tickerallnames")
    //     .then(response3 => {
    //       this.allowed = response3.data;
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
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
    // async getLiveData() {
    //   await this.axios
    //     .get("/api/LiveTicker/" + this.$route.params.id + "/")
    //     .then(response3 => {
    //       this.livedata = response3.data;
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
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
        .then(response1 => {
          this.subheaders = response1.data[0];

          this.livedata = response1.data;
          // this.$store.dispatch(SET_BREADCRUMB, [{ title: "خلاصه سهم" }]);

          this.$store.dispatch(ADD_BREADCRUMB, [
            { title: this.subheaders.ticker }
          ]);
          // console.log(this.$store.getters.breadcrumbs);
          // console.log(this.$store.getters.pageTitle);
        })
        .catch(error => {
          console.error(error);
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
    },
    // %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get", id: this.$route.params.id };
        this.$socketLiveTickerData.send(JSON.stringify(barier));
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
    let barier = { request: "halt" };
    this.$socketLiveTickerData.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
