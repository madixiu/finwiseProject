<template>
  <div>
    <div id="controls"></div>
    <div class="hello" ref="chartdiv"></div>
  </div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import am4themes_dataviz from "@amcharts/amcharts4/themes/dataviz";
import * as am4plugins_rangeSelector from "@amcharts/amcharts4/plugins/rangeSelector";
am4core.useTheme(am4themes_animated);
am4core.useTheme(am4themes_dataviz);
// import json from '../assets/StockChartData.json'

export default {
  name: "StockChart",
  /////////////////////////
  data() {
    return {
      // StockData : json
    };
  },

  mounted() {
    let chart = am4core.create(this.$refs.chartdiv, am4charts.XYChart);

    chart.padding = (0, 15, 0, 15);

    // let newData = [];
    // let visits = 10;
    // for (let i = 1; i < 366; i++) {
    // visits += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 10);
    // data.push({ date: new Date(2018, 0, i), name: "name" + i, value: visits });
    // } // end of for
    /////////////////////data
    // data.push({Date: new Date()})
    // Load external data
    chart.dataSource.url =
      "https://www.amcharts.com/wp-content/uploads/assets/stock/MSFT.csv";
    chart.dataSource.parser = new am4core.CSVParser();
    chart.dataSource.parser.options.useColumnNames = true;
    chart.dataSource.parser.options.reverse = true;

    // the following line makes value axes to be arranged vertically.
    chart.leftAxesContainer.layout = "vertical";
    let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.renderer.grid.template.location = 0;
    dateAxis.renderer.ticks.template.length = 8;
    dateAxis.renderer.ticks.template.strokeOpacity = 0.1;
    dateAxis.renderer.grid.template.disabled = true;
    dateAxis.renderer.ticks.template.disabled = false;
    dateAxis.renderer.ticks.template.strokeOpacity = 0.2;
    dateAxis.renderer.minLabelPosition = 0.01;
    dateAxis.renderer.maxLabelPosition = 0.99;
    dateAxis.keepSelection = true;
    dateAxis.minHeight = 30;

    dateAxis.groupData = true;
    dateAxis.minZoomCount = 5;

    // y axis
    let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.tooltip.disabled = true;
    // valueAxis.renderer.minWidth = 35;
    // height of axis
    valueAxis.height = am4core.percent(65);

    valueAxis.renderer.gridContainer.background.fill = am4core.color("#000000");
    valueAxis.renderer.gridContainer.background.fillOpacity = 0.05;
    valueAxis.renderer.inside = true;
    valueAxis.renderer.labels.template.verticalCenter = "bottom";
    valueAxis.renderer.labels.template.padding(2, 2, 2, 2);

    //valueAxis.renderer.maxLabelPosition = 0.95;
    valueAxis.renderer.fontSize = "0.8em";

    // series

    let series = chart.series.push(new am4charts.LineSeries());
    series.dataFields.dateX = "Date";
    series.dataFields.valueY = "Adj Close";

    series.tooltipText = "{valueY.value}";
    series.name = "MSFT: Value";
    series.defaultState.transitionDuration = 0;

    chart.cursor = new am4charts.XYCursor();

    var selector = new am4plugins_rangeSelector.DateAxisRangeSelector();

    selector.periods.unshift(
      { name: "day", interval: { timeUnit: "day", count: 1 } },
      { name: "week", interval: { timeUnit: "day", count: 7 } }
    );

    // selector.periods.shift(
    //   {name: "روز", interval: {timeUnit: "day",count:1}},
    //   {name: "هفته", interval: {timeUnit: "day", count:7}}
    // )

    selector.container = document.getElementById("controls");
    selector.axis = dateAxis;
    this.chart = chart;
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.dispose();
    }
  }
};
</script>

<style scoped>
.hello {
  width: 99%;
  height: 220px;
  direction: ltr;
}
#chartdiv {
  width: 100%;
  height: 250px;
  max-width: 100%;
}

#controls {
  overflow: hidden;
  padding-bottom: 3px;
  direction: ltr;
}
</style>
