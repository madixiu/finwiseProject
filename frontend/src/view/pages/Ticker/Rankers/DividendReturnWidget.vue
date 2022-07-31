<template>
  <v-card rounded="lg">
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em">
        نسبت های سود نقدی
      </v-toolbar-title>
    </v-toolbar>
    <div class="d-flex flex-column pt-2">
      <!-- <v-row no-gutters>
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
      </v-row> -->
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
          <span>{{ item.now }}%</span>
        </template>
        <template v-slot:[`item.industry`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            class="blured"
            :color="getColor(item.industry * 100)"
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
            :color="getColor(item.historic * 100)"
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
export default {
  name: "DivWidget",
  props: ["RatioData"],
  data() {
    return {
      search: "",
      // FinancialStrength: 5,
      RatioItems: [],
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
      ValuatedItems: []
    };
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
    },
    FillRatios() {
      this.RatioItems = this.RatioData;
      if (this.RatioItems === undefined || this.RatioItems.length == 0) {
        this.RatioItems = [];
      } else {
        this.RatioItems.filter(d => {
          if (d.Ratio == "Dividend_PayoutRatio") {
            this.ValuatedItems.push({
              name: "Dividend_PayoutRatio",
              persianname: "پرداخت سود نقدی",
              historic: d.toHistoricAverage,
              now: Math.round(d.RatioValue * 100),
              industry: d.toIndustryAverage
            });
          }
          if (d.Ratio == "Dividend_yield") {
            this.ValuatedItems.push({
              name: "Dividend_yield",
              persianname: "بازده سود نقدی",
              historic: d.toHistoricAverage,
              now: Math.round(d.RatioValue * 100),
              industry: d.toIndustryAverage
            });
          }
        });
      }
    }
  },
  watch: {
    RatioData() {
      this.FillRatios();
    }
  }
};
</script>
