<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <!-- <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        {{ this.Nemad }}<span class="small mr-5">{{ this.tickerfull }}</span>
      </h3>
    </div> -->
    <div class="row border-0 pb-4 pt-2">
      <div class="col-xxl-3 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1E88E5" text-color="#FAFAFA">
          بازار
        </v-chip>
        {{ this.market }}
      </div>
      <div class="col-xxl-3 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1E88E5" text-color="#FAFAFA">
          صنعت
        </v-chip>
        {{ this.industry }}
      </div>
      <div class="col-xxl-3 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1E88E5" text-color="#FAFAFA">
          تابلو
        </v-chip>
        {{ this.tablo }}
      </div>
      <div class="col-xxl-3 FinancialStrength pr-5 pb-2 pt-2">
        <v-chip class="ma-2 mr-2" color="#1E88E5" text-color="#FAFAFA">
          گروه
        </v-chip>
        {{ this.subindustry }}
      </div>
    </div>

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
            <v-card-text>
              <div class="row">
                <div class="col-xxl-3 FinancialStrength">
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
                  <h5 class="titleHeaders">
                    ارزش بازار : {{ this.marketcap }}
                  </h5>
                </div>

                <div class="col-xxl-3 FinancialStrength">
                  <h5 class="titleHeaders">کف قیمت : {{ this.min }}</h5>
                  <h5 class="titleHeaders">سقف قیمت: {{ this.max }}</h5>
                  <h5 class="titleHeaders">کمترین قیمت: {{ this.low }}</h5>
                  <h5 class="titleHeaders">بیشترین قیمت : {{ this.high }}</h5>
                </div>
                <div class="col-xxl-3 FinancialStrength">
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
                <div class="col-xxl-3 FinancialStrength">
                  <h5 class="titleHeaders">چارت</h5>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <div class="row">
                <div class="col-xxl-3">
                  <h5 class="titleHeaders">خریداران حقیقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد خریداران : {{ this.countbuyerHaghighi }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم خرید : {{ this.volumebuyerHaghighi }}
                  </h5>
                </div>
                <div class="col-xxl-3">
                  <h5 class="titleHeaders">خریداران حقوقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد خریداران : {{ this.countbuyerHoghughi }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم خرید : {{ this.volumebuyerHoghughi }}
                  </h5>
                </div>
                <div class="col-xxl-3">
                  <h5 class="titleHeaders">فروشندگان حقیقی</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    تعداد فروشندگان : {{ this.countsellerHaghighi }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم فروش : {{ this.volumesellerHaghighi }}
                  </h5>
                </div>
                <div class="col-xxl-3">
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
                <div class="col-xxl-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات ارزش معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    میانگین ارزش معاملات ۳ ماهه : {{ this.avgval3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    میانگین ارزش معاملات ۱۲ ماهه : {{ this.avgval12month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین ارزش معاملات ۳ ماهه :{{ this.rankval3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین ارزش معاملات ۱۲ ماهه :{{ this.rankval12month }}
                  </h5>
                </div>
                <div class="col-xxl-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات حجم معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    میانگین حجم معاملات ۳ ماهه : {{ this.avgvol3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    میانگین حجم معاملات ۱۲ ماهه : {{ this.avgvol12month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین حجم معاملات ۳ ماهه :{{ this.rankvol3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    رتبه میانگین حجم معاملات ۱۲ ماهه :{{ this.rankvol12month }}
                  </h5>
                </div>
                <div class="col-xxl-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات تعداد معاملات</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    میانگین تعداد معاملات ۳ ماهه : {{ this.avgcount3month }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    میانگین تعداد معاملات ۱۲ ماهه : {{ this.avgcount12month }}
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
                <div class="col-xxl-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات معاملاتی آخرین روز</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    ارزش معاملات آخرین روز : {{ this.yesterdaytvalue }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    حجم معاملات آخرین روز : {{ this.yesterdaytvolume }}
                  </h5>
                  <h5 class="titleHeaders-smaller ">
                    تعداد معاملات آخرین روز :{{ this.yesterdaytcount }}
                  </h5>
                </div>
                <div class="col-xxl-2 FinancialStrength">
                  <h5 class="titleHeaders">اطلاعات ارزش بازار</h5>
                  <hr />
                  <h5 class="titleHeaders-smaller ">
                    ارزش بازار دیروز : {{ this.marketcapyesterday }}
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

export default {
  name: "PWidget",
  data() {
    return {
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
      avgval3month: 123,
      avgval12month: 113,
      rankval3month: 2,
      rankval12month: 8,
      avgvol3month: 12312312312,
      avgvol12month: 22231112,
      rankvol3month: 5,
      rankvol12month: 15,
      avgcount3month: 12311111,
      avgcount12month: 5153,
      rankcount3month: 15,
      rankcount12month: 18,
      marketcapyesterday: 454848484848,
      marketcapyesterdayrank: 12,
      yesterdaytvalue: 848484,
      yesterdaytvolume: 848484,
      yesterdaytcount: 848484,
      opendayscount3month: 48,
      opendayscount12month: 210,
      countbuyerHaghighi: 154,
      countbuyerHoghughi: 2,
      volumebuyerHaghighi: 1544444,
      volumebuyerHoghughi: 188791157,
      countsellerHaghighi: 250,
      countsellerHoghughi: 15,
      volumesellerHaghighi: 14844,
      volumesellerHoghughi: 1848484
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
    // reference; kt_stats_widget_7_chart
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
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
</style>
