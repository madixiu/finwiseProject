<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <!-- <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        {{ this.Nemad }}<span class="small mr-5">{{ this.tickerfull }}</span>
      </h3>
    </div> -->

    <v-card>
      <v-tabs vertical>
        <v-tab class="FinancialStrength">
          اطلاعات معاملات
          <v-icon left>mdi-access-point</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          حقیقی -حقوقی
          <v-icon left>mdi-information</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          آمار سهم
          <v-icon left>mdi-thermostat</v-icon>
        </v-tab>
        <v-tab-item>
          <v-card flat>
            <!-- <v-card-text> -->
            <div class="row">
              <div class="col-xxl-3 col-lg-3 col-3 FinancialStrength">
                <h5 class="titleHeaders">
                  قیمت پایانی : {{ this.close }} (
                  <span
                    v-bind:class="[
                      this.close > this.open ? 'greenItem' : 'redItem'
                    ]"
                  >
                    % {{ setclosingperc }}
                  </span>
                  )
                  <v-icon
                    left
                    small
                    v-bind:class="[
                      this.close >= this.open ? 'greenItem' : 'redItem'
                    ]"
                    >mdi-arrow-{{
                      this.close >= this.open ? "up" : "down"
                    }}-circle-outline</v-icon
                  >
                </h5>
                <h5 class="titleHeaders">
                  قیمت آخرین معامله : {{ this.last }} (
                  <span
                    v-bind:class="[
                      last > open ? 'greenItem' : 'redItem ltr_aligned'
                    ]"
                    >% {{ setlastperc }}</span
                  >)
                  <v-icon
                    left
                    v-bind:class="[
                      this.last >= this.open ? 'greenItem' : 'redItem'
                    ]"
                    small
                    >mdi-arrow-{{
                      this.last >= this.open ? "up" : "down"
                    }}-circle-outline</v-icon
                  >
                </h5>
                <h5 class="titleHeaders">اولین قیمت : {{ this.open }}</h5>
                <h5 class="titleHeaders">ارزش بازار : {{ this.marketcap }}</h5>
              </div>

              <div class="col-xxl-3 col-lg-3 col-3 FinancialStrength">
                <h5 class="titleHeaders">کف قیمت : {{ this.min }}</h5>
                <h5 class="titleHeaders">سقف قیمت: {{ this.max }}</h5>
                <h5 class="titleHeaders">کمترین قیمت: {{ this.low }}</h5>
                <h5 class="titleHeaders">بیشترین قیمت : {{ this.high }}</h5>
              </div>
              <div class="col-xxl-3 col-lg-3 col-3 FinancialStrength">
                <h5 class="titleHeaders">
                  تعداد معاملات : {{ this.tradecount }}
                </h5>
                <h5 class="titleHeaders">
                  حجم معاملات : {{ this.tradeVolume }}
                </h5>
                <h5 class="titleHeaders">
                  ارزش معاملات : {{ this.tradevalue }}
                </h5>
                <h5 class="titleHeaders">
                  میانگین حجم ۱ ماهه : {{ this.close }}
                </h5>
              </div>
              <div class="col-xxl-3 col-lg-3 col-3">
                <!-- <h5 class="titleHeaders">چارت</h5> -->
                <ApexChart
                  type="area"
                  height="100%"
                  width="100%"
                  :series="priceOverViewSeries"
                  :chartOptions="priceOverViewchartOptions"
                >
                </ApexChart>
              </div>
            </div>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <div class="row">
                <div class="col-xxl-3 col-lg-3 col-3">
                  <h5 class="titleHeaders">خریداران حقیقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد خریداران : {{ this.countbuyerHaghighi }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم خرید : {{ this.volumebuyerHaghighi }}
                  </h5>
                </div>
                <div class="col-xxl-3 col-lg-3 col-3">
                  <h5 class="titleHeaders">خریداران حقوقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد خریداران : {{ this.countbuyerHoghughi }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم خرید : {{ this.volumebuyerHoghughi }}
                  </h5>
                </div>
                <div class="col-xxl-3 col-lg-3 col-3">
                  <h5 class="titleHeaders">فروشندگان حقیقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد فروشندگان : {{ this.countsellerHaghighi }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم فروش : {{ this.volumesellerHaghighi }}
                  </h5>
                </div>
                <div class="col-xxl-3 col-lg-3 col-3">
                  <h5 class="titleHeaders">فروشندگان حقوقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد فروشندگان : {{ this.countsellerHoghughi }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم فروش : {{ this.volumesellerHoghughi }}
                  </h5>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <div class="row">
                <div class="col-xxl-2 col-lg-2 col-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات ارزش معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    میانگین ارزش معاملات ۳ ماهه :
                    <span
                      >{{
                        numberWithCommas(
                          roundTo(this.avgval3month / 1000000000, 2)
                        )
                      }}<br />
                      میلیارد ریال</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    میانگین ارزش معاملات ۱۲ ماهه :
                    <span
                      >{{
                        numberWithCommas(
                          roundTo(this.avgval12month / 1000000000, 2)
                        )
                      }}<br />
                      میلیارد ریال</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین ارزش معاملات ۳ ماهه :{{ this.rankval3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین ارزش معاملات ۱۲ ماهه :{{ this.rankval12month }}
                  </h5>
                </div>
                <div class="col-xxl-2 col-lg-2 col-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات حجم معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    میانگین حجم معاملات ۳ ماهه :
                    <span
                      >{{
                        numberWithCommas(
                          roundTo(this.avgval3month / 1000000, 2)
                        )
                      }}<br />
                      میلیون</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    میانگین حجم معاملات ۱۲ ماهه :<span
                      >{{
                        numberWithCommas(
                          roundTo(this.avgvol12month / 1000000, 2)
                        )
                      }}<br />
                      میلیون</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین حجم معاملات ۳ ماهه :{{ this.rankvol3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین حجم معاملات ۱۲ ماهه :{{ this.rankvol12month }}
                  </h5>
                </div>
                <div class="col-xxl-2 col-lg-2 col-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات تعداد معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    میانگین تعداد معاملات ۳ ماهه :
                    <span
                      >{{ numberWithCommas(this.avgcount3month) }}<br />
                    </span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    میانگین تعداد معاملات ۱۲ ماهه :
                    <span
                      >{{ numberWithCommas(this.avgcount12month) }}<br />
                    </span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین تعداد معاملات ۳ ماهه :{{
                      this.rankcount3month
                    }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین تعداد معاملات ۱۲ ماهه :{{
                      this.rankcount12month
                    }}
                  </h5>
                </div>
                <div class="col-xxl-2 col-lg-2 col-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات معاملاتی آخرین روز</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    ارزش معاملات آخرین روز :<span
                      >{{
                        numberWithCommas(
                          roundTo(this.yesterdaytvalue / 1000000000, 2)
                        )
                      }}<br />
                      میلیارد ریال</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم معاملات آخرین روز :
                    <span
                      >{{
                        numberWithCommas(
                          roundTo(this.yesterdaytvolume / 1000000, 2)
                        )
                      }}<br />
                      میلیون</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    تعداد معاملات آخرین روز :<span
                      >{{ numberWithCommas(this.yesterdaytcount) }}<br />
                    </span>
                  </h5>
                </div>
                <div class="col-xxl-2 col-lg-2 col-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات ارزش بازار</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    ارزش بازار دیروز :<span
                      >{{
                        numberWithCommas(
                          roundTo(this.marketcapyesterday / 1000000000, 2)
                        )
                      }}<br />
                      میلیارد ریال</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه ارزش بازار دیروز : {{ this.marketcapyesterdayrank }}
                  </h5>
                </div>
                <div class="col-xxl-2 FinancialStrength">
                  <h5 class="titleHeaders">حضور در بازار</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد روزهای باز در ۳ ماه گذشته :
                    {{ this.opendayscount3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    تعداد روزهای باز در ۱۲ ماه گذشته :
                    {{ this.opendayscount12month }}
                  </h5>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
import ApexChart from "@/view/content/charts/ApexChart";

export default {
  name: "PWidget",
  components: {
    ApexChart
  },
  props: ["statistics"],
  data() {
    return {
      priceOverViewSeries: [
        {
          name: "series1",
          data: [31, 40, 28, 51, 42, 109, 100]
        }
      ],
      priceOverViewchartOptions: {
        chart: {
          height: 350,
          type: "area",
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 2,
          curve: "smooth"
        },
        xaxis: {
          type: "datetime",
          categories: [
            "2018-09-19T00:00:00.000Z",
            "2018-09-19T01:30:00.000Z",
            "2018-09-19T02:30:00.000Z",
            "2018-09-19T03:30:00.000Z",
            "2018-09-19T04:30:00.000Z",
            "2018-09-19T05:30:00.000Z",
            "2018-09-19T06:30:00.000Z"
          ]
        },
        tooltip: {
          x: {
            format: "dd/MM/yy HH:mm"
          }
        }
      },
      search: "",
      Nemad: "شستا",
      tickerfull: "تامین اجتماعی",
      industry: "سرمایه گذاری",
      subindustry: "شرکتی",
      market: "بورس",
      tablo: "اول بورس",
      close: "1500",
      open: "1400",
      first: "2200",
      last: "1250",
      high: "1200",
      low: "1320",
      tradeVolume: "50000",
      tradevalue: "11111111",
      tradecount: "123213",
      marketcap: "12321312321312",
      min: "131",
      max: "141",
      avgval3month: "-",
      avgval12month: "-",
      rankval3month: "-",
      rankval12month: "-",
      avgvol3month: "-",
      avgvol12month: "-",
      rankvol3month: "-",
      rankvol12month: "-",
      avgcount3month: "-",
      avgcount12month: "-",
      rankcount3month: "-",
      rankcount12month: "-",
      marketcapyesterday: "-",
      marketcapyesterdayrank: "-",
      yesterdaytvalue: "-",
      yesterdaytvolume: "-",
      yesterdaytcount: "-",
      opendayscount3month: "-",
      opendayscount12month: "-",
      countbuyerHaghighi: "-",
      countbuyerHoghughi: "-",
      volumebuyerHaghighi: "-",
      volumebuyerHoghughi: "-",
      countsellerHaghighi: "-",
      countsellerHoghughi: "-",
      volumesellerHaghighi: "-",
      volumesellerHoghughi: "-"
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    setclosingperc: function() {
      return Math.round((this.close / this.open - 1) * 100 * 100) / 100;
    },
    setlastperc: function() {
      return Math.round((this.last / this.open - 1) * 100 * 100) / 100;
    }
  },
  methods: {
    numberWithCommas(x) {
      if (x == "-") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
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
    },
    populateData() {
      this.DataItems2 = this.statistics;
      Object.keys(this.DataItems2).forEach(key => {
        let val = this.DataItems2[key]; // value of the current key
        if (val.Item == "Avg Value 3 month") {
          this.avgval3month = val.value;
        }
        if (val.Item == "Avg Value 12 month") {
          this.avgval12month = val.value;
        }
        if (val.Item == "Rank _ value 3 month") {
          this.rankval3month = val.value;
        }
        if (val.Item == "Rank_value 12 month") {
          this.rankval12month = val.value;
        }
        if (val.Item == "Avg Volume 3 month") {
          this.avgvol3month = val.value;
        }
        if (val.Item == "Avg Volume 12 month") {
          this.avgvol12month = val.value;
        }
        if (val.Item == "Rank Volume 3 month") {
          this.rankvol3month = val.value;
        }
        if (val.Item == "Rank Volume 12 month") {
          this.rankvol12month = val.value;
        }
        if (val.Item == "Avg Count 3 month") {
          this.avgcount3month = val.value;
        }
        if (val.Item == "Avg Count 12 month") {
          this.avgcount12month = val.value;
        }
        if (val.Item == "Rank Count 3 month") {
          this.rankcount3month = val.value;
        }
        if (val.Item == "Rank Count 12 month") {
          this.rankcount12month = val.value;
        }
        if (val.Item == "Value Last Day") {
          this.yesterdaytvalue = val.value;
        }
        if (val.Item == "Volume last Day") {
          this.yesterdaytvolume = val.value;
        }
        if (val.Item == "Count Last Day") {
          this.yesterdaytcount = val.value;
        }
        if (val.Item == "Market Cap Last Day") {
          this.marketcapyesterday = val.value;
        }
        if (val.Item == "Market Cap Rank Last Day") {
          this.marketcapyesterdayrank = val.value;
        }
        if (val.Item == "Open Days Count in 3 months") {
          this.opendayscount3month = val.value;
        }
        if (val.Item == "Open Days Count in 12 month") {
          this.opendayscount12month = val.value;
        }
      });
    },
    // set FinancialStrength percent
    setFinancialStrengthPercent: function() {
      this.FinancialStrengthPercent = this.FinancialStrength * 10;
    },

    getWaccPercent: function(item) {
      let all = item.WACC + item.ROIC;
      return (100 * item.WACC) / all;
    },
    // get ROIC percent
    getRoicPercent: function(item) {
      let all = item.WACC + item.ROIC;
      return (100 * item.ROIC) / all;
    },
    getColor: function(value) {
      if (value >= 80) {
        return "#0DCD0A";
      } else if (value < 80 && value >= 60) {
        return "#72FF59";
      }
      if (value < 60 && value >= 40) {
        return "#FFCE00";
      } else if (value < 40 && value >= 20) {
        return "#FD6700";
      } else if (value < 20) {
        return "#FF0000";
      }
      return "";
    }
  },
  mounted() {
    // this.setFinancialStrengthPercent();
    this.populateData();
    // reference; kt_stats_widget_7_chart
  },
  watch: {
    statistics() {
      // console.log("Watcher");
      this.populateData();
    }
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.rtl_centerd {
  direction: rtl;
  text-align: center;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left;
}
.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
}
.greenItem {
  color: #088a2f93 !important;
}
.titleHeaders {
  padding: 5px;
  font-size: 0.8em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
</style>
