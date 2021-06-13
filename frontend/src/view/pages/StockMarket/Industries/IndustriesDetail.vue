<template>
  <div id="testtt" ref="testtt">
    <div class="row">
      <div class="col-xxl-6 col-lg-6 mt-1" style="padding-left:5px">
        <v-card height="343">
          <v-toolbar dense>
            <v-toolbar-title>شرکتهای موجود در شاخص</v-toolbar-title>
          </v-toolbar>
          <b-table
            thClass="shakhes-table-head"
            class="shakhes-table"
            tbody-tr-class="shakhes-table-row"
            sticky-header="285px"
            hover
            striped
            sort-icon-left
            small
            :items="TableData"
            :fields="headerstock"
          >
            <template #cell(ticker)="data">
              <b class="shakhes-table-cell-ticker" @click="tickerClick(data)">{{
                data.value
              }}</b>
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
      </div>
      <div class="col-xxl-6 col-lg-6 mt-1" style="padding-right:5px">
        <v-card height="343">
          <v-toolbar dense>
            <v-toolbar-title>شاخص صنعت</v-toolbar-title>
          </v-toolbar>
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
      <div class="col-xxl-6 col-lg-6" style="padding-left:5px; padding-top:0px">
        <v-card height="343">
          <v-toolbar dense>
            <v-toolbar-title>ارزش شرکت ها</v-toolbar-title>
          </v-toolbar>
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
      <div
        class="col-xxl-6 col-lg-6"
        style="padding-right:5px; padding-top:0px"
      >
        <v-card height="343">
          <v-toolbar dense>
            <v-toolbar-title>تکنیکال</v-toolbar-title>
          </v-toolbar>
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
      <div
        class="col-xxl-6 col-md-6 "
        style="padding-left:5px; padding-top:0px"
      >
        <v-card>
          <v-toolbar dense>
            <v-toolbar-title>تاثیر در شاخص</v-toolbar-title>
          </v-toolbar>
          <ApexChart
            v-if="ImpactSeries.length"
            type="bar"
            width="100%"
            height="200%"
            :series="ImpactSeries"
            :chartOptions="ImpactOptions"
          />
          <div class="industryDetailChip">
            <v-chip class="mb-2" label large>
              مجموع وضعیت تاثیر در شاخص
              <v-chip
                :class="[
                  this.sumImpact >= 0
                    ? 'industryDetailGreenChip'
                    : 'industryDetailRedChip'
                ]"
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
      <div
        class="col-xxl-6 col-md-6 "
        style="padding-right:5px; padding-top:0px"
      >
        <v-card>
          <v-toolbar dense>
            <v-toolbar-title>ورود و خروج حقیقی</v-toolbar-title>
          </v-toolbar>
          <ApexChart
            v-if="HHseries.length"
            type="bar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
          <div class="industryDetailChip">
            <v-chip class="mb-2" label large>
              مجموع ورود خروج حقیقی
              <v-chip
                v-bind:class="[
                  this.sumHH >= 0
                    ? 'industryDetailGreenChip'
                    : 'industryDetailRedChip'
                ]"
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
    </div>
  </div>
