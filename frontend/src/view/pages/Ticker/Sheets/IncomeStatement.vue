<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <IncomeStatementWidget :notices="notice"></IncomeStatementWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import IncomeStatementWidget from "@/view/pages/Ticker/TickerWidgets/IncomeStatementWidget.vue";
// import axios from "axios";
export default {
  name: "Notifications",
  components: {
    SubHeaderWidget,
    IncomeStatementWidget
  },
  data() {
    return {
      subheaders: [],
      notice: [],
      typeofReport: ""
    };
  }, created() {
    document.title = "Finwise - صورت سود و زیان";
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "صورت و سود زیان خام" }]);
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
        //add this to package.json in developement
        //         "eslintConfig": {
        //     "rules": {
        //       "no-console": "off",
        //       "no-unused-vars": "off"
        //     }
        // },
        // eslint-disable-next-line no-unused-vars
        this.getTwo();
      });
    },
    async getTwo() {
      await this.axios
        .get("api/Statement/IncomeStatement/" + this.$route.params.id + "/")
        .then(response2 => {
          this.notice = response2.data;
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
