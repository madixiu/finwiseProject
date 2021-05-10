<template>
  <!--begin::Mixed Widget 14-->
  <!-- <div class="card card-custom card-stretch gutter-b"> -->
  <v-card>
    <!--begin::Header-->
    <!-- <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        نسبت های سود نقدی
      </h3>
    </div> -->
    <v-card-title>
      نسبت های سود نقدی
    </v-card-title>
    <v-divider class="mt-0"></v-divider>
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
            <span class="small">Dividend & Buyback</span>
          </v-tooltip>
        </div>
        <div class="col-sm-2 strong blured">
          {{ this.FinancialStrength }}/10
        </div>
        <div class="col-sm-6">
          <v-progress-linear
            class="blured"
            :value="this.FinancialStrength * 10"
            :color="getColor(this.FinancialStrength * 10)"
            background-color="#E9ECEF"
            rounded
            height="25"
          >
          </v-progress-linear>
        </div>
      </div>
      <v-data-table
        :headers="headers"
        :items="ValuatedItems"
        :hide-default-footer="true"
        class="elevation-1 FinancialStrength"
        :header-props="{ sortIcon: null }"
      >
        <template v-slot:[`item.persianname`]="{ item }">
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <v-chip label small v-on="on">{{ item.persianname }}</v-chip>
            </template>
            <span class="small">{{ item.name }}</span>
          </v-tooltip>
        </template>
        <template v-slot:[`item.now`]="{ item }">
          <span class="small blured">{{ item.now }}</span>
        </template>
        <template v-slot:[`item.industry`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            class="blured"
            :color="getColor(item.FinancialStrength * 100)"
            :value="item.industry * 100"
          >
          </v-progress-linear>
        </template>
        <template v-slot:[`item.historic`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            class="blured"
            :width="150"
            :rounded="true"
            :color="getColor(item.FinancialStrength * 100)"
            :value="item.historic * 100"
          >
          </v-progress-linear>
        </template>
      </v-data-table>
    </div>
    <!--end::Body-->
    <!-- </div> -->
  </v-card>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "DivWidget",
  data() {
    return {
      search: "",
      FinancialStrength: 5,
      headers: [
        {
          text: "نسبت مالی",
          value: "persianname",
          sortabale: false,
          algin: "center"
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
          name: "Divident Yield%",
          persianname: "درصد سود نقدی",
          historic: 0.6,
          now: "30%",
          industry: 0.2,
          FinancialStrength: 0.8
        },
        {
          name: "Dividend Payout Ratio",
          persianname: "پرداخت سود نقدی",
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
  filter: blur(10px);
}
</style>
