<template>
  <div class="One">
    <div id="chart">
      <apexchart
        :type="type"
        :width="width"
        :height="height"
        :options="chartOptions"
        :series="series"
      ></apexchart>
    </div>
    <!-- </v-card> -->
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
#chart {
  direction: ltr;
}
</style>
