<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <TechnicalWidget :notices="notice"></TechnicalWidget>
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
import TechnicalWidget from "@/view/pages/Ticker/TickerWidgets/TechnicalIndicatorsDetailsWidget.vue";
export default {
  name: "TechnicalMoreInfo",
  components: {
    SubHeaderWidget,
    TechnicalWidget
  },
  data() {
    return {
      allowed: [],
      subheaders: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - تحلیل تکنیکال";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "تکنیکال سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "بررسی اندیکاتورها" }]);
    if (this.$store.getters.getLiveTickerData != null) {
      this.subheaders = this.$store.getters.getLiveTickerData;
      this.loadData();
    } else {
      // eslint-disable-next-line no-unused-vars
      this.getLiveTickerData().then(Response => {
        this.loadData();
      });
    }
  },
  methods: {
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
    },
    async loadData() {
      await this.axios
        .get(
          "/api/Ticker/TechnicalIndicatorSingle/" + this.$route.params.id + "/"
        )
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
    //// loadData() {
    // ///eslint-disable-next-line no-unused-vars
    // ///this.getOne().then(response2 => {
    // ///  this.getTwo().then(function() {});
    // ///});
    // ///});
    // ///},
    // ///async getAllowed() {
    // ///  await this.axios
    // ///    .get("/api/tickerallnames")
    // ///    .then(response3 => {
    // ///      this.allowed = response3.data;
    // ///    })
    // ///    .catch(error => {
    // ///      console.error(error);
    // ///    });
    // ///},
  }
};
</script>
