<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12 col-lg-12 col-md-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12 col-lg-12 col-md-12">
        <liveWidget :statistics="stats"></liveWidget>
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
      <div class="col-xxl-4 col-lg-4 col-md-4">
        <MoreStatisticsWidget></MoreStatisticsWidget>
      </div>
      <div class="col-xxl-12 col-lg-12 col-md-12">
        <AnalystWidget></AnalystWidget>
      </div>
    </div>
    <!--end::Dashboard-->
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import liveWidget from "@/view/pages/Ticker/Rankers/liveWidget.vue";
import FSWidget from "@/view/pages/Ticker/Rankers/FinStrengthWidget.vue";
import VWidget from "@/view/pages/Ticker/Rankers/ValuationWidget.vue";
import PWidget from "@/view/pages/Ticker/Rankers/ProfitabilityWidget.vue";
import ReturnWidget from "@/view/pages/Ticker/Rankers/ValuationReturnWidget.vue";
import DivWidget from "@/view/pages/Ticker/Rankers/DividendReturnWidget.vue";
import AnalystWidget from "@/view/pages/Ticker/Rankers/AnalystWidget.vue";
import MoreStatisticsWidget from "@/view/pages/Ticker/Rankers/MoreInfoWidget.vue";
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
    AnalystWidget,
    MoreStatisticsWidget,
    SubHeaderWidget
  },
  data() {
    return {
      search: "",
      subheaders: [],
      allowed: [],
      stats: []
    };
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "خلاصه سهم" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
      // console.log(this.notices);
    },
    "$route.params": {
      handler(newValue, oldValue) {
        console.log(newValue);
        console.log(oldValue);

        if (newValue != oldValue) {
          this.loadData();
          this.$store.dispatch(SET_BREADCRUMB, [{ title: "خلاصه سهم" }]);
        }

        // const { userName } = newValue

        // this.fetchData(userName)
      },
      immediate: true
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getAllowed().then(response => {
        // eslint-disable-next-line no-unused-vars
        this.getOne().then(response2 => {
          this.getTwo().then(function() {});
        });
      });
    },
    async getAllowed() {
      await this.axios
        .get("/api/tickerallnames")
        .then(response3 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.allowed = response3.data;
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getTwo() {
      await this.axios
        .get("/api/StatsTicker/" + this.$route.params.id + "/")
        .then(response2 => {
          // console.log(response.data[0][0]);
          // console.log(this.$route.params.id);
          // console.log("SecondDone");
          this.stats = response2.data;
          // console.log(response2.data);
          // console.log("GetTwoStart:");
          // console.log(response.data);
          // console.log(this.notice);
          // console.log("GetTwoEnd:");
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getOne() {
      await this.axios
        .get("/api/SubHeaderW/" + this.$route.params.id + "/")
        .then(response1 => {
          // console.log("firstDone");
          this.subheaders = response1.data[0];
          // console.log(response1.data);
        })
        .catch(error => {
          // console.log("GetOneCatch");
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
