<template>
  <div>
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <SupportTrendWidget :notices="notice"></SupportTrendWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import SupportTrendWidget from "@/view/pages/Ticker/TickerWidgets/SupportTrendWidget.vue";

// import axios from "axios";
export default {
  name: "TickerTechnicalTrend",
  components: {
    SubHeaderWidget,
    SupportTrendWidget
  },
  data() {
    return {
      subheaders: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - تحلیل تکنیکال";
  },
  mounted() {
    // this.loadData2();
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "بررسی ترند" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      // this.getAllowed().then(response => {
      //add this to package.json in developement
      //         "eslintConfig": {
      //     "rules": {
      //       "no-console": "off",
      //       "no-unused-vars": "off"
      //     }
      // },
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(response2 => {
        this.getTwo().then(function() {});
      });
      // });
    },
    // async getAllowed() {
    //   await this.axios
    //     .get("/api/tickerallnames")
    //     .then(response3 => {
    //       this.allowed = response3.data;
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
    async getTwo() {
      await this.axios
        .get("/api/Ticker/TechnicalTrends/" + this.$route.params.id + "/")
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
