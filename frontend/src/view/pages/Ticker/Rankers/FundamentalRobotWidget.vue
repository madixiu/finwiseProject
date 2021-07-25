<template>
  <!--begin::Mixed Widget 14-->
  <!-- <div class="card card-custom card-stretch gutter-b"> -->
  <v-card>
    <!--begin::Header-->
    <!-- <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        ربات تحلیلگر بنیادی
      </h3>
    </div> -->
    <v-card-title>
      ربات تحلیلگر بنیادی
    </v-card-title>
    <v-divider class="mt-0"></v-divider>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column">
      <div class="row FinancialStrength valign">
        <ApexChart
          type="bar"
          width="100%"
          :series="series"
          :chartOptions="chartOptions"
        />
      </div>
    </div>
    <!--end::Body-->
    <!-- </div> -->
  </v-card>
  <!--end::Mixed Widget 14-->
</template>

<script>
import ApexChart from "@/view/content/charts/ApexChart";
export default {
  name: "FundamentalRobot",
  components: {
    ApexChart
  },
  data() {
    return {
      series: [
        {
          data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
        }
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 350
        },
        plotOptions: {
          bar: {
            horizontal: true
          }
        },
        dataLabels: {
          enabled: false
        },
        xaxis: {
          categories: [
            "Earning Power Value",
            "Current Asset Value",
            "TangibleBook",
            "Projected FCF",
            "Median PS Value",
            "Graham Number",
            "Peter Lynch Value",
            "DCF (FCF BASED)",
            "DCF (Earning Based)"
          ]
        },
        annotations: {
          xaxis: [
            {
              x: 1100,
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
  methods: {},
};
</script>
