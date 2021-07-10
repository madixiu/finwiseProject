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
<style scoped>
#ApexChartTemplate {
  direction: ltr;
}
</style>
