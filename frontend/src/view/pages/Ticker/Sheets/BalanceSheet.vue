<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <BalanceSheetWidget :notices="notice"></BalanceSheetWidget>
      </div>
    </div>
  </div>
</template>
<script>
import {
  SET_BREADCRUMB,
  SET_BREADCRUMB_TITLE,
  ADD_BREADCRUMB
} from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/TickerWidgets/subHeaderWidget.vue";

import BalanceSheetWidget from "@/view/pages/Ticker/TickerWidgets/BalanceSheetWidget.vue";
export default {
  name: "BalanceSheet",
  components: {
    SubHeaderWidget,
    BalanceSheetWidget
  },
  data() {
    return {
      subheaders: [],
      notice: [],
      typeofReport: ""
    };
  },
  created() {
    document.title = "Finwise - ترازنامه";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "صورت ها" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "ترازنامه خام" }]);
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
    async loadData() {
      await this.axios
        .get("api/Statement/BalanceSheet/" + this.$route.params.id + "/", {
          headers: {
            Authorization: `bearer ${this.$store.getters.currentUserAccessToken}`
          }
        })
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getLiveTickerData() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id)
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
