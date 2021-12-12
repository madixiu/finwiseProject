<template>
  <v-card rounded="lg" height="400">
    <v-toolbar
      dense
      class="IndexChartToolbars elevation-2 mb-1"
      style="height:36px;"
    >
      <v-toolbar-title style="height:20px;font-size:0.95em"
        >وضعیت صعود و نزول در صنایع</v-toolbar-title
      >
    </v-toolbar>
    <div id="AdvancingDiv" class="d-flex">
      <highcharts
        class="hc"
        width="100%"
        :options="chartOptions"
        ref="chart"
      ></highcharts>
    </div>
  </v-card>
</template>

<script>
export default {
  name: "AdvancingWidget",
  props: {
    inputDataInd: Array
  },
  data() {
    return {
      ascendings: 0,
      descend: 0,
      //   categories: ["کل"],
      categories: [],
      chartOptions: {}
    };
  },
  mounted() {
    let div = document.getElementById("AdvancingDiv").clientWidth;
    this.chartOptions.chart.width = div;
    this.chartOptions.chart.height = ((400 / div) * 100).toString() + "%";
  },
  watch: {
    inputDataInd() {
      let that = this;
      this.chartOptions.series[1].data = [];
      this.chartOptions.series[0].data = [];
      // this.categories = [];
      this.inputDataInd.filter(d => {
        that.categories.push(d.CorrectName);
        that.chartOptions.series[1].data.push(d.ascending);
        that.chartOptions.series[0].data.push(d.descending * -1);
      });
    }
  },
  created() {
    // eslint-disable-next-line no-unused-vars
    const that = this;
    this.chartOptions = {
      credits: {
        enabled: false
      },
      chart: {
        type: "bar",
        width: "450",
        height: "10%"
      },
      title: {
        text: ""
      },
      xAxis: [
        {
          categories: that.categories,
          reversed: false
        },
        {
          // mirror axis on right side
          opposite: true,
          reversed: false,
          categories: that.categories,
          linkedTo: 0,
          labels: {
            step: 1
          }
        }
      ],
      yAxis: {
        title: {
          text: null
        },
        labels: {
          formatter: function() {
            return Math.abs(this.value);
          }
        }
      },

      plotOptions: {
        series: {
          stacking: "normal"
        }
      },

      tooltip: {
        formatter: function() {
          return `<b>${this.series.name}  ${this.point.category}:  ${Math.abs(
            this.point.y
          )}</b>`;
        }
      },

      series: [
        {
          name: "سهم های منفی",
          data: []
        },
        {
          name: "سهم های مثبت",
          data: []
        }
      ]
    };
  }
};
</script>
