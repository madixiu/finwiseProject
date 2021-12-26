<template>
  <div class="col-xxl-12 col-lg-12 col-md-12" style="margin-top:10px">
    <div class="row d-flex">
      <div class="col-xxl-6 col-lg-6 col-md-12" style="padding-top:0px">
        <v-card rounded="lg" height="500">
          <v-toolbar dense class="IndexChartToolbars elevation-2 mb-1">
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >روند خرید و فروش حقیقی و حقوقی</v-toolbar-title
            >
          </v-toolbar>
          <div
            class="d-flex flex-column justify-content-center my-auto"
            v-if="notices.length == 0"
          >
            <v-icon size="30px" color="#e09f3e">mdi-alert-box</v-icon>
            <div class="d-flex justify-content-center my-2">
              <span style="font-size:0.8em">داده موجود نیست</span>
            </div>
          </div>
          <div id="tickerHHdiv" class="d-flex">
            <highcharts
              v-show="notices.length"
              :constructorType="'stockChart'"
              class="hc"
              width="100%"
              :options="chartOptions"
              ref="chart"
            ></highcharts>
          </div>
        </v-card>
      </div>
      <div class="col-xxl-6 col-lg-6 col-md-12" style="padding-top:0px">
        <v-card rounded="lg" height="500">
          <v-toolbar dense class="IndexChartToolbars elevation-2 mb-1">
            <v-toolbar-title style="height:20px;font-size:0.95em"
              >روند سرانه حقیقی و حقوقی</v-toolbar-title
            >
          </v-toolbar>
          <div
            class="d-flex flex-column justify-content-center my-auto"
            v-if="notices.length == 0"
          >
            <v-icon size="30px" color="#e09f3e">mdi-alert-box</v-icon>
            <div class="d-flex justify-content-center my-4">
              <span style="font-size:0.8em">داده موجود نیست</span>
            </div>
          </div>
          <div id="tickerHHdiv2" v-show="notices.length" class="d-flex">
            <highcharts
              v-show="notices.length"
              :constructorType="'stockChart'"
              class="hc"
              width="100%"
              :options="chartOptions2"
              ref="chart"
            ></highcharts>
          </div>
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HHHistoryWidget",
  // props: ["notices"],
  props: {
    notices: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      loading: true,
      noData: false,
      fullData: [],
      chartOptions: {},
      chartOptions2: {},
      groupingUnits: [
        [
          "week", // unit name
          [1] // allowed multiples
        ],
        ["month", [1, 2, 3, 4, 6]]
      ]
    };
  },
  mounted() {
    let div = document.getElementById("tickerHHdiv").clientWidth;
    this.chartOptions.chart.width = div;
    this.chartOptions.chart.height = ((700 / div) * 100).toString() + "%";

    let div2 = document.getElementById("tickerHHdiv2").clientWidth;
    this.chartOptions2.chart.width = div2;
    this.chartOptions2.chart.height = ((700 / div2) * 100).toString() + "%";
  },
  created() {
    const that = this;
    this.chartOptions = {
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
      navigator: {
        enabled: true,
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
          let buyHaghighi = this.points[0].point.y;
          let toolTip1 = `<div><span style=font-size:0.9em;margin-left:2px>ارزش خرید حقیقی:</span><span style=font-size:0.9em>${buyHaghighi.toLocaleString()}</span></div>`;

          let buyHoghughi = this.points[1].point.y;
          let toolTip2 = `<div><span style=font-size:0.9em;margin-left:2px>ارزش خرید حقوقی:</span><span style=font-size:0.9em>${buyHoghughi.toLocaleString()}</span></div>`;

          let SellHaghighi = this.points[2].point.y;
          let toolTip3 = `<div><span style=font-size:0.9em;margin-left:2px>ارزش فروش حقیقی:</span><span style=font-size:0.9em>${SellHaghighi.toLocaleString()}</span></div>`;

          let Sellhoghughi = this.points[3].point.y;
          let toolTip4 = `<div><span style=font-size:0.9em;margin-left:2px>ارزش فروش حقوقی:</span><span style=font-size:0.9em>${Sellhoghughi.toLocaleString()}</span></div>`;

          let unix = this.points[0].point.x;
          let dateEX = new Date(unix);
          let year = dateEX.getFullYear().toString();
          let month = (dateEX.getMonth() + 1).toString();
          let day = dateEX.getDate().toString();
          //   console.log(year + "/" + month + "/" + day);

          let xAxisTooltip = that
            .$moment(year + "/" + month + "/" + day, "YYYY/MM/DD")
            .locale("fa")
            .format("YYYY/MM/DD");
          xAxisTooltip = `<span style=font-size:0.9em>${xAxisTooltip}</span>`;
          return [xAxisTooltip].concat(toolTip1, toolTip2, toolTip3, toolTip4);
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
            text: "ارزش معاملات"
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
      }
    };
    this.chartOptions2 = {
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
        enabled: true,
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
          let buyHaghighi = this.points[0].point.y;
          let toolTip1 = `<div><span style=font-size:0.9em;margin-left:2px>سرانه خرید حقیقی:</span><span style=font-size:0.9em>${buyHaghighi.toLocaleString()}</span></div>`;

          let buyHoghughi = this.points[1].point.y;
          let toolTip2 = `<div><span style=font-size:0.9em;margin-left:2px>سرانه خرید حقوقی:</span><span style=font-size:0.9em>${buyHoghughi.toLocaleString()}</span></div>`;

          let SellHaghighi = this.points[2].point.y;
          let toolTip3 = `<div><span style=font-size:0.9em;margin-left:2px>سرانه فروش حقیقی:</span><span style=font-size:0.9em>${SellHaghighi.toLocaleString()}</span></div>`;

          let Sellhoghughi = this.points[3].point.y;
          let toolTip4 = `<div><span style=font-size:0.9em;margin-left:2px>سرانه فروش حقوقی:</span><span style=font-size:0.9em>${Sellhoghughi.toLocaleString()}</span></div>`;

          let unix = this.points[0].point.x;
          let dateEX = new Date(unix);
          let year = dateEX.getFullYear().toString();
          let month = (dateEX.getMonth() + 1).toString();
          let day = dateEX.getDate().toString();
          //   console.log(year + "/" + month + "/" + day);

          let xAxisTooltip = that
            .$moment(year + "/" + month + "/" + day, "YYYY/MM/DD")
            .locale("fa")
            .format("YYYY/MM/DD");
          xAxisTooltip = `<span style=font-size:0.9em>${xAxisTooltip}</span>`;
          return [xAxisTooltip].concat(toolTip1, toolTip2, toolTip3, toolTip4);
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
            text: "سرانه"
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
      }
    };
  },
  watch: {
    notices(newValue, oldValue) {
      if (
        newValue != oldValue &&
        newValue.length == 0 &&
        oldValue.length == 0
      ) {
        this.noData = true;
        this.loading = false;
      } else {
        // this.tablePaginationLength = this.pagination(this.notices.length);
        this.loading = false;
        this.GetFiltered();
      }
    }
  },

  methods: {
    GetFiltered() {
      let that = this;
      if (
        !(
          this.notices === null ||
          this.notices === undefined ||
          this.notices === []
        )
      ) {
        let Data = this.notices;
        // eslint-disable-next-line no-unused-vars
        let Filtered1 = [];
        let Filtered2 = [];
        let Filtered3 = [];
        let Filtered4 = [];
        let Filtered5 = [];
        let Filtered6 = [];
        let Filtered7 = [];
        let Filtered8 = [];
        let unique = [];
        Data.filter(d => {
          //   let D = new Date(
          //     d.engDate.substring(0, 4),
          //     d.engDate.substring(4, 6) - 1,
          //     d.engDate.substring(6, 8)
          //   ).getTime();
          let D = that.$moment(d.engDate, "YYYYMMDD").unix() * 1000;
          if (unique.includes(d.engDate)) {
            // console.log(d.engDate);
          } else {
            Filtered1.push({
              x: D,
              y: Math.round(d.buy_Haghighi_Value * 100) / 100
            });
            Filtered2.push({
              x: D,
              y: Math.round(d.buy_Hoghughi_Value * 100) / 100
            });
            Filtered3.push({
              x: D,
              y: Math.round(d.sell_Haghighi_Value * 100) / 100
            });
            Filtered4.push({
              x: D,
              y: Math.round(d.sell_Hoghughi_Value * 100) / 100
            });
            Filtered5.push({
              x: D,
              y: Math.round(d.buyPerHaghighi * 100) / 100
            });
            Filtered6.push({
              x: D,
              y: Math.round(d.buyPerHoghughi * 100) / 100
            });
            Filtered7.push({
              x: D,
              y: Math.round(d.sellPerHaghighi * 100) / 100
            });
            Filtered8.push({
              x: D,
              y: Math.round(d.sellPerHoghughi * 100) / 100
            });
            unique.push(d.engDate);
          }
        });
        this.chartOptions.series = [];
        this.chartOptions.series.push({
          type: "line",
          name: "ارزش خرید حقیقی",
          data: Filtered1,
          color: "#050A30",
          upColor: "#30cc5a"
        });
        this.chartOptions.series.push({
          type: "line",
          name: "ارزش خرید حقوقی",
          data: Filtered2,
          color: "#0000FF",
          upColor: "#30cc5a"
        });
        this.chartOptions.series.push({
          type: "line",
          name: "ارزش فروش حقیقی",
          data: Filtered3,
          color: "#000C66",
          upColor: "#30cc5a"
        });
        this.chartOptions.series.push({
          type: "line",
          name: "ارزش فروش حقوقی",
          data: Filtered4,
          color: "#7EC8E3",
          upColor: "#30cc5a"
        });
        this.chartOptions2.series = [];
        this.chartOptions2.series.push({
          type: "line",
          name: "سرانه خرید حقیقی",
          data: Filtered5,
          color: "#050A30",
          upColor: "#30cc5a",
          dataGrouping: {
            units: that.groupingUnits
          }
        });
        this.chartOptions2.series.push({
          type: "line",
          name: "سرانه خرید حقوقی",
          data: Filtered6,
          color: "#0000FF",
          upColor: "#30cc5a",
          dataGrouping: {
            units: that.groupingUnits
          }
        });
        this.chartOptions2.series.push({
          type: "line",
          name: "سرانه فروش حقیقی",
          data: Filtered7,
          color: "#000C66",
          upColor: "#30cc5a",
          dataGrouping: {
            units: that.groupingUnits
          }
        });
        this.chartOptions2.series.push({
          type: "line",
          name: "سرانه فروش حقوقی",
          data: Filtered8,
          color: "#7EC8E3",
          upColor: "#30cc5a",
          dataGrouping: {
            units: that.groupingUnits
          }
        });
      }
    }
  }
};
</script>
