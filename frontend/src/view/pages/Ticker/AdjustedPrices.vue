<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <AdjustedPricesWidget :adjusted="adjustedprices"></AdjustedPricesWidget>
      </div>
    </div>
  </div>
</template>
<script>
import {
  SET_BREADCRUMB,
  SET_BREADCRUMB_TITLE
} from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import AdjustedPricesWidget from "@/view/pages/Ticker/TickerWidgets/AdjustedPricesWidget.vue";
export default {
  name: "AdjustedPrices",
  components: {
    SubHeaderWidget,
    AdjustedPricesWidget
  },
  data() {
    return {
      subheaders: [],
      adjustedprices: []
    };
  },
  created() {
    document.title = "Finwise - سابقه قیمت تعدیلی";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "سابقه قیمت" }]);
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
        .get("/api/AdjustedPricesCodal/" + this.$route.params.id + "/")
        .then(responsePrice => {
          this.adjustedprices = responsePrice.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
