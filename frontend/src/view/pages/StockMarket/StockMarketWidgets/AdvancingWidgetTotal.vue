<template>
  <v-card rounded="lg" height="150" class="mt-3">
    <v-toolbar
      dense
      class="IndexChartToolbars elevation-2 mb-1"
      style="height:36px;"
    >
      <v-toolbar-title style="height:20px;font-size:0.95em"
        >وضعیت صعود و نزول در بازار</v-toolbar-title
      >
    </v-toolbar>
    <div id="AdvancingDivTotal" class="d-flex">
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
  name: "AdvancingWidgetTotal",
  props: {
    inputData: Array,
  },
  data() {
    return {
      ascendings: 0,
      descend: 0,
      categories: ["کل"],
      // categories: [],
      chartOptions: {}
    };
  },
  mounted() {
    let div = document.getElementById("AdvancingDivTotal").clientWidth;
    this.chartOptions.chart.width = div;
    this.chartOptions.chart.height = ((100 / div) * 100).toString() + "%";
  },
  watch: {
    inputData() {
      // console.log(this.chartOptions.series)
      // console.log(this.inputData.length)

      if (this.inputData.length > 0) {
        this.chartOptions.series[1].data = [];
        this.chartOptions.series[1].data.push(this.inputData[0].ascending);
        this.chartOptions.series[0].data = [];
        this.chartOptions.series[0].data.push(
          this.inputData[0].descending * -1
        );
      }
    }
  },
  created() {
    // eslint-disable-next-line no-unused-vars
    const that = this;
    this.chartOptions = {
        credits: {
        enabled: false
      },
      title: {
    text: ''
},
      chart: {
        type: "bar",
        width: "450",
        height: "20%"
      },
      xAxis: [
        {
          categories: that.categories,
          reversed: false,
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
          return `<b>${this            .series.name} ${this.point.category}:${Math.abs(this.point.y)}`;
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
