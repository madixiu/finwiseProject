<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <IncomeStatementAnalysisWidget
          :IS="IncS"
          :ISAGG="IncAG"
        ></IncomeStatementAnalysisWidget>
      </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable no-unused-vars */
import {
  SET_BREADCRUMB,
  SET_BREADCRUMB_TITLE,
  ADD_BREADCRUMB
} from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/TickerWidgets/subHeaderWidget.vue";

import IncomeStatementAnalysisWidget from "@/view/pages/Ticker/TickerWidgets/IncomeStatementAnalysisWidget.vue";
export default {
  name: "IncomeStatementAnalysis",
  components: {
    SubHeaderWidget,
    IncomeStatementAnalysisWidget
  },
  data() {
    return {
      subheaders: [],
      IncS: [],
      IncAG: []
    };
  },
  created() {
    document.title = "Finwise - تحلیل صورتهای مالی";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "صورت ها" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "تحلیل صورت سود و زیان" }]);
    if (this.$store.getters.getLiveTickerData != null) {
      this.subheaders = this.$store.getters.getLiveTickerData;
      this.loadData();
    } else {
      this.getLiveTickerData().then(Response => {
        this.loadData();
      });
    }
  },
  methods: {
    loadData() {
      this.getTwo().then(responsey => {
        this.getThree();
      });
    },
    async getTwo() {
      await this.axios
        .get(
          "api/Statement/IncomeStatementAggregated/" +
            this.$route.params.id +
            "/"
        )
        .then(response3 => {
          this.IncAG = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getThree() {
      await this.axios
        .get("api/Statement/IncomeStatement/" + this.$route.params.id + "/")
        .then(response4 => {
          this.IncS = response4.data;
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
