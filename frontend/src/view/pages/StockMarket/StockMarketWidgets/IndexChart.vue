/* eslint-disable no-unused-vars */
<template>
  <div class="card card-custom card-stretch gutter-b">
    <v-card>
      <v-card-title>شاخص کل</v-card-title>
      <v-divider class="mt-0"></v-divider>
      <div class="row">
        <div
          id="Chartcontainer_index"
          class="col-xxl-9 col-lg-9 col-md-12 col-sm-12"
        ></div>
      </div>
      <!--end::Header-->
    </v-card>
  </div>
</template>

<script>
import * as d3 from "d3";

// eslint-disable-next-line no-unused-vars
export default {
  name: "IndexChart",
  props: { inputDataIndex: Array },
  data() {
    return {
      loading: true,
      jsonData: {},
      indexData: [],
      min: 0,
      max: 10,
      number: 3,
      margin: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0
      },
      offsetY: 0
    };
  },
  watch: {
    inputDataIndex() {
      this.renderData();
      if (this.isRealValue(this.indexData)) {
        this.renderChart();
      }
    }
  },
  // In the beginning...
  mounted() {
    this.renderData();
    this.initrender();
    if (!(this.indexData === undefined || this.indexData.length == 0)) {
      this.renderChart();
    }
  },
  computed: {},
  methods: {
    numberWithCommas(x) {
      if (x == "-") {
        return x;
      }
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    roundTo(n, digits) {
      if (n == "-") {
        return n;
      }

      let negative = false;
      if (digits === undefined) {
        digits = 0;
      }
      if (n < 0) {
        negative = true;
        n = n * -1;
      }
      let multiplicator = Math.pow(10, digits);
      n = parseFloat((n * multiplicator).toFixed(11));
      n = (Math.round(n) / multiplicator).toFixed(digits);
      if (negative) {
        n = (n * -1).toFixed(digits);
      }
      return n;
    },
    isRealValue(obj) {
      return obj && obj !== "null" && obj !== "undefined";
    },
    initrender() {
      if (document.getElementById("Chartcontainer_index_svg")) {
        d3.selectAll("#Chartcontainer_index_svg").remove();
      }
      this.width =
        0.85 * parseInt(d3.select("#Chartcontainer_index").style("width"), 10);
      this.height = (this.width * 8) / 16;
      this.margin.top = this.height * 0.05;
      this.margin.bottom = this.height * 0.05;
      this.margin.right =
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.075;
      this.margin.left =
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.075;
      this.offsetY = this.margin.top;
      var parent = document.getElementById("Chartcontainer_index");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "Chartcontainer_index_svg")
        .attr(
          "viewBox",
          `0 0 ${this.width + this.margin.right + this.margin.left},${this
            .height +
            this.margin.top +
            this.margin.bottom}`
        )
        .attr("preserveAspectRatio", "xMidYMid meet");
      // eslint-disable-next-line no-unused-vars
    },
    renderData() {
      let data = [...this.inputDataIndex];
      console.log(data);
      var parseTime = d3.timeParse("%Y-%m-%d %H:%M:%S");
      data.forEach(
        function(d) {
          d.date = parseTime(d.englishDate.split(".")[0]);
          d.value = d.Index;
        },
        // eslint-disable-next-line no-unused-vars
        function(error, data) {
          if (error) throw error;
        }
      );
      data.sort(function(a, b) {
        return a.date - b.date;
      });
      console.log(data);
      data = data.filter(function(d) {
        if (d.date.getHours() > 8 && d.Market == 1) {
          return d;
        }
      });
      this.indexData = data;
    },
    renderChart() {
      if (document.getElementById("Chartcontainer_index_svg")) {
        d3.selectAll("#Chartcontainer_index_svg").remove();
      }

      var parent = document.getElementById("Chartcontainer_index");
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "Chartcontainer_index_svg")
        .attr(
          "viewBox",
          `0 0 ${this.width + this.margin.right + this.margin.left},${this
            .height +
            this.margin.top +
            this.margin.bottom}`
        )
        .attr("preserveAspectRatio", "xMidYMid meet");
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      // eslint-disable-next-line no-unused-vars
      var xScale = d3
        .scaleTime()
        .domain(d3.extent(this.indexData, d => d.date))
        .range([0, this.width - this.margin.right]);
      // eslint-disable-next-line no-unused-vars
      var yScale = d3
        .scaleLinear()
        .domain([
          d3.min(this.indexData, function(d) {
            return d.value;
          }),
          d3.max(this.indexData, function(d) {
            return d.value;
          })
        ])
        .nice()
        .range([this.height - this.margin.bottom, this.margin.top]);
      // eslint-disable-next-line no-unused-vars
      var xAxis = g =>
        g
          .attr("class", "xAxis")
          .attr("transform", `translate(0,${this.height - this.margin.top})`)
          .transition()
          .duration(1000)
          .ease(d3.easeSin)
          .call(
            d3
              .axisBottom(xScale)
              .ticks(this.width / 80)
              .tickSizeOuter(0)
          )
          .style("font-family", "Dirooz FD")
          .style("stroke-opacity", ".1");

      let xAxisAxe = chart.append("g").call(xAxis);
      xAxisAxe
        .style("font-size", `${this.width / 1000}em`)
        .style("font-family", "Dirooz FD")
        .style("font-weight", "800");
      var yAxis = g =>
        g
          .attr("class", "yAxis")
          .attr("transform", `translate(${this.margin.left},0)`)
          .transition()
          .duration(1000)
          .call(d3.axisLeft(yScale))
          .style("stroke-opacity", ".1")
          .style("font-family", "Dirooz FD");
      let yAxisAxe = chart.append("g").call(yAxis);
      yAxisAxe
        .style("text-anchor", "start")
        .attr("transform", `translate(0,0)`)
        .style("font-size", `${this.width / 1000}em`)
        .style("font-family", "Dirooz FD")
        .style("font-weight", "800");
d3.selectAll("g.yAxis g.tick")
    .append("line")
    .attr("class", "gridline")
    .attr("x1", 0)
    .attr("y1", 0)
    .attr("x2", this.width-this.margin.left*2)
    .attr("y2", 0);
      var line = d3
        .line()
        .defined(d => !isNaN(d.date))
        .x(d => xScale(d.date))
        .y(d => yScale(d.value));

      // eslint-disable-next-line no-unused-vars
      var path = chart
        .append("path")
        .datum(this.indexData.filter(line.defined()))
        .style("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 4)
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("d", line);
      const pathLength = path.node().getTotalLength();
const transitionPath = d3
  .transition()
  .ease(d3.easeSinOut)
  .duration(5500);

path
  
  .attr("stroke-dashoffset", pathLength)
  
  .attr("stroke-dasharray", pathLength)
  .transition(transitionPath)
  .attr("stroke-dashoffset", 0)
    }
  }
};
</script>

