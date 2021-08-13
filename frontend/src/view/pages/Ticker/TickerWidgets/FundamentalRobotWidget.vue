<template>
  <ApexChart
    type="bar"
    width="100%"
    height="200%"
    :key="ApexChartKey"
    :series="series"
    :chartOptions="chartOptions"
  />
</template>

<script>
import ApexChart from "@/view/content/charts/ApexChart";

export default {
  name: "FundamentalRobot",
  components: {
    ApexChart
  },
  props: { liveData: Array, FundamentalRobot: Array },
  data() {
    return {
      ApexChartKey: 0,
      loading: true,
      lastUpdate: "",
      series: [
        {
          name: "",
          data: []
        }
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 350,
          toolbar: {
            show: false
          }
        },
        legend: {
          show: false
        },
        colors: [
          "#011627",
          "#E09F3E",
          "#9E2A2B",
          "#05668D",
          "#1AA47C",
          "#335C67",
          "#118AB2"
        ],
        // colors: [
        //   "#EF476F","#E09F3E","#5F2663","#118AB2","#073B4C","#73BB6F",
        //   "#068292",
        //   "#50A3AB",
        //   "#B50D45",
        //   "#5ACCB7"
        // ],
        noData: {
          text: "دیتای موردنظر وجود ندارد",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            // fontSize: "18px",
            fontFamily: "Vazir-Medium-FD"
          }
        },
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: "60%",
            distributed: true
          }
        },
        dataLabels: {
          enabled: true,

          // offsetX:10,
          offsetY: 5,
          textAnchor: "middle",
          style: {
            fontSize: "0.8em",
            fontFamily: "Vazir-Light-FD",
            colors: ["#fff"]
          }
        },

        tooltip: {
          enabled: true
        },
        yaxis: {
          // min:0,
          max: 200000,

          labels: {
            style: {
              fontSize: "0.7em"
            }
          }
        },
        xaxis: {
          labels: {
            style: {
              fontSize: "0.7em"
            }
          },
          categories: [
            // "Earning Power Value",
            // "Current Asset Value",
            // "TangibleBook",
            // "Projected FCF",
            // "Median PS Value",
            // "Graham Number",
            // "Peter Lynch Value",
            // "DCF (FCF BASED)",
            // "DCF (Earning Based)"
          ]
        },
        annotations: {
          xaxis: [
            {
              x: 0,
              strokeDashArray: 6,
              borderColor: "#000",
              fillColor: "#c2c2c2",
              opacity: 1,
              offsetX: 0,
              offsetY: 0,
              label: {
                borderColor: "#c2c2c2",
                borderWidth: 1,
                borderRadius: 2,
                text: "قیمت سهم",
                textAnchor: "middle",
                position: "top",
                orientation: "horizontal",
                offsetX: 0,
                offsetY: 0,
                style: {
                  background: "#fff",
                  color: "#777",
                  fontSize: "12px",
                  fontWeight: 400,
                  fontFamily: undefined,
                  cssClass: "apexcharts-xaxis-annotation-label"
                }
              }
            }
          ]
        }
      }
    };
  },
  watch: {
    FundamentalRobot() {
      this.renderData();
    }
  },
  methods: {
    renderData() {
      // console.log(this.FundamentalRobot);
      if (
        !(
          this.FundamentalRobot.length == 0 ||
          this.FundamentalRobot === undefined
        )
      ) {
        let max = [];
        this.chartOptions.xaxis.categories = [];
        this.series[0].data = [];
        // this.series = [];
        this.FundamentalRobot.filter(d => {
          if (d.RatioValue != "NaN") max.push(d.RatioValue);

          this.lastUpdate = d.CalculatedOn;
          console.log(d.RatioValue);
          // this.chartOptions.xaxis.categories.push(d.Ratio);
          this.chartOptions.xaxis.categories.push(d.displayTitle);
          if (d.Ratio == "PeterLynch") {
            this.series[0].data.push(Math.round(d.RatioValue) / 10);
          } else this.series[0].data.push(Math.round(d.RatioValue));
        });

        if (!(this.liveData.length == 0 || this.liveData === undefined)) {
          this.liveData.filter(d => {
            // console.log(d.close)
            this.chartOptions.annotations.xaxis[0].x = d.close;
            if (d.close != "NaN") max.push(d.close);
          });
        }
        console.log("max:", max);
        let Max = Math.max(...max);
        console.log("max:", Max);
        Max = Max + (Max / 10);

        this.chartOptions.yaxis.max = Max;

        this.ApexChartKey = this.ApexChartKey + 1;
        this.loading = false;
      } else {
        this.loading = false;
      }
    }
  }
};
</script>
