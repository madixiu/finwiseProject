<template>
  <div>
    <div class="row" style="padding-top:5px">
      <div
        class="col-xxl-3 col-md-3 col-sm-6 col-xs-12"
        style="padding-left:0px;padding-top:0px"
      >
        <v-card shaped>
          <v-toolbar dense>
            <v-toolbar-title>ارزش بازار صنایع</v-toolbar-title>
            <v-spacer></v-spacer>

            <v-btn icon v-if="PieChartkey == 1" @click="PieChartBackButton">
              <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
          </v-toolbar>
          <!-- <v-card-title>ارزش بازار صنایع</v-card-title>
          <v-divider class="mt-0 mb-0"></v-divider> -->

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
      </div>
      <div
        class="col-xxl-9 col-md-9 col-sm-12 col-xs-12"
        style="padding-right:10px;padding-top:0px"
      >
        <v-card v-if="Barseries.length">
          <v-toolbar dense>
            <v-toolbar-title>صنایع با بیشترین ارزش معاملات</v-toolbar-title>
          </v-toolbar>
          <ApexChart
            type="bar"
            height="200%"
            width="100%"
            :series="Barseries"
            :chartOptions="BarchartOptions"
          />
        </v-card>
        <v-card class="mt-3" v-if="HHseries.length">
          <v-toolbar dense>
            <v-toolbar-title>ورود و خروج حقیقی به صنایع</v-toolbar-title>
          </v-toolbar>
          <ApexChart
            type="bar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
        </v-card>
        <v-card class="mt-3" v-if="EffectOnIndexSeries.length">
          <v-toolbar dense>
            <v-toolbar-title>تاثیر صنایع در شاخص</v-toolbar-title>
          </v-toolbar>
          <ApexChart
            type="bar"
            width="100%"
            height="200%"
            :series="EffectOnIndexSeries"
            :chartOptions="EffectOnIndexOptions"
          />
        </v-card>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <IndustryChart :inputData="this.IndustryData"></IndustryChart>
      </div>
    </div>
  </div>
