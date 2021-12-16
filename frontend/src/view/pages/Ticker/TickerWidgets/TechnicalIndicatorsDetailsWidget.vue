<template>
  <v-row no-gutters>
    <div
      class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12 mt-1"
      style="padding-left:0px;"
    >
      <v-card rounded="lg" id="ParentCard" :height="cardheight">
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em"
            >مجموع</v-toolbar-title
          >
        </v-toolbar>
        <GaugeChart v-if="dataFetched" :degree="degree" class="mt-1" />

        <v-row no-gutters class="d-flex flex-row px-3">
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خرید</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#30cc5a">{{ positive }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خنثی</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#414554">{{ neutral }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">فروش</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#f63538">{{ negative }}</span></v-col
            >
          </v-col>
        </v-row>
      </v-card>
    </div>
    <div
      class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12 mt-1 d-flex"
      style="padding-left:0px;padding-right:5px"
    >
      <v-card rounded="lg" :height="cardheight" style="width:100%">
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em"
            >Moving Average</v-toolbar-title
          >
        </v-toolbar>
        <GaugeChart v-if="dataFetched" :degree="degreeMA" class="mt-1" />

        <!-- <v-divider class="mt-0 mb-0"></v-divider>
        <div class="" id="ChartGeneral2"></div> -->
        <v-row no-gutters class="d-flex flex-row px-3">
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خرید</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#30cc5a">{{ positiveMa }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خنثی</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#414554">{{ neutralMa }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">فروش</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#f63538">{{ negativeMa }}</span></v-col
            >
          </v-col>
        </v-row>
      </v-card>
    </div>
    <div
      class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12 mt-1"
      style="padding-left:0px;padding-right:5px"
    >
      <v-card rounded="lg" :height="cardheight">
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em"
            >Indicators</v-toolbar-title
          >
        </v-toolbar>
        <GaugeChart v-if="dataFetched" :degree="degreeIndic" class="mt-1" />

        <v-row no-gutters class="d-flex flex-row px-3" v-if="dataFetched">
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خرید</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#30cc5a">{{ positiveIndic }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خنثی</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#414554">{{ neutralIndic }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">فروش</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#f63538">{{ negativeIndic }}</span></v-col
            >
          </v-col>
        </v-row>
      </v-card>
    </div>
    <div
      class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12 mt-1"
      style="padding-right:5px"
    >
      <v-card rounded="lg" :height="cardheight" width="100%">
        <v-toolbar dense class="elevation-2" style="height:36px;">
          <v-toolbar-title style="height:20px;font-size:0.95em">
            <div v-if="lastUpdate">
              <span style="font-size:0.7em;color:#222">
                آخرین بروزرسانی :
              </span>
              <span style="font-size:0.7em;color:#222">{{
                this.lastUpdate.substring(0, 4) +
                  "/" +
                  this.lastUpdate.substring(4, 6) +
                  "/" +
                  this.lastUpdate.substring(6, 8)
              }}</span>
            </div>
          </v-toolbar-title>
        </v-toolbar>
        <b-table
          :sticky-header="`${cardheight - 80}px`"
          class="technicalIndicator-table mt-1"
          thClass="technicalIndicator-tableHeader"
          tbody-tr-class="technicalIndicator-table-row"
          small
          hover
          :responsive="true"
          :items="tableData"
          :fields="headers"
        >
          <template #cell(Value)="data">
            <span dir="ltr">{{ data.value }}</span>
          </template>
        </b-table>
      </v-card>
    </div>
  </v-row>
</template>

