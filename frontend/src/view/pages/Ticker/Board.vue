<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 pt-3 pb-1">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <BoardCeoWidget :notices="notice" :deposits="deposit"></BoardCeoWidget>
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

import BoardCeoWidget from "@/view/pages/Ticker/TickerWidgets/BoardCeoWidget.vue";
export default {
  name: "Board",
  components: {
    SubHeaderWidget,
    BoardCeoWidget
  },
  data() {
    return {
      subheaders: [],
      notice: [],
      deposit: []
    };
  },
  created() {
    document.title = "Finwise - هیئت مدیره";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات سهم" }]);
    this.$store.dispatch(ADD_BREADCRUMB, [{ title: "اطلاعات هیئت مدیره" }]);
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
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getTwo().then(response => {
        this.getThree();
      });
    },
    async getTwo() {
      await this.axios
        .get("/api/CurrentBoard/" + this.$route.params.id + "/")
        .then(response2 => {
          this.notice = response2.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getThree() {
      await this.axios
        .get("/api/CurrentCeo/" + this.$route.params.id + "/")
        .then(response3 => {
          this.deposit = response3.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
