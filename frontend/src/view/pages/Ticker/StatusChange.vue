/* eslint-disable no-unused-vars */
<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12 col-lg-12 col-md-12 col-xs-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-3 col-xs-12"></div>
      <div class="col-xxl-4 col-lg-4 col-md-6 col-xs-12">
        <StatusChangesWidget :notices="notice"></StatusChangesWidget>
      </div>
      <div class="col-xxl-4 col-lg-4 col-md-3 col-xs-12"></div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import StatusChangesWidget from "@/view/pages/Ticker/TickerWidgets/StatusChangeWidget.vue";
// import axios from "axios";
export default {
  name: "Notifications",
  components: {
    SubHeaderWidget,
    StatusChangesWidget
  },
  data() {
    return {
      allowed: [],
      subheaders: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - تغییر وضعیت سهم";
  },
  mounted() {
    // this.loadData2();
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "تغییر وضعیت سهم" }]);
  },
  watch: {
    subheaders() {
      this.$store.dispatch(ADD_BREADCRUMB, [{ title: this.subheaders.ticker }]);
    }
  },
  methods: {
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getOne().then(response2 => {
        this.getTwo();
      });
    },
    async getTwo() {
      await this.axios
        .get("/api/StatusChanges/" + this.$route.params.id + "/")
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