</template>
<script>
import ApexChart from "@/view/content/charts/ApexChart";
import { SET_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";
import { ADD_BREADCRUMB } from "@/core/services/store/breadcrumbs.module";

export default {
  components: {
    ApexChart
  },
  data() {
    return {
      // IDs
      IndustriesID: [],
      HHID: [],
      ImpactID: [],

      TableData: [],
      sumImpact: 0,
      sumHH: 0,

      headerstock: [
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
              strokeColors: "#073b4c",
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
          followCursor: true,
          intersect: true,
          //   fillSeriesColor: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let n = series[seriesIndex][dataPointIndex];
            let Class = null;
            if (parseFloat(n) < 0) Class = "redSpan";
            else if (parseFloat(n) > 0) Class = "greenSpan";

            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${w.globals.labels[dataPointIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span class="${Class}">${n}</span>
            

              </div>
              </div>
            `;
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
          tickAmount: 5,
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
          name: "",
          // data: this.generateDayWiseTimeSeries(0, 30)
          data: null
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
          // theme:false,
          style: {
            fontFamily: "Vazir-Medium-FD"
          },
          // shared: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let n = series[seriesIndex][dataPointIndex];

            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${w.globals.seriesNames[0]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span>${n}</span>
            

              </div>
              </div>
            `;
          },
          x: {
            show: true,
            format: "hh:mm",
            // formatter: undefined,
            style: {
              fontFamily: "Vazir-Medium-FD"
            }
          }
          // y: {
          //   formatter: function(val) {
          //     return val.toFixed(0);
          //   }
          // }
        }
      },
      IndustriesValue: [],
      IndustriesValueOptions: {
        chart: {
          width: 380,
          type: "pie",
          fontFamily: "Vazir-Medium-FD",
          events: {
            // legendClick: function(chartContext, seriesIndex, config) {
            // },
            dataPointSelection: (event, chartContext, config) => {
              this.ChartClick(
                "Industries",
                chartContext,
                config.dataPointIndex
              );
            }
          }
        },
        // colors: ["#011627", "#E09F3E", "#9E2A2B"
        // , "#1AA47C", "#003049","#0E5D52","#540B0E","#069E97","#068292"
        // ,"#05668D"],
        colors: ["#EF476F", "#E09F3E", "#06D6A0", "#118AB2", "#073B4C"],
        labels: [],
        legend: {
          show: true,
          position: "right"
        },
        responsive: [
          {
            breakpoint: 380,
            options: {
              chart: {
                width: 200
              }
            }
          }
        ],
        stroke: {
          width: 1,
          colors: ["#3e3e4e"]
        },
        tooltip: {
          // eslint-disable-next-line no-unused-vars
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let backgroundColor = w.config.colors[seriesIndex];
            let n = series[seriesIndex];
            // let val = ""
            if (n != undefined) {
              //   let parts = n.toString().split(".");
              // parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              //  val = parts.join(".");
              let val = (n / 1000000000).toLocaleString();
              return `<div class="ApexTooltip">
            <div class="topDivTooltip" style=background-color:${backgroundColor}> 
              <span style=color:#fff>
              ${w.globals.labels[seriesIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span style=color:#000;font-size:0.8em class=mr-1>میلیارد ریال</span>
              <span style=color:#000;font-size:0.8em>${val}</span>

            

              </div>
              </div>
            `;
            } else {
              return null;
            }
          }
        }
      },

      ImpactSeries: [],
      ImpactOptions: {
        chart: {
          type: "bar",
          height: 100,
          toolbar: {
            show: false
          },
          events: {
            dataPointSelection: (event, chartContext, config) => {
              this.ChartClick("Impact", chartContext, config.dataPointIndex);
            }
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
          followCursor: true,
          intersect: false,
          fillSeriesColor: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let n = series[seriesIndex][dataPointIndex];

            let Class = null;
            if (parseFloat(n) < 0) Class = "redSpan";
            else if (parseFloat(n) > 0) Class = "greenSpan";

            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${w.globals.labels[dataPointIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span class="${Class}">${n}</span>
            

              </div>
              </div>
            `;
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
          },
          events: {
            dataPointSelection: (event, chartContext, config) => {
              this.ChartClick("HH", chartContext, config.dataPointIndex);
            }
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
          labels: {
            formatter: function(value) {
              return (value / 1000000000).toLocaleString();
            }
          },
          // min: -5,
          // max: 5,
          title: {
            text: "میلیارد ریال"
          }
        },
        tooltip: {
          followCursor: true,
          intersect: false,
          fillSeriesColor: true,
          custom: function({ series, seriesIndex, dataPointIndex, w }) {
            let n = series[seriesIndex][dataPointIndex];
            let Class = null;
            if (parseFloat(n) < 0) Class = "redSpan";
            else if (parseFloat(n) > 0) Class = "greenSpan";
            return `<div class="ApexTooltip">
            <div class="topDivTooltip"> 
              <span>
              ${w.globals.labels[dataPointIndex]}
              </span>
              </div>
              <div class="bottomDivTooltip">
              <span class="${Class}">${n.toLocaleString()}</span>
            

              </div>
              </div>
            `;
          }
        },

        xaxis: {
          categories: [],
          labels: {}
        }
      }
    };
  },
  created() {
    document.title = "Finwise - صنایع";
    this.$store.dispatch(SET_BREADCRUMB, [{ title: "خلاصه صنعت" }]);
  },
  computed: {},
  mounted() {
    this.loadData();
  },
  methods: {
    ChartClick(ChartType, context, seriesIndex) {
      if (ChartType == "Impact")
        this.$router.push({
          path: `/ticker/Overview/Overall/${this.ImpactID[seriesIndex]}`
        });
      else if (ChartType == "HH")
        this.$router.push({
          path: `/ticker/Overview/Overall/${this.HHID[seriesIndex]}`
        });
      else if (ChartType == "Industries")
        this.$router.push({
          path: `/ticker/Overview/Overall/${this.IndustriesID[seriesIndex]}`
        });
    },
    tickerClick(data) {
      this.$router.push({ path: `/ticker/Overview/Overall/${data.item.id}` });
    },
    fixer(input) {
      return this.truncate(input / 1000000000, 2);
    },
    truncate(num, fixed) {
      var re = new RegExp("^-?\\d+(?:.\\d{0," + (fixed || -1) + "})?");
      return num.toString().match(re)[0];
    },
    async loadData() {
      await this.axios
        .get("/api/IndexDetails/" + this.$route.params.id)
        .then(responsex => {
          let data = responsex.data;

          let IndustriesList = [];
          let technicalList = [];
          let technicalNames = [];
          let HHseries = [];
          let impactList = [];
          let ImpactNames = [];
          let HHNames = [];
          let IndustriesListNames = [];
          this.$store.dispatch(ADD_BREADCRUMB, [
            { title: data.Tepix.CorrectName }
          ]);
          this.Shakhes = [
            { name: data.Tepix.CorrectName, data: data.Tepix.apexData }
          ];

          for (let i = 0; i < data.Impact.ImpactData.length; i++) {
            this.IndustriesID.push(data.marketCap.marketCapData[i].id);
            this.HHID.push(data.HH.HHData[i].id);
            this.ImpactID.push(data.Impact.ImpactData[i].id);

            IndustriesList.push(data.marketCap.marketCapData[i].marketcap);
            impactList.push(data.Impact.ImpactData[i].Impact);
            HHseries.push(data.HH.HHData[i].HH);
            ImpactNames.push(data.Impact.ImpactData[i].ticker);
            HHNames.push(data.HH.HHData[i].ticker);
            IndustriesListNames.push(data.marketCap.marketCapData[i].ticker);
            technicalList.push(data.Technical.TechnicalData[i].signal);
            technicalNames.push(data.Technical.TechnicalData[i].ticker);
          }

          this.sumImpact = data.Impact.Sum;
          this.sumHH = data.HH.Sum;
          this.HHoptions.labels = HHNames;
          this.ImpactOptions.labels = ImpactNames;
          this.IndustriesValueOptions.labels = IndustriesListNames;
          this.HHoptions.xaxis.categories = HHNames;
          this.ImpactOptions.xaxis.categories = ImpactNames;
          this.TechnicalOptions.xaxis.categories = technicalNames;

          this.TableData = data.Table.TableData;
          this.HHseries = [{ data: HHseries }];
          this.ImpactSeries = [{ data: impactList }];
          this.TechnicalSeries = [{ data: technicalList }];

          this.IndustriesValue = IndustriesList;

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
  margin-top: 5px;
  /* font-size: 1em; */
  line-height: 1;
  font-family: "Vazir-Medium-FD" !important;
}
.shakhes-table-head {
  font-size: 0.8rem !important;
  font-weight: 500;
}

.shakhes-table-cell-ticker {
  cursor: pointer;
  vertical-align: middle !important;
  text-align: center;
  font-size: 0.9em;
  line-height: 1;
  font-weight: 400;
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
/* .cellItem {
  font-family: "Vazir-Medium-FD";
  font-weight: 700;
} */
/* .FinancialStrength {
  direction: rtl;
  text-align: right;
} */
/* .Persiantable {
  direction: rtl;
  text-align: right;
} */
.industryDetailChip {
  text-align: center;
}
.industryDetailRedChip {
  color: aliceblue;
  background-color: #f63538 !important;
  font-family: "Vazir-Medium-FD" !important;
}
.industryDetailGreenChip {
  color: aliceblue;
  background-color: #30cc5a !important;
  font-family: "Vazir-Medium-FD" !important;
}
.ApexTooltip {
  /* background-color: blueviolet; */
  border-width: 1px;
  border-style: solid;
  border-color: #bdbdbd;
  border-radius: 8px;
  display: flex;
  /* flex-wrap: nowrap; */
  flex-direction: column;
  justify-content: center;
  align-items: stretch;
  align-content: center;
}
.topDivTooltip {
  background-color: #d7d7d7;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  padding-right: 22px;
  padding-left: 22px;
}
.bottomDivTooltip {
  background-color: #eaeaea;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  padding-right: 22px;
  padding-left: 22px;
}
.redSpan {
  color: red;
}
.greenSpan {
  color: green;
}
</style>
