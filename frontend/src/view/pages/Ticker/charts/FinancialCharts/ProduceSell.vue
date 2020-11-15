<template>
  <apexchart
    id="ProduceSell"
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
          name: "مقدار تولید",
          data: [65, 34, 23, 12, 34, 105, 67, 10, 94]
        },
        {
          name: "مقدار فروش",
          data: [35, 56, 123, 67, 49, 10, 52, 53, 41]
        }
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
#ProduceSell {
  direction: ltr;
}
</style>
