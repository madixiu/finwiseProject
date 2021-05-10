<template>
  <div>
    <div class="row">
      <div class="col-12">
        <IndustryChart :inputData="this.IndustryData"></IndustryChart>
      </div>

      <div class="col-xxl-3 col-md-3 col-sm-6 col-xs-12">
        <v-card>
          <v-card-title>ارزش بازار صنایع</v-card-title>
          <ApexChart
            v-if="Pieseries.length"
            type="pie"
            height="200%"
            width="100%"
            :series="Pieseries"
            :chartOptions="PiechartOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-9 col-md-9 col-sm-12 col-xs-12">
        <v-card class="mt-1">
          <v-card-title>صنایع با بیشترین ارزش معاملات</v-card-title>
          <ApexChart
            v-if="Barseries.length"
            type="bar"
            height="200%"
            width="100%"
            :series="Barseries"
            :chartOptions="BarchartOptions"
          />
        </v-card>
        <v-card class="mt-1">
          <v-card-title>ورود و خروج حقیقی به صنایع</v-card-title>
          <ApexChart
            v-if="HHseries.length"
            type="bar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
        </v-card>
        <v-card class="mt-1">
          <v-card-title>تاثیر صنایع در شاخص</v-card-title>
          <ApexChart
            v-if="EffectOnIndexSeries.length"
            type="bar"
            width="100%"
            height="200%"
            :series="EffectOnIndexSeries"
            :chartOptions="EffectOnIndexOptions"
          />
        </v-card>
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
    // MarqueeText
  },
  data() {
    return {
      // paused: false,
      IndustryData: [],
      Pieseries: [],
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
            return (
              '<div class="arrow_box">' +
              "<span>" +
              w.globals.labels[dataPointIndex] +
              ": " +
              val +
              "</span>" +
              "</div>"
            );
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
            return (
              '<div class="arrow_box">' +
              "<span>" +
              w.globals.labels[dataPointIndex] +
              ": " +
              val +
              "</span>" +
              "</div>"
            );
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
            barHeight: "100%",
            distributed: true
          }
        },
        colors: ["#33b2df", "#546E7A", "#d4526e", "#13d8aa", "#A5978B"],
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
            colors: ["#fff"]
          }
        },
        xaxis: {
          categories: [],
          title: {
            text: "میلیارد ریال"
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
        }
      },
      PiechartOptions: {
        chart: {
          width: 400,
          height: 100,
          type: "pie",
          fontFamily: "Vazir-Medium-FD",
          animations: {
            enabled: false
          },
          events: {
            // legendClick: function(chartContext, seriesIndex, config) {
            // },
            dataPointSelection: (event, chartContext, config) => {
              this.pieChartClick(config.dataPointIndex);
            }
          }
        },
        legend: {
          // show: false,
          fontSize: 10,
          fontFamily: "Vazir-Medium-FD",
          position: "bottom"
        },
        labels: [],
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
        EffectOnIndexOptions: {
          chart: {
            type: "bar",
            height: 100,
            fontFamily: "Vazir-Medium-FD",
            // stacked: true,
            toolbar: {
              show: false
            }
          },
          tooltip: {
            custom: function({ series, seriesIndex, dataPointIndex, w }) {
              return (
                '<div class="arrow_box">' +
                "<span>" +
                w.globals.labels[dataPointIndex] +
                ": " +
                series[seriesIndex][dataPointIndex] +
                "</span>" +
                "</div>"
              );
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
    pieChartClick(seriesIndex) {
      // this.PiechartOptions.labels = persianNames;

      // this.Pieseries = marketCaps;
      this.$router.push({
        name: "IndustriesDetail",
        params: { id: seriesIndex }
      });
    },
    changeTimeFrame() {
      this.ReturnSeries = [
        { data: [123, 121, 110, 100, 98, 90, 76, 68, 61, 57, 43] }
      ];
      document.getElementById("fi").style.color = "red !important";
    },
    index() {
      this.$router.push({ name: "IndustriesDetail", params: { id: 2 } });
    },
    numberWithCommas(x) {
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
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
    loadData() {
      // eslint-disable-next-line no-unused-vars
      // this.getAll().then();
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
    async getAll() {
      await this.axios
        .get("/api/IndsutriesPage")
        .then(first_response => {
          this.IndustryData = first_response.data[0];
          /////////////////
          let second = first_response.data[1];
          let persianNames = [];
          let marketCaps = [];
          let itemValue = [];
          for (let item of second[0].TopIndustries) {
            persianNames.push(item.persianName);
            marketCaps.push(item.marketCap);
            itemValue.push({ name: item.persianName, value: item.TradeValue });
          }
          marketCaps.push(second[1].Others.marketCapSum);
          persianNames.push("سایر");
          this.PiechartOptions.labels = persianNames;
          this.Pieseries = marketCaps;
          itemValue.sort(this.compareValues("value", "desc"));
          itemValue = itemValue.slice(0, 6);
          let names = [];
          let values = [];
          for (let item of itemValue) {
            names.push(item.name);
            values.push(item.value);
          }
          this.Barseries = [{ data: values }];
          this.BarchartOptions.xaxis.categories = names;
          /////////////
          let third = first_response.data[2];
          // this.HHseries = data;
          // eslint-disable-next-line no-unused-vars
          let HHseries2Labels = [];
          let HHseries2data = [];
          for (let i = 0; i < third.length; i++) {
            // IndustriesList.push(data.marketCap.marketCapData[i].marketcap);
            HHseries2Labels.push(third[i]["CorrectName"]);
            HHseries2data.push(third[i]["sum"]);
          }
          this.HHseries = [{ data: HHseries2data }];
          this.HHoptions.labels = HHseries2Labels;
          this.HHoptions.xaxis.categories = HHseries2Labels;
          /////
          let fourth = first_response.data[3];
          // this.HHseries = data;
          // eslint-disable-next-line no-unused-vars
          let Impactseries2Labels = [];
          let Impactseries2data = [];
          for (let i = 0; i < fourth.length; i++) {
            // IndustriesList.push(data.marketCap.marketCapData[i].marketcap);
            Impactseries2Labels.push(fourth[i]["CorrectName"]);
            Impactseries2data.push(fourth[i]["IMPACT"]);
          }
          this.EffectOnIndexSeries = [{ data: Impactseries2data }];
          this.EffectOnIndexOptions.labels = Impactseries2Labels;
          this.EffectOnIndexOptions.xaxis.categories = Impactseries2Labels;
        })
        .catch(error => {
          console.error(error);
        });
    },
    async getPieChartData() {
      await this.axios.get("/api/IndexMarketCap").then(responsive => {
        let data = responsive.data;
        let persianNames = [];
        let marketCaps = [];
        let itemValue = [];
        for (let item of data[0].TopIndustries) {
          persianNames.push(item.persianName);
          marketCaps.push(item.marketCap);
          itemValue.push({ name: item.persianName, value: item.TradeValue });
        }
        marketCaps.push(data[1].Others.marketCapSum);
        persianNames.push("سایر");
        this.PiechartOptions.labels = persianNames;
        this.Pieseries = marketCaps;
        itemValue.sort(this.compareValues("value", "desc"));
        itemValue = itemValue.slice(0, 6);
        let names = [];
        let values = [];
        for (let item of itemValue) {
          names.push(item.name);
          values.push(item.value);
        }
        this.Barseries = [{ data: values }];
        this.BarchartOptions.xaxis.categories = names;
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
          let data = responsea.data;
          // this.HHseries = data;
          // eslint-disable-next-line no-unused-vars
          let Impactseries2Labels = [];
          let Impactseries2data = [];
          for (let i = 0; i < data.length; i++) {
            // IndustriesList.push(data.marketCap.marketCapData[i].marketcap);
            Impactseries2Labels.push(data[i]["CorrectName"]);
            Impactseries2data.push(data[i]["IMPACT"]);
          }
          this.EffectOnIndexSeries = [{ data: Impactseries2data }];
          this.EffectOnIndexOptions.labels = Impactseries2Labels;
          this.EffectOnIndexOptions.xaxis.categories = Impactseries2Labels;
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
/* @import "~bootstrap/dist/css/bootstrap.css"; */
/* #fi {
  color: red !important;
} */
/* .apexcharts-pie-label,
.apexcharts-datalabels,
.apexcharts-datalabel,
.apexcharts-datalabel-label,
.apexcharts-datalabel-value {
  cursor: default;
  pointer-events: none;
  font-family: "Vazir-Medium-FD" !important;
} */
.apexcharts-legend-text,
.apexcharts-text,
.apexcharts-title-text,
.apexcharts-tooltip {
  /* font-family: Poppins, Helvetica, "sans-serif" !important; */
  font-family: "Vazir-Medium-FD" !important;
}
/* .apexcharts-series {
  font-family: "Vazir-Medium-FD" !important;

}
.apexcharts-text tspan {
  font-family: "Vazir-Medium-FD" !important;
}
.apexcharts-legend-text,
.apexcharts-text,
.apexcharts-title-text {
  font-family: "Vazir-Medium-FD" !important;
} */
</style>
