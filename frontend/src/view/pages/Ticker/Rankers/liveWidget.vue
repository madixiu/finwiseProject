<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <v-skeleton-loader
      type=" table-heading, table-thead, table-tbody"
      v-if="loading"
    ></v-skeleton-loader>
    <v-card>
      <v-tabs vertical v-if="loading == false">
        <v-tab class="FinancialStrength">
          اطلاعات معاملات
          <v-icon left>mdi-access-point</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          حقیقی -حقوقی
          <v-icon left>mdi-account-circle</v-icon>
        </v-tab>
        <v-tab class="FinancialStrength">
          آمار سهم
          <v-icon left>mdi-thermostat</v-icon>
        </v-tab>
        <!-- <v-tab class="FinancialStrength">
          اطلاعات سهم
          <v-icon left>mdi-information-variant</v-icon>
        </v-tab> -->
        <v-tab-item>
          <v-card flat>
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
          <v-card flat>
            <v-card-text>
              <div class="row">
                <div
                  class="col-xl-3 col-lg-3 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">خریداران حقیقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد خریداران :
                    <span
                      class="spandata"
                      v-if="!isNaN(this.countbuyerHaghighi)"
                    >
                      {{ numberWithCommas(this.countbuyerHaghighi) }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم خرید :
                    <span
                      class="spandata"
                      v-if="!isNaN(this.volumebuyerHaghighi)"
                    >
                      {{ numberWithCommas(this.volumebuyerHaghighi) }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-3 col-lg-3 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">خریداران حقوقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد خریداران :
                    <span
                      class="spandata"
                      v-if="!isNaN(this.countbuyerHoghughi)"
                    >
                      {{ numberWithCommas(this.countbuyerHoghughi) }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم خرید :

                    <span
                      class="spandata"
                      v-if="!isNaN(this.volumebuyerHoghughi)"
                    >
                      {{ numberWithCommas(this.volumebuyerHoghughi) }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-3 col-lg-3 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">فروشندگان حقیقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد فروشندگان :
                    <span
                      class="spandata"
                      v-if="!isNaN(this.countsellerHaghighi)"
                    >
                      {{ numberWithCommas(this.countsellerHaghighi) }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم فروش :
                    <span
                      class="spandata"
                      v-if="!isNaN(this.volumesellerHaghighi)"
                    >
                      {{ numberWithCommas(this.volumesellerHaghighi) }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-3 col-lg-3 col-md-6 col-sm-12 FinancialStrength"
                >
                  <h5 class="subheaderTitles">فروشندگان حقوقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد فروشندگان :
                    <span
                      class="spandata"
                      v-if="!isNaN(this.countsellerHoghughi)"
                    >
                      {{ numberWithCommas(this.countsellerHoghughi) }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم فروش :
                    <span
                      class="spandata"
                      v-if="!isNaN(this.volumesellerHoghughi)"
                    >
                      {{ numberWithCommas(this.volumesellerHoghughi) }}
                    </span>
                    <span v-else>بدون داده</span>
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
                <div
                  class="col-xl-2 col-lg-2 col-md-4 col-sm-6 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات ارزش معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smallest">
                    میانگین ارزش معاملات ۳ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.avgval3month)"
                      >{{
                        numberWithCommas(
                          roundTo(this.avgval3month / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    میانگین ارزش معاملات ۱۲ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.avgval12month)"
                      >{{
                        numberWithCommas(
                          roundTo(this.avgval12month / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    رتبه میانگین ارزش معاملات ۳ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.rankval3month)">
                      {{ this.rankval3month }}</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    رتبه میانگین ارزش معاملات ۱۲ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.rankval12month)">
                      {{ this.rankval12month }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-2 col-lg-2 col-md-4 col-sm-6 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات حجم معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smallest ">
                    میانگین حجم معاملات ۳ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.avgval3month)">
                      {{
                        numberWithCommas(
                          roundTo(this.avgval3month / 1000000000, 2)
                        )
                      }}
                      میلیون</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    میانگین حجم معاملات ۱۲ ماهه :
                    <br /><br />
                    <span v-if="!isNaN(this.avgval12month)" class="spandata"
                      >{{
                        numberWithCommas(
                          roundTo(this.avgvol12month / 1000000, 2)
                        )
                      }}<br />
                      میلیون
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    رتبه میانگین حجم معاملات ۳ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.rankvol3month)">
                      {{ this.rankvol3month }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    رتبه میانگین حجم معاملات ۱۲ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.rankvol12month)">
                      {{ this.rankvol12month }}
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-2 col-lg-2 col-md-4 col-sm-6 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات تعداد معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smallest ">
                    میانگین تعداد معاملات ۳ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.avgcount3month)">
                      {{ numberWithCommas(this.avgcount3month) }}<br />
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    میانگین تعداد معاملات ۱۲ ماهه :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.avgcount12month)">
                      >{{ numberWithCommas(this.avgcount12month) }}<br />
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    رتبه میانگین تعداد معاملات ۳ ماهه :
                    <br /><br />
                    <span
                      class="spandata"
                      v-if="!isNaN(this.rankcount3month)"
                      >{{ this.rankcount3month }}</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    رتبه میانگین تعداد معاملات ۱۲ ماهه :
                    <br /><br />
                    <span
                      class="spandata"
                      v-if="!isNaN(this.rankcount12month)"
                      >{{ this.rankcount12month }}</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-2 col-lg-2 col-md-4 col-sm-6 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات معاملاتی آخرین روز</h5>
                  <hr />
                  <h5 class="titleHeaders-smallest ">
                    ارزش معاملات آخرین روز :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.yesterdaytvalue)"
                      >{{
                        numberWithCommas(
                          roundTo(this.yesterdaytvalue / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    حجم معاملات آخرین روز :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.yesterdaytvolume)"
                      >{{
                        numberWithCommas(
                          roundTo(this.yesterdaytvolume / 1000000, 2)
                        )
                      }}
                      میلیون</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    تعداد معاملات آخرین روز :
                    <br /><br />
                    <span class="spandata" v-if="!isNaN(this.yesterdaytcount)"
                      >{{ numberWithCommas(this.yesterdaytcount) }}<br />
                    </span>
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-2 col-lg-2 col-md-4 col-sm-6 FinancialStrength"
                >
                  <h5 class="subheaderTitles">اطلاعات ارزش بازار</h5>
                  <hr />
                  <h5 class="titleHeaders-smallest ">
                    ارزش بازار دیروز :
                    <br /><br />
                    <span
                      class="spandata"
                      v-if="!isNaN(this.marketcapyesterday)"
                      >{{
                        numberWithCommas(
                          roundTo(this.marketcapyesterday / 1000000000, 2)
                        )
                      }}
                      میلیارد ریال</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    رتبه ارزش بازار دیروز :
                    <br /><br />
                    <span
                      class="spandata"
                      v-if="!isNaN(this.marketcapyesterdayrank)"
                    >
                      {{ this.marketcapyesterdayrank }}</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                </div>
                <div
                  class="col-xl-2 col-lg-2 col-md-4 col-sm-6 FinancialStrength"
                >
                  <h5 class="subheaderTitles">حضور در بازار</h5>
                  <hr />
                  <h5 class="titleHeaders-smallest ">
                    تعداد روزهای باز در ۳ ماه گذشته :
                    <br /><br />

                    <span
                      class="spandata"
                      v-if="!isNaN(this.opendayscount3month)"
                    >
                      {{ this.opendayscount3month }}</span
                    >
                    <span v-else>بدون داده</span>
                  </h5>
                  <h5 class="titleHeaders-smallest ">
                    تعداد روزهای باز در ۱۲ ماه گذشته :
                    <br /><br />

                    <span
                      class="spandata"
                      v-if="!isNaN(this.opendayscount12month)"
                    >
                      {{ this.opendayscount12month }}</span
                    >
                    <span v-else>بدون داده</span>
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
// import ApexChart from "@/view/content/charts/ApexChart";

export default {
  name: "PWidget",
  components: {
    // ApexChart
  },
  props: ["statistics", "hh", "liveData"],
  data() {
    return {
      loading: true,
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
      industry: "سرمایه گذاری",
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
    populateData2() {
      this.DataItems3 = this.hh;
      if (this.DataItems3.length != 0) {
        this.countbuyerHaghighi = this.DataItems3[0]["CountBuy_Haghighi"];
        this.countbuyerHoghughi = this.DataItems3[0]["CountBuy_Hoguhgi"];
        this.volumebuyerHaghighi = this.DataItems3[0]["VolumeBuy_Haghighi"];
        this.volumebuyerHoghughi = this.DataItems3[0]["VolumeBuy_Hoghughi"];
        this.countsellerHaghighi = this.DataItems3[0]["CountSell_Haghighi"];
        this.countsellerHoghughi = this.DataItems3[0]["CountSell_Hoghughi"];
        this.volumesellerHaghighi = this.DataItems3[0]["VolumeSell_Haghighi"];
        this.volumesellerHoghughi = this.DataItems3[0]["VolumeSell_Hoghughi"];
      }
    },
    populateData3() {
      this.DataItems3 = this.liveData;
      if (this.DataItems3.length != 0) {
        this.tickerfull = this.DataItems3[0]["name"];
        this.tradeVolume = this.DataItems3[0]["TradeVolume"];
        this.tradevalue = this.DataItems3[0]["TradeValue"];
        this.tradecount = this.DataItems3[0]["TradeCount"];
        this.marketcap =
          this.DataItems3[0]["close"] * this.DataItems3[0]["ShareCount"];

        this.low = this.DataItems3[0]["low"];
        this.first = this.DataItems3[0]["first"];
        this.last = this.DataItems3[0]["last"];
        this.close = this.DataItems3[0]["close"];
        this.market = this.DataItems3[0]["market"];
        this.high = this.DataItems3[0]["high"];
        this.open = this.DataItems3[0]["yesterday"];
        this.Nemad = this.DataItems3[0]["ticker"];
        this.eps = this.DataItems3[0]["EPS"];
        this.sharecount = this.DataItems3[0]["ShareCount"];
        this.shenavar = this.DataItems3[0]["Shenavari"];
        this.mabna = this.DataItems3[0]["Mabna"];
        this.status = this.DataItems3[0]["Status"];
      }
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
    this.populateData();
    this.populateData2();
    this.populateData3();
  },
  watch: {
    statistics() {
      this.populateData();
    },
    hh() {
      this.populateData2();
    },
    liveData() {
      this.loading = false;
      this.populateData3();
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
