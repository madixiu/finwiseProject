<template>
  <div id="ApexChartTemplate">
    <apexchart
      :type="type"
      :width="width"
      :height="height"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  props: {
    series: Array,
    chartOptions: Object,
    type: String,
    width: String,
    height: String
  }
};
</script>
<style>
#ApexChartTemplate {
  direction: ltr;
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
  direction: ltr;
}
.apexcharts-legend-text,
.apexcharts-text,
.apexcharts-title-text,
.apexcharts-tooltip .apexcharts-tooltip .apexcharts-tooltip-text-value {
  font-family: "Vazir-Medium-FD" !important;
}
</style>
