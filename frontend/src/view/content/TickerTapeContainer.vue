<template>
  <div
    class="subheader py-2 py-lg-4"
    v-bind:class="subheaderClasses"
    id="kt_subheader"
  >
    <div
      class="d-flex align-items-center justify-content-between flex-wrap flex-sm-nowrap container-custom"
    >
      <TickerTape
        v-if="Ticker"
        :TickerType="true"
        :duration="60"
        :TickerData="TickerTapeData"
      />
      <TickerTape
        v-if="!Ticker"
        :TickerType="false"
        :duration="200"
        :TickerData="IndustryTapeData"
      />
    </div>
  </div>
</template>

<style scoped>
.container-custom {
  width: 100%;
  padding-right: 0px;
  padding-left: 0px;
  margin-right: auto;
  margin-left: auto;
}
</style>

<script>
import { mapGetters } from "vuex";
import TickerTape from "@/view/content/TickerTape.vue";
export default {
  name: "TickerTapeContainer",
  components: {
    TickerTape
  },
  watch: {
    $route() {
      this.RouteCheck();
    }
  },
  data() {
    return {
      TickerTapeData: [],
      IndustryTapeData: [],
      Ticker: true
    };
  },
  //   props: {
  //     breadcrumbs: Array,Vazir
  //     title: String
  //   },
  mounted() {
    this.RouteCheck();
    this.getTickerTapeData();
  },
  methods: {
    RouteCheck() {
      if (this.$route.name != "Dashboard") this.Ticker = false;
      else this.Ticker = true;
    },
    async getTickerTapeData() {
      await this.axios
        .get("/api/TapeData")
        .then(TickerTapeResponse => {
          let data = TickerTapeResponse.data;
          
          this.TickerTapeData = data[0];
          this.IndustryTapeData = data[1];

          // this.TickerTape.pop();
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  computed: {
    ...mapGetters(["layoutConfig"]),

    /**
     * Check if subheader width is fluid
     */
    widthFluid() {
      return this.layoutConfig("subheader.width") === "fluid";
    },

    subheaderClasses() {
      const classes = [];
      const style = this.layoutConfig("subheader.style");
      if (style) {
        classes.push(style);

        if (style === "solid") {
          classes.push("bg-white");
        }

        if (this.layoutConfig("subheader.fixed")) {
          classes.push("border-top");
        }
      }
      return classes.join(" ");
    }
  }
};
</script>
