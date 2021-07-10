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
        v-if="Ticker && TickerTapeData.length"
        :TickerType="true"
        :duration="60"
        :TickerData="TickerTapeData"
      />
      <TickerTape
        v-if="!Ticker && IndustryTapeData != 'noData'"
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
      if (this.$route.name != "Dashboard" || this.$route.name != "Industries") {
        clearInterval(this.interval);
        this.WebsocketRequest = false;
      }
    }
  },
  data() {
    return {
      TickerTapeData: [],
      IndustryTapeData: [],
      Ticker: true
    };
  },
  mounted() {
    this.getTickerTapeData();
    this.RouteCheck();
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
          if (data[0]) this.TickerTapeData = data[0];
          this.IndustryTapeData = data[1];

          // this.TickerTape.pop();
        })
        .catch(error => {
          console.error(error);
        });
    },

    //? %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    liveData() {
      this.interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(this.interval._id);
          return;
        }
        // let barier = {
        //   request: "get",
        //   data: {
        //     marketName: this.tableMarketSelected,
        //     marketIndustry: this.tableMarketIndustrySelected
        //   }
        // };
        // this.$socketMarketWatch.send(JSON.stringify(barier));
        this.getTickerTapeData();
      }, 60000);
    },
    liveChecker() {
      let date = new Date();
      if (
        date.getHours() > 8 &&
        date.getHours() < 14 &&
        date.getDay() != 5 &&
        date.getDay() != 4
      ) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    }
    //? %%%%%%%%%%%%%%%%%%%%%%% WEBSOCKET METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
  },
  beforeDestroy() {
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  },
  destroyed() {
    // let barier = { request: "halt" };
    // this.$socketMarketWatch.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
    clearInterval(this.interval);
    // console.log("destroy");
  }
};
</script>
