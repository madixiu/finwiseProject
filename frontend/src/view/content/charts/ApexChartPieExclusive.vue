<template>
  <div>
    <v-card outlined>
      <div id="chart">
        <apexchart
          :type="type"
          :height="height"
          :width="width"
          :options="chartOptions"
          :series="series"
        ></apexchart>
      </div>
    </v-card>
  </div>
</template>
<script>
export default {
  props: {
    series: Array,
    chartOptions: Object,
    type: String,
    width: String
  }
};
</script>
