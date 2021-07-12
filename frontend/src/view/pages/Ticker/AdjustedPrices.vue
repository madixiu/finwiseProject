<template>
  <div>
    <div class="row">
      <div class="col-xxl-12">
        <SubHeaderWidget :tickerdata="subheaders"></SubHeaderWidget>
      </div>
      <div class="col-xxl-12">
        <AdjustedPricesWidget :adjusted="adjustedprices"></AdjustedPricesWidget>
      </div>
    </div>
  </div>
</template>

<script>
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import SubHeaderWidget from "@/view/pages/Ticker/Rankers/subHeaderWidget.vue";
import AdjustedPricesWidget from "@/view/pages/Ticker/TickerWidgets/AdjustedPricesWidget.vue";
export default {
  name: "adjustedPrices",
  components: {
    SubHeaderWidget,
    AdjustedPricesWidget
  },
  data() {
    return {
      subheaders: [],
      adjustedprices: []
    };
  },
  created() {
    document.title = "Finwise - سابقه قیمت تعدیلی";
  },
  mounted() {
    this.loadData();
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "سابقه قیمت" }]);
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
        this.getTwo();
      });
    },
    async getTwo() {
      await this.axios
        .get("/api/AdjustedPrices/" + this.$route.params.id + "/")
        .then(responsePrice => {
          this.adjustedprices = responsePrice.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getOne() {
      await this.axios
        .get("/api/LiveTicker/" + this.$route.params.id + "/")
        .then(responseHeader => {
          this.subheaders = responseHeader.data[0];
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
