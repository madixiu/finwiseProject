<template>
  <div style="padding-top:0px">
    <v-row
      no-gutters
      class="d-flex flex-row justify-content-between"
      v-if="!loading"
      style="flex-wrap: nowrap"
    >
      <v-col cols="4" class="flex-grow-2 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <!--//? top header -->
          <v-row
            no-gutters
            class="d-flex flex-row justify-content-around  pt-1 px-3"
          >
            <v-col style="direction:ltr;text-align:right" class="">
              {{ LiveDataItems.ticker }}
            </v-col>
            <v-col style="padding-bottom:5px;padding-left:5px">
              <v-chip x-small outlined :color="StatusColor">
                {{ LiveDataItems.Status }}
              </v-chip>
            </v-col>
          </v-row>
          <!--//? 2nd line -->
          <v-row no-gutters cols="12" class="px-3" style="text-align:right">
            <v-col
              ><span class="tickerSubInfo"
                >({{ LiveDataItems.name }})</span
              ></v-col
            >
            <v-col class="d-flex justify-end">
              <div class="d-flex mr-2">
                <span style="font-family:Vazir-Light-FD;font-size:0.9em"
                  >آخرین قیمت:
                </span>
                <span style="font-size:0.9em">{{ closePrice }} </span>
              </div>
              <div class="d-flex">
                <span
                  dir="ltr"
                  class="spandata"
                  v-bind:class="[
                    [
                      LiveDataItems.last > LiveDataItems.yesterday
                        ? 'greenItem'
                        : LiveDataItems.last == LiveDataItems.yesterday
                        ? 'blackItem'
                        : LiveDataItems.last < LiveDataItems.yesterday
                        ? 'redItem'
                        : ''
                    ]
                  ]"
                  >%{{ closePercent }}</span
                >
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters cols="12" class="px-3" style="text-align:right">
            <v-col
              ><span class="tickerSubInfo">{{
                LiveDataItems.market
              }}</span></v-col
            >
            <v-col class="d-flex justify-end">
              <div class="d-flex mr-2">
                <span
                  style="font-family:Vazir-Light-FD;font-size:0.9em"
                  class="mr-1"
                  >قیمت پایانی:
                </span>
                <span style="font-size:0.9em">{{ finalPrice }} </span>
              </div>
              <div class="d-flex">
                <span
                  dir="ltr"
                  class="spandata"
                  v-bind:class="[
                    [
                      LiveDataItems.close > LiveDataItems.yesterday
                        ? 'greenItem'
                        : LiveDataItems.close == LiveDataItems.yesterday
                        ? 'blackItem'
                        : LiveDataItems.close < LiveDataItems.yesterday
                        ? 'redItem'
                        : ''
                    ]
                  ]"
                  >%{{ finalPercent }}</span
                >
              </div>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <div class="d-flex flex-column">
            <v-row no-gutters class="px-3 pt-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">ارزش معاملات:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ Value }}</span>
                </div>
                <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیارد ریال</span>
                </div>
              </v-col>
            </v-row>

            <v-row no-gutters class="px-3">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">حجم معاملات:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ Volume }}</span>
                </div>
                <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیون</span>
                </div>
              </v-col>
            </v-row>
            <v-row no-gutters class="px-3">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">ارزش بازار:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ marketCap }}</span>
                </div>
                <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیارد ریال</span>
                </div>
              </v-col>
            </v-row>
            <!-- <v-row no-gutters class="px-3 pb-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">تعداد سهام:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ ShareCount }}</span>
                </div>
                <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیارد</span>
                </div>
              </v-col>
            </v-row> -->
          </div>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <div class="d-flex flex-column">
            <v-row no-gutters class="px-3 pt-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">تعداد سهام:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ ShareCount }}</span>
                </div>
                <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیارد</span>
                </div>
              </v-col>
            </v-row>

            <v-row no-gutters class="px-3">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">میانگین حجم ماه:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">-</span>
                </div>
                <!-- <div class="d-flex align-center">
                  <span class="tickerSubInfo">%</span>
                </div> -->
              </v-col>
            </v-row>
            <v-row no-gutters class="px-3">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem"> تعداد معاملات:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ LiveDataItems.TradeCount }}</span>
                </div>
                  <!-- <div class="d-flex align-center">
                    <span class="tickerSubInfo">میلیون سهم</span>
                  </div> -->
              </v-col>
            </v-row>
            <!-- <v-row no-gutters class="px-3 pb-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">P/B:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">-</span>
                </div>
          
              </v-col>
            </v-row> -->
          </div>
        </v-card>
      </v-col>

      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <div class="d-flex flex-column">
            <v-row no-gutters class="px-3 pt-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">EPS:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ LiveDataItems.EPS }}</span>
                </div>
                <!-- <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیارد ریال</span>
                </div> -->
              </v-col>
            </v-row>

            <v-row no-gutters class="px-3">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">درصد شناوری:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ LiveDataItems.Shenavari }}</span>
                </div>
                <!-- <div class="d-flex align-center">
                  <span class="tickerSubInfo">%</span>
                </div> -->
              </v-col>
            </v-row>
            <v-row no-gutters class="px-3">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">حجم مبنا:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ Mabna }}</span>
                </div>
                <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیون سهم</span>
                </div>
              </v-col>
            </v-row>
            <!-- <v-row no-gutters class="px-3 pb-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">P/B:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">-</span>
                </div>
          
              </v-col>
            </v-row> -->
          </div>
        </v-card>
      </v-col>
      <v-col cols="2" class="flex-grow-1 flex-shrink-0 pl-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <div class="d-flex flex-column">
            <!-- <v-row no-gutters class="px-3 pt-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">EPS:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">{{ LiveDataItems.EPS }}</span>
                </div>
         
              </v-col>
            </v-row> -->

            <v-row no-gutters class="px-3 pt-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">EV:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">-</span>
                </div>
                <!-- <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیون</span>
                </div> -->
              </v-col>
            </v-row>
            <v-row no-gutters class="px-3">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">P/E(TTM):</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">-</span>
                </div>
                <!-- <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیارد ریال</span>
                </div> -->
              </v-col>
            </v-row>
            <v-row no-gutters class="px-3 pb-1">
              <v-col class="d-flex justify-start">
                <div>
                  <span class="tickerItem">P/B:</span>
                </div>
                <div class="d-flex mr-1">
                  <span class="tickerItem">-</span>
                </div>
                <!-- <div class="d-flex align-center">
                  <span class="tickerSubInfo">میلیارد</span>
                </div> -->
              </v-col>
            </v-row>
          </div>
        </v-card>
      </v-col>

      <!-- <v-col cols="2" class="flex-grow-1 flex-shrink-0 pr-1">
        <v-card rounded="lg" height="100%" elevation="5">
          <v-col cols="12" style="direction:ltr" class="CardHeaderTitle">
            وضعیت
          </v-col>
          <v-col cols="12" style="padding-bottom:5px;padding-left:5px">
            <v-chip x-small outlined :color="StatusColor">
              {{ LiveDataItems.Status }}
            </v-chip>
          </v-col>
        </v-card>
      </v-col> -->
    </v-row>
  </div>
