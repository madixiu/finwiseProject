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
    ...mapGetters(["layoutConfig"])
  },
  methods: {
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
