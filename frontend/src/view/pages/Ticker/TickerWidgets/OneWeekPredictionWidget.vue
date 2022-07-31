<template>
  <!--begin::Mixed Widget 14-->
  <!-- <div class="card card-custom card-stretch gutter-b"> -->
  <v-card rounded="lg" height="358">
    <v-toolbar
      dense
      class="IndexChartToolbars elevation-2 mb-1"
      style="height:36px;"
    >
      <v-toolbar-title style="height:20px;font-size:0.95em"
        >پیش بینی هفتگی روند سهم</v-toolbar-title
      >
    </v-toolbar>
    <div
      class="d-flex flex-column justify-content-center my-auto"
      style="height:70%"
      v-if="PredictionData.length == 0 && !loading"
    >
      <v-icon size="30px" color="#e09f3e">mdi-alert-box</v-icon>
      <div class="d-flex justify-content-center my-2">
        <span style="font-size:0.8em">داده موجود نیست</span>
      </div>
    </div>
    <div
      class="d-flex flex-column justify-content-center my-auto"
      style="height:70%"
      v-if="PredictionData.length == 0 && loading"
    >
      <v-icon size="30px" color="#e09f3e">mdi-alert-box</v-icon>
      <div class="d-flex justify-content-center my-2">
        <span style="font-size:0.8em">در حال بازیابی داده ها</span>
      </div>
    </div>
    <div id="PredictionPriceDiv" class="d-flex">
      <highcharts
        v-show="PredictionData.length"
        class="hc"
        width="100%"
        :options="chartOptions"
        ref="chart"
      ></highcharts>
    </div>
  </v-card>
</template>

