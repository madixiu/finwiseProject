<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <AdminNoticeWidget :notices="notice"></AdminNoticeWidget>
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

import AdminNoticeWidget from "@/view/pages/Ticker/TickerWidgets/AdministrationNoticeWidget.vue";
export default {
  name: "Administration",
  components: {
    SubHeaderWidget,
    AdminNoticeWidget
  },
  data() {
    return {
      subheaders: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - پیام ناظر";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "پیام ناظر" }]);
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

  mounted() {
    // this.loadData();
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
        .get("/api/AdminNotice/" + this.$route.params.id + "/")
        .then(response2 => {
          if (response2.data != "noData") {
            this.notice = response2.data;
          }
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