<script>
import GaugeChart from "@/view/pages/Ticker/charts/FinancialCharts/GaugeChart.vue";
export default {
  name: "TechnicalDetailsWidget",
  props: ["notices"],
  components: {
    GaugeChart
  },
  data() {
    return {
      chartOptions: {},
      dataFetched: false,
      errorinData: false,
      headers: [
        {
          label: "عنوان",
          key: "title",
          thClass: "technicalIndicator-tableHeader"
        },
        {
          label: "مقدار محاسبه شده",
          key: "Value",
          thClass: "technicalIndicator-tableHeader"
        }
      ],
      lastUpdate: "",
      sum: 0,
      neutral: 0,
      positive: 0,
      negative: 0,
      sumMa: 0,
      neutralMa: 0,
      positiveMa: 0,
      negativeMa: 0,
      sumIndic: 0,
      neutralIndic: 0,
      positiveIndic: 0,
      negativeIndic: 0,
      tableData: []
    };
  },
  created() {
    this.chartOptions = {
      credits: {
        enabled: false
      },
      chart: {
        type: "gauge",
        plotBackgroundColor: null,
        plotBackgroundImage: null,
        plotBorderWidth: 0,
        plotShadow: false
      },

      title: {
        text: null
      },

      pane: {
        startAngle: -90,
        endAngle: 90,
        background: null
      },

      plotOptions: {
        gauge: {
          dataLabels: {
            enabled: false
          },
          dial: {
            baseLength: "0%",
            baseWidth: 10,
            radius: "100%",
            rearLength: "0%",
            topWidth: 1
          }
        }
      },

      // the value axis
      yAxis: {
        labels: {
          enabled: false
          // x: 35,
          // y: -10
        },
        tickLength: 0,
        minorTickLength: 0,
        min: 0,
        max: 100,
        plotBands: [
          {
            from: 0,
            to: 20,
            color: "#f63538",
            // text: "fuck",
            thickness: "40%"
          },
          {
            from: 20,
            to: 40,
            color: "#b33b43",
            thickness: "40%"
          },
          {
            from: 40,
            to: 60,
            color: "#404e55",
            thickness: "40%"
          },

          {
            from: 60,
            to: 80,
            color: "#379a58",
            thickness: "40%"
          },
          {
            from: 80,
            to: 100,
            color: "#30cc5a",
            thickness: "40%"
          }
        ]
      },

      series: [
        {
          name: "Speed",
          data: [17.64]
        }
      ]
    };
  },
  mounted() {
    this.alignLabel(this.$refs.Gaugechart.chart);
  },
  watch: {
    notices: {
      // eslint-disable-next-line no-unused-vars
      handler: function(val, oldVal) {
        try {
          this.lastUpdate = this.notices.info.persiandate;

          this.sum = this.notices.score.sum;
          this.neutral = this.notices.score.neutral;
          this.positive = this.notices.score.positive;
          this.negative = this.notices.score.negative;
          this.sumMa = this.notices.score.sumMa;
          this.neutralMa = this.notices.score.neutralMa;
          this.positiveMa = this.notices.score.positiveMa;
          this.negativeMa = this.notices.score.negativeMa;
          this.sumIndic = this.notices.score.sumIndic;
          this.neutralIndic = this.notices.score.neutralIndic;
          this.positiveIndic = this.notices.score.positiveIndic;
          this.negativeIndic = this.notices.score.negativeIndic;
          this.tableData = this.notices.tableData;
          this.dataFetched = true;
          this.errorinData = false;
        } catch {
          console.error("error");
          this.tableData = [];
          this.dataFetched = false;
          this.errorinData = true;
        }
      },
      deep: true
    }
  },
  computed: {
    degree() {
      // return 80
      if (this.sum != 0) {
        return ((17 + this.sum) / 34) * 100;
      } else return 50;
    },
    degreeMA() {
      if (this.sumMa != 0) {
        return ((17 + this.sumMa) / 34) * 100;
      } else return 50;
    },
    degreeIndic() {
      if (this.sumIndic != 0) {
        return ((17 + this.sumIndic) / 34) * 100;
      } else return 50;
    },
    cardheight() {
      if (screen.height * 2 > screen.width) {
        // console.log(screen.height * 0.5)
        return Math.max(350, screen.height * 0.4);
      } else {
        if (screen.height * 1.5 > screen.width) {
          return Math.max(450, screen.height * 0.45);
        } else {
          if (screen.height > screen.width) {
            return Math.max(500, screen.height * 0.6);
          } else return Math.max(600, screen.height * 0.75);
        }
      }
    }
  },
  methods: {
    alignLabel() {
      var chart = this.$refs.Gaugechart.chart;

      var newX = chart.plotWidth / 2 + chart.plotLeft,
        newY = chart.plotHeight / 2 + chart.plotTop;

      var addText = function(text, posX, posY) {
        return chart.renderer
          .text(text, newX + posX, newY + posY)
          .attr({
            align: "center",
            zIndex: 100,
            rotation: 0
          })
          .css({
            color: "#333",
            fontSize: "0.8em"
          })
          .add();
      };
      addText("خنثی", 0, -120);
      // addText("خرید قوی", 128, -10);
      // addText("فروش قوی", -117, -30);
      addText("فروش", -110, -65);
      addText("خرید", 110, -65);
    }
  }
};
</script>
<style scoped>
.technicalIndicator-table {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  background-color: white;
  font-family: "Vazir-Medium-FD";
}
.technicalIndicator-table /deep/ .technicalIndicator-tableHeader {
  font-size: 1em !important;
  /* font-weight: 300; */
  text-align: center;
  /* min-width: 200px; */
}
.technicalIndicator-table /deep/ .ticker-assembly-table-row {
  direction: ltr;
  vertical-align: middle !important;
  text-align: center;
}
</style>
