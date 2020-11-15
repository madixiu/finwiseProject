<template>
  <apexchart
    id="CashFlow"
    type="bar"
    :height="Chartheight"
    :options="chartOptions"
    :series="series"
  ></apexchart>
</template>
<script>
export default {
  data() {
    return {
      Chartheight: 200,
      series: [
        {
          name: "Operatin Cash Flow",
          data: [65, 34, 23, 12, 34, 105, 67, 10, 94]
        },
        {
          name: "Free Cash Flow",
          data: [35, 56, 123, 67, 49, 10, 52, 53, 41]
        },
        { name: "Net Income", data: [78, 12, 165, 23, 90, 20, 23, 43, 67] }
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 350
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "55%",
            endingShape: "rounded"
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          show: true,
          width: 2,
          colors: ["transparent"]
        },
        xaxis: {
          categories: [
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct"
          ]
        },
        yaxis: {
          title: {
            text: "$ (thousands)"
          }
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return "$ " + val + " thousands";
            }
          }
        }
      }
    };
  }
};
</script>
<style scoped>
#CashFlow {
  direction: ltr;
}
</style>
