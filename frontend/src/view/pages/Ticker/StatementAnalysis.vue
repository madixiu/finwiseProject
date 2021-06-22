/* eslint-disable no-unused-vars */
<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <StatementAnalysisWidget
          :IS="Inc"
          :BS="Bal"
          :CF="CashF"
        ></StatementAnalysisWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import StatementAnalysisWidget from "@/view/pages/Ticker/TickerWidgets/StatementAnalysisWidget.vue";
// import axios from "axios";
export default {
  name: "StatementAnalysis",
  components: {
    SubHeaderWidget,
    StatementAnalysisWidget
  },
  data() {
    return {
      subheaders: [],
      Inc: [],
      Bal: [],
      CashF: [],
      typeofReport: ""
    };
  },
  created() {
    document.title = "Finwise - تحلیل صورتهای مالی";
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "تحلیل صورت" }]);
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
          this.getThree().then(responsex => {
            this.getFour();
          });
        });
      });
    },
    async getTwo() {
      await this.axios
        .get("api/Statement/IncomeStatement/" + this.$route.params.id + "/")
        .then(response3 => {
          this.Inc = response3.data;
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
    async getFour() {
      await this.axios
        .get("api/Statement/CashFlow/" + this.$route.params.id + "/")
        .then(response2 => {
          this.CashF = response2.data;
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
