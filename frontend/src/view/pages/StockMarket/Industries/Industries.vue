<template>
  <div>
    <div class="row">
      <!-- <div class="col-12">
        <IndustryChart :inputData="this.IndustryData"></IndustryChart>
      </div> -->

      <div class="col-xxl-6 col-md-6 mb-4">
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

      <div class="col-xxl-6 col-md-6">
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
            type="bar"
            width="100%"
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
// import IndustryChart from "@/view/pages/StockMarket/Industries/Content/IndustriesChart.vue";
// import IndustryTechnicalBest from "@/view/pages/StockMarket/Industries/Content/IndustryTechnical‌Best";
// import IndustryTechnicalWorse from "@/view/pages/StockMarket/Industries/Content/IndustryTechnicalWorse";
export default {
  name: "Industries",
  components: {
    ApexChart
    // IndustryChart
    // IndustryTechnicalBest,
    // IndustryTechnicalWorse,
    // MarqueeText
  },
  data() {
    return {
      // paused: false,
      IndustryData: [],
      ReturnSeries: [
        {
          data: [
            400,
            390,
            386,
            378,
            375,
            364,
            355,
            341,
            337,
            332,
            323,
            321,
            286,
            278,
            275,
            264,
            255,
            241,
            237,
            232,
            223,
            221,
            186,
            178,
            175,
            164,
            155,
            141,
            137,
            132,
            123,
            121,
            86,
            78,
            75,
            64,
            55,
            41,
            37,
            32,
            23,
            21
          ]
        }
      ],
      ReturnOptions: {
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
        plotOptions: {
          bar: {
            horizontal: true,
            distributed: true,
            barHeight: "100%",
            dataLabels: {
              position: "bottom"
            }
          }
        },
        dataLabels: {
          enabled: true,
          textAnchor: "start",
          style: {
            colors: ["#fff"]
          },
          formatter: function(val, opt) {
            return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val;
          }
        },
        xaxis: {
          categories: [
            "ماشین آلات",
            "فراورده نفتی",
            "کانه فلزی",
            "کانی غیرفلزی",
            "غذایی بجز قند",
            "اطلاعات و ارتباطات",
            "ذغال سنگ",
            "خودرو",
            "قند و شکر",
            "حمل و نقل",
            "وسایل ارتباطی",
            "سایرمالی",
            "انتشار و چاپ",
            "فلزات اساسی",
            "شیمیایی",
            "دستگاههای برقی",
            "سرمایه گذاریها",
            "زراعت",
            "لاستیک",
            "چند رشته ای صنعتی",
            "رادیویی",
            "محصولات چوبی",
            "بیمه و بازنشسته",
            "منسوجات",
            "ابزار پزشکی",
            "اداره بازارهای مالی",
            "سایر معادن",
            "استخراجنفتجزکشف",
            "خرده فروشی به جز وسایل نقلیه",
            "محصولات چرمی",
            "سیمان",
            "بانکها",
            "محصولات کاغذ",
            "شاخص صنعت",
            "فنی مهندسی",
            "تامین آب، برق، گاز",
            "کاشی و سرامیک",
            "محصولات فلزی",
            "مواد دارویی",
            "انبوه سازی",
            "رایانه"
          ],
          labels: {
            formatter: function(val) {
              return val + "K";
            }
          }
        },
        yaxis: {
          title: {
            text: undefined
          }
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val + "K";
            }
          }
        },
        fill: {
          opacity: 1
        }
      },
      test: [
        {
          data: [
            1.4,
            2,
            2.2,
            2.5,
            2.8,
            3,
            3.8,
            4.6,
            2,
            2.2,
            2.5,
            2.8,
            3,
            3.8,
            4.6,
            2,
            2.2,
            2.5,
            2.8,
            3,
            3.8,
            4.6
          ]
        },
        {
          data: [
            -2.0,
            -2.9,
            -3.7,
            -3.6,
            -4.4,
            -4.5,
            -4.8,
            -5,
            -2.9,
            -3.7,
            -3.6,
            -4.4,
            -4.5,
            -4.8,
            -5,
            -2.9,
            -3.7,
            -3.6,
            -4.4,
            -4.5,
            -4.8,
            -5
          ]
        }
      ],
      testOptions: {
        chart: {
          type: "bar",
          height: 440,
          stacked: true,
          toolbar: {
            show: false
          }
        },
        colors: ["#008FFB", "#FF4560"],
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: "100%",
            dataLabels: {
              position: "top"
            }
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 0,
          colors: ["#fff"]
        },

        grid: {
          xaxis: {
            tickPlacement: "on",
            lines: {
              show: false
            }
          }
        },
        yaxis: {
          min: -10,
          max: 10,
          title: {
            // text: 'Age',
          },
          tickPlacement: "on"
        },
        tooltip: {
          shared: false,
          x: {
            formatter: function(val) {
              return val;
            }
          },
          y: {
            formatter: function(val) {
              return Math.abs(val) + "%";
            }
          }
        },
        xaxis: {
          categories: [
            "85+",
            "80-84",
            "75-79",
            "70-74",
            "65-69",
            "60-64",
            "55-59",
            "50-54"
          ]
        }
      },
      Pieseries: [],
      Barseries: [],
      HHseries: [],
      HHoptions: {
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
      },
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
      },
      EffectOnIndexSeries: [
        {
          data: []
        }
      ],
      BarchartOptions: {
        chart: {
          type: "bar",
          height: 350,
          animations: {
            enabled: false
          },
          toolbar: {
            show: false
          },
          fontFamily: "Vazir"
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

          style: {
            colors: ["#fff"]
          }
        },
        xaxis: {
          categories: [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
            "France",
            "Japan",
            "United States",
            "China",
            "Germany"
          ],
          labels: {
            show: true
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
            //   // console.log(chartContext);
            //   // console.log(seriesIndex);
            //   // console.log(config);
            // },
            dataPointSelection: (event, chartContext, config) => {
              // console.log(chartContext);
              // console.log(event);
              // console.log(config);
              console.log(config);
              this.testing(config.dataPointIndex);
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
  mounted() {
    this.loadData();
  },
  methods: {
    testing(seriesIndex) {
      // console.log(this.PiechartOptions.labels[seriesIndex]);
      // console.log(this.Pieseries[seriesIndex]);
      // this.PiechartOptions.labels = persianNames;
      // console.log(this.chartOptions.labels);

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
    loadData() {
      // eslint-disable-next-line no-unused-vars

      // eslint-disable-next-line no-unused-vars
      this.getPieChartData().then(resx => {
        // eslint-disable-next-line no-unused-vars
        this.getIndustries().then(resy => {
          // eslint-disable-next-line no-undef
          this.getHHDATA().then();
        });
      });
    },
    async getPieChartData() {
      await this.axios.get("/api/IndexMarketCap").then(responsive => {
        let data = responsive.data;
        let persianNames = [];
        let marketCaps = [];
        let itemValue = [];
        console.log(data);
        for (let item of data[0].TopIndustries) {
          // console.log(item);
          persianNames.push(item.persianName);
          marketCaps.push(item.marketCap);
          itemValue.push({ name: item.persianName, value: item.TradeValue });
        }
        marketCaps.push(data[1].Others.marketCapSum);
        persianNames.push("سایر");
        // console.log(persianNames);
        this.PiechartOptions.labels = persianNames;

        // console.log(this.chartOptions.labels);
        // marketCaps.sort(function(a, b) {
        //   return b - a;
        // });
        this.Pieseries = marketCaps;
        itemValue.sort(this.compareValues("value", "desc"));
        itemValue = itemValue.slice(0, 6);
        // console.log(itemValue);
        let names = [];
        let values = [];
        for (let item of itemValue) {
          names.push(item.name);
          values.push(item.value);
        }

        this.Barseries = [{ data: values }];
        this.BarchartOptions.xaxis.categories = names;
      });
    },
    async getIndustries() {
      await this.axios
        .get("/api/Indices/HistoricCap/ ")
        .then(responseInd => {
          this.IndustryData = responseInd.data;
        })
        .catch(error => {
          // console.log("GetTwoeCatch");
          console.log(error);
        });
    },
    async getHHDATA() {
      await this.axios
        .get("/api/Indices/HH")
        .then(responsea => {
          let data = responsea.data;
          // this.HHseries = data;
          // eslint-disable-next-line no-unused-vars
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
          console.log(HHseries2data);
        })
        .catch(error => {
          console.log(error);
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
          console.log(Impactseries2data);
        })
        .catch(error => {
          console.log(error);
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
<style scoped>
@import "~bootstrap/dist/css/bootstrap.css";
#fi {
  color: red !important;
}

.apexcharts-text tspan {
  font-family: "Vazir";
}
</style>
