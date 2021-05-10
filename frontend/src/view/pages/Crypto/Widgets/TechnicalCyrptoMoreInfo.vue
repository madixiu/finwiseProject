<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <TechnicalWidget :notices="notice"></TechnicalWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
// import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import TechnicalWidget from "@/view/pages/Ticker/TickerWidgets/TechnicalIndicatorsDetailsWidget.vue";
// import axios from "axios";
export default {
  name: "Notifications",
  components: {
    TechnicalWidget
  },
  data() {
    return {
      allowed: [],
      subheaders: [],
      notice: []
    };
  }, created() {
    document.title = "Finwise - تحلیل تکنیکال";
  },
  mounted() {
    // this.loadData2();
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "بررسی اندیکاتورها" }]);
  },
  watch: {
  },
  methods: {
    loadData() {
        this.getTwo().then(function() {});
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
        .get(
          "/api/Crypto/TechnicalIndicatorSingle/" + this.$route.params.id + "/"
        )
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
