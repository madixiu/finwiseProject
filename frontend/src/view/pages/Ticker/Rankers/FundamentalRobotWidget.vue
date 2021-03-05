<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        ربات تحلیلگر بنیادی
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column">
      <div class="row FinancialStrength valign">
        <div class="col-sm-4">
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <v-chip color="danger" label text-color="white" v-on="on">
                امتیاز کلی
                <v-icon left>mdi-label</v-icon>
              </v-chip>
            </template>
            <span class="small">Valuation</span>
          </v-tooltip>
        </div>
        <div class="col-sm-2 strong blured">
          {{ this.FinancialStrength }}/10
        </div>
        <div class="col-sm-6">
          <v-progress-linear
            :value="this.FinancialStrength * 10"
            :color="getColor(this.FinancialStrength * 10)"
            background-color="#E9ECEF"
            rounded
            class="blured"
            height="25"
          >
          </v-progress-linear>
        
        </div>
        <div class="blured">
         <ApexChart
            type="bar"
            width="100%"
            :series="series"
            :chartOptions="chartOptions"
          />
        </div>
      </div>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
import ApexChart from "@/view/content/charts/ApexChart";
export default {
  name: "FundamentalRobot",
  components: {
    ApexChart
  },
  data() {
    return {
        
      search: "",
      FinancialStrength: 7,
      series: [{
            data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
          }],
          chartOptions: {
            chart: {
              type: 'bar',
              height: 350
            },
            plotOptions: {
              bar: {
                horizontal: true,
              }
            },
            dataLabels: {
              enabled: false
            },
            xaxis: {
              categories: ['Earning Power Value', 'Current Asset Value', 'TangibleBook', 
              'Projected FCF', 'Median PS Value', 'Graham Number', 'Peter Lynch Value',
                'DCF (FCF BASED)', 'DCF (Earning Based)'
              ],
            }
          },
      headers: [
        {
          text: "نسبت مالی",
          value: "persianname",
          sortabale: false
        },
        { text: "مقدار فعلی", value: "now", sortabale: false },
        { text: "در مقایسه با صنعت", value: "industry", sortabale: false },
        {
          text: "در مقایسه با تاریخ سهم",
          value: "historic",
          sortabale: false
        }
      ],
      ValuatedItems: [
        {
          name: "PE Ratio",
          persianname: "نسبت P/E",
          historic: 0.6,
          now: "30%",
          industry: 0.2,
          FinancialStrength: 0.8
        },
        {
          name: "Forward PE Ratio",
          persianname: "P/E Forward",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "PE Ratio Without NRI",
          persianname: "P/E - NRI",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "Price-to-Owner-Earnings",
          persianname: "نسبت قیمت به درآمد مالک",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "PB Ratio",
          persianname: "P/B",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "PS Ratio",
          persianname: "P/S",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "Price-to-Free-Cash-Flow",
          persianname: "قیمت به جریان نقدی عملیاتی",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        }
      ]
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    // set FinancialStrength percent
    setFinancialStrengthPercent: function() {
      this.FinancialStrengthPercent = this.FinancialStrength * 10;
    },
    getWaccPercent: function(item) {
      let all = item.WACC + item.ROIC;
      return (100 * item.WACC) / all;
    },
    // get ROIC percent
    getRoicPercent: function(item) {
      let all = item.WACC + item.ROIC;
      return (100 * item.ROIC) / all;
    },
    getColor: function(value) {
      if (value >= 80) {
        return "#0DCD0A";
      } else if (value < 80 && value >= 60) {
        return "#72FF59";
      }
      if (value < 60 && value >= 40) {
        return "#FFCE00";
      } else if (value < 40 && value >= 20) {
        return "#FD6700";
      } else if (value < 20) {
        return "#FF0000";
      }
      return "";
    }
  },
  mounted() {
    // this.setFinancialStrengthPercent();
    // reference; kt_stats_widget_7_chart
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.valign * {
  vertical-align: middle;
}
.blured {
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(5px);
}
</style>
