<template>
  <v-card rounded="lg" class="mt-1 mb-2" height="351">
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em"
        >نمودار وضعیت صنایع</v-toolbar-title
      >
      <v-spacer></v-spacer>
      <v-radio-group class="mt-5" row v-model="SortByIndustryChart" mandatory>
        <v-radio
          class="radioBTN"
          label="ورود و خروج حقیقی"
          :value="0"
        ></v-radio>
        <v-radio class="radioBTN" label="تاثیر در شاخص" :value="1"></v-radio>
      </v-radio-group>
    </v-toolbar>
    <HHChart
      v-show="SortByIndustryChart == 0"
      v-if="HHseries.length != 0"
      :HHseries="HHseries"
      :HHLabels="HHLabels"
      :HHmax="HHmax"
      :HHmin="HHmin"
    ></HHChart>
    <EffectOnIndexChart
      v-show="SortByIndustryChart != 0"
      v-if="EffectOnIndexSeries.length != 0"
      :EffectOnIndexSeries="EffectOnIndexSeries"
      :EffectOnIndexLabels="EffectOnIndexLabels"
      :EffectOnIndexmin="EffectOnIndexmin"
      :EffectOnIndexmax="EffectOnIndexmax"
    ></EffectOnIndexChart>
  </v-card>
</template>

<script>
import HHChart from "@/view/pages/StockMarket/Industries/Content/HHChart.vue";
import EffectOnIndexChart from "@/view/pages/StockMarket/Industries/Content/EffectOnIndex.vue";
export default {
  name: "ChartIndustries",
  components: {
    HHChart,
    EffectOnIndexChart
  },
  // computed: {
  //   // cardHeight() {
  //   //   if (this.HHseries.length != 0) {
  //   //     let height = document.getElementById("HHChartID").clientHeight + 36;
  //   //     console.log(document.getElementById("HHChartID"));
  //   //     return height;
  //   //   } else return 315;
  //   // }
  // },
  props: { inpuDataIndustryHH: Array, inputDataIndustryImpact: Array },
  data() {
    return {
      SortByIndustryChart: 0,
      HHseries: [],
      HHLabels: [],
      HHmax: null,
      HHmin: null,
      EffectOnIndexSeries: [],
      EffectOnIndexLabels: [],
      EffectOnIndexmin: null,
      EffectOnIndexmax: null
    };
  },
  watch: {
    inpuDataIndustryHH() {
      let data = this.inpuDataIndustryHH;
      let HHseries2Labels = [];
      let HHseries2data = [];
      for (let i = 0; i < data.length; i++) {
        HHseries2Labels.push(data[i]["CorrectName"]);
        HHseries2data.push(data[i]["sum"]);
      }

      if (
        HHseries2data[0] >= Math.abs(HHseries2data[HHseries2data.length - 1])
      ) {
        this.HHmin = HHseries2data[0] * -1;
        this.HHmax = HHseries2data[0];
      } else {
        this.HHmin = HHseries2data[HHseries2data.length - 1];
        this.HHmax = Math.abs(HHseries2data[HHseries2data.length - 1]);
      }
      this.HHLabels = HHseries2Labels;
      this.HHseries = [{ data: HHseries2data }];
    },
    inputDataIndustryImpact() {
      let data = this.inputDataIndustryImpact;
      let Impactseries2Labels = [];
      let Impactseries2data = [];
      for (let i = 0; i < data.length; i++) {
        Impactseries2Labels.push(data[i]["CorrectName"]);
        Impactseries2data.push(data[i]["IMPACT"]);
      }

      if (
        Impactseries2data[0] >=
        Math.abs(Impactseries2data[Impactseries2data.length - 1])
      ) {
        this.EffectOnIndexmax = Impactseries2data[0];
        this.EffectOnIndexmin = Impactseries2data[0] * -1;
      } else {
        this.EffectOnIndexmax = Math.abs(
          Impactseries2data[Impactseries2data.length - 1]
        );
        this.EffectOnIndexmin = Impactseries2data[Impactseries2data.length - 1];
      }
      this.EffectOnIndexLabels = Impactseries2Labels;
      this.EffectOnIndexSeries = [{ data: Impactseries2data }];
    }
  }
};
</script>

<style scoped>
.radioBTN /deep/ .v-input--selection-controls__ripple {
  height: 16px !important;
  width: 16px !important;
  left: -3px !important;
  top: calc(50% - 15px) !important;
}
.radioBTN /deep/ .v-icon.v-icon {
  font-size: 18px !important;
}
.radioBTN /deep/ .v-input--selection-controls__input {
  margin-left: 0px !important;
}

.radioBTN /deep/ label {
  display: inline-block;
  margin-bottom: 0rem;
}
.radioBTN /deep/ .v-label {
  font-size: 0.8em !important;
}
.radioBTN /deep/ .theme--light.v-label {
  color: #000 !important;
  font-size: 0.7em !important;
  font-family: "Vazir-Light-FD";
}
</style>
