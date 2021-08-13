/* eslint-disable no-unused-vars */
<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <StatementAnalysisWidget
          :BS="Bal"
          :BSAGG="BalAg"
        ></StatementAnalysisWidget>
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

import StatementAnalysisWidget from "@/view/pages/Ticker/TickerWidgets/StatementAnalysisWidget.vue";
export default {
  name: "StatementAnalysis",
  components: {
    SubHeaderWidget,
    StatementAnalysisWidget
  },
  data() {
    return {
      subheaders: [],
      Bal: [],
      BalAg: []
    };
  },
  created() {
    document.title = "Finwise - تحلیل صورتهای مالی";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "صورت ها" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "تحلیل ترازنامه" }]);
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
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getTwo().then(responsey => {
        // eslint-disable-next-line no-unused-vars
        this.getThree();
      });
    },
    async getTwo() {
      await this.axios
        .get(
          "api/Statement/BalanceSheetAggregated/" + this.$route.params.id + "/"
        )
        .then(response3 => {
          this.BalAg = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getThree() {
      await this.axios
        .get("api/Statement/BalanceSheet/" + this.$route.params.id + "/")
        .then(response4 => {
          this.Bal = response4.data;
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
