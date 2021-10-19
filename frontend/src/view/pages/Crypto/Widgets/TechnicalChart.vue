<template>
  <v-card rounded="lg">
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em"
        >بررسی تکنیکال رمز ارزها</v-toolbar-title
      >
      <v-spacer></v-spacer>
      <div class="d-flex justify-content-center" v-if="updatedAt.length">
        <span class="pl-1" :style="`font-size:${this.width / 900}em`"
          >بهترین و بدترین های تکنیکال بازار در تحلیل</span
        >
        <span dir="ltr" :style="`font-size:${this.width / 900}em`">{{
          updatedAt
        }}</span>
      </div>
    </v-toolbar>
    <div id="Chartcontainer_CryptoTechnical"></div>
  </v-card>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "TechnicalCrypto",
  props: { inpuDataTechnical: Array },
  data() {
    return {
      loading: true,
      ChartData: [],
      height: 0,
      width: 0,
      updatedAt: "",
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
    //// this.renderData();
    this.initrender();
    //// if (!(this.ChartData === undefined || this.ChartData.length == 0)) {
    ////   this.renderChart();
    //// }
  },
  computed: {},
  methods: {
    isRealValue(obj) {
      return obj && obj !== "null" && obj !== "undefined";
    },
    initrender() {
      if (document.getElementById("Chartcontainer_CryptoTechnical_svg")) {
        d3.selectAll("#Chartcontainer_CryptoTechnical_svg").remove();
      }
      this.width = parseInt(
        d3.select("#Chartcontainer_CryptoTechnical").style("width"),
        10
      );
      this.height = (this.width * 9) / 16;
      this.margin.top = this.height * 0.05;
      this.margin.bottom = this.height * 0.05;
      this.margin.right =
        parseInt(
          d3.select("#Chartcontainer_CryptoTechnical").style("width"),
          10
        ) * 0.05;
      this.margin.left =
        parseInt(
          d3.select("#Chartcontainer_CryptoTechnical").style("width"),
          10
        ) * 0.05;
      var parent = document.getElementById("Chartcontainer_CryptoTechnical");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "Chartcontainer_CryptoTechnical_svg")
        .attr(
          "viewBox",
          `0 0 ${this.width + this.margin.right + this.margin.left},${this
            .height +
            this.margin.top +
            this.margin.bottom}`
        )
        .attr("preserveAspectRatio", "xMidYMid meet");
    },
    renderData() {
      if (
        !(
          this.inpuDataTechnical === undefined ||
          this.inpuDataTechnical.length == 0
        )
      ) {
        let data = [...this.inpuDataTechnical];
        this.updatedAt = data[0].engdate.replace(/-/g, "/");

        data.sort(function(a, b) {
          return a.sum_signal - b.sum_signal;
        });
        this.ChartData = data
          .slice(Math.max(data.length - 10, 0))
          .sort(function(a, b) {
            return b.sum_signal - a.sum_signal;
          })
          .concat(data.slice(0, 10));
      }
    },
    renderChart() {
      if (document.getElementById("Chartcontainer_CryptoTechnical_svg")) {
        d3.selectAll("#Chartcontainer_CryptoTechnical_svg").remove();
      }

      var parent = document.getElementById("Chartcontainer_CryptoTechnical");
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "Chartcontainer_CryptoTechnical_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .style(
          "background",
          "url(../media/logos/fadedfinwise.png) no-repeat center "
        );
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      var xScale = d3
        .scaleLinear()
        .domain([
          -1 *
            d3.max(this.ChartData, function(d) {
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
      var yScale = d3
        .scaleBand()
        .domain(this.ChartData.map(x => x.original_symbol))
        .range([
          this.margin.top,
          this.height - this.margin.bottom - this.margin.top
        ]);
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
          .style("font-family", "Vazir-Medium-FD")
          .style("stroke-opacity", ".1");

      let xAxisAxe = chart.append("g").call(xAxis);
      xAxisAxe
        .selectAll("text")
        .style("font-family", "Vazir-Light-FD")
        .style("font-size", `1.15em`)
        .style("text-anchor", "middle")
        .style("direction", "ltr");
      var yAxis = g =>
        g
          .attr("class", "yAxis")
          .attr("transform", `translate(${xScale(0)},0)`)
          .transition()
          .duration(1000)
          .call(d3.axisLeft(yScale))
          .style("stroke-opacity", ".1");
      let yAxisAxe = chart.append("g").call(yAxis);
      yAxisAxe
        .selectAll("text")
        .style("text-anchor", "start")
        .attr("transform", `translate(${0},${1})`)
        .style("font-size", `1.1em`)
        .style("font-weight", "600")
        .style("font-family", "Vazir-Light-FD");

      var greenColor = d3
        .scaleLinear()
        .domain([0, Math.max(...this.ChartData.map(x => x.sum_signal)) * 1.2])
        .range(["#66BB6A", "#1B5E20"]);
      var redColor = d3
        .scaleLinear()
        .domain([0, Math.min(...this.ChartData.map(x => x.sum_signal)) * 1.2])
        .range(["#ff7096", "#ff0a54"]);
      // let that = this;
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
            return redColor(d.sum_signal);
          } else {
            return greenColor(d.sum_signal);
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
      //       .style("font-family", "Vazir-Medium-FD");
      //     const pathnew = g
      //       .selectAll("pathnew")
      //       .data([null])
      //       .join("path")
      //       .attr("fill", "#001170")
      //       .style("font-family", "Vazir-Medium-FD")
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
      //           .style("font-family", "Vazir-Medium-FD")
      //           .text(d => d.split("-")[1].split(" ")[0])
      //       )
      //       .style("fill", "white")
      //       .style("font-family", "Vazir-Medium-FD")
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
      // svg
      //   .append("text")
      //   // .attr("class", "title")
      //   .attr("x", this.width / 2)

      //   .attr("y", this.margin.top)
      //   .attr("text-anchor", "middle")
      //   .text(
      //     "بهترین و بدترین های تکنیکال بازار در تحلیل " + `${this.updatedAt}`
      //   )
      //   .style("font-size", `${this.width / 900}em`);
      svg
        .append("text")

        // .attr("class", "title")
        .attr("x", this.margin.left)

        .attr("y", this.height * 0.5)
        .attr("text-anchor", "middle")
        .text("تمامی محاسبات بر حسب معاملات با USDT در بایننس انجام شده است")
        // .style("font-family", 'Vazir-Medium-FD')
        .style("font-size", `${this.width / 900}em`)

        .attr("transform", function() {
          var x1 = this.getBBox().x + this.getBBox().width / 2; //the center x about which you want to rotate
          var y1 = this.getBBox().y + this.getBBox().height / 2; //the center y about which you want to rotate
          return `rotate(-90, ${x1}, ${y1})`; //rotate 180 degrees about x and y
        });
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
