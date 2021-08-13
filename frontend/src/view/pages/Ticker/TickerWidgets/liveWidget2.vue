<template>
  <div>
    <v-row no-gutters class="d-flex flex-row justify-content-between">
      <!--//? 1ST -->
      <!-- <v-col cols="3" class="flex-grow-1 flex-shrink-0 pl-1"
        ><v-card rounded="lg">
          <v-toolbar
            dense
            class="IndexChartToolbars elevation-2"
            style="height:36px;"
          >
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >اطلاعات</v-toolbar-title
            >
          </v-toolbar>
          <v-row>
            <v-col cols="6">
              <v-col
                class="d-flex flex-column align-center align-content-center p-0 mt-1 mb-1 mr-1"
                style="border:1px solid black;border-radius:8px"
              >
                <span class="titleInfoSpan">نام شرکت:</span>
                <span class="titleInfoSpan">{{ liveData[0].name }}</span>
              </v-col>
              <v-col
                class="d-flex flex-column  align-center align-content-center pt-0"
              >
                <span class="titleInfoSpan">بازار:</span>
                <span class="titleInfoSpan">{{ liveData[0].market }}</span>
              </v-col>
              <v-row
                no-gutters
                class="d-flex flex-row  align-center align-content-center pt-0"
              >
                <span class="titleInfoSpan">صنعت:</span>
                <span class="titleInfoSpan">{{ liveData[0].name }}</span>
              </v-row>
              <v-row
                no-gutters
                class="d-flex flex-row  align-center align-content-center pt-0"
              >
                <span class="titleInfoSpan">ارزش بازار:</span>
                <span class="titleInfoSpan">{{ marketCap }}</span>
              </v-row>
              <v-col class="d-flex pt-0">
                <span class="titleInfoSpan">میانگین حجم ماه:</span>
                <span class="titleInfoSpan">NO DATA</span>
              </v-col>
              <v-col class="d-flex pt-0">
                <span class="titleInfoSpan">تعداد سهام:</span>
                <span class="titleInfoSpan">{{ ShareCount }}</span>
                <span class="titleInfoSpan">میلیارد</span>
              </v-col>
            </v-col>
            <v-col cols="6">
              <v-col class="d-flex flex-column">
                <v-card elevation="4" rounded="md">
                  <v-row
                    no-gutters
                    class="pt-1 pb-1 d-flex justify-content-center"
                  >
                    <span class="titleInfoSpan">حجم مبنا:</span>
                    <span class="titleInfoSpan">{{ Mabna }}</span>
                  </v-row>
                </v-card>
              </v-col>
              <v-col class="d-flex pt-0">
                <span class="titleInfoSpan">شناور:</span>
                <span class="titleInfoSpan">{{ liveData[0].Shenavari }}</span>
              </v-col>
              <v-col class="d-flex pt-0">
                <span class="titleInfoSpan">EPS:</span>
                <span class="titleInfoSpan">{{ liveData[0].EPS }}</span>
              </v-col>
              <v-col class="d-flex pt-0">
                <span class="titleInfoSpan">EV:</span>
                <span class="titleInfoSpan">NO DATA</span>
              </v-col>
              <v-col class="d-flex pt-0">
                <span class="titleInfoSpan">P/E(TTM):</span>
                <span class="titleInfoSpan">NO DATA</span>
              </v-col>
              <v-col class="d-flex pt-0">
                <span class="titleInfoSpan">P/B:</span>
                <span class="titleInfoSpan">NO DATA</span>
              </v-col>
            </v-col>
          </v-row>
        </v-card></v-col
      > -->
      <!--//? 2ND -->
      <v-col cols="6" class="flex-grow-1 flex-shrink-0 pl-1"
        ><v-card rounded="lg" height="358">
          <v-toolbar
            dense
            class="IndexChartToolbars elevation-2"
            style="height:36px;"
          >
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >سابقه قیمت</v-toolbar-title
            >
          </v-toolbar>
          <PriceHistoryWidget
            class="py-1"
            :priceHistory="priceHistory"
          ></PriceHistoryWidget> </v-card
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
              >ربات تحلیلگر بنیادی</v-toolbar-title
            >
          </v-toolbar>
          <FundamentalRobotWidget
            :liveData="liveData"
            :FundamentalRobot="FundamentalRobot"
          ></FundamentalRobotWidget> </v-card
      ></v-col>
      <!--//? 4TH -->
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
          <TechnicalWidget
            v-show="Indicators.length != 0"
            :Indicators="Indicators"
          ></TechnicalWidget> </v-card
      ></v-col>
    </v-row>
  </div>
</template>
<script>
// import ApexChart from "@/view/content/charts/ApexChart";
import PriceHistoryWidget from "@/view/pages/Ticker/TickerWidgets/TickerPriceHistory.vue";
import TechnicalWidget from "@/view/pages/Ticker/TickerWidgets/TechnicalIndicators.vue";
import FundamentalRobotWidget from "@/view/pages/Ticker/TickerWidgets/FundamentalRobotWidget.vue";
export default {
  components: {
    // ApexChart,
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
