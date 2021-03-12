<template>
  <div>
    <div class="row">
      <div class="col-xxl-3 col-lg-6 ">
        <v-card height="343">
          <v-card-title>شرکتهای موجود در شاخص</v-card-title>
          <b-table
            thClass="shakhes-table-head"
            class="shakhes-table"
            tbody-tr-class="shakhes-table-row"
            sticky-header="285px"
            hover
            sort-icon-left
            small
            :items="TableData"
            :fields="headerstock2"
          >
            <template #cell(ticker)="data">
              <b class="shakhes-table-cell">{{ data.value }}</b>
            </template>
            <template #cell(last)="data">
              <b class="shakhes-table-cell">{{
                data.value.toLocaleString()
              }}</b>
            </template>
            <template #cell(lastPercent)="data">
              <b v-if="data.value == 0" class="shakhes-table-cell">{{
                data.value
              }}</b>
              <b v-if="data.value < 0" class="shakhes-table-cell-red">{{
                data.value
              }}</b>
              <b v-if="data.value > 0" class="shakhes-table-cell-green">{{
                data.value
              }}</b>
            </template>
          </b-table>
        </v-card>
        <!-- <v-card>
          <v-card-title>شرکتهای موجود در شاخص</v-card-title>
          <v-divider></v-divider>
          <v-data-table
            :headers="headerstock"
            :items="stocklist"
            class="elevation-1 FinancialStrength"
            :hide-default-footer="true"
          >
            <template v-slot:[`item.marketcap`]="{ item }">
              <span class="cellItem"
                >{{ numberWithCommas(roundTo(item.marketcap / 1000000000, 2)) }}
                میلیارد ریال
              </span>
            </template>
            <template v-slot:[`item.close`]="{ item }">
              <span
                class="spandata"
                v-bind:class="[
                  item.close > item.open ? 'greenItem' : 'redItem'
                ]"
              >
              </span>
            </template>
          </v-data-table>
        </v-card> -->
      </div>
      <div class="col-xxl-3 col-lg-6 ">
        <v-card height="343">
          <v-card-title>شاخص صنعت</v-card-title>
          <ApexChart
            v-if="Shakhes.length"
            type="area"
            width="100%"
            height="180%"
            :series="Shakhes"
            :chartOptions="ShakhesOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-3 col-lg-6">
        <v-card height="343">
          <v-card-title>ارزش شرکت ها</v-card-title>
          <ApexChart
            v-if="IndustriesValue.length"
            type="pie"
            width="100%"
            height="180%"
            :series="IndustriesValue"
            :chartOptions="IndustriesValueOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-3 col-lg-6">
        <v-card height="343">
          <v-card-title>تکنیکال</v-card-title>
          <ApexChart
            v-if="TechnicalSeries.length"
            type="radar"
            width="100%"
            height="200%"
            :series="TechnicalSeries"
            :chartOptions="TechnicalOptions"
          />
        </v-card>
      </div>
      <!-- <div class="col-xxl-3 col-md-6 ">
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
      </div> -->
      <div class="col-xxl-6 col-md-6 ">
        <v-card>
          <v-card-title>تاثیر در شاخص</v-card-title>
          <ApexChart
            v-if="ImpactSeries.length"
            type="bar"
            width="100%"
            height="200%"
            :series="ImpactSeries"
            :chartOptions="ImpactOptions"
          />
          <div class="Mychips">
            <v-chip class="mb-2" label large>
              مجموع وضعیت تاثیر در شاخص
              <v-chip
                v-bind:class="[this.sumImpact >= 0 ? 'greenItem' : 'redItem']"
                small
                dark
                label
                class="mr-3"
              >
                <span style="font-family:'Vazir-Medium-FD';direction:ltr">{{
                  parseInt(sumImpact)
                }}</span>
              </v-chip>
            </v-chip>
          </div>
        </v-card>
      </div>
      <div class="col-xxl-6 col-md-6 ">
        <v-card>
          <v-card-title>ورود و خروج حقیقی</v-card-title>
          <ApexChart
            v-if="HHseries.length"
            type="bar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
          <div class="Mychips">
            <v-chip class="mb-2" label large>
              مجموع ورود خروج حقیقی
              <v-chip
                v-bind:class="[this.sumHH >= 0 ? 'greenItem' : 'redItem']"
                small
                dark
                label
                class="mr-3"
              >
                <span style="font-family:'Vazir-Medium-FD';direction:ltr">{{
                  fixer(sumHH)
                }}</span>
                <span class="mr-1">میلیارد ریال</span>
              </v-chip>
            </v-chip>
          </div>
        </v-card>
      </div>
      <!-- <div class="col-xxl-4 col-md-6 col-xs-12 col-sm-12">
        <FSWidget />
      </div>
      <div class="col-xxl-4 col-md-6 col-xs-12 col-sm-12">
        <VWidget />
      </div>

      <div class="col-xxl-4 col-md-4">
        <PWidget />  <div class="col-xxl-3 col-md-6 ">
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
      </div>
      <div class="col-xxl-4 col-md-4">
        <ReturnWidget />
      </div>
      <div class="col-xxl-4 col-md-4">
        <DivWidget />
      </div> -->

      <!-- <div class="col-xxl-12 col-md-12">
        <v-card>
          <v-card-title>یه سری پای چارت</v-card-title>
          <div>
            <ApexChart
              type="pie"
              width="100%"
              height="150%"
              :series="IndustriesValue"
              :chartOptions="IndustriesValueOptions"
            />
          </div>
        </v-card>
      </div> -->
    </div>
  </div>
