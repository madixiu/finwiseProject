<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <ShareholdersWidget :notices="notice"></ShareholdersWidget>
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

import ShareholdersWidget from "@/view/pages/Ticker/TickerWidgets/ShareholdersWidget.vue";
export default {
  name: "shareholders",
  components: {
    SubHeaderWidget,
    ShareholdersWidget
  },
  data() {
    return {
      subheaders: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - سهامداران عمده ";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "سهامداران عمده" }]);
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
    },
    async loadData() {
      await this.axios
        .get("/api/Shareholders/" + this.$route.params.id)
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
