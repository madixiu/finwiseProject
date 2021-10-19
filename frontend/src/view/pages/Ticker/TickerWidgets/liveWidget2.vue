<template>
  <div>
    <v-row no-gutters class="d-flex flex-row justify-content-between">
      <!--//? 1ST -->
      <v-col cols="6" class="flex-grow-1 flex-shrink-0 pl-1">
        <PriceHistoryWidget :priceHistory="priceHistory"></PriceHistoryWidget>
      </v-col>
      <!--//? 2ND -->
      <v-col cols="3" class="flex-grow-1 flex-shrink-0 pl-1"
        ><v-card rounded="lg" height="358">
          <v-toolbar
            dense
            class="IndexChartToolbars elevation-2"
            style="height:36px;"
          >
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >ربات تحلیلگر بنیادی</v-toolbar-title
            >
          </v-toolbar>
          <div
            class="d-flex flex-column justify-content-center my-auto"
            style="height:70%"
            v-if="FundamentalRobot.length == 0"
          >
            <v-icon size="30px" color="#e09f3e">mdi-alert-box</v-icon>
            <div class="d-flex justify-content-center my-2">
              <span style="font-size:0.8em">داده موجود نیست</span>
            </div>
          </div>
          <FundamentalRobotWidget
            v-show="FundamentalRobot.length"
            :liveData="liveData"
            :FundamentalRobot="FundamentalRobot"
          ></FundamentalRobotWidget> </v-card
      ></v-col>
      <!--//? 3RD -->
      <v-col cols="3" class="flex-grow-1 flex-shrink-0 pl-1"
        ><v-card rounded="lg" height="358">
          <v-toolbar
            dense
            class="IndexChartToolbars elevation-2"
            style="height:36px;"
          >
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >وضعیت تکنیکال سهم</v-toolbar-title
            >
          </v-toolbar>
          <div
            class="d-flex flex-column justify-content-center my-auto"
            style="height:70%"
            v-if="Indicators.length == 0"
          >
            <v-icon size="30px" color="#e09f3e">mdi-alert-box</v-icon>
            <div class="d-flex justify-content-center my-2">
              <span style="font-size:0.8em">داده موجود نیست</span>
            </div>
          </div>
          <TechnicalWidget
            v-show="Indicators.length != 0"
            :Indicators="Indicators"
          ></TechnicalWidget> </v-card
      ></v-col>
    </v-row>
  </div>
</template>
<script>
import PriceHistoryWidget from "@/view/pages/Ticker/TickerWidgets/TickerPriceHistory.vue";
import TechnicalWidget from "@/view/pages/Ticker/TickerWidgets/TechnicalIndicators.vue";
import FundamentalRobotWidget from "@/view/pages/Ticker/TickerWidgets/FundamentalRobotWidget.vue";
export default {
  components: {
    PriceHistoryWidget,
    FundamentalRobotWidget,
    TechnicalWidget
  },

  data() {
    return {
      //? full object
      liveTickerInfo: null,
      //* live ticker data
      tickerfull: null,
      tradeVolume: null,
      tradevalue: null,
      tradecount: null,
      marketcap: null,
      low: null,
      first: null,
      last: null,
      close: null,
      market: null,
      high: null,
      open: null,
      Nemad: null,
      eps: null,
      sharecount: null,
      shenavar: null,
      mabna: null,
      status: null
      //* *****************
    };
  },
  props: {
    liveData: Array,
    Indicators: Array,
    FundamentalRobot: Array,
    priceHistory: Array
  },
  // watch: {
  //   FundamentalRobotWidget(newValue, oldValue) {
  //     console.log(newValue, oldValue);
  //   }
  // },
  computed: {
    marketCap() {
      let marketcap = this.liveData[0].close * this.liveData[0].ShareCount;
      return this.roundTo(marketcap / 1000000000, 2).toLocaleString();
    },
    Mabna() {
      return this.roundTo(this.liveData[0].Mabna / 1000000, 2).toLocaleString();
    },
    ShareCount() {
      return this.roundTo(
        this.liveData[0].ShareCount / 1000000000,
        2
      ).toLocaleString();
    }
  },
  methods: {
    roundTo(n, digits) {
      if (n == "-") {
        return n;
      }

      let negative = false;
      if (digits === undefined) {
        digits = 0;
      }
      if (n < 0) {
        negative = true;
        n = n * -1;
      }
      let multiplicator = Math.pow(10, digits);
      n = parseFloat((n * multiplicator).toFixed(11));
      n = (Math.round(n) / multiplicator).toFixed(digits);
      if (negative) {
        n = (n * -1).toFixed(digits);
      }
      return n;
    }
  }
};
</script>
<style scoped>
.titleInfoSpan {
  font-family: "Vazir-Light-FD";
  font-size: 0.85em;
}
</style>
