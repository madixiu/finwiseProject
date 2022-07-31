<template>
  <ApexChart
    v-if="HHseries.length != 0"
    type="bar"
    width="100%"
    height="210%"
    :series="HHseries"
    :chartOptions="HHoptions"
  />
</template>
<script>
import ApexChart from "@/view/content/charts/ApexChart";

export default {
  components: {
    ApexChart
  },
  props: {
    HHseries: Array,
    HHLabels: Array,
    HHmin: Number,
    HHmax: Number
  },
  beforeMount() {
    this.HHoptions.labels = this.HHLabels;
    this.HHoptions.xaxis.categories = this.HHLabels;
    this.HHoptions.yaxis.max = this.HHmax;
    this.HHoptions.yaxis.min = this.HHmin;
  },
  data() {
    return {
      attrs: {
        class: "mb-6",
        boilerplate: true,
        elevation: 2
      },
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
            let val = series[seriesIndex][dataPointIndex];
            let Class = null;
            if (parseFloat(val) < 0) Class = "industryApexChartTooltipRedSpan";
            else if (parseFloat(val) > 0)
              Class = "industryApexChartTooltipGreenSpan";

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
      }
    };
  }
};
</script>
