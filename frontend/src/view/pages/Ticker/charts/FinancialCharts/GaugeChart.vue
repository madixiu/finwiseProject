<template>
  <highcharts
    class="hc"
    width="100%"
    :height="100"
    :options="chartOptions"
    ref="Gaugechart"
  ></highcharts>
</template>
<script>
export default {
  props: ["degree"],
  data() {
    return {
      chartOptions: {}
    };
  },
  created() {
    this.chartOptions = {
      credits: {
        enabled: false
      },
      chart: {
        type: "gauge",
        height: "70%",
        plotBackgroundColor: null,
        plotBackgroundImage: null,
        plotBorderWidth: 0,
        plotShadow: false
      },

      title: {
        text: null
      },

      pane: {
        startAngle: -90,
        endAngle: 90,
        background: null
      },

      plotOptions: {
        gauge: {
          dataLabels: {
            enabled: false
          },
          dial: {
            baseLength: "0%",
            baseWidth: 10,
            radius: "100%",
            rearLength: "0%",
            topWidth: 1
          }
        }
      },

      // the value axis
      yAxis: {
        labels: {
          enabled: false
          // x: 35,
          // y: -10
        },
        tickLength: 0,
        /* tickPositions: [80, 90], */
        minorTickLength: 0,
        min: 0,
        max: 100,
        plotBands: [
          {
            from: 0,
            to: 20,
            // color: "rgb(192, 0, 0)", // red
            color: "#f63538", // red
            // text: "fuck",
            thickness: "40%"
          },
          {
            from: 20,
            to: 40,
            color: "#b33b43", // yellow
            thickness: "40%"
          },
          {
            from: 40,
            to: 60,
            color: "#404e55", // yellow
            thickness: "40%"
          },

          {
            from: 60,
            to: 80,
            color: "#379a58", // green
            thickness: "40%"
          },
          {
            from: 80,
            to: 100,
            color: "#30cc5a", // green
            thickness: "40%"
          }
        ]
      },

      series: [
        {
          name: "",
          data: []
        }
      ]
    };
  },
  mounted() {
    this.alignLabel(this.$refs.Gaugechart.chart);
    console.log("====================================");
    console.log(this.$refs.Gaugechart.chart);
    console.log("====================================");
    this.chartOptions.series = { name: "", data: [this.degree] };
  },
  methods: {
    alignLabel() {
      var chart = this.$refs.Gaugechart.chart;

      var newX = chart.plotWidth / 2 + chart.plotLeft,
        newY = chart.plotHeight / 2 + chart.plotTop;

      var addText = function(text, posX, posY) {
        return chart.renderer
          .text(text, newX + posX, newY + posY)
          .attr({
            align: "center",
            zIndex: 100,
            rotation: 0
          })
          .css({
            color: "#333",
            fontSize: "0.8em"
          })
          .add();
      };
      addText("خنثی", 0, -90);
      // addText("خرید قوی", 128, -10);
      // addText("فروش قوی", -117, -30);
      addText("فروش", -80, -55);
      addText("خرید", 80, -55);
    }
  }
};
</script>
