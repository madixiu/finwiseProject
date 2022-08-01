<template>
  <div>
    <v-row no-gutters>
      <div class="col-xxl-12" style="padding-bottom:0px">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12" style="padding-top:5px">
        <NotificationsWidget :notices="notice"></NotificationsWidget>
      </div>
    </v-row>
  </div>
</template>
<script>
import {
  SET_BREADCRUMB,
  SET_BREADCRUMB_TITLE,
  ADD_BREADCRUMB
} from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/TickerWidgets/subHeaderWidget.vue";

import NotificationsWidget from "@/view/pages/Ticker/TickerWidgets/NotificationsWidget.vue";
export default {
  name: "Notifications",
  components: {
    SubHeaderWidget,
    NotificationsWidget
  },
  data() {
    return {
      subheaders: [],
      notice: []
    };
  },
  created() {
    document.title = "Finwise - کدال";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "اطلاعیه های کدال" }]);
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
        .get("/api/CodalNotices/" + this.$route.params.id)
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
