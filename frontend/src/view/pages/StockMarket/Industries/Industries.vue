<template>
  <div>
    <div class="row" style="padding-top:5px">
      <div
        class="col-xxl-3 col-md-3 col-sm-6 col-xs-12"
        style="padding-left:0px"
      >
        <v-card :loading="Pieseries.length == 0" shaped>
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >ارزش بازار صنایع</v-toolbar-title
            >
            <v-spacer></v-spacer>

            <v-btn icon v-if="PieChartkey == 1" @click="PieChartBackButton">
              <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
          </v-toolbar>
          <!-- <v-card-title>ارزش بازار صنایع</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider> -->
          <v-skeleton-loader
            v-if="!Pieseries.length"
            v-bind="attrs"
            type="card-avatar, article, actions"
          ></v-skeleton-loader>
          <ApexChart
            :key="ApexChartcomponentKey"
            v-if="Pieseries.length"
            type="pie"
            height="300%"
            width="100%"
            :series="Pieseries"
            :chartOptions="PiechartOptions"
          />
        </v-card>
        <v-card :loading="Barseries.length == 0" class="mt-3" shaped>
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >صنایع با بیشترین ارزش معاملات</v-toolbar-title
            >
          </v-toolbar>
          <v-skeleton-loader
            v-if="!Barseries.length"
            v-bind="attrs"
            type="card"
          ></v-skeleton-loader>
          <ApexChart
            v-if="Barseries.length"
            type="bar"
            height="180%"
            width="100%"
            :series="Barseries"
            :chartOptions="BarchartOptions"
          />
        </v-card>
      </div>
      <div
        class="col-xxl-9 col-md-9 col-sm-12 col-xs-12"
        style="padding-right:10px"
      >
        <!--//! Changed HH -->
        <v-card rounded="lg" :loading="HHseries.length == 0">
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >ورود و خروج حقیقی به صنایع</v-toolbar-title
            >
          </v-toolbar>
          <v-skeleton-loader
            v-if="HHseries.length == 0"
            v-bind="attrs"
            type="card"
          ></v-skeleton-loader>
          <HHChart
            v-if="HHseries.length != 0"
            :HHseries="HHseries"
            :HHLabels="HHLabels"
            :HHmax="HHmax"
            :HHmin="HHmin"
          ></HHChart>
        </v-card>

        <v-card
          rounded="lg"
          class="mt-3"
          :loading="EffectOnIndexSeries.length == 0"
        >
          <v-toolbar dense class="elevation-2" style="height:36px;">
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >تاثیر صنایع در شاخص</v-toolbar-title
            >
          </v-toolbar>
          <v-skeleton-loader
            v-if="!EffectOnIndexSeries.length"
            v-bind="attrs"
            type="card"
          ></v-skeleton-loader>
          <EffectOnIndexChart
            v-if="EffectOnIndexSeries.length != 0"
            :EffectOnIndexSeries="EffectOnIndexSeries"
            :EffectOnIndexLabels="EffectOnIndexLabels"
            :EffectOnIndexmin="EffectOnIndexmin"
            :EffectOnIndexmax="EffectOnIndexmax"
          ></EffectOnIndexChart>
        </v-card>
      </div>
      <div class="col-12 pt-0">
        <IndustryChart :inputData="this.IndustryData"></IndustryChart>
      </div>
    </div>
  </div>
