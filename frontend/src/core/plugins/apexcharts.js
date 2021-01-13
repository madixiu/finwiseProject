import Vue from "vue";
import VueApexCharts from "vue-apexcharts";

Vue.use(VueApexCharts);
window.Apex.chart = { fontFamily: "Vazir" };
window.Apex.xaxis = {
  labels: {
    style: {
      fontFamily: "Vazir",
      fontSize: "0.9em"
    }
  }
};
Vue.component("apexchart", VueApexCharts);
