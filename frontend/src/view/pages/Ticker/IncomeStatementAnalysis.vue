/* eslint-disable no-unused-vars */
<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12" style="padding-bottom:5px;padding-top:0px">
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
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
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
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "تحلیل صورت سود و زیان" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(response => {
        // eslint-disable-next-line no-unused-vars
        this.getTwo().then(responsey => {
          // eslint-disable-next-line no-unused-vars
          this.getThree();
        });
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
    async getOne() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id + "/")
        .then(response1 => {
          this.subheaders = response1.data[0];
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