</template>
<script>
import HHChart from "@/view/pages/StockMarket/Industries/Content/HHChart.vue";
import EffectOnIndexChart from "@/view/pages/StockMarket/Industries/Content/EffectOnIndex.vue";
import ApexChart from "@/view/content/charts/ApexChart";
import IndustryChart from "@/view/pages/StockMarket/Industries/Content/IndustriesChart.vue";
// import IndustryTechnicalBest from "@/view/pages/StockMarket/Industries/Content/IndustryTechnical‌Best";
// import IndustryTechnicalWorse from "@/view/pages/StockMarket/Industries/Content/IndustryTechnicalWorse";
export default {
  name: "Industries",
  components: {
    ApexChart,
    HHChart,
    EffectOnIndexChart,
    IndustryChart
    // IndustryTechnicalBest,
    // IndustryTechnicalWorse,
  },
  data() {
    return {
      attrs: {
        class: "mb-6",
        boilerplate: true,
        elevation: 2
      },
      ApexChartcomponentKey: 0,
      PieChartData: null,
      PieChartkey: 0,
      // paused: false,
      TopIndustries: [],
      IndustryData: [],
      persianNamesOthers: [],
      marketCapsOthers: [],
      Pieseries: [],
      PieseriesOthers: [],
      Barseries: [],
      HHseries: [],
      HHLabels: [],
      HHmax: null,
      HHmin: null,

      EffectOnIndexSeries: [],
      EffectOnIndexLabels: [],
      EffectOnIndexmin: null,
      EffectOnIndexmax: null,

      BarchartOptions: {
        chart: {
          type: "bar",
          height: 350,
          animations: {
            enabled: false
          },
          toolbar: {
            show: false
          }
        },
        legend: {
          show: false
        },
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: "70%",
            distributed: true
          }
        },
        colors: [
          "#011627",
          "#E09F3E",
          "#9E2A2B",
          "#05668D",
          "#1AA47C",
          "#335C67"
        ],
        dataLabels: {
          enabled: true,
          formatter: function(value) {
            let n = value / 1000000000;
            let negative = false;
            let digits = 0;
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
            let parts = n.toString().split(".");
            parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            return parts.join(".");
          },
          // offsetX:10,
          offsetY: 5,
          textAnchor: "middle",
          style: {
            fontSize: "0.8em",
            fontFamily: "Vazir-Medium-FD",
            colors: ["#fff"]
          }
        },
        xaxis: {
          categories: [],
          title: {
            text: "میلیارد ریال",
            offsetY: 25
          },
          labels: {
            // eslint-disable-next-line no-unused-vars
            formatter: function(value, opts) {
              let n = value / 1000000000;
              let negative = false;
              let digits = 0;
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
              let parts = n.toString().split(".");
              parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              return parts.join(".");
            },
            show: true,
            style: {
              fontFamily: "Vazir-Medium-FD"
            }
          },

          offsetX: 109,
          offsetY: 500
        },
        tooltip: {
          followCursor: true,
          intersect: false,
          fillSeriesColor: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let n = series[seriesIndex][dataPointIndex];
            // let val = ""
            if (n != undefined) {
              //   let parts = n.toString().split(".");
              // parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              //  val = parts.join(".");
              let val = n.toLocaleString();
              return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${w.globals.labels[dataPointIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span style=color:#000;font-size:0.8em class=mr-1>ریال</span>

              <span style=color:#000;font-size:0.8em>${val}</span>
            

              </div>
              </div>
            `;
            } else {
              return null;
            }

            // n = n.toString().toLocaleString();
          }
        }
      },
      PiechartOptions: {
        chart: {
          width: 400,
          height: 100,
          type: "pie",
          fontFamily: "Vazir-Medium-FD",
          animations: {
            enabled: true
          },
          events: {
            // legendClick: function(chartContext, seriesIndex, config) {
            // },
            dataPointSelection: (event, chartContext, config) => {
              this.pieChartClick(chartContext, config.dataPointIndex);
            }
          }
        },
        legend: {
          // show: false,
          fontSize: 10,
          fontFamily: "Vazir-Medium-FD",
          position: "bottom"
        },
        colors: [
          "#EF476F",
          "#E09F3E",
          "#5F2663",
          "#118AB2",
          "#073B4C",
          "#73BB6F",
          "#068292",
          "#50A3AB",
          "#B50D45",
          "#5ACCB7"
        ],
        labels: [],
        stroke: {
          width: 1,
          colors: ["#3e3e4e"]
        },
        responsive: [
          {
            breakpoint: 400,
            options: {
              chart: {
                width: 200
              }
            }
          }
        ],
        tooltip: {
          // eslint-disable-next-line no-unused-vars
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let backgroundColor = w.config.colors[seriesIndex];
            let n = series[seriesIndex];
            // let val = ""
            if (n != undefined) {
              //   let parts = n.toString().split(".");
              // parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              //  val = parts.join(".");
              let val = (n / 1000000000).toLocaleString();
              return `<div class="ApexTooltip">
            <div class="topDivTooltip" style=background-color:${backgroundColor}> 
              <span style=color:#fff>
              ${w.globals.labels[seriesIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span style=color:#000;font-size:0.8em class=mr-1>میلیارد ریال</span>
              <span style=color:#000;font-size:0.8em>${val}</span>

            

              </div>
              </div>
            `;
            } else {
              return null;
            }
          }
        }
      }
    };
  },
  created() {
    document.title = "Finwise - صنایع";
    this.loadData();
  },
  methods: {
    forceUpdate() {
      this.ApexChartcomponentKey += 1;
    },
    PieChartBackButton() {
      // console.log(this.PieChartData);
      let data = JSON.parse(JSON.stringify(this.PieChartData));
      // console.log(data);

      let marketCaps = data.TopIndustries.marketCap;
      let persianNames = data.TopIndustries.persianName;
      this.Pieseries = marketCaps;
      this.PiechartOptions.labels = persianNames;
      this.PieChartkey = 0;
      this.forceUpdate();
    },
    checkSign(change) {
      if (change > 0) return "industryApexChartTooltipGreenSpan";
      else if (change < 0) return "industryApexChartTooltipRedSpan";
      else return "industryApexChartTooltipBlackSpan";
    },
    pieChartClick(context, seriesIndex) {
      if (seriesIndex == 9 && this.PieChartkey == 0) {
        let data = JSON.parse(JSON.stringify(this.PieChartData));

        this.Pieseries = data.OtherIndustries.marketCap;
        this.PiechartOptions.labels = data.OtherIndustries.persianName;
        this.PieChartkey = 1;
        this.forceUpdate();
      } else if (seriesIndex != 9 && this.PieChartkey == 0) {
        // let name = context.w.globals.labels[seriesIndex];
        this.$router.push({
          name: "IndustriesDetail",
          params: { id: this.PieChartData.TopIndustries.indexID[seriesIndex] }
        });
      } else {
        this.$router.push({
          name: "IndustriesDetail",
          params: { id: this.PieChartData.OtherIndustries.indexID[seriesIndex] }
        });
      }
    },
    changeTimeFrame() {
      this.ReturnSeries = [
        { data: [123, 121, 110, 100, 98, 90, 76, 68, 61, 57, 43] }
      ];
      document.getElementById("fi").style.color = "red !important";
    },
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getPieChartData().then(resx => {
        // eslint-disable-next-line no-unused-vars
        this.getHHDATA().then(resz => {
          // eslint-disable-next-line no-unused-vars
          this.getImpactData().then(resy => {
            this.getIndustries();
          });
        });
      });
    },
    async getPieChartData() {
      await this.axios.get("/api/IndexMarketCap").then(responsive => {
        let data = responsive.data;
        // BarChart Data injection **************
        this.Barseries = [{ data: data.BarChart.TradeValue }];
        this.BarchartOptions.xaxis.categories = data.BarChart.persianName;
        // *************************************

        //? PieChart Data injection**************
        this.PieChartData = data.PieChart;
        let marketCaps = data.PieChart.TopIndustries.marketCap;
        marketCaps.push(data.PieChart.OtherIndustries.marketCapSum);
        let persianNames = data.PieChart.TopIndustries.persianName;
        persianNames.push("سایر");
        this.Pieseries = marketCaps;
        this.PiechartOptions.labels = persianNames;
      });
    },
    async getIndustries() {
      await this.axios
        .get("/api/Indices/HistoricCap/")
        .then(responseInd => {
          this.IndustryData = responseInd.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getHHDATA() {
      await this.axios
        .get("/api/Indices/HH")
        .then(responsea => {
          let data = responsea.data;
          let HHseries2Labels = [];
          let HHseries2data = [];
          for (let i = 0; i < data.length; i++) {
            HHseries2Labels.push(data[i]["CorrectName"]);
            HHseries2data.push(data[i]["sum"]);
          }
          this.HHseries = [{ data: HHseries2data }];
          //    // this.HHoptions.labels = HHseries2Labels;
          //  // this.HHoptions.xaxis.categories = HHseries2Labels;
          this.HHLabels = HHseries2Labels;

          if (
            HHseries2data[0] >=
            Math.abs(HHseries2data[HHseries2data.length - 1])
          ) {
            //      // this.HHoptions.yaxis.min = HHseries2data[0] * -1;
            //      // this.HHoptions.yaxis.max = HHseries2data[0];
            this.HHmin = HHseries2data[0] * -1;
            this.HHmax = HHseries2data[0];
          } else {
            //      // this.HHoptions.yaxis.min = HHseries2data[HHseries2data.length - 1];
            //      // this.HHoptions.yaxis.max = Math.abs(
            //      //   HHseries2data[HHseries2data.length - 1]
            //      // );
            this.HHmin = HHseries2data[HHseries2data.length - 1];
            this.HHmax = Math.abs(HHseries2data[HHseries2data.length - 1]);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getImpactData() {
      await this.axios
        .get("/api/Indices/Impact")
        .then(responsea => {
          if (responsea.data != "noData") {
            let data = responsea.data;
            let Impactseries2Labels = [];
            let Impactseries2data = [];
            for (let i = 0; i < data.length; i++) {
              Impactseries2Labels.push(data[i]["CorrectName"]);
              Impactseries2data.push(data[i]["IMPACT"]);
            }
            this.EffectOnIndexSeries = [{ data: Impactseries2data }];
            this.EffectOnIndexLabels = Impactseries2Labels;
            //// this.EffectOnIndexOptions.labels = Impactseries2Labels;
            //// this.EffectOnIndexOptions.xaxis.categories = Impactseries2Labels;

            if (
              Impactseries2data[0] >=
              Math.abs(Impactseries2data[Impactseries2data.length - 1])
            ) {
              //// this.EffectOnIndexOptions.yaxis.min = Impactseries2data[0] * -1;
              //// this.EffectOnIndexOptions.yaxis.max = Impactseries2data[0];
              this.EffectOnIndexmax = Impactseries2data[0];
              this.EffectOnIndexmin = Impactseries2data[0] * -1;
            } else {
              //// this.EffectOnIndexOptions.yaxis.min =
              ////   Impactseries2data[Impactseries2data.length - 1];
              //// this.EffectOnIndexOptions.yaxis.max = Math.abs(
              ////   Impactseries2data[Impactseries2data.length - 1]
              //// );
              this.EffectOnIndexmax = Math.abs(
                Impactseries2data[Impactseries2data.length - 1]
              );
              this.EffectOnIndexmin =
                Impactseries2data[Impactseries2data.length - 1];
            }
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    compareValues(key, order = "asc") {
      return function innerSort(a, b) {
        if (!a.hasOwnProperty(key) || !b.hasOwnProperty(key)) {
          // property doesn't exist on either object
          return 0;
        }

        const varA = typeof a[key] === "string" ? a[key].toUpperCase() : a[key];
        const varB = typeof b[key] === "string" ? b[key].toUpperCase() : b[key];

        let comparison = 0;
        if (varA > varB) {
          comparison = 1;
        } else if (varA < varB) {
          comparison = -1;
        }
        return order === "desc" ? comparison * -1 : comparison;
      };
    }
  }
};
</script>
<style scoped></style>