</template>

<script>
export default {
  name: "SubHeaderWidget",
  props: ["tickerdata"],
  data() {
    return {
      loading: true,
      search: "",
      LiveDataItems: []
    };
  },
  computed: {
    marketCap() {
      let marketcap = this.LiveDataItems.close * this.LiveDataItems.ShareCount;
      return this.roundTo(marketcap / 1000000000, 2).toLocaleString();
    },
    Mabna() {
      return this.roundTo(
        this.LiveDataItems.Mabna / 1000000,
        2
      ).toLocaleString();
    },
    ShareCount() {
      return this.roundTo(
        this.LiveDataItems.ShareCount / 1000000000,
        2
      ).toLocaleString();
    },
    closePercent() {
      return (
        Math.round(
          (this.LiveDataItems.last / this.LiveDataItems.yesterday - 1) *
            100 *
            100
        ) / 100
      );
    },
    closePrice() {
      if (this.LiveDataItems.last != undefined)
        return this.LiveDataItems.last.toLocaleString();
      else return "-";
    },
    finalPrice() {
      if (this.LiveDataItems.close != undefined)
        return this.LiveDataItems.close.toLocaleString();
      else return "-";
    },
    finalPercent() {
      return (
        Math.round(
          (this.LiveDataItems.close / this.LiveDataItems.yesterday - 1) *
            100 *
            100
        ) / 100
      );
    },
    Volume() {
      if (this.LiveDataItems.TradeVolume != undefined)
        return this.roundTo(
          this.LiveDataItems.TradeVolume / 1000000,
          2
        ).toLocaleString();
      else return "-";
    },
    Value() {
      if (this.LiveDataItems.TradeValue != undefined)
        return this.roundTo(
          this.LiveDataItems.TradeValue / 1000000000,
          2
        ).toLocaleString();
      else return "-";
    },
    StatusColor() {
      if (this.LiveDataItems.Status == "مجاز") return "#014f86";
      else return "black";
    }
  },
  methods: {
    LivepopulateData() {
      this.LiveDataItems = this.tickerdata;
      if (this.LiveDataItems === undefined || this.LiveDataItems.length == 0) {
        this.LiveDataItems = [
          {
            ID: "-",
            englishDate: "-",
            Status: "-",
            Hour: "-",
            ticker: "-",
            name: "-",
            ShareCount: "-",
            Mabna: "-",
            Shenavari: "-",
            persianDate: "-",
            first: "-",
            close: "-",
            last: "-",
            low: "-",
            high: "-",
            yesterday: "-",
            TradeCount: "-",
            TradeValue: "-",
            TradeVolume: "-",
            EPS: "-",
            market: "-"
          }
        ];
      }
      this.loading = false;
    },
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
      return parseFloat(n);
    }
  },
  mounted() {
    this.LivepopulateData();
  },
  watch: {
    tickerdata() {
      this.LivepopulateData();
    }
  }
};
</script>
<style scoped>
.CardHeaderTitle {
  direction: ltr;
  align-items: right;
  display: flex;
  flex-wrap: nowrap;
  justify-content: flex-end;
  padding-bottom: 0px;
  padding-top: 5px;
  font-family: "Vazir-Light-FD";
  font-weight: 500;
  /* font-family: "IRANSansXFaNum-Regular"; */
}
.tickerItem {
  font-size: 0.9em !important;
  font-family: "Vazir-Light-FD";
}
.tickerSubInfo {
  font-size: 0.7em;
  font-family: "Vazir-Light-FD";
}
.redItem {
  color: #ef5350 !important;
}

.greenItem {
  /* color: #088a2f93 !important; */
  color: green;
}
.blackItem {
  color: black;
}
</style>
