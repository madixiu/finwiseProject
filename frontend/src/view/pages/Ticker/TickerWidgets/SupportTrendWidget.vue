<template>
  <!--begin::Mixed Widget 14-->
  <div class="row">
    <div
      class="col-xxl-9 col-xl-9 col-lg-9  col-md-12 col-xs-12 mt-1"
      style="padding-left:0px;padding-right:20px"
    >
      <!-- <div
            class="card card-custom  col-xxl-12 col-lg-12 col-md-12 col-sm-12"
          > -->
      <v-card>
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em"
            >وضعیت ترند-سطوح مقاومت و حمایت با قیمت های تعدیلی محاسبه شده
            است</v-toolbar-title
          >
        </v-toolbar>

        <ApexChart
          :key="ChartTopKey"
          height="400%"
          width="100%"
          :series="Chart1options.series"
          :chartOptions="Chart1options"
        />
        <!-- <ApexChart
          :key="ChartBotKey"
          height="100%"
          width="100%"
          :series="ChartoptionsBar.series"
          :chartOptions="ChartoptionsBar"
        /> -->
      </v-card>
      <!-- </div> -->
    </div>
    <div
      class="col-xxl-3 col-xl-3 col-lg-3 ccol-md-12 ol-xs-12 mt-1"
      style="padding-left:0px;padding-right:20px"
    >
      <!-- <div
            class="card card-custom  col-xxl-12 col-lg-12 col-md-12 col-sm-12"
          > -->
      <v-card>
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em"
            >وضعیت ترند</v-toolbar-title
          >
        </v-toolbar>
      </v-card>
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
import ApexChart from "@/view/content/charts/ApexChart";
export default {
  name: "SupportTrendWidget",
  props: {
    notices: {
      type: Object,
      default: null
    }
  },
  components: {
    ApexChart
  },
  data() {
    return {
      ChartTopKey: 0,
      ChartBotKey: 0,
      Chart1options: {
        series: [
          {
            data: []
          }
        ],
        chart: {
          type: "line",
          height: 290,
          toolbar: {
            show: false
          },

          animations: {
            enabled: true,
            easing: "easeinout",
            speed: 800,
            animateGradually: {
              enabled: true,
              delay: 150
            },
            dynamicAnimation: {
              enabled: true,
              speed: 350
            }
          },
          stroke: {
            width: [],
            dashArray: []
          },
          legend: {
            show: false
          }
          //   id: "candles",
          //   toolbar: {
          //     autoSelected: "pan",
          //     show: false
          //   },
          //   zoom: {
          //     enabled: false
          //   }
        },
        tooltip: {
          enabled: true,
          shared: true,
          // eslint-disable-next-line no-unused-vars
          custom: function({ seriesIndex, dataPointIndex, w }) {
            // eslint-disable-next-line no-unused-vars
            var o = w.globals.seriesCandleO[0][dataPointIndex];
            // eslint-disable-next-line no-unused-vars
            var h = w.globals.seriesCandleH[0][dataPointIndex];
            // eslint-disable-next-line no-unused-vars
            var l = w.globals.seriesCandleL[0][dataPointIndex];
            // eslint-disable-next-line no-unused-vars
            var c = w.globals.seriesCandleC[0][dataPointIndex];
            if (c != undefined) {
              return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span style=color:#fff>
              قیمت
              </span>
              </div>
              <div class="bottomDivTooltip">
              <p style=color:#000;font-size:0.8em>پایانی : ${c.toLocaleString()} ریال</p>
              <p style=color:#000;font-size:0.8em>اولین : ${o.toLocaleString()} ریال</p>
              <p style=color:#000;font-size:0.8em>پایین ترین : ${l.toLocaleString()} ریال</p>
              <p style=color:#000;font-size:0.8em>بالاترین : ${h.toLocaleString()} ریال</p>
              </div>
              </div>
            `;
            } else {
              return null;
            }
          }
        },
        dataLabels: {
          enabled: false
        },
        xaxis: {
          tickAmount: 10,
          type: "category",
          labels: {
            formatter: function(val) {
              return String(new Date(val).toLocaleDateString("fa-IR"));
            }
          },
          axisBorder: {
            show: true,
            color: "#78909C",
            offsetX: 0,
            offsetY: 0
          },
          axisTicks: {
            show: true,
            borderType: "solid",
            color: "#78909C",
            width: 6,
            offsetX: 0,
            offsetY: 0
          },
          title: {
            text: "تاریخ",
            rotate: -90,
            offsetX: 0,
            offsetY: 0,
            style: {
              fontSize: "12px",
              fontFamily: "Helvetica, Arial, sans-serif",
              fontWeight: 600,
              cssClass: "apexcharts-yaxis-title"
            }
          }
        },
        yaxis: {
          axisBorder: {
            show: true,
            color: "#78909C",
            offsetX: 0,
            offsetY: 0
          },
          axisTicks: {
            show: true,
            borderType: "solid",
            color: "#78909C",
            width: 6,
            offsetX: 0,
            offsetY: 0
          },
          title: {
            text: "قیمت تعدیلی",
            rotate: -90,
            offsetX: 0,
            offsetY: 0,
            style: {
              fontSize: "12px",
              fontFamily: "Helvetica, Arial, sans-serif",
              fontWeight: 600,
              cssClass: "apexcharts-yaxis-title"
            }
          },
          tooltip: {
            enabled: true
          }
        }
      },
      ChartoptionsBar: {
        series: [
          {
            name: "volume",
            data: [
              {
                x: new Date(1538778600000),
                y: [62222]
              }
            ]
          }
        ],
        chart: {
          height: 160,
          type: "bar",
          brush: {
            enabled: true,
            target: "candles"
          },
          selection: {
            enabled: true,
            xaxis: {
              min: new Date("20 Jan 2017").getTime(),
              max: new Date("10 Dec 2017").getTime()
            },
            fill: {
              color: "#ccc",
              opacity: 0.4
            },
            stroke: {
              color: "#0D47A1"
            }
          }
        },
        dataLabels: {
          enabled: false
        },
        plotOptions: {
          bar: {
            columnWidth: "80%",
            colors: {
              ranges: [
                {
                  from: -1000,
                  to: 0,
                  color: "#F15B46"
                },
                {
                  from: 1,
                  to: 10000,
                  color: "#FEB019"
                }
              ]
            }
          }
        },
        stroke: {
          width: 0
        },
        xaxis: {
          type: "datetime",
          axisBorder: {
            offsetX: 13
          }
        },
        yaxis: {
          labels: {
            show: false
          }
        }
      }
    };
  },
  computed: {},
  methods: {
    GetFiltered() {
      if (
        !(
          this.notices === null ||
          this.notices === undefined ||
          this.notices === []
        )
      ) {
        let Data = this.notices.candles;

        // eslint-disable-next-line no-unused-vars
        let Filtered = [];
        Data.filter(d => {
          let D = new Date(
            d.engdate.split("-")[0],
            d.engdate.split("-")[1],
            d.engdate.split("-")[2]
          ).getTime();
          Filtered.push({
            x: D,
            y: [
              Math.round(d.adjustedfirst * 100) / 100,
              Math.round(d.adjustedhigh * 100) / 100,
              Math.round(d.adjustedlow * 100) / 100,
              Math.round(d.adjustedclosing * 100) / 100
            ]
          });
        });
        this.Chart1options.series = [];
        this.Chart1options.series.push({
          name: "candle",
          type: "candlestick",
          data: Filtered
        });
        this.Chart1options.chart.stroke.width.push(3);
        this.Chart1options.chart.stroke.dashArray.push(0);
        let supplines = [];
        let resistlines = [];
        let Supp = this.notices.supppoints;
        let Resistence = this.notices.resistancepoints;
        Supp.filter(d => {
          let suppline = [];
          d.filter(item => {
            let D = new Date(
              item.x.split("-")[0],
              item.x.split("-")[1],
              item.x.split("-")[2]
            ).getTime();
            suppline.push({
              x: D,
              y: [item.y]
            });
          });
          supplines.push(suppline);
        });
        let scounter = 1;
        supplines.filter(d => {
          this.Chart1options.series.push({
            name: "حمایت " + scounter,
            type: "line",
            data: d
          });
          this.Chart1options.chart.stroke.width.push(1);
          this.Chart1options.chart.stroke.dashArray.push(1);
          scounter = scounter + 1;
        });

        Resistence.filter(d => {
          let resistline = [];
          d.filter(item => {
            let D = new Date(
              item.x.split("-")[0],
              item.x.split("-")[1],
              item.x.split("-")[2]
            ).getTime();
            resistline.push({
              x: D,
              y: [item.y]
            });
          });
          resistlines.push(resistline);
        });
        let rcounter = 1;
        resistlines.filter(d => {
          this.Chart1options.series.push({
            name: "مقاومت" + rcounter,
            type: "line",
            data: d
          });
          this.Chart1options.chart.stroke.width.push(0);
          this.Chart1options.chart.stroke.dashArray.push(1);
          rcounter = rcounter + 1;
        });
        //// console.log(this.Chart1options.chart.stroke);
        this.ChartTopKey = this.ChartTopKey + 1;
      }
    }
  },
  created() {
    // this.cardheight = this.heightCalc();
  },
  mounted() {},
  watch: {
    notices() {
      this.GetFiltered();
    }
  }
};
</script>
<style scoped></style>