<style scoped>
.Chart1title * {
  font-size: 1.2em;
  font-family: "Dirooz FD";
}

/deep/ .dot {
  height: 25px;
  width: 25px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}
/deep/ .d3-tip {
  font-family: "Vazir-Medium-FD";
  line-height: 1.4;
  z-index: 300;
  padding: 20px;
  pointer-events: none !important;
  color: #203d5d;
  box-shadow: 0 4px 20px 4px rgba(0, 20, 60, 0.1),
    0 4px 80px -8px rgba(0, 20, 60, 0.2);
  background-color: #fff;
  border-radius: 4px;
  opacity: 80%;
}

/* Creates a small triangle extender for the tooltip */
/deep/ .d3-tip:after {
  box-sizing: border-box;
  display: inline;
  font-size: 10px;
  width: 100%;
  line-height: 1;
  color: rgb(139, 129, 129);
  position: absolute;
  pointer-events: none;
}

/* Northward tooltips */
/deep/ .d3-tip.n:after {
  content: "▼";
  margin: -1px 0 0 0;
  top: 100%;
  left: 0;
  text-align: center;
}

/* Eastward tooltips */
/deep/ .d3-tip.e:after {
  content: "◀";
  margin: -4px 0 0 0;
  top: 50%;
  left: -8px;
}

/* Southward tooltips */
/deep/ .d3-tip.s:after {
  content: "▲";
  margin: 0 0 1px 0;
  top: -8px;
  left: 0;
  text-align: center;
}

/* Westward tooltips */
/deep/ .d3-tip.w:after {
  content: "▶";
  margin: -4px 0 0 -1px;
  top: 50%;
  left: 100%;
}
</style>