<script>
export default {
  name: "oneWeekPredictionWidget",
  props: {
    PredictionData: Array,
    priceHistory: Array
  },
  data() {
    return {
      search: "",
      groupingUnits: [
        [
          "week", // unit name
          [1] // allowed multiples
        ],
        ["month", [1, 2, 3, 4, 6]]
      ],
      fullData: [],
      chartOptions: {},
      realdata: [],
      predictedData: [],
      realData: [],
      loading: true
    };
  },
  methods: {
    // set FinancialStrength percent
    renderRatioComponentData() {
      if (
        this.PredictionData === null ||
        this.PredictionData === undefined ||
        this.PredictionData == [] ||
        this.priceHistory === null ||
        this.priceHistory === undefined ||
        this.priceHistory == []
      ) {
        this.predictedData = [];
        this.realData = [];
      } else {
        let realOnes = this.priceHistory.slice(
          Math.max(this.priceHistory.length - 10, -1)
        );
        realOnes.sort(function(first, second) {
          return first.engdate - second.engdate;
        });
        realOnes.filter(d => {
          this.realData.push({
            x: new Date(d.engdate).getTime(),
            y: d.adjustedclosing
          });
          // console.log((new Date(d.engdate)).getTime())
        });
        let lastData = this.realData.slice(-1)[0].y;
        // let unique = [...new Set(this.realData.map(item => item.x))];
        this.PredictionData.filter(d => {
          if (
            // !unique.includes(new Date(d.date).getTime()) &&
            d.tag == "prediction"
          ) {
            // console.log(d.close)
            this.predictedData.push({
              x: new Date(d.date).getTime(),
              y: d.close
            });
          }
        });

        let firstPrediction = this.predictedData.slice(-1)[0].y;
        let Difference = Math.abs(firstPrediction - lastData);
        // console.log(this.predictedData);
        if (lastData > firstPrediction) {
          if (firstPrediction / lastData - 1 < -0.05) {
            this.predictedData.filter(d => {
              d.y = d.y + Difference + -0.05 * lastData;
            });
          }
        } else {
          if (firstPrediction / lastData - 1 > 0.05) {
            this.predictedData.filter(d => {
              d.y = d.y - Difference + 0.05 * lastData;
            });
          }
        }

        console.log(this.predictedData);
        this.predictedData.sort(function(first, second) {
          return second.x - first.x;
        });
        this.chartOptions.series = [];
        this.chartOptions.series.push({ name: "سهم", data: this.realData });
        this.chartOptions.series.push({
          name: "پیش بینی",
          data: this.predictedData
        });
        this.loading = false;
        // console.log(this.predictedData);
        // console.log(this.realData)
      }
    }
  },
  mounted() {
    let div = document.getElementById("PredictionPriceDiv").clientWidth;
    this.chartOptions.chart.width = div;
    this.chartOptions.chart.height = ((300 / div) * 100).toString() + "%";
  },
  watch: {
    PredictionData() {
      this.predictedData = [];
      this.realData = [];
      //   console.log(this.PredictionData);
      if (
        this.priceHistory === null ||
        this.priceHistory === undefined ||
        this.priceHistory == [] ||
        this.PredictionData === null ||
        this.PredictionData === undefined ||
        this.PredictionData == []
      ) {
        this.predictedData = [];
        this.realData = [];
      } else {
        this.renderRatioComponentData();
      }
      // console.log(this.ComponentData);
    },
    priceHistory() {
      this.predictedData = [];
      this.realData = [];
      if (
        this.priceHistory === null ||
        this.priceHistory === undefined ||
        this.priceHistory == [] ||
        this.PredictionData === null ||
        this.PredictionData === undefined ||
        this.PredictionData == []
      ) {
        this.predictedData = [];
        this.realData = [];
      } else {
        this.renderRatioComponentData();
      }
    }
  },
  created() {
    const that = this;
    this.chartOptions = {
      title: {
        text: "پیش بینی"
      },
      credits: {
        enabled: false
      },

      chart: {
        // height: (9 / 16 * 100)-5 + '%', // 16:9 ratio
        width: "900",
        // height: "40%"
        height: "35%"
        // lang: {
        //   rangeSelectorZoom: "بازه"
        // }
      },
      rangeSelector: {
        inputEnabled: false,
        selected: 10,
        buttonTheme: {
          width: 60
        },
        allButtonsEnabled: false,
        buttons: []
        // selected: 1
      },
      navigator: {
        enabled: false,
        maskFill: "rgba(115, 113, 115, 0.2)",
        outlineColor: "rgba(190, 179, 9, 0.2)",
        outlineWidth: 2,
        // maskInside:false,
        series: {
          type: "areaspline",
          color: "#ff00af",
          fillOpacity: 0.4,
          dataGrouping: {
            smoothed: false
          },
          lineWidth: 2,
          lineColor: "#072b44",
          fillColor: {
            linearGradient: {
              x1: 0,
              y1: 0,
              x2: 0,
              y2: 1
            },
            stops: [
              [0, "#0974be"],
              [1, "#89e0db"]
            ]
          },
          marker: {
            enabled: false
          },
          shadow: true
        },
        yAxis: {
          reversed: false
        }
      },
      tooltip: {
        split: true,
        useHTML: true,

        formatter: function() {
          // let high = this.points[0].point.high;
          // let low = this.points[0].point.low;
          // let open = this.points[0].point.open;
          let close = this.points[0].point.y;
          let toolTip1 = `
          <div style=font-size:0.9em;margin-left:2px><span>پایانی:</span><span style=font-size:0.9em>${close.toLocaleString()}</span></div>`;

          // let toolTip2 = `<span style=font-size:0.9em;margin-left:2px >حجم:</span> <span style=font-size:0.9em>${this.points[1].point.y.toLocaleString()}</span>`;
          // let toolTip1 = `"Open:${open}\nClose:${close}\nHigh:${high}\nLow:${low}"`

          let unix = this.x;
          let dateEX = new Date(unix);
          let year = dateEX.getFullYear().toString();
          let month = (dateEX.getMonth() + 1).toString();
          let day = dateEX.getDate().toString();
          // console.log(year + "/" + month + "/" + day);

          let xAxisTooltip = that
            .$moment(year + "/" + month + "/" + day, "YYYY/MM/DD")
            .locale("fa")
            .format("YYYY/MM/DD");
          xAxisTooltip = `<span style=font-size:0.9em>${xAxisTooltip}</span>`;
          return [xAxisTooltip].concat(toolTip1);
        }
      },
      series: [],
      yAxis: [
        {
          labels: {
            align: "right",
            x: -3
          },
          title: {
            text: "قیمت"
          },
          lineWidth: 2,
          resize: {
            enabled: true
          }
        }
      ],
      xAxis: {
        // type: 'datetime',
        labels: {
          formatter: function() {
            // console.log(this.value);
            let unix = this.value;
            let dateEX = new Date(unix);
            let year = dateEX.getFullYear().toString();
            let month = (dateEX.getMonth() + 1).toString();
            let day = dateEX.getDate().toString();
            // console.log(year + "/" + month + "/" + day);

            return that
              .$moment(year + "/" + month + "/" + day, "YYYY/MM/DD")
              .locale("fa")
              .format("YYYY/MM/DD");
            // return this.value
            // return this.$Highcharts.dateFormat('%YYYY %MM %dd', this.date);
          }
        }
      },
      responsive: {
        rules: [
          {
            condition: {
              maxWidth: 500
            },
            chartOptions: {
              legend: {
                layout: "horizontal",
                align: "center",
                verticalAlign: "bottom"
              }
            }
          }
        ]
      }
    };
  }
};
</script>
