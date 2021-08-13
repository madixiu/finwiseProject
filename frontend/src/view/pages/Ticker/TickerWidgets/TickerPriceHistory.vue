<template>
  <div>
    <highcharts
      :constructorType="'stockChart'"
      class="hc"
      :options="chartOptions"
      ref="chart"
    ></highcharts>
  </div>
</template>

<script>
export default {
  props: {
    priceHistory: Array
  },
  data() {
    return {
      groupingUnits: [
        [
          "week", // unit name
          [1] // allowed multiples
        ],
        ["month", [1, 2, 3, 4, 6]]
      ],
      fullData: [],
      chartOptions: {}
    };
  },
  watch: {
    priceHistory() {
      let ohlc = [];
      let volume = [];
      //// for (let i = this.priceHistory.length - 1; i >= 0; i -= 1) {
      for (let i = 0; i < this.priceHistory.length; i += 1) {
        ohlc.push([
          this.priceHistory[i].unix, // the date
          this.priceHistory[i].first, // open
          this.priceHistory[i].high, // high
          this.priceHistory[i].low, // low
          this.priceHistory[i].last // close
        ]);
        volume.push([this.priceHistory[i].unix, this.priceHistory[i].volume]);
      }
      this.chartOptions.series[0].data = ohlc;
      this.chartOptions.series[1].data = volume;
    }
  },
  created() {
    const that = this;
    this.chartOptions = {
      credits: {
        enabled: false
      },

      chart: {
        // height: (9 / 16 * 100) + '%' // 16:9 ratio
        height: "50%",
        lang: {
          rangeSelectorZoom: "بازه"
        }
      },
      rangeSelector: {
        inputEnabled: false,
        selected: 10,
        buttonTheme: {
          width: 60
        },
        allButtonsEnabled: true,
        buttons: [
          {
            type: "month",
            count: 1,
            title: "یک ماهه",
            text: "یک ماهه"

            // text: "۱ ماه"
          },
          {
            type: "month",
            count: 3,
            title: "سه ماهه",
            text: "سه ماهه"

            // text: "۳ ماه"
          },
          {
            type: "month",
            count: 6,
            text: "شش ماهه",
            title: "View 6 months"
          },
          // {
          //   type: "ytd",
          //   text: "YTD",
          //   title: "View year to date"
          // },
          {
            type: "year",
            count: 1,
            text: "یک ساله",
            title: "View 1 year"
          },
          {
            type: "all",
            text: "همه",
            title: "View all"
          }
        ]
        // selected: 1
      },
      navigator: {
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
          let high = this.points[0].point.high;
          let low = this.points[0].point.low;
          let open = this.points[0].point.open;
          let close = this.points[0].point.close;
          let toolTip1 = `<div><span style=font-size:0.9em;margin-left:2px>اولین:</span><span style=font-size:0.9em>${open.toLocaleString()}</span></div>
          <div style=font-size:0.9em;margin-left:2px><span>آخرین:</span><span style=font-size:0.9em>${close.toLocaleString()}</span></div>
          <div style=font-size:0.9em;margin-left:2px><span>بیشترین:</span><span style=font-size:0.9em>${high.toLocaleString()}</span></div>
          <div><span style=font-size:0.9em;margin-left:2px>کمترین:</span><span style=font-size:0.9em>${low.toLocaleString()}</span></div>`;

          let toolTip2 = `<span style=font-size:0.9em;margin-left:2px >حجم:</span> <span style=font-size:0.9em>${this.points[1].point.y.toLocaleString()}</span>`;
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
          return [xAxisTooltip].concat(toolTip1, toolTip2);
        }
      },
      series: [
        {
          type: "candlestick",
          name: "AAPL",
          data: [],
          color: "#f63538",
          upColor: "#30cc5a",

          dataGrouping: {
            units: that.groupingUnits
          }
        },
        {
          type: "column",
          name: "Volume",
          data: [],
          color: "#00a8ff",
          yAxis: 1,
          dataGrouping: {
            units: that.groupingUnits
          }
        }
      ],
      yAxis: [
        {
          labels: {
            align: "right",
            x: -3
          },
          title: {
            text: "قیمت"
          },
          height: "70%",
          lineWidth: 2,
          resize: {
            enabled: true
          }
        },
        {
          labels: {
            align: "right",
            x: -3
          },
          title: {
            text: "حجم"
          },
          top: "75%",
          height: "15%",
          offset: 0,
          lineWidth: 2
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
            console.log(year + "/" + month + "/" + day);

            return that
              .$moment(year + "/" + month + "/" + day, "YYYY/MM/DD")
              .locale("fa")
              .format("YYYY/MM/DD");
            // return this.value
            // return this.$Highcharts.dateFormat('%YYYY %MM %dd', this.date);
          }
        }
      }
    };
  }
};
</script>
