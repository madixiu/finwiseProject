<template>
  <v-card class="mt-1 pb-8">
    <v-toolbar dense>
      <v-toolbar-title>نمودار وضعیت صنایع</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-radio-group class="mt-5" row v-model="SortByIndustryChart" mandatory>
        <v-radio
          class="radioBTN"
          label="ورود و خروج حقیقی"
          value="HH"
        ></v-radio>
        <v-radio
          class="radioBTN"
          label="تاثیر در شاخص"
          value="Impact"
        ></v-radio>
      </v-radio-group>
    </v-toolbar>
    <v-card class="mt-1" v-show="SortByIndustryChart == 'HH'">
      <ApexChart
        type="bar"
        width="100%"
        height="200%"
        :series="HHseries"
        :chartOptions="HHoptions"
      />
    </v-card>
    <v-card class="mt-1" v-show="SortByIndustryChart == 'Impact'">
      <ApexChart
        width="100%"
        height="200%"
        :series="EffectOnIndexSeries"
        :chartOptions="EffectOnIndexOptions"
      />
    </v-card>
  </v-card>
</template>

<script>
import ApexChart from "@/view/content/charts/ApexChart";
export default {
  name: "ChartIndustries",
  components: {
    ApexChart
  },
  props: { inpuDataIndustryHH: Array, inputDataIndustryImpact: Array },
  data() {
    return {
      SortByIndustryChart: "HH",
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
        noData: {
          text: "No Data",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
        tooltip: {
          followCursor: true,
          intersect: false,
          fillSeriesColor: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let val = series[seriesIndex][dataPointIndex];
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
              <span style=color:#000;font-size:0.8em class=mr-1>ریال</span>
              <span style='font-size:0.8em' class="${Class}">${val.toLocaleString()}</span>
            

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
        noData: {
          text: "No Data",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
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
            console.log(w.globals);
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
      }
    };
  },
  watch: {
    inpuDataIndustryHH() {
      //   let data = this.inpuDataIndustryHH;
      let HHseries2Labels = [];
      let HHseries2data = [];
      this.inpuDataIndustryHH.filter(item => {
        HHseries2Labels.push(item.CorrectName);
        HHseries2data.push(item.sum);
      });
      this.HHoptions.labels = HHseries2Labels;
      this.HHoptions.xaxis.categories = HHseries2Labels;
      this.HHseries = [{ data: HHseries2data }];
    },
    inputDataIndustryImpact() {
      if (this.inputDataIndustryImpact != "noData") {
        let data = this.inputDataIndustryImpact;
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
    }
  }
};
</script>

<style scoped>
.radioBTN /deep/ .v-input--selection-controls__ripple {
  height: 16px !important;
  width: 16px !important;
  left: -3px !important;
  top: calc(50% - 15px) !important;
}
.radioBTN /deep/ .v-icon.v-icon {
  font-size: 18px !important;
}
.radioBTN /deep/ .v-application--is-rtl .v-input--selection-controls__input {
  margin-left: 1px;
}

.radioBTN /deep/ label {
  display: inline-block;
  margin-bottom: 0rem;
}
.radioBTN /deep/ .v-label {
  font-size: 0.8em !important;
}
.radioBTN /deep/ .theme--light.v-label {
  color: #000 !important;
}
</style>
