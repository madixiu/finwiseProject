<template>
  <div class="card  card-stretch">
    <v-skeleton-loader
      type=" table-heading, table-thead, table-tbody"
      v-if="loading"
    ></v-skeleton-loader>
    <v-card height="500">
      
    </v-card>
  </div>

  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
// import ApexChart from "@/view/content/charts/ApexChart";

export default {
  name: "NonETFSideWidget",
  components: {
    // ApexChart
  },
  props: [],
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
    // populateData() {
    //   this.DataItems2 = this.statistics;
    //   Object.keys(this.DataItems2).forEach(key => {
    //     let val = this.DataItems2[key]; // value of the current key
    //     if (val.Item == "Avg Value 3 month") {
    //       this.avgval3month = val.value;
    //     }
    //     if (val.Item == "Avg Value 12 month") {
    //       this.avgval12month = val.value;
    //     }
    //     if (val.Item == "Rank _ value 3 month") {
    //       this.rankval3month = val.value;
    //     }
    //     if (val.Item == "Rank_value 12 month") {
    //       this.rankval12month = val.value;
    //     }
    //     if (val.Item == "Avg Volume 3 month") {
    //       this.avgvol3month = val.value;
    //     }
    //     if (val.Item == "Avg Volume 12 month") {
    //       this.avgvol12month = val.value;
    //     }
    //     if (val.Item == "Rank Volume 3 month") {
    //       this.rankvol3month = val.value;
    //     }
    //     if (val.Item == "Rank Volume 12 month") {
    //       this.rankvol12month = val.value;
    //     }
    //     if (val.Item == "Avg Count 3 month") {
    //       this.avgcount3month = val.value;
    //     }
    //     if (val.Item == "Avg Count 12 month") {
    //       this.avgcount12month = val.value;
    //     }
    //     if (val.Item == "Rank Count 3 month") {
    //       this.rankcount3month = val.value;
    //     }
    //     if (val.Item == "Rank Count 12 month") {
    //       this.rankcount12month = val.value;
    //     }
    //     if (val.Item == "Value Last Day") {
    //       this.yesterdaytvalue = val.value;
    //     }
    //     if (val.Item == "Volume last Day") {
    //       this.yesterdaytvolume = val.value;
    //     }
    //     if (val.Item == "Count Last Day") {
    //       this.yesterdaytcount = val.value;
    //     }
    //     if (val.Item == "Market Cap Last Day") {
    //       this.marketcapyesterday = val.value;
    //     }
    //     if (val.Item == "Market Cap Rank Last Day") {
    //       this.marketcapyesterdayrank = val.value;
    //     }
    //     if (val.Item == "Open Days Count in 3 months") {
    //       this.opendayscount3month = val.value;
    //     }
    //     if (val.Item == "Open Days Count in 12 month") {
    //       this.opendayscount12month = val.value;
    //     }
    //   });
    // },
    // populateData2() {
    //   this.DataItems3 = this.hh;
    //   if (this.DataItems3.length != 0) {
    //     this.countbuyerHaghighi = this.DataItems3[0]["CountBuy_Haghighi"];
    //     this.countbuyerHoghughi = this.DataItems3[0]["CountBuy_Hoguhgi"];
    //     this.volumebuyerHaghighi = this.DataItems3[0]["VolumeBuy_Haghighi"];
    //     this.volumebuyerHoghughi = this.DataItems3[0]["VolumeBuy_Hoghughi"];
    //     this.countsellerHaghighi = this.DataItems3[0]["CountSell_Haghighi"];
    //     this.countsellerHoghughi = this.DataItems3[0]["CountSell_Hoghughi"];
    //     this.volumesellerHaghighi = this.DataItems3[0]["VolumeSell_Haghighi"];
    //     this.volumesellerHoghughi = this.DataItems3[0]["VolumeSell_Hoghughi"];
    //   }
    // },
    // populateData3() {
    //   this.DataItems3 = this.liveData;
    //   if (this.DataItems3.length != 0) {
    //     this.tickerfull = this.DataItems3[0]["name"];
    //     this.tradeVolume = this.DataItems3[0]["TradeVolume"];
    //     this.tradevalue = this.DataItems3[0]["TradeValue"];
    //     this.tradecount = this.DataItems3[0]["TradeCount"];
    //     this.marketcap =
    //       this.DataItems3[0]["close"] * this.DataItems3[0]["ShareCount"];

    //     this.low = this.DataItems3[0]["low"];
    //     this.first = this.DataItems3[0]["first"];
    //     this.last = this.DataItems3[0]["last"];
    //     this.close = this.DataItems3[0]["close"];
    //     this.market = this.DataItems3[0]["market"];
    //     this.high = this.DataItems3[0]["high"];
    //     this.open = this.DataItems3[0]["yesterday"];
    //     this.Nemad = this.DataItems3[0]["ticker"];
    //     this.eps = this.DataItems3[0]["EPS"];
    //     this.sharecount = this.DataItems3[0]["ShareCount"];
    //     this.shenavar = this.DataItems3[0]["Shenavari"];
    //     this.mabna = this.DataItems3[0]["Mabna"];
    //     this.status = this.DataItems3[0]["Status"];
    //   }
    // },
    // set FinancialStrength percent


  },
  mounted() {
    // this.populateData();
    // this.populateData2();
    // this.populateData3();
    this.loading = false;
  },
  watch: {
    statistics() {
    //   this.populateData();
    },
    hh() {
    //   this.populateData2();
    },
    liveData() {
      this.loading = false;
    //   this.populateData3();
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
