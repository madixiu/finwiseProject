<template>
  <ApexChart
    v-if="EffectOnIndexSeries.length != 0"
    type="bar"
    width="100%"
    height="210%"
    :series="EffectOnIndexSeries"
    :chartOptions="EffectOnIndexOptions"
  />
</template>
<script>
import ApexChart from "@/view/content/charts/ApexChart";

export default {
  components: {
    ApexChart
  },
  props: {
    EffectOnIndexSeries: Array,
    EffectOnIndexLabels: Array,
    EffectOnIndexmin: Number,
    EffectOnIndexmax: Number
  },
  beforeMount() {
    this.EffectOnIndexOptions.labels = this.EffectOnIndexLabels;
    this.EffectOnIndexOptions.xaxis.categories = this.EffectOnIndexLabels;
    this.EffectOnIndexOptions.yaxis.max = this.EffectOnIndexmax;
    this.EffectOnIndexOptions.yaxis.min = this.EffectOnIndexmin;
  },
  data() {
    return {
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