</template>
<script>
import ApexChart from "@/view/content/charts/ApexChart";
// import FSWidget from "@/view/pages/Ticker/Rankers/FinStrengthWidget.vue";
// import VWidget from "@/view/pages/Ticker/Rankers/ValuationWidget.vue";
// import PWidget from "@/view/pages/Ticker/Rankers/ProfitabilityWidget.vue";
// import ReturnWidget from "@/view/pages/Ticker/Rankers/ValuationReturnWidget.vue";
// import DivWidget from "@/view/pages/Ticker/Rankers/DividendReturnWidget.vue";
export default {
  components: {
    ApexChart
    // FSWidget,
    // VWidget,
    // PWidget,
    // ReturnWidget,
    // DivWidget
  },
  data() {
    return {
      TableData: [],
      sumImpact: 0,
      sumHH: 0,
      headerstock: [
        {
          text: "نماد",
          value: "ticker"
        },
        {
          text: "ارزش بازار",
          value: "marketcap"
        },
        {
          text: "زمان ارسال",
          value: "close"
        }
      ],
      headerstock2: [
        {
          label: "نماد",
          key: "ticker",
          sortable: true,
          thClass: "shakhes-table-head"
        },
        {
          label: "آخرین قیمت",
          key: "last",
          sortable: true,
          thClass: "shakhes-table-head"
        },
        {
          label: "درصد آخرین قیمت",
          key: "lastPercent",
          sortable: true,
          thClass: "shakhes-table-head"
        }
      ],

      TechnicalSeries: [],
      TechnicalOptions: {
        chart: {
          height: 100,
          type: "radar",
          toolbar: {
            show: false
          }
        },

        labels: [],
        dataLabels: {
          enabled: true
        },
        plotOptions: {
          radar: {
            size: 100,
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
      Shakhes: [
        {
          name: "XYZ MOTORS",
          data: this.generateDayWiseTimeSeries(0, 30)
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
            show: false,
            autoSelected: "zoom"
          }
        },
        labels: [],
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
      IndustriesValue: [],
      IndustriesValueOptions: {
        chart: {
          width: 380,
          type: "pie",
          fontFamily: "Vazir-Medium-FD"
        },
        // colors: ["#573956", "#9e556a", "#db7b6a", "#fdb462", "#f9f871"],
        labels: [],
        legend: {
          show: true,
          position: "right"
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

      ImpactSeries: [],
      ImpactOptions: {
        chart: {
          type: "bar",
          height: 100,
          toolbar: {
            show: false
          }
        },
        labels: [],
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
            distributed: false
          }
        },
        dataLabels: {
          enabled: false,
          style: {
            fontSize: "0.7em",
            fontFamily: "Vazir-Medium-FD"
          }
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
            text: "تاثیر در شاخص",
            fontFamily: "Vazir-Light-FD"
          },
          fontFamily: "Vazir-Light-FD"
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
              return val + "%";
            }
          }
        },
        // title: {
        //   text: "Mauritius population pyramid 2011"
        // },
        legend: {
          show: false
        },
        xaxis: {
          categories: [],

          labels: {
            show: true
            // formatter: function(val) {
            //   return Math.abs(Math.round(val)) + "%";
            // }
          }
        }
      },
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
        tooltip: {
          shared: false,
          followCursor: true,
          intersect: false,
          fillSeriesColor: true,

          x: {
            formatter: function(val) {
              return val;
            }
          },
          y: {
            title: {
              formatter: seriesName => seriesName
            }
            // formatter: function(value) {
            //   return value;
            // }
          }
        },
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
  computed: {},
  mounted() {
    this.loadData();
  },
  watch: {
    // News() {
    //   this.populateData();
    //   this.loading = false;
    // }
  },
  methods: {
    fixer(input) {
      return this.truncate(input / 1000000000, 2);
    },
    truncate(num, fixed) {
      var re = new RegExp("^-?\\d+(?:.\\d{0," + (fixed || -1) + "})?");
      return num.toString().match(re)[0];
    },
    // numberWithCommas(x) {
    //   if (x == "-") {
    //     return x;
    //   }
    //   let parts = x.toString().split(".");
    //   parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    //   return parts.join(".");
    // },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    // roundTo(n, digits) {
    //   if (n == "-") {
    //     return n;
    //   }

    //   let negative = false;
    //   if (digits === undefined) {
    //     digits = 0;
    //   }
    //   if (n < 0) {
    //     negative = true;
    //     n = n * -1;
    //   }
    //   let multiplicator = Math.pow(10, digits);
    //   n = parseFloat((n * multiplicator).toFixed(11));
    //   n = (Math.round(n) / multiplicator).toFixed(digits);
    //   if (negative) {
    //     n = (n * -1).toFixed(digits);
    //   }
    //   return n;
    // },
    // loadData() {
    //   this.getNews();
    // },
    // populateData() {
    //   this.stocklist = this.News;

    // },
    generateDayWiseTimeSeries(s, count) {
      let values = [
        [4, 3, 10, 9, 29, 19, 25, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5],
        [4, 3, 8, 7, 22, 16, 23, 7, 11, 5, 12, 5, 10, 4, 15, 2, 6, 2]
      ];
      let i = 0;
      let series = [];
      let x = new Date("11 Nov 2021").getTime();
      while (i < count) {
        series.push([x, values[s][i]]);
        x += 3000000;
        i++;
      }
      return series;
    },
    async loadData() {
      await this.axios
        .get("/api/IndexDetails/" + this.$route.params.id + "/")
        .then(responsex => {
          let data = responsex.data[0];
          //     this.IndustriesValue = this.News.map(function(obj) {
          //   return obj["marketcap"];
          // });
          // this.IndustriesValueOptions.labels = this.News.map(function(obj) {
          //   return obj["ticker"];
          // });
          let IndustriesList = [];
          // let IndustriesListNames = [];
          let technicalList = [];
          let technicalNames = [];
          let HHseries = [];
          let impactList = [];
          let ImpactNames = [];
          let HHNames = [];
          let IndustriesListNames = [];

          for (let i = 0; i < data.Impact.ImpactData.length; i++) {
            IndustriesList.push(data.marketCap.marketCapData[i].marketcap);
            impactList.push(data.Impact.ImpactData[i].Impact);
            HHseries.push(data.HH.HHData[i].HH);
            ImpactNames.push(data.Impact.ImpactData[i].ticker);
            HHNames.push(data.HH.HHData[i].ticker);
            IndustriesListNames.push(data.marketCap.marketCapData[i].ticker);
            technicalList.push(data.Technical.TechnicalData[i].signal);
            technicalNames.push(data.Technical.TechnicalData[i].ticker);
          }
          // for (let item of this.News) {
          //   IndustriesList.push(item.marketcap);
          //   impactList.push(item.Impact);
          //   Names.push(item.ticker);
          //   HHseries.push(item.HH);
          //   this.sumImpact = item.Impact + this.sumImpact;
          //   this.sumHH = item.HH + this.sumHH;
          // }

          this.sumImpact = data.Impact.Sum;
          this.sumHH = data.HH.Sum;
          this.HHoptions.labels = HHNames;
          this.ImpactOptions.labels = ImpactNames;
          this.IndustriesValueOptions.labels = IndustriesListNames;
          this.HHoptions.xaxis.categories = HHNames;
          this.ImpactOptions.xaxis.categories = ImpactNames;
          this.TechnicalOptions.xaxis.categories = technicalNames;
          // this.IndustriesValueOptions.xaxis.categories = IndustriesListNames;

          // this.HHoptions.labels = Names;
          // this.ImpactOptions.labels = Names;
          // this.IndustriesValueOptions.labels = Names;
          this.TableData = data.Table.TableData;
          this.HHseries = [{ data: HHseries }];
          this.ImpactSeries = [{ data: impactList }];
          this.TechnicalSeries = [{ data: technicalList }];
          // IndustriesList.sort(function(a, b) {
          //   return b - a;
          // });

          this.IndustriesValue = IndustriesList;
          // this.HHoptions.xaxis.categories = Names;
          // this.ImpactOptions.xaxis.categories = Names;
          // this.IndustriesValueOptions.xaxis.categories = Names;

          // impactList.sort(function(a, b) {
          //   return b - a;
          // });
          // HHseries.sort(function(a, b) {
          //   return b - a;
          // });
          // this.MaxMinChartsImpact(impactList[0], impactList[impactList.length - 1]);
          // this.MaxMinChartsHH(HHseries[0], HHseries[HHseries.length - 1]);

          if (impactList[0] >= Math.abs(impactList[impactList.length - 1])) {
            this.ImpactOptions.yaxis.min = impactList[0] * -1;
            this.ImpactOptions.yaxis.max = impactList[0];
          } else {
            this.ImpactOptions.yaxis.min = impactList[impactList.length - 1];
            this.ImpactOptions.yaxis.max = Math.abs(
              impactList[impactList.length - 1]
            );
          }
          if (HHseries[0] >= Math.abs(HHseries[HHseries.length - 1])) {
            this.HHoptions.yaxis.min = HHseries[0] * -1;
            this.HHoptions.yaxis.max = HHseries[0];
          } else {
            this.HHoptions.yaxis.min = HHseries[HHseries.length - 1];
            this.HHoptions.yaxis.max = Math.abs(HHseries[HHseries.length - 1]);
          }

        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
<style>
.apexcharts-text tspan {
  font-family: "Vazir-Medium-FD" !important;
}
.apexcharts-legend-text,
.apexcharts-text,
.apexcharts-title-text {
  font-family: "Vazir-Medium-FD" !important;
}
.shakhes-table {
  text-align: center;
  /* font-size: 1em; */
  line-height: 1;
  font-family: "Vazir-Medium-FD" !important;
}
.shakhes-table-head {
  font-size: 0.8rem !important;
  font-weight: 500;
}

.shakhes-table-cell {
  vertical-align: middle !important;
  text-align: center;
  font-size: 0.9em;
  line-height: 1;
  font-weight: 400;
  font-family: "Vazir-Medium-FD" !important;
}
.shakhes-table-cell-green {
  vertical-align: middle !important;
  text-align: center;
  font-size: 0.9em;
  line-height: 1;
  color: green;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
}
.shakhes-table-cell-red {
  text-align: center;
  vertical-align: middle !important;
  font-size: 0.9em;
  line-height: 1;
  color: red;
  font-weight: 400;
  font-family: "Vazir-Medium-FD";
  /* font-family: "Dirooz FD"; */
}
.shakhes-table-row {
  direction: ltr;
  vertical-align: middle !important;
}
.cellItem {
  font-family: "Vazir-Medium-FD";
  font-weight: 700;
}
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.Persiantable {
  direction: rtl;
  text-align: right;
}
.Mychips {
  text-align: center;
}
.redItem {
  color: aliceblue;
  background-color: #f63538 !important;
  font-family: "Vazir-Medium-FD" !important;
}
.greenItem {
  color: aliceblue;
  background-color: #30cc5a !important;
  font-family: "Vazir-Medium-FD" !important;
}
</style>
