<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-6">
        <DPSWidget :notices="notice"></DPSWidget>
      </div>
      <div class="col-xxl-6">
        <ICWidget :notices="deposits"></ICWidget>
      </div>
    </div>
  </div>
</template>

<script>
import {
  SET_BREADCRUMB,
  ADD_BREADCRUMB,
  SET_BREADCRUMB_TITLE
} from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import DPSWidget from "@/view/pages/Ticker/AssemblyWidget/AssemblyDPSWidget.vue";
import ICWidget from "@/view/pages/Ticker/AssemblyWidget/AssemblyICwidget.vue";
export default {
  name: "TickerAssemblyDPSAndIC",
  components: {
    SubHeaderWidget,
    DPSWidget,
    ICWidget
  },
  data() {
    return {
      //// allowed: [],
      subheaders: [],
      deposits: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - DPS و EPS";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "مجامع" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [
      { title: "سود نقدی و افزایش سرمایه" }
    ]);
     if (this.$store.getters.getLiveTickerData != null) {
      this.subheaders = this.$store.getters.getLiveTickerData;
    } else {
      // eslint-disable-next-line no-unused-vars
      this.getLiveTickerData().then(Response => {
        this.loadData();
      });
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getThree().then(response2 => {
        this.getTwo();
      });
    },
    async getTwo() {
      await this.axios
        .get("/api/Alldps/" + this.$route.params.id + "/")
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getThree() {
      await this.axios
        .get("/api/LatestICDone/" + this.$route.params.id + "/")
        .then(responsex => {
          this.deposits = responsex.data;
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
          this.$store.dispatch("SetLiveTickerData", this.subheaders);
          this.$store.dispatch("SetLiveTickerID", this.subheaders.ID);
          this.$store.dispatch(SET_BREADCRUMB_TITLE, this.subheaders.ticker);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
