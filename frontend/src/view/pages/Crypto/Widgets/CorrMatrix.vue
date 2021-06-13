/* eslint-disable no-unused-vars */
<template>
    <div>
    <v-card class="mt-2">
      <v-toolbar dense>
        <v-toolbar-title>بررسی همبستگی رمزارزهای اصلی</v-toolbar-title>
      </v-toolbar>
      <div id="Chartcontainer2_index"></div>
    </v-card>
  </div>
</template>

<script>
import * as d3 from "d3";

// eslint-disable-next-line no-unused-vars
export default {
  name: "TechnicalCrypto",
  props: { inpuDataCorr: Array },
  data() {
    return {
      loading: true,
      jsonData: {},
      ChartData2: [],
      ChartLabels2: [],
      height: 0,
      width: 0,
      updatedAt: "",
      number: 3,
      margin: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0
      }
    };
  },
  watch: {
    inpuDataCorr() {
      this.renderData();
      if (this.isRealValue(this.ChartData2)) {
        this.renderChart();
      }
    }
  },
  // In the beginning...
  mounted() {
    this.renderData();
    this.initrender();
    if (!(this.ChartData2 === undefined || this.ChartData2.length == 0)) {
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
      if (document.getElementById("Chartcontainer2_index_svg")) {
        d3.selectAll("#Chartcontainer2_index_svg").remove();
      }
      this.width = parseInt(
        d3.select("#Chartcontainer2_index").style("width"),
        10
      );
      this.height = (this.width * 9) / 16;
      this.margin.top = this.height * 0.1;
      this.margin.bottom = this.height * 0.05;
      this.margin.right =
        parseInt(d3.select("#Chartcontainer2_index").style("width"), 10) * 0.05;
      this.margin.left =
        parseInt(d3.select("#Chartcontainer2_index").style("width"), 10) * 0.05;
      var parent = document.getElementById("Chartcontainer2_index");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "Chartcontainer2_index_svg")
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
      if (!(this.inpuDataCorr === undefined || this.inpuDataCorr.length == 0)) {
        let data = [...this.inpuDataCorr];
        let that = this;
        this.updatedAt = data[0].englishDate;
        let json_data = JSON.parse(data[0].corrMatrix);
        var result = [];
        var labels = [];
        for (var i in json_data) {
          let dictionary = json_data[i];
          var values = Object.keys(dictionary).map(function(key) {
            return that.roundTo(dictionary[key], 2);
          });
          result.push(values);
        }
        this.ChartData2 = result;
        for (var j in json_data) {
          labels.push(j);
        }
        this.ChartLabels2 = labels;
      }
    },
    renderChart() {
      if (document.getElementById("Chartcontainer2_index_svg")) {
        d3.selectAll("#Chartcontainer2_index_svg").remove();
      }

      var parent = document.getElementById("Chartcontainer2_index");
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "Chartcontainer2_index_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .style('background','url(../media/logos/fadedfinwise.png) no-repeat center ');
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      var numrows = this.ChartData2.length;
      // eslint-disable-next-line no-unused-vars
      //   var background = chart
      //     .append("rect")
      //     // .style("stroke", "gray")
      //     .style("stroke-width", "2px")
      //     .attr("width", this.width - this.margin.left - this.margin.right)
      //     .attr("height", this.height - this.margin.top - this.margin.bottom);
      // eslint-disable-next-line no-unused-vars
      var x = d3
        .scaleBand()
        .domain(d3.range(numrows))
        .range([
          this.margin.left,
          this.width - this.margin.left - this.margin.right
        ]);
      // eslint-disable-next-line no-unused-vars
      var maxValue = d3.max(this.ChartData2, function(layer) {
        return d3.max(layer, function(d) {
          return d;
        });
      });
      // eslint-disable-next-line no-unused-vars
      var minValue = d3.min(this.ChartData2, function(layer) {
        return d3.min(layer, function(d) {
          return d;
        });
      });
      // eslint-disable-next-line no-unused-vars
      var y = d3
        .scaleBand()
        .domain(d3.range(numrows))
        .range([
          this.margin.top,
          this.height - this.margin.bottom - this.margin.top
        ]);
      let that = this;
      // eslint-disable-next-line no-unused-vars
      var colorMap = d3
        .scaleLinear()
        .domain([0, maxValue])
        .range(["#fff", "#1b4332"]);
      var colorMapNeg = d3
        .scaleLinear()
        .domain([minValue, 0])
        .range(["#ba181b", "#fff"]);
      // eslint-disable-next-line no-unused-vars

      // eslint-disable-next-line no-unused-vars
      var row = chart
        .selectAll(".row")
        .data(this.ChartData2)
        .enter()
        .append("g")
        // .attr("width",this.width-this.margin.left-this.margin.right)
        // .attr("height", )
        .attr("class", "row")
        .attr("transform", function(d) {
          return "translate(0," + y(that.ChartData2.indexOf(d)) + ")";
        });
      // eslint-disable-next-line no-unused-vars
      var cell = row
        .selectAll(".cell")
        .data(this.ChartData2)
        .enter()
        .append("g")
        .attr("class", "cell")
        .attr("transform", function(d) {
          return "translate(" + x(that.ChartData2.indexOf(d)) + ", 0)";
        });
      var c = 0;
      cell
        .append("rect")
        .attr("width", x.bandwidth())
        .attr("height", y.bandwidth())
        .data(function(d, i) {
          return that.ChartData2[i];
        })
        .attr("fill", function(d, i) {
          // console.log(i);
          let g = that.ChartData2[c][i];
          if (i == numrows - 1) {
            c = c + 1;
          }
          if (g > 0) {
            return colorMap(g);
          } else {
            if (g == 1) {
              return "#000";
            } else {
              return colorMapNeg(g);
            }
          }
        });
      // eslint-disable-next-line no-unused-vars
      c = 0;
      cell
        .append("text")
        .data(this.ChartData2)
        .attr("dy", ".32em")
        .attr("x", x.bandwidth() / 2)
        .attr("y", y.bandwidth() / 2)
        .attr("text-anchor", "middle")
        // eslint-disable-next-line no-unused-vars
        .style("font-family", "Vazir-Medium-FD")
        .style("direction", "ltr")
        .style("font-size", `1.1em`)
        .text(function(d, i) {
          // console.log(i);
          let g = that.ChartData2[c][i];
          if (i == numrows - 1) {
            c = c + 1;
          }
          return g;
        });
      // row
      //   .selectAll(".cell")
      //   // eslint-disable-next-line no-unused-vars

      var labels = svg.append("g").attr("class", "labels");

      var columnLabels = labels
        .selectAll(".column-label")
        .data(this.ChartLabels2)
        .enter()
        .append("g")
        .attr("class", "column-label")
        .attr("transform", function(d) {
          return `translate(${that.margin.left +
            x(that.ChartLabels2.indexOf(d))},${that.margin.top})`;
        });

      columnLabels
        .append("line")
        .style("stroke", "black")
        .style("stroke-width", "1px")
        .attr("x1", x.bandwidth() / 2)
        .attr("x2", x.bandwidth() / 2)
        .attr("y1", this.margin.top)
        .attr("y2", this.margin.top + 10)
        .style("opacity", "0.4");

      columnLabels
        .append("text")
        .attr("x", this.margin.left + 5)
        .attr("y", y.bandwidth() / 2 + this.margin.top / 2)
        // .attr("dy", ".82em")
        .style("font-family", "Vazir-Medium-FD")
        .attr("text-anchor", "start")
        .style("font-weight", "600")
        // .attr("transform", "rotate(-60)")
        // eslint-disable-next-line no-unused-vars
        .text(function(d, i) {
          return d;
        });

      var rowLabels = labels
        .selectAll(".row-label")
        .data(this.ChartLabels2)
        .enter()
        .append("g")
        .attr("class", "row-label")
        .attr("transform", function(d) {
          return `translate(${
            that.margin.left
          },${that.margin.top + y(that.ChartLabels2.indexOf(d))})`;
        });
      rowLabels
        .append("line")
        .style("stroke", "black")
        .style("stroke-width", "1px")
        .attr("x1", this.margin.left + 5)
        .attr("x2", this.margin.left + 10)
        .attr("y1", y.bandwidth() / 2)
        .attr("y2", y.bandwidth() / 2)
        .style("opacity", "0.4");

      rowLabels
        .append("text")
        .attr("x", this.margin.left)
        .attr("y", y.bandwidth() / 2)
        .attr("dy", ".32em")
        .style("font-family", "Vazir-Medium-FD")
        .attr("text-anchor", "start")
        .style("font-weight", "600")
        // eslint-disable-next-line no-unused-vars
        .text(function(d, i) {
          return d;
        });
      window.addEventListener("resize", this.renderChart);
      svg
        .append("text")
        // .attr("class", "title")
        .attr("x", this.width / 2)
        .attr("y", this.margin.top / 2)
        .attr("text-anchor", "middle")
        .text("تحلیل همبستگی در تاریخ " + `${this.updatedAt}`);

      svg
        .append("text")
        .attr("class", "source")
        .attr("x", this.width - this.margin.left)
        .attr("y", this.height * 0.1)
        .attr("text-anchor", "start")
        .text("Source: FinWise")
        .style("font-weight", "700")
        .style("font-family", "'Tlwg Mono', sans-serif")
        .style("font-size", "10px")
        .style("opacity", "0.4");
    }
  }
};
</script>
