<template>
  <div>
    <!--begin::Dashboard-->
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <BoardCeoWidget :notices="notice" :deposits="deposit"></BoardCeoWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import BoardCeoWidget from "@/view/pages/Ticker/TickerWidgets/BoardCeoWidget.vue";
// import axios from "axios";
export default {
  name: "BoardView",
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
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "اطلاعات هیيت مدیره" }]);
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
        this.getTwo().then(response => {
          this.getThree();
        });
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