</template>
<script>
import ApexChart from "@/view/content/charts/ApexChart";
import IndustryChart from "@/view/pages/StockMarket/Industries/Content/IndustriesChart.vue";
// import IndustryTechnicalBest from "@/view/pages/StockMarket/Industries/Content/IndustryTechnical‌Best";
// import IndustryTechnicalWorse from "@/view/pages/StockMarket/Industries/Content/IndustryTechnicalWorse";
export default {
  name: "Industries",
  components: {
    ApexChart,
    IndustryChart
    // IndustryTechnicalBest,
    // IndustryTechnicalWorse,
  },
  data() {
    return {
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
      HHoptions: {
        chart: {
          animations: { enabled: false },
          type: "bar",
          height: 100,
          fontFamily: "Vazir-Medium-FD",
          // stacked: true,
          toolbar: {
            show: false
          }
        },
        tooltip: {
          followCursor: true,
          intersect: false,
          fillSeriesColor: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let n = series[seriesIndex][dataPointIndex] / 1000000000;
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
            let val = parts.join(".");
            let Class = null;
            if (parseFloat(val) < 0) Class = "redSpan";
            else if (parseFloat(val) > 0) Class = "greenSpan";

            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${w.globals.labels[dataPointIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span class="${Class}">${val}</span>
            

              </div>
              </div>
            `;
          }
        },
        labels: [],
        // colors: ["#16f222", "#FF4560"],
        colors: [
          function({ value }) {
            if (value > 0) {
              return "#00ad13";
            } else {
              return "#dc0600";
            }
          }
        ],
        plotOptions: {
          bar: {
            horizontal: false,
            barHeight: "100%",
            startingShape: "flat"
            // endingShape: "rounded"
          }
        },
        dataLabels: {
          enabled: false
        },

        grid: {
          xaxis: {
            lines: {
              show: false
            }
          }
        },
        stroke: {
          width: 1,
          colors: ["#3e3e4e"]
        },
        yaxis: {
          // min: -5,
          // max: 5,
          title: {
            text: "میلیارد ریال"
          },
          labels: {
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
            }
          }
        },
        // tooltip: {
        //   shared: false,
        //   followCursor: true,
        //   intersect: false,
        //   fillSeriesColor: true,

        //   x: {
        //     formatter: function(val) {
        //       return val;
        //     }
        //   },
        //   y: {
        //     title: {
        //       formatter: seriesName => seriesName
        //     }
        //     // formatter: function(value) {
        //     //   return value;
        //     // }
        //   }
        // },
        // title: {
        //   text: "Mauritius population pyramid 2011"
        // },
        xaxis: {
          categories: [],
          labels: {
            // formatter: function(val) {
            //   return Math.abs(Math.round(val)) + "%";
            // }
          }
        }
      },
      EffectOnIndexSeries: [],
      EffectOnIndexOptions: {
        chart: {
          animations: { enabled: false },
          type: "bar",
          height: 100,
          fontFamily: "Vazir-Medium-FD",
          // stacked: true,
          toolbar: {
            show: false
          }
        },
        tooltip: {
          followCursor: true,
          intersect: false,
          fillSeriesColor: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let n = series[seriesIndex][dataPointIndex];
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
            let val = parts.join(".");
            let Class = null;
            if (parseFloat(val) < 0) Class = "redSpan";
            else if (parseFloat(val) > 0) Class = "greenSpan";
            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${w.globals.labels[dataPointIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span class="${Class}">${val}</span>
            

              </div>
              </div>
            `;
          }
        },
        labels: [],
        // colors: ["#16f222", "#FF4560"],
        colors: [
          function({ value }) {
            if (value > 0) {
              return "#00ad13";
            } else {
              return "#dc0600";
            }
          }
        ],
        plotOptions: {
          bar: {
            horizontal: false,
            barHeight: "100%",
            startingShape: "flat"
            // endingShape: "rounded"
          }
        },
        dataLabels: {
          enabled: false
        },

        grid: {
          xaxis: {
            lines: {
              show: false
            }
          }
        },
        stroke: {
          width: 1,
          colors: ["#3e3e4e"]
        },
        yaxis: {
          // min: -5,
          // max: 5,
          labels: {
            formatter: function(value) {
              let n = value;
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
            }
          }
        },
        // tooltip: {
        //   shared: false,
        //   followCursor: true,
        //   intersect: false,
        //   fillSeriesColor: true,

        //   x: {
        //     formatter: function(val) {
        //       return val;
        //     }
        //   },
        //   y: {
        //     title: {
        //       formatter: seriesName => seriesName
        //     }
        //     // formatter: function(value) {
        //     //   return value;
        //     // }
        //   }
        // },
        // title: {
        //   text: "Mauritius population pyramid 2011"
        // },
        xaxis: {
          categories: [],
          labels: {
            // formatter: function(val) {
            //   return Math.abs(Math.round(val)) + "%";
            // }
          }
        }
      },
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
            barHeight: "80%",
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

          style: {
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
              <span>${val}</span>
            

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
            breakpoint: 480,
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
  },
  mounted() {
    this.loadData();
  },
  methods: {
    forceUpdate() {
      this.ApexChartcomponentKey += 1;
    },
    PieChartBackButton() {
      console.log(this.PieChartData);
      let data = JSON.parse(JSON.stringify(this.PieChartData));
      console.log(data);

      let marketCaps = data.TopIndustries.marketCap;
      let persianNames = data.TopIndustries.persianName;
      this.Pieseries = marketCaps;
      this.PiechartOptions.labels = persianNames;
      this.PieChartkey = 0;
      this.forceUpdate();
    },
    checkSign(change) {
      if (change > 0) return "greenSpan";
      else if (change < 0) return "redSpan";
      else return "blackSpan";
    },
    pieChartClick(context, seriesIndex) {
      // this.PiechartOptions.labels = persianNames;

      // console.log(founded[0].indexID);

      if (seriesIndex == 9 && this.PieChartkey == 0) {
        let data = JSON.parse(JSON.stringify(this.PieChartData));

        this.Pieseries = data.OtherIndustries.marketCap;
        this.PiechartOptions.labels = data.OtherIndustries.persianName;
        this.PieChartkey = 1;
        this.forceUpdate();
      } else if (seriesIndex != 9 && this.PieChartkey == 0) {
        // let name = context.w.globals.labels[seriesIndex];
        // let dataClicked = this.PieChartData.TopIndustries.filter(e => {
        //   return e.persianName == name;
        // });
        // this.$router.push({
        //   name: "IndustriesDetail",
        //   params: { id: dataClicked[0].indexID }
        // });
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
      // this.Pieseries = marketCaps;
      // this.$router.push({
      //   name: "IndustriesDetail",
      //   params: { id: seriesIndex }
      // });
    },
    changeTimeFrame() {
      this.ReturnSeries = [
        { data: [123, 121, 110, 100, 98, 90, 76, 68, 61, 57, 43] }
      ];
      document.getElementById("fi").style.color = "red !important";
    },
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getIndustries().then(resy => {
        // eslint-disable-next-line no-unused-vars
        this.getPieChartData().then(resx => {
          // eslint-disable-next-line no-unused-vars
          this.getHHDATA().then(resz => {
            this.getImpactData();
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

        // PieChart Data injection**************
        this.PieChartData = data.PieChart;
        let marketCaps = data.PieChart.TopIndustries.marketCap;
        marketCaps.push(data.PieChart.OtherIndustries.marketCapSum);
        let persianNames = data.PieChart.TopIndustries.persianName;
        persianNames.push("سایر");
        this.Pieseries = marketCaps;
        this.PiechartOptions.labels = persianNames;

        // let persianNames = [];
        // let marketCaps = [];
        // let marketCapsOthers = [];
        // let itemValue = [];
        // for (let item of data.TopIndustries) {
        //   persianNames.push(item.persianName);
        //   marketCaps.push(item.marketCap);
        //   itemValue.push({ name: item.persianName, value: item.TradeValue });
        // }
        // for (let item of data.Others.List) {
        //   marketCapsOthers.push(item.marketCap);
        //   this.persianNamesOthers.push(item.persianName);
        // }
        // marketCaps.push(data.Others.marketCapSum);
        // persianNames.push("سایر");
        // this.PiechartOptions.labels = persianNames;
        // this.Pieseries = marketCaps;
        // this.marketCapsOthers = marketCapsOthers;

        // bar chart data fill MUST BE DONE IN BACKEND ** IMPORTANT **
        // itemValue.sort(this.compareValues("value", "desc"));
        // itemValue = itemValue.slice(0, 10);
        // let names = [];
        // let values = [];
        // for (let item of itemValue) {
        //   names.push(item.name);
        //   values.push(item.value);
        // }
        // this.Barseries = [{ data: values }];
        // this.BarchartOptions.xaxis.categories = names;
        // console.log(this.Barseries);
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
            // IndustriesList.push(data.marketCap.marketCapData[i].marketcap);
            HHseries2Labels.push(data[i]["CorrectName"]);
            HHseries2data.push(data[i]["sum"]);
          }
          this.HHseries = [{ data: HHseries2data }];
          this.HHoptions.labels = HHseries2Labels;
          this.HHoptions.xaxis.categories = HHseries2Labels;
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
            this.EffectOnIndexOptions.labels = Impactseries2Labels;
            this.EffectOnIndexOptions.xaxis.categories = Impactseries2Labels;
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
<style>
.redSpan {
  color: red;
}
.greenSpan {
  color: green;
}
.ApexTooltip {
  /* background-color: blueviolet; */
  border-width: 1px;
  border-style: solid;
  border-color: #bdbdbd;
  border-radius: 8px;
  display: flex;
  /* flex-wrap: nowrap; */
  flex-direction: column;
  justify-content: center;
  align-items: stretch;
  align-content: center;
}
.topDivTooltip {
  background-color: #d7d7d7;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  padding-right: 22px;
  padding-left: 22px;
}
.bottomDivTooltip {
  background-color: #eaeaea;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  padding-right: 22px;
  padding-left: 22px;
  direction: ltr;
}
.apexcharts-legend-text,
.apexcharts-text,
.apexcharts-title-text,
.apexcharts-tooltip {
  font-family: "Vazir-Medium-FD" !important;
}
</style>
