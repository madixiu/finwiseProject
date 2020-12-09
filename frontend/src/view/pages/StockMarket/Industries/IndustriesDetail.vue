<template>
  <div>
    <div class="row">
      <div class="col-xxl-12 col-md-12 mb-3">
        <v-card>
          <v-card-title>شرکتهای موجود در شاخص</v-card-title>
        </v-card>
      </div>
      <div class="col-xxl-5 col-md-5 mb-3">
        <v-card>
          <v-card-title>شاخص صنعت</v-card-title>
          <ApexChart
            type="area"
            width="100%"
            height="200%"
            :series="Shakhes"
            :chartOptions="ShakhesOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-4 col-md-4 mb-3">
        <v-card>
          <v-card-title>ارزش شرکت ها</v-card-title>
          <ApexChart
            type="pie"
            width="100%"
            height="200%"
            :series="IndustruesValue"
            :chartOptions="IndustruesValueOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-3 col-md-3 mb-3">
        <v-card>
          <v-card-title>?</v-card-title>
          <template>
            <v-data-table
              dense
              :headers="headersEX"
              :items="itemsEX"
              item-key="name"
              class="elevation-1 Persiantable"
              :hide-default-footer="true"
            ></v-data-table>
          </template>
        </v-card>
      </div>
      <div class="col-xxl-6 col-md-6 mb-3">
        <v-card>
          <v-card-title>تاثیر در شاخص</v-card-title>
          <ApexChart
            type="bar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
          <div class="Mychips">
            <v-chip class="mb-2" label large>
              مجموع وضعیت تاثیر در شاخص
              <v-chip color="#ad0018" small dark label class="mr-3">
                4.7-
              </v-chip>
            </v-chip>
          </div>
        </v-card>
      </div>
      <div class="col-xxl-6 col-md-6 mb-3">
        <v-card>
          <v-card-title>ورود و خروج حقیقی</v-card-title>
          <ApexChart
            type="bar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
          <div class="Mychips">
            <v-chip class="mb-2" label large>
              مجموع وضعیت تاثیر در شاخص
              <v-chip color="#00ad19" small dark label class="mr-3">
                3.7
              </v-chip>
            </v-chip>
          </div>
        </v-card>
      </div>
      <div class="col-xxl-4 col-md-6 col-xs-12 col-sm-12">
        <FSWidget />
      </div>
      <div class="col-xxl-4 col-md-6 col-xs-12 col-sm-12">
        <VWidget />
      </div>

      <div class="col-xxl-4 col-md-4">
        <PWidget />
      </div>
      <div class="col-xxl-4 col-md-4">
        <ReturnWidget />
      </div>
      <div class="col-xxl-4 col-md-4">
        <DivWidget />
      </div>
      <div class="col-xxl-4 col-md-4 mb-4">
        <v-card>
          <v-card-title>technical</v-card-title>
          <ApexChart
            type="radar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-12 col-md-12">
        <v-card>
          <v-card-title>یه سری پای چارت</v-card-title>
          <div>
            <ApexChart
              type="pie"
              width="100%"
              height="150%"
              :series="IndustruesValue"
              :chartOptions="IndustruesValueOptions"
            />
          </div>
        </v-card>
      </div>
    </div>
  </div>
