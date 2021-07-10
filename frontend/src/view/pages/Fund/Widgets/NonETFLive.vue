<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <v-skeleton-loader
      type=" table-heading, table-thead, table-tbody"
      v-if="loading"
    ></v-skeleton-loader>
    <v-card>
      <v-tabs grow center-active color="#333333" v-if="loading == false">
        <v-tabs-slider color="#333333"></v-tabs-slider>
        <v-tab class="FinancialStrength">
          نگاه کلی
          <v-icon left small>mdi-poll</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          اطلاعات معامله
          <v-icon left small>mdi-shopping</v-icon>
        </v-tab>
        <v-tab  class="FinancialStrength">
          چارت
          <v-icon left small>mdi-poll</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          اخبار
          <v-icon left small>mdi-newspaper</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          تاریخچه
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          نوع دارایی
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          صنایع سرمایه گذاری شده
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          بازدهی صندوق
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          اطلاعات صندوق
          <v-icon left small>mdi-chart-line</v-icon>
        </v-tab>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text>
              <div class="row">
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات قیمت</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    قیمت پایانی :
                    <span class="spandata">{{ this.close }} ریال</span> (
                    <span
                      dir="ltr"
                      class="spandata"
                      v-bind:class="[
                        this.close > this.open ? 'greenItem' : 'redItem'
                      ]"
                    >
                      %{{ setclosingperc.toString() }}
                    </span>
                    )

                    <v-icon
                      left
                      small
                      v-bind:class="[
                        this.close >= this.open ? 'greenItem' : 'redItem'
                      ]"
                      >mdi-chevron-{{
                        this.close >= this.open ? "up" : "down"
                      }}</v-icon
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    قیمت آخرین معامله :
                    <span class="spandata">{{ this.last }} ریال</span> (
                    <span
                      dir="ltr"
                      class="spandata"
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
                      >mdi-chevron-{{
                        this.last >= this.open ? "up" : "down"
                      }}</v-icon
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    اولین قیمت :
                    <span class="spandata">{{ this.first }} ریال</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    ارزش بازار :
                    <span class="spandata" v-if="!isNaN(this.marketcap)"
                      >{{
                        numberWithCommas(
                          roundTo(this.marketcap / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                  </h5>
                </div>

                <div
                  class="col-xl-4 col-lg-5 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">مشخصات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    وضعیت:
                    <span class="spandata">{{ this.status }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    EPS (منبع TSE):
                    <span class="spandata" dir="ltr">{{ this.eps }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    تعداد سهام:
                    <span class="spandata" dir="ltr">
                      {{
                        numberWithCommas(
                          roundTo(this.sharecount / 1000000000, 2)
                        )
                      }}
                      میلیارد
                    </span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    درصد شناوری :
                    <span class="spandata">{{ this.shenavar }}</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم مبنا :
                    <span class="spandata">
                      {{ numberWithCommas(roundTo(this.mabna / 1000000, 2)) }}
                      میلیون سهم</span
                    >
                  </h5>
                </div>
                <div
                  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد معاملات :
                    <span class="spandata">
                      {{ numberWithCommas(this.tradecount) }}
                    </span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم معاملات :
                    <span class="spandata" v-if="!isNaN(this.tradeVolume)"
                      >{{
                        numberWithCommas(roundTo(this.tradeVolume / 1000000, 2))
                      }}
                      میلیون</span
                    >
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    ارزش معاملات :
                    <span class="spandata" v-if="!isNaN(this.tradevalue)"
                      >{{
                        numberWithCommas(
                          roundTo(this.tradevalue / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                  </h5>
                </div>
                <!-- <div
                  class="col-xl-3 col-lg-3 col-md-6 col-sm-12 FinancialStrength"
                > -->
                <!-- here -->
                <!-- <h5 class="titleHeaders-smaller ">چارت</h5> -->
                <!-- <ApexChart
                    type="area"
                    height="100%"
                    width="100%"
                    :series="priceOverViewSeries"
                    :chartOptions="priceOverViewchartOptions"
                  >
                  </ApexChart> -->
                <!-- </div> -->
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card height="450" flat>
            <v-card-text> </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
// import ApexChart from "@/view/content/charts/ApexChart";

export default {
  name: "NonETFMainWidget",
  components: {
    // ApexChart
  },
  props: ["meta", "industry", "assettype"],
  data() {
    return {
      loading: false,
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
      Nemad: "",
      tickerfull: "",
      subindustry: "",
      market: "",
      tablo: "",
      close: "",
      open: "",
      first: "",
      last: "",
      high: "",
      low: "",
      tradeVolume: "",
      tradevalue: "",
      tradecount: "",
      marketcap: "",
      min: "",
      max: "",
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
      volumesellerHoghughi: "-",
      eps: "",
      sharecount: "",
      mabna: "",
      shenavar: "",
      status: ""
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
      this.DataItems1 = this.meta;
    },
    populateData2() {
      this.DataItems2 = this.industry;
      // if (this.DataItems3.length != 0) {
      //   this.countbuyerHaghighi = this.DataItems3[0]["CountBuy_Haghighi"];
      //   this.countbuyerHoghughi = this.DataItems3[0]["CountBuy_Hoguhgi"];
      //   this.volumebuyerHaghighi = this.DataItems3[0]["VolumeBuy_Haghighi"];
      //   this.volumebuyerHoghughi = this.DataItems3[0]["VolumeBuy_Hoghughi"];
      //   this.countsellerHaghighi = this.DataItems3[0]["CountSell_Haghighi"];
      //   this.countsellerHoghughi = this.DataItems3[0]["CountSell_Hoghughi"];
      //   this.volumesellerHaghighi = this.DataItems3[0]["VolumeSell_Haghighi"];
      //   this.volumesellerHoghughi = this.DataItems3[0]["VolumeSell_Hoghughi"];
      // }
    },
    populateData3() {
      this.DataItems3 = this.assettype;
      // if (this.DataItems3.length != 0) {
      //   this.tickerfull = this.DataItems3[0]["name"];
      //   this.tradeVolume = this.DataItems3[0]["TradeVolume"];
      //   this.tradevalue = this.DataItems3[0]["TradeValue"];
      //   this.tradecount = this.DataItems3[0]["TradeCount"];
      //   this.marketcap =
      //     this.DataItems3[0]["close"] * this.DataItems3[0]["ShareCount"];

      //   this.low = this.DataItems3[0]["low"];
      //   this.first = this.DataItems3[0]["first"];
      //   this.last = this.DataItems3[0]["last"];
      //   this.close = this.DataItems3[0]["close"];
      //   this.market = this.DataItems3[0]["market"];
      //   this.high = this.DataItems3[0]["high"];
      //   this.open = this.DataItems3[0]["yesterday"];
      //   this.Nemad = this.DataItems3[0]["ticker"];
      //   this.eps = this.DataItems3[0]["EPS"];
      //   this.sharecount = this.DataItems3[0]["ShareCount"];
      //   this.shenavar = this.DataItems3[0]["Shenavari"];
      //   this.mabna = this.DataItems3[0]["Mabna"];
      //   this.status = this.DataItems3[0]["Status"];
      // }
    }
  },
  mounted() {
    this.populateData();
    // this.populateData2();
    // this.populateData3();
  },
  watch: {
    meta() {
      this.populateData();
    },
    industry() {
      // this.populateData2();
    },
    assettype() {
      this.loading = false;
      // this.populateData3();
    }
  }
};
</script>
<style scoped>
.subheaderTitles {
  font-size: 1.1em;
  font-weight: 900;
  text-align: center;
}

.FinancialStrength {
  direction: rtl;
  text-align: right;
  font-size: 1em;
  
  letter-spacing: 0px;
}
/* .v-tab {
color: black;
} */

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
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smallest {
  padding: 5px;
  font-size: 1em;
  font-weight: 700;
  text-align: right;
  font-family: "Vazir-Medium-FD";
}
.titleHeaders-smaller {
  padding: 5px;
  font-size: 1.2em;
  font-weight: 700;
  /* text-align: right; */
  font-family: "Vazir-Medium-FD";
}
.spandata {
  color: rgb(4, 17, 53);
  font-size: 1.1em;
  font-weight: 800;
  margin-top: 5px;
  font-family: "Vazir-Medium-FD";
}
</style>
