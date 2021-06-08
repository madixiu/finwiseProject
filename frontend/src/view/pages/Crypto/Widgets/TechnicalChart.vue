/* eslint-disable no-unused-vars */
<template>
  <!-- <div class="card card-custom"> -->
  <div class="row col-xxl-12 col-lg-12 col-md-12 col-sm-12 row">
    <v-card width="100%">
      <v-card-title> بررسی تکنیکال رمز ارزها </v-card-title>
      <v-divider class="mt-0 mb-0"></v-divider>
      <div id="Chartcontainer_index"></div>
    </v-card>
  </div>
  <!-- </div> -->
</template>

<script>
import * as d3 from "d3";

// eslint-disable-next-line no-unused-vars
export default {
  name: "TechnicalCrypto",
  props: { inpuDataTechnical: Array },
  data() {
    return {
      loading: true,
      jsonData: {},
      ChartData: [],
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
    inpuDataTechnical() {
      this.renderData();
      if (this.isRealValue(this.ChartData)) {
        this.renderChart();
      }
    }
  },
  // In the beginning...
  mounted() {
    this.renderData();
    this.initrender();
    if (!(this.ChartData === undefined || this.ChartData.length == 0)) {
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
      this.width = parseInt(
        d3.select("#Chartcontainer_index").style("width"),
        10
      );
      this.height = (this.width * 9) / 16;
      this.margin.top = this.height * 0.05;
      this.margin.bottom = this.height * 0.05;
      this.margin.right =
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.05;
      this.margin.left =
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.05;
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
      if (
        !(
          this.inpuDataTechnical === undefined ||
          this.inpuDataTechnical.length == 0
        )
      ) {
        let data = [...this.inpuDataTechnical];
        this.updatedAt = data[0].engdate;
        // var parseTime = d3.timeParse("%Y-%m-%d %H:%M:%S");
        // data.forEach(
        //   function(d) {
        //     d.date = parseTime(d.englishDate.split(".")[0]);
        //     d.value = d.Index;
        //   },
        //   // eslint-disable-next-line no-unused-vars
        //   function(error, data) {
        //     if (error) throw error;
        //   }
        // );
        data.sort(function(a, b) {
          return a.sum_signal - b.sum_signal;
        });
        this.ChartData = data
          .slice(Math.max(data.length - 10, 0))
          .sort(function(a, b) {
            return b.sum_signal - a.sum_signal;
          })
          .concat(data.slice(0, 10));
        // console.log(this.ChartData);
      }
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
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .style('background','url(../media/logos/fadedfinwise.png) no-repeat center ')
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      // eslint-disable-next-line no-unused-vars
      var xScale = d3
        .scaleLinear()
        .domain([
          -1 *
            d3.max(this.ChartData, function(d) {
              // console.log(d)
              return Math.abs(d.sum_signal);
            }),

          d3.max(this.ChartData, function(d) {
            return Math.abs(d.sum_signal);
          })
        ])
        .range([
          this.margin.left,
          this.width - this.margin.right - this.margin.left
        ]);
      // eslint-disable-next-line no-unused-vars
      var yScale = d3
        .scaleBand()
        .domain(this.ChartData.map(x => x.original_symbol))
        .range([
          this.margin.top,
          this.height - this.margin.bottom - this.margin.top
        ]);
      // eslint-disable-next-line no-unused-vars
      var xAxis = g =>
        g
          .attr("class", "xAxis")
          .attr("transform", `translate(${0},${this.margin.top})`)
          .transition()
          .duration(1000)
          .ease(d3.easeSin)
          .call(
            d3
              .axisTop(xScale)
              .ticks(this.width / 80)
              .tickSizeInner(
                this.height * -1 + this.margin.bottom + this.margin.top * 2
              )
          )
          .style("font-family", "Dirooz FD")
          .style("stroke-opacity", ".1");

      let xAxisAxe = chart.append("g").call(xAxis);
      xAxisAxe
        .selectAll("text")
        .style("font-size", `${this.width / 1000}em`)
        .style("font-family", "Dirooz FD")
        .style("font-size", `1.4em`)
        .style("font-weight", "800")
        .style("text-anchor", "end")
        .style("font-family", "Dirooz FD");
      var yAxis = g =>
        g
          .attr("class", "yAxis")
          .attr("transform", `translate(${xScale(0)},0)`)
          .transition()
          .duration(1000)
          .call(d3.axisLeft(yScale))
          .style("stroke-opacity", ".1")
          .style("font-family", "Dirooz FD");
      let yAxisAxe = chart.append("g").call(yAxis);
      yAxisAxe
        .selectAll("text")
        .style("text-anchor", "start")
        .attr("transform", `translate(${0},${4})`)
        .style("font-size", `1.3em`)
        .style("font-weight", "800")
        .style("font-family", "Dirooz FD");

      var mycolor = d3
        .scaleLinear()
        .domain([0, Math.max(...this.ChartData.map(x => x.sum_signal)) * 1.2])
        .range(["#66BB6A", "#1B5E20"]);
      var mycolor2 = d3
        .scaleLinear()
        .domain([0, Math.min(...this.ChartData.map(x => x.sum_signal)) * 1.2])
        .range(["#ff7096", "#ff0a54"]);
      // eslint-disable-next-line no-unused-vars
      let that = this;
      chart
        .selectAll()
        .data(this.ChartData)
        .enter()
        .append("rect")
        .attr("width", function(d) {
          if (xScale(d.sum_signal) > xScale(0)) {
            return xScale(d.sum_signal) - xScale(0);
          } else {
            if (xScale(d.sum_signal) == xScale(0)) {
              return 0;
            } else {
              return xScale(d.sum_signal);
            }
          }
        })
        .attr("x", function(d) {
          if (xScale(d.sum_signal) > xScale(0)) {
            return xScale(0);
          } else {
            if (xScale(d.sum_signal) == xScale(0)) {
              return xScale(0);
            } else {
              return xScale(0) - xScale(d.sum_signal);
            }
          }
        })
        .attr("y", d => yScale(d.original_symbol) + yScale.bandwidth() * 0.25)
        .transition()
        .duration(2000)
        .ease(d3.easePolyOut)
        .attr("height", yScale.bandwidth() * 0.7)
        .attr("fill", function(d) {
          if (d.sum_signal < 0) {
            return mycolor2(d.sum_signal);
          } else {
            return mycolor(d.sum_signal);
          }
        })
        .style("opacity", 0.5);
      //   d3.selectAll("g.yAxis g.tick")
      //     .append("line")
      //     .attr("class", "gridline")
      //     .attr("x1", 0)
      //     .attr("y1", 0)
      //     .attr("x2", this.width - this.margin.left * 2)
      //     .attr("y2", 0);
      //   var line = d3
      //     .line()
      //     .curve(d3.curveBasis)
      //     .defined(d => !isNaN(d.date))
      //     .x(d => xScale(d.date))
      //     .y(d => yScale(d.value));

      //   // eslint-disable-next-line no-unused-vars
      //   var path = chart
      //     .append("path")
      //     .datum(this.inpuDataTechnical.filter(line.defined()))
      //     .style("fill", "none")
      //     .attr("stroke", "steelblue")
      //     .attr("stroke-width", 2)
      //     .attr("stroke-linejoin", "round")
      //     .attr("stroke-linecap", "round")
      //     .attr("d", line);
      //   const pathLength = path.node().getTotalLength();
      //   const transitionPath = d3
      //     .transition()
      //     .ease(d3.easeSinOut)
      //     .duration(5500);

      //   path
      //     .attr("stroke-dashoffset", pathLength)
      //     .attr("stroke-dasharray", pathLength)
      //     .transition(transitionPath)
      //     .attr("stroke-dashoffset", 0);

      //   const tooltip = chart.append("g");
      //   var dates = this.inpuDataTechnical.map(function(d) {
      //     return d.date;
      //   });
      //   function formatValue(value) {
      //     return value.toLocaleString("en", {});
      //   }
      //   function formatDate(date) {
      //     return date.toLocaleString("en", {
      //       hour: "numeric",
      //       minute: "numeric",
      //       second: "numeric"
      //     });
      //   }
      //   let that = this;
      //   // eslint-disable-next-line no-unused-vars
      //   var callout2 = (g, value1, value2, value) => {
      //     if (!value2) return g.style("display", "none");
      //     g.style("display", null).style("pointer-events", "none");
      //     const path = g
      //       .selectAll("path")
      //       .data([null])
      //       .join("path")
      //       .attr("fill", "white")
      //       .attr("stroke", "black")
      //       .style("stroke-dasharray", "2, 6")
      //       .style("Opacity", "0.4 ");
      //     path.attr(
      //       "d",
      //       `M${0} ${0} L${0} ${that.height -
      //         that.margin.top -
      //         yScale(that.inpuDataTechnical[value2].value)} L${0} ${that.margin
      //         .top - yScale(that.inpuDataTechnical[value2].value)}`
      //     );
      //     // eslint-disable-next-line no-unused-vars
      //     const circle = g
      //       .selectAll("circle")
      //       .data([null])
      //       .join("circle")
      //       .attr("fill", "steelblue")
      //       .attr("stroke-width", 2)
      //       .style("stroke", "black");

      //     circle
      //       .attr("r", "5")
      //       .attr("cx", "0")
      //       .attr("cy", "0");
      //     // eslint-disable-next-line no-unused-vars
      //     const text = g
      //       .selectAll("text")
      //       .data([null])
      //       .join("text")
      //       .call(text =>
      //         text
      //           .selectAll("tspan")
      //           .data((value + "").split(/\n/))
      //           .join("tspan")
      //           .attr("x", 0)
      //           .attr("y", (d, i) => `${i * 1.1}em`)
      //           .style("font-weight", (_, i) => (i ? null : "bold"))
      //           .style("font-size", "14px")
      //           .style("font-family", "Vazir-Medium-FD")
      //           .text(d => d.split("-")[0])
      //       )
      //       .style("fill", "black");

      //     //eslint-disable-next-line no-unused-vars
      //     const { x, y, width: w, height: h } = text.node().getBBox();
      //     text
      //       .attr("transform", `translate(${that.margin.left + w / 10},${-h})`)
      //       .style("font-family", "Dirooz FD");
      //     const pathnew = g
      //       .selectAll("pathnew")
      //       .data([null])
      //       .join("path")
      //       .attr("fill", "#001170")
      //       .style("font-family", "Dirooz FD")
      //       .style("stroke", "black")
      //       .style("stroke-dasharray", "3,3")
      //       .style("Opacity", "0.8");
      //     pathnew
      //       .attr(
      //         "d",
      //         `M${0} ${that.height -
      //           that.margin.top -
      //           yScale(that.inpuDataTechnical[value2].value)} H-6
      //           l7,-5l5,5H 25 V
      //           ${that.height -
      //             that.margin.top -
      //             yScale(that.inpuDataTechnical[value2].value) +
      //             40} H-30 V${that.height -
      //           that.margin.top -
      //           yScale(that.inpuDataTechnical[value2].value)}z`
      //       )
      //       .attr("stroke", "black");

      //     const text2 = g
      //       .selectAll("text2")
      //       .data([null])
      //       .join("text")
      //       .call(text2 =>
      //         text2
      //           .selectAll("tspan")
      //           .data((value + "").split(/\n/))
      //           .join("tspan")
      //           .attr("x", 0)
      //           .attr("y", (d, i) => `${i * 1.1}em`)
      //           .style("font-weight", (_, i) => (i ? null : "bold"))
      //           .style("font-family", "Dirooz FD")
      //           .text(d => d.split("-")[1].split(" ")[0])
      //       )
      //       .style("fill", "white")
      //       .style("font-family", "Dirooz FD")
      //       .style("font-size", "11px")
      //       .style("Opacity", "1 ");
      //     // eslint-disable-next-line no-unused-vars
      //     const { x2, y2, width: w2, height: h2 } = text2.node().getBBox();
      //     text2.attr(
      //       "transform",
      //       `translate(${w2 / 2},${that.height -
      //         that.margin.top -
      //         yScale(that.inpuDataTechnical[value2].value) +
      //         20})`
      //     );
      //     const pathnew2 = g
      //       .selectAll("pathnew2")
      //       .data([null])
      //       .join("path")
      //       .attr("fill", "gray")
      //       .style("stroke", "black")
      //       // .style("stroke-dasharray", ("3,3"))
      //       .style("Opacity", "0.4");
      //     pathnew2
      //       .attr("d", `M${-10} ${-10} H${90} V${-50} H${-10}z`)
      //       .attr("stroke", "black");
      //   };

      //   svg.on("touchmove mousemove", function(event) {
      //     const x1 = d3.pointer(event, this)[0];
      //     const y1 = d3.pointer(event, this)[1];
      //     if (x1 - that.margin.left < that.width - that.margin.right) {
      //       const date = xScale.invert(x1 - that.margin.left);
      //       // eslint-disable-next-line no-unused-vars
      //       const y2 = yScale.invert(y1 - that.margin.top);
      //       const idx = d3.bisect(dates, date);
      //       tooltip
      //         .attr(
      //           "transform",
      //           `translate(${xScale(that.inpuDataTechnical[idx].date)},${yScale(
      //             that.inpuDataTechnical[idx].value
      //           )})`
      //         )
      //         .call(
      //           callout2,
      //           x1,
      //           idx,
      //           `${formatValue(that.inpuDataTechnical[idx].value)}-${formatDate(
      //             that.inpuDataTechnical[idx].date
      //           )}-`
      //         );
      //     }
      //   });

      //   svg.on("touchend mouseleave", () => tooltip.call(callout2, null));
      svg
        .append("text")
        .attr("class", "title")
        .attr("x", this.width / 2)

        .attr("y", this.margin.top)
        .attr("text-anchor", "middle")
        .text(
          "بهترین و بدترین های تکنیکال بازار در تحلیل " + `${this.updatedAt}`
        )
        .style("font-size", `${this.width / 1000}em`);
       svg
        .append("text")
       
        .attr("class", "title")
        .attr("x",this.margin.left)

        .attr("y", this.height*0.5)
        .attr("text-anchor", "middle")
        .text(
          "تمامی محاسبات بر حسب معاملات با USDT در بایننس انجام شده است" 
        )
        .style("font-size", `${this.width / 1000}em`) .attr("transform", function() {
          var me = this;
          var x1 = me.getBBox().x + me.getBBox().width / 2; //the center x about which you want to rotate
          var y1 = me.getBBox().y + me.getBBox().height / 2; //the center y about which you want to rotate

          return `rotate(-90, ${x1}, ${y1})`; //rotate 180 degrees about x and y
        })
      // svg
      //   .append("text")
      //   .attr("class", "source")
      //   .attr("x", this.width - this.margin.left)
      //   .attr("y", this.height * 0.9)
      //   .attr("text-anchor", "start")
      //   .text("Source: FinWise")
      //   .style("font-weight", "700")
      //   .style("font-family", "'Tlwg Mono', sans-serif")
      //   .style("font-size", "10px")
      //   .style("opacity", "0.4");
    }
  }
};
</script>

<style scoped>
.cellHeader {
  /* direction: ltr; */
  text-align: right;
  font-family: "Vazir-Medium-FD";
  font-size: 0.9em;
}
.cellItem {
  direction: ltr;
  text-align: right;
  font-family: "Vazir-Medium-FD";
  /* font-weight: 700; */
  font-size: 0.9em;
}
.cellItem2 {
  font-family: "Vazir-Medium-FD";
  font-weight: 600;
  font-size: 0.7em;
}
.redItem {
  color: red !important;
  font-size: 0.9em;
  font-family: "Vazir-Medium-FD" !important;
}
.greenItem {
  color: green !important;
  font-size: 0.9em;
  font-family: "Vazir-Medium-FD" !important;
}
.Chart1title * {
  font-size: 1.2em;
  font-family: "Dirooz FD";
}

.dot {
  height: 25px;
  width: 25px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}
.d3-tip {
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
.inlineIcon {
  display: inline;
}
/* Creates a small triangle extender for the tooltip */
.d3-tip:after {
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
.d3-tip.n:after {
  content: "▼";
  margin: -1px 0 0 0;
  top: 100%;
  left: 0;
  text-align: center;
}

/* Eastward tooltips */
.d3-tip.e:after {
  content: "◀";
  margin: -4px 0 0 0;
  top: 50%;
  left: -8px;
}

/* Southward tooltips */
.d3-tip.s:after {
  content: "▲";
  margin: 0 0 1px 0;
  top: -8px;
  left: 0;
  text-align: center;
}

/* Westward tooltips */
.d3-tip.w:after {
  content: "▶";
  margin: -4px 0 0 -1px;
  top: 50%;
  left: 100%;
}

</style>