</template>
<script>
import ApexChart from "@/view/content/charts/ApexChart";
import FSWidget from "@/view/pages/Ticker/Rankers/FinStrengthWidget.vue";
import VWidget from "@/view/pages/Ticker/Rankers/ValuationWidget.vue";
import PWidget from "@/view/pages/Ticker/Rankers/ProfitabilityWidget.vue";
import ReturnWidget from "@/view/pages/Ticker/Rankers/ValuationReturnWidget.vue";
import DivWidget from "@/view/pages/Ticker/Rankers/DividendReturnWidget.vue";
export default {
  components: {
    ApexChart,
    FSWidget,
    VWidget,
    PWidget,
    ReturnWidget,
    DivWidget
  },
  data() {
    return {
      radarChartSeries: [{ data: [20, 100, 40, 30, 50, 80, 33] }],
      radarChartOptions: {
        chart: {
          height: 350,
          type: "radar"
        },
        dataLabels: {
          enabled: true
        },
        plotOptions: {
          radar: {
            size: 140,
            polygons: {
              strokeColors: "#e9e9e9",
              fill: {
                colors: ["#f8f8f8", "#fff"]
              }
            }
          }
        },
        colors: ["#FF4560"],
        // markers: {
        //   size: 4,
        //   colors: ["#fff"],
        //   strokeColor: "#FF4560",
        //   strokeWidth: 2
        // },
        tooltip: {
          y: {
            formatter: function(val) {
              return val;
            }
          }
        },
        xaxis: {
          categories: [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
          ]
        },
        yaxis: {
          tickAmount: 7,
          labels: {
            formatter: function(val, i) {
              if (i % 2 === 0) {
                return val;
              } else {
                return "";
              }
            }
          }
        }
      },
      headersEX: [
        {
          text: "Dessert (100g serving)",
          align: "start",
          sortable: false,
          value: "name"
        },
        { text: "Calories", value: "calories" },
        { text: "Fat (g)", value: "fat" },
        { text: "Carbs (g)", value: "carbs" },
        { text: "Protein (g)", value: "protein" },
        { text: "Iron (%)", value: "iron" }
      ],
      itemsEX: [
        {
          name: "Frozen Yogurt",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%"
        },
        {
          name: "Ice cream sandwich",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%"
        },
        {
          name: "Eclair",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%"
        }
      ],
      Shakhes: [
        {
          name: "XYZ MOTORS",
          data: this.generateDayWiseTimeSeries(0, 18)
        }
      ],
      ShakhesOptions: {
        chart: {
          type: "area",
          stacked: false,
          height: 350,
          zoom: {
            type: "x",
            enabled: true,
            autoScaleYaxis: true
          },
          toolbar: {
            autoSelected: "zoom"
          }
        },
        dataLabels: {
          enabled: false
        },
        markers: {
          size: 0
        },
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100]
          }
        },
        yaxis: {
          labels: {
            formatter: function(val) {
              return val.toFixed(0);
            }
          },
          title: {
            text: "شاخص"
          }
        },
        xaxis: {
          type: "datetime"
        },
        tooltip: {
          shared: false,
          y: {
            formatter: function(val) {
              return val.toFixed(0);
            }
          }
        }
      },
      IndustruesValue: [44, 55, 13, 43, 22],
      IndustruesValueOptions: {
        chart: {
          width: 380,
          type: "pie"
        },
        labels: ["Team A", "Team B", "Team C", "Team D", "Team E"],
        legend: {
          show: false,
          position: "bottom"
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              }
            }
          }
        ]
      },

      HHseries: [
        {
          data: [
            5.4,
            4.65,
            3.76,
            2.88,
            2.5,
            2.1,
            2,
            1.8,
            -4,
            -4.4,
            -4.3,
            -4.2,
            -4,
            -3,
            -2.5,
            -1
          ]
        }
      ],
      HHoptions: {
        chart: {
          type: "bar",
          height: 100,
          stacked: true,
          toolbar: {
            show: false
          }
        },
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
            startingShape: "flat",
            endingShape: "rounded"
          }
        },
        dataLabels: {
          enabled: false
        },
        // stroke: {
        //   width: 1,
        //   colors: ["#fff"]
        // },
        grid: {
          xaxis: {
            lines: {
              show: true
            }
          }
        },
        stroke: {
          width: 0,
          colors: ["#fff"]
        },
        yaxis: {
          min: -5,
          max: 5,
          title: {
            // text: 'Age',
          }
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
        // title: {
        //   text: "Mauritius population pyramid 2011"
        // },
        xaxis: {
          categories: [
            "85+",
            "80-84",
            "75-79",
            "70-74",
            "65-69",
            "60-64",
            "55-59",
            "50-54",
            "45-49",
            "40-44",
            "35-39",
            "30-34",
            "25-29",
            "20-24",
            "15-19",
            "10-14",
            "5-9",
            "0-4"
          ],
          labels: {
            formatter: function(val) {
              return Math.abs(Math.round(val)) + "%";
            }
          }
        }
      }
    };
  },
  computed: {},

  methods: {
    generateDayWiseTimeSeries(s, count) {
      let values = [
        [4, 3, 10, 9, 29, 19, 25, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5],
        [2, 3, 8, 7, 22, 16, 23, 7, 11, 5, 12, 5, 10, 4, 15, 2, 6, 2]
      ];
      let i = 0;
      let series = [];
      let x = new Date("11 Nov 2012").getTime();
      while (i < count) {
        series.push([x, values[s][i]]);
        x += 3000000;
        i++;
      }
      console.log(series);
      return series;
    }
  }
};
</script>
<style scoped>
.Persiantable {
  direction: rtl;
  text-align: right;
}
.Mychips {
  text-align: center;
}
</style>
