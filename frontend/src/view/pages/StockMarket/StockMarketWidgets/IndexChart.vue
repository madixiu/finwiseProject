/* eslint-disable no-unused-vars */
<template>
  <div class="card card-custom">
    <v-card>
      <v-card-title>شاخص کل</v-card-title>
      <v-divider class="mt-0"></v-divider>
      <div class="row">
        <div
          id="Chartcontainer_index"
          class="col-xxl-9 col-lg-9 col-md-12 col-sm-12"
        ></div>
        <div class="col-xxl-3 col-lg-3 col-md-12 col-sm-12 card card-custom">
          <v-card-title>شاخص کل {{ this.latestIndex }}</v-card-title>
          <v-divider class="mt-0"></v-divider>
          <v-card-title>شاخص هم وزن {{ this.latestIndex }}</v-card-title>
          <v-divider class="mt-0"></v-divider>
          <v-card-title>شاخص فرابورس {{ this.latestIndex }}</v-card-title>
          <v-divider class="mt-0"></v-divider>
          <v-card-title>ارزش بازار بورس {{ this.latestIndex }}</v-card-title>
          <v-divider class="mt-0"></v-divider>
          <v-card-title>ارزش بازار فرابورس {{ this.latestIndex }}</v-card-title>
          <v-divider class="mt-0"></v-divider>
          <v-card-title>ارزش معاملات بورس {{ this.latestIndex }}</v-card-title>
          <v-divider class="mt-0"></v-divider>
          <v-card-title
            >ارزش معاملات فرابورس {{ this.latestIndex }}</v-card-title
          >
          <v-divider class="mt-0"></v-divider>
        </div>
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
      latestIndex: 0,
      latestSW: 0,
      latestTradeValue: 0,
      MarketCapTotal: 0,
      IFBlatestIndex: 0,
      IFBMarketCapTotal: 0,

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

      data = data.filter(function(d) {
        if (d.date.getHours() > 8 && d.Market == 1) {
          return d;
        }
      });
      this.indexData = [...data];
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
        .attr("x2", this.width - this.margin.left * 2)
        .attr("y2", 0);
      var line = d3
        .line()
        .curve(d3.curveBasis)
        .defined(d => !isNaN(d.date))
        .x(d => xScale(d.date))
        .y(d => yScale(d.value));

      // eslint-disable-next-line no-unused-vars
      var path = chart
        .append("path")
        .datum(this.indexData.filter(line.defined()))
        .style("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 2)
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
        .attr("stroke-dashoffset", 0);

      const tooltip = chart.append("g");
      var dates = this.indexData.map(function(d) {
        return d.date;
      });
      function formatValue(value) {
        return value.toLocaleString("en", {});
      }
      function formatDate(date) {
        return date.toLocaleString("en", {
          hour: "numeric",
          minute: "numeric",
          second: "numeric"
        });
      }
      // eslint-disable-next-line no-unused-vars
      var callout2 = (g, value1, value2, value) => {
        if (!value2) return g.style("display", "none");
        // g.style("display", null).style("pointer-events", "none");
        // const path = g
        //   .selectAll("path")
        //   .data([null])
        //   .join("path")
        //   .attr("fill", "white")
        //   .attr("stroke", "black")
        //   .style("stroke-dasharray", "2, 6")
        //   .style("Opacity", "0.2 ");
        // path.attr(
        //   "d",
        //   `M${0} ${0} L${0} ${this.height -
        //     this.margin.top -
        //     yScale(this.indexData[value2].value)} L${0} ${this.margin.top -
        //     yScale(this.indexData[value2].value)}`
        // );
        // const circle = g
        //   .selectAll("circle")
        //   .data([null])
        //   .join("circle")
        //   .attr("fill", "steelblue")
        //   .attr("stroke-width", 2)
        //   .style("stroke", "black");

        // circle
        //   .attr("r", "5")
        //   .attr("cx", "0")
        //   .attr("cy", "0");
        // const text = g
        //   .selectAll("text")
        //   .data([null])
        //   .join("text")
        //   .call(text =>
        //     text
        //       .selectAll("tspan")
        //       .data((value + "").split(/\n/))
        //       .join("tspan")
        //       .attr("x", 0)
        //       .attr("y", (d, i) => `${i * 1.1}em`)
        //       .style("font-weight", (_, i) => (i ? null : "bold"))
        //       .text(d => d.split("-")[0])
        //   )
        //   .style("fill", "black")
        //   .style("font-size", "14px");
        // // eslint-disable-next-line no-unused-vars
        // const { x, y, width: w, height: h } = text.node().getBBox();
        // text.attr("transform", `translate(${0},${-h})`);
        // const pathnew = g
        //   .selectAll("pathnew")
        //   .data([null])
        //   .join("path")
        //   .attr("fill", "#001170")
        //   .style("stroke", "black")
        //   .style("stroke-dasharray", "3,3")
        //   .style("Opacity", "0.8");
        // pathnew
        //   .attr(
        //     "d",
        //     `M${0} ${this.height -
        //       this.margin.top -
        //       yScale(this.indexData[value2].value)} H-6 l7,-5l5,5H 25 V${this.height -
        //       this.margin.top -
        //       yScale(this.indexData[value2].value) +
        //       40} H-30 V${this.height - this.margin.right - yScale(this.indexData[value2].value)}z`
        //   )
        //   .attr("stroke", "black");

        // const text2 = g
        //   .selectAll("text2")
        //   .data([null])
        //   .join("text")
        //   .call(text2 =>
        //     text2
        //       .selectAll("tspan")
        //       .data((value + "").split(/\n/))
        //       .join("tspan")
        //       .attr("x", 0)
        //       .attr("y", (d, i) => `${i * 1.1}em`)
        //       .style("font-weight", (_, i) => (i ? null : "bold"))
        //       .text(d => d.split("-")[1].split(" ")[0])
        //   )
        //   .style("fill", "white")
        //   .style("font-size", "11px")
        //   .style("Opacity", "1 ");
        // // eslint-disable-next-line no-unused-vars
        // const { x2, y2, width: w2, height: h2 } = text2.node().getBBox();
        // text2.attr(
        //   "transform",
        //   `translate(${-w2 / 2 - 1},${this.height -
        //     this.margin.top -
        //     yScale(this.indexData[value2].value) +
        //     20})`
        // );
        // const pathnew2 = g
        //   .selectAll("pathnew2")
        //   .data([null])
        //   .join("path")
        //   .attr("fill", "gray")
        //   .style("stroke", "black")
        //   // .style("stroke-dasharray", ("3,3"))
        //   .style("Opacity", "0.4");
        // pathnew2
        //   .attr("d", `M${-10} ${-10} H${90} V${-50} H${-10}z`)
        //   .attr("stroke", "black");
      };
      chart.on("touchmove mousemove", function(event) {
        const x1 = d3.pointer(event, this)[0];
        const y1 = d3.pointer(event, this)[1];
        if (x1 - this.margin.left < this.width - this.margin.right) {
          const date = xScale.invert(x1 - this.margin.left);
          // eslint-disable-next-line no-unused-vars
          const y2 = yScale.invert(y1 - this.margin.top);
          const idx = d3.bisect(dates, date);
          tooltip
            .attr(
              "transform",
              `translate(${xScale(this.indexData[idx].date)},${yScale(
                this.indexData[idx].value
              )})`
            )
            .call(
              callout2,
              x1,
              idx,
              `${formatValue(this.indexData[idx].value)}-${formatDate(
                this.indexData[idx].date
              )}-`
            );
        }
      });

      chart.on("touchend mouseleave", () => tooltip.call(callout2, null));
      svg
        .append("text")
        .attr("class", "title")
        .attr("x", this.width / 2 + this.margin.left)
        .attr("y", 40)
        .attr("text-anchor", "middle")
        .text("شاخص کل");
      svg
        .append("text")
        .attr("class", "source")
        .attr("x", this.width - this.margin.left)
        .attr("y", this.height*0.9)
        .attr("text-anchor", "start")
        .text("Source: FinWise")
        .style("font-weight", "700")
        .style("font-family", "'Tlwg Mono', sans-serif")
        .style("font-size", "10px")
        .style("opacity", "0.3");
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
