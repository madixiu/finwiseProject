<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        سایر اطلاعات
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column">
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
        <template v-slot:[`item.value`]="{ item }">
            <span class="small blured">{{ item.value }}</span>
        </template>
      </v-data-table>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "PWidget",
  data() {
    return {
      search: "",
      FinancialStrength: 5,
      headers: [
        {
          text: "عنوان",
          value: "persianname",
          sortabale: false
        },
        { text: "مقدار", value: "value", sortabale: false }
      ],
      ValuatedItems: [
        {
          name: "Revenue(TTM)",
          persianname: "درآمد",
          value: "123456"
        },
        {
          name: "EPS(TTM)",
          persianname: " درآمد هر سهم",
          value: "12"
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
.blured{
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(10px);
}
</style>
