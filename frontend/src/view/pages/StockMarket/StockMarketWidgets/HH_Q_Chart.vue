<template>
  <!-- <div class="card card-custom"> -->
  <!-- <v-skeleton-loader
      type=" table-heading,table-row@12"
      v-if="loading"
    ></v-skeleton-loader> -->
  <v-card>
    <v-card-title
      >نمودار وضعیت بازار -
      <b-form-group class="pt-3">
        <b-form-radio-group
          :click="this.renderChart1()"
          v-model="SortBy1"
          value="HH"
          :options="options1"
          name="radio-inline_q"
        ></b-form-radio-group> </b-form-group
    ></v-card-title>
    <v-divider class="mt-0"></v-divider>
    <div id="ChartContainer_HH"></div>
    <!--end::Header-->
  </v-card>
  <!-- </div> -->
</template>

<script>
import * as d3 from "d3";
export default {
  name: "ChartHH",
  props: { inputDataHH: Array, inputDataQ: Array },
  data() {
    return {
      jsonData: [],
      jsonData2: [],
      loading: true,
      highestValues: [],
      highestVolumes: [],
      highestImpcats: [],
      lowestImpcats: [],
      margin: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0
      },
      options1: [
        { text: "بیشترین ورود و خروج حقیقی", value: "HH" },
        { text: "بیشترین عرضه تقاضای لحظه ای", value: "DS" }
      ],
      SortBy1: "HH"
    };
  },
  watch: {
    inputDataHH() {
      this.renderData1();
      if (this.isRealValue(this.highestValues)) {
        this.renderChart1();
      }
    },
    inputDataQ() {
      this.renderData1();
      if (this.isRealValue(this.highestValues)) {
        this.renderChart1();
      }
    }
  },
  mounted() {
    this.renderData1();
    this.initrender();
    if (this.isRealValue(this.highestValues)) {
      this.renderChart1();
    }
  },
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
    renderData1() {
      if (!(this.inputDataHH === undefined || this.inputDataHH.length == 0)) {
        this.jsonData = [...this.inputDataHH];
        this.jsonData.sort((a, b) => b.netHaghighi - a.netHaghighi);
        this.highestValues = this.jsonData.slice(0, 10);
        this.jsonData.sort((a, b) => a.netHaghighi - b.netHaghighi);
        this.highestVolumes = this.jsonData.slice(0, 10);
        // console.log("HH");
        // console.log(this.highestValues);
        // console.log(this.highestVolumes);
      }
      if (!(this.inputDataQ === undefined || this.inputDataQ.length == 0)) {
        this.jsonData2 = [...this.inputDataQ[1]];
        this.jsonData2.sort((a, b) => b.Value - a.Value);
        this.highestImpcats = this.jsonData2.slice(0, 10);
        // console.log("Demands");
        // console.log(this.highestImpcats);
        this.jsonData3 = [...this.inputDataQ[0]];
        this.jsonData3.sort((a, b) => b.Value - a.Value);
        this.lowestImpcats = this.jsonData3.slice(0, 10);
        // console.log("Supplies");
        // console.log(this.lowestImpcats);
      }
    },
    initrender() {
      if (document.getElementById("ChartContainer_HH_svg")) {
        d3.selectAll("#ChartContainer_HH_svg").remove();
      }
      this.width =
        0.85 * parseInt(d3.select("#ChartContainer_HH").style("width"), 10);
      this.height = (this.width * 8) / 16;
      this.margin.top = this.height * 0.05;
      this.margin.bottom = this.height * 0.05;
      this.margin.right =
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) * 0.075;
      this.margin.left =
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) * 0.075;
      this.offsetY = this.margin.top;
      var parent = document.getElementById("ChartContainer_HH");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "ChartContainer_HH_svg")
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
    renderChart1() {
      if (document.getElementById("ChartContainer_HH_svg")) {
        d3.selectAll("#ChartContainer_HH_svg").remove();
      }

      var parent = document.getElementById("ChartContainer_HH");
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "ChartContainer_HH_svg")
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
      svg
        .append("text")
        .attr("class", "source")
        .attr("x", this.width / 2 + this.margin.right)
        .attr("y", this.height * 0.1)
        .attr("text-anchor", "start")
        .text("Source: FinWise")
        .style("font-weight", "700")
        .style("font-family", "'Tlwg Mono', sans-serif")
        .style("font-size", "10px")
        .style("opacity", "0.3");
      if (this.SortBy1 == "HH") {
        const xLeft = d3
          .scaleBand()
          .domain(this.highestValues.map(x => x.ticker))
          .range([0, (this.width - this.margin.right) / 2])
          .padding(0.15);

        const yLeft = d3
          .scaleLinear()
          .domain([
            0,
            Math.abs(
              Math.max(
                Math.max(
                  ...this.highestValues.map(x => {
                    if (x.netHaghighi > 0) {
                      return x.netHaghighi;
                    } else {
                      return x.netHaghighi * -1;
                    }
                  })
                ),
                Math.max(
                  ...this.highestVolumes.map(x => {
                    if (x.netHaghighi > 0) {
                      return x.netHaghighi;
                    } else {
                      return x.netHaghighi * -1;
                    }
                  })
                )
              ) * 1.2
            )
          ])
          // .domain([
          //   0,
          //   Math.max(...this.highestValues.map(x => x.netHaghighi)) * 1.2
          // ])
          .range([this.height - this.margin.bottom, this.margin.top])
          .nice();
        // eslint-disable-next-line no-unused-vars
        const xRight = d3
          .scaleBand()
          .domain(this.highestVolumes.map(x => x.ticker))
          .range([this.width, (this.width - this.margin.right) / 2])
          .padding(0.15);

        // eslint-disable-next-line no-unused-vars
        const yRight = d3
          .scaleLinear()
          .domain([
            0,
            -1 *
              Math.abs(
                Math.max(
                  Math.max(
                    ...this.highestValues.map(x => {
                      if (x.netHaghighi > 0) {
                        return x.netHaghighi;
                      } else {
                        return x.netHaghighi * -1;
                      }
                    })
                  ),
                  Math.max(
                    ...this.highestVolumes.map(x => {
                      if (x.netHaghighi > 0) {
                        return x.netHaghighi;
                      } else {
                        return x.netHaghighi * -1;
                      }
                    })
                  )
                ) * 1.2
              )
          ])
          .range([this.height - this.margin.bottom, this.margin.top])
          .nice();
        ///////////////
        var mycolor = d3
          .scaleLinear()
          .domain([
            0,
            Math.max(...this.highestValues.map(x => x.netHaghighi)) * 1.2
          ])
          .range(["#66BB6A", "#1B5E20"]);
        var mycolor2 = d3
          .scaleLinear()
          .domain([
            0,
            Math.min(...this.highestVolumes.map(x => x.netHaghighi)) * 1.2
          ])
          .range(["#4DD0E1", "#006064"]);
        //////////////
        let aXisY2 = d3
          .axisLeft(yLeft)
          .tickFormat(d => {
            if (d <= 0) {
              return d;
            } else {
              return (
                this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                "  " +
                "میلیارد ریال"
              );
            }
          })
          .tickSizeInner(-this.width / 2 + this.margin.left / 2);
        let aXisY2Axe = chart.append("g").call(aXisY2);
        aXisY2Axe
          .selectAll("text")
          .style("text-anchor", "start")
          .attr("transform", `translate(0,0)`)
          // .attr("dx", "-8em")
          .style("font-size", `${this.width / 1000}em`)
          .style("font-family", "Dirooz FD")
          .style("font-weight", "800");
        aXisY2Axe
          .selectAll(".tick line")
          .attr("stroke", "#b0a8b9")
          .style("opacity", "0.2");
        chart
          .append("g")
          .call(d3.axisBottom(xLeft))
          .attr("transform", `translate(0,${this.height - this.margin.bottom})`)
          .selectAll("text")
          .style("Visibility", "hidden");

        ////////////////
        let aXisY1 = d3
          .axisRight(yRight)
          .tickFormat(d => {
            if (d >= 0) {
              return d;
            } else {
              return (
                this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                "  " +
                "میلیارد ریال"
              );
            }
          })
          .tickSizeInner(-this.width / 2 - this.margin.right / 2);
        var aXisY1Axe = chart
          .append("g")
          .call(aXisY1)
          .attr("transform", `translate(${this.width},0)`);

        aXisY1Axe
          .selectAll("text")
          .style("text-anchor", "end")
          .style("font-size", `${this.width / 1000}em`)
          .style("font-family", "Dirooz FD")
          .style("font-weight", "800");
        aXisY1Axe
          .selectAll(".tick line")
          .attr("stroke", "#b0a8b9")
          .style("opacity", "0.2");

        chart
          .append("g")
          .call(d3.axisBottom(xRight))
          .attr("transform", `translate(0,${this.height - this.margin.bottom})`)
          .selectAll("text")
          .style("Visibility", "hidden");
        chart
          .selectAll("text.bar")
          .data(this.highestValues)
          .enter()
          .append("text")
          .attr("class", "yAxis-label")
          .attr("text-anchor", "middle")
          .attr("fill", "#70747a")
          .style("font-size", `${this.width / 950}em`)
          .attr("x", d => xLeft(d.ticker) + xLeft.bandwidth() * 0.5)
          .attr("y", d => {
            return yLeft(d["netHaghighi"]) - 0.05 * this.height;
          })
          .text(d => d.ticker)
          .attr("transform", function() {
            var me = this;
            var x1 = me.getBBox().x + me.getBBox().width / 2; //the center x about which you want to rotate
            var y1 = me.getBBox().y + me.getBBox().height / 2; //the center y about which you want to rotate

            return `rotate(-90, ${x1}, ${y1})`; //rotate 180 degrees about x and y
          });
        chart
          .selectAll("text.bar")
          .data(this.highestVolumes)
          .enter()
          .append("text")
          .attr("class", "yAxis-label")
          .attr("text-anchor", "middle")
          .attr("fill", "#70747a")
          .style("font-size", `${this.width / 950}em`)
          .attr("x", d => xRight(d.ticker) + xRight.bandwidth() * 0.5)
          .attr("y", d => {
            return yRight(d["netHaghighi"]) - 0.05 * this.height;
          })
          .text(d => d.ticker)
          .attr("transform", function() {
            var me = this;
            var x1 = me.getBBox().x + me.getBBox().width / 2; //the center x about which you want to rotate
            var y1 = me.getBBox().y + me.getBBox().height / 2; //the center y about which you want to rotate

            return `rotate(-90, ${x1}, ${y1})`; //rotate 180 degrees about x and y
          });

        chart
          .append("line")
          .style("stroke", "black")
          .attr("x1", xRight(0))
          // eslint-disable-next-line no-unused-vars
          .attr("y1", `${this.height - this.margin.bottom}`)
          .attr("x2", xRight(0))
          .attr("y2", `${this.margin.top}`)
          // eslint-disable-next-line no-unused-vars
          .attr(
            "transform",
            `translate(${(this.width - this.margin.right) / 2},0)`
          );
        chart
          .append("line")
          .style("stroke", "steelblue")
          .attr("x1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr("y1", 0)
          .attr(
            "x2",
            `${(this.width - this.margin.right - this.margin.left) / 2}`
          )
          .attr("y1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr(
            "transform",
            `translate(${(this.width - this.margin.right) / 2 + 20},${
              this.margin.top
            })`
          );
        chart
          .append("line")
          .style("stroke", "steelblue")
          .attr("x1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr("y1", 0)
          .attr(
            "x2",
            `${(this.width - this.margin.right - this.margin.left) / 2}`
          )
          .attr("y1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr("transform", `translate(20,${this.margin.top})`);
        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr("x", (this.width - this.margin.right) / 6 + this.margin.left)
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-size", "1em")
          .text("بیشترین ورود حقیقی");

        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr(
            "x",
            ((this.width - this.margin.right) * 4) / 6 + this.margin.left
          )
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-size", "1em")
          .text("بیشترین خروج حقیقی");

        // eslint-disable-next-line no-unused-vars
        const tooltip = d3
          .select(parent)
          .append("div")
          .attr("class", "d3-tip")
          .style("position", "absolute")
          .style("visibility", "hidden")
          .style("left", this.width / 3 + "px")
          .style("top", this.height / 3 + "px");
        const tooltip2 = d3
          .select(parent)
          .append("div")
          .attr("class", "d3-tip")
          .style("position", "absolute")
          .style("visibility", "hidden")
          .style("left", (this.width * 7) / 12 + "px")
          .style("top", this.height / 3 + "px");
        // eslint-disable-next-line no-unused-vars
        let that = this;
        chart
          .selectAll()
          .data(this.highestVolumes)
          .enter()
          .append("rect")
          .attr("x", d => xRight(d.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mouseenter touchstart", function(event, d) {
            tooltip2
              .html(
                "نماد: " +
                  d.ticker +
                  "<hr/>" +
                  " ارزش معاملات: " +
                  that.numberWithCommas(
                    that.roundTo(d.TradeValue / 1000000000, 0)
                  ) +
                  "میلیارد ریال " +
                  "<br>" +
                  " حجم معاملات: " +
                  that.numberWithCommas(
                    that.roundTo(d.TradeVolume / 1000000, 0)
                  ) +
                  "میلیون " +
                  "<br>" +
                  "خروج حقیقی: " +
                  that.numberWithCommas(
                    that.roundTo((d.netHaghighi * -1) / 1000000000, 0)
                  ) +
                  "میلیارد ریال " +
                  "<br>" +
                  "صنعت:" +
                  d.industry
              )
              .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 0.5);
          })
          .on("mouseleave touchend", function() {
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            tooltip2.style("visibility", "hidden");
          })
          .transition()
          .duration(2000)
          .ease(d3.easePolyOut)
          .attr("y", function(d) {
            return yRight(d.netHaghighi);
          })
          .attr("height", s =>
            Math.max(
              yRight(0) - yRight(s.netHaghighi),
              yRight(s.netHaghighi) - yRight(0)
            )
          )
          .attr("width", xRight.bandwidth())
          .attr("fill", function(d) {
            return mycolor2(d.netHaghighi);
          });
        chart
          .selectAll()
          .data(this.highestValues)
          .enter()
          .append("rect")
          .attr("x", s => xLeft(s.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mouseenter touchstart", function(event, d) {
            tooltip
              .html(
                "نماد: " +
                  d.ticker +
                  "<hr/>" +
                  " ارزش معاملات: " +
                  that.numberWithCommas(
                    that.roundTo(d.TradeValue / 1000000000, 0)
                  ) +
                  "میلیارد ریال " +
                  "<br>" +
                  " حجم معاملات: " +
                  that.numberWithCommas(
                    that.roundTo(d.TradeVolume / 1000000, 0)
                  ) +
                  "میلیون " +
                  "<br>" +
                  "ورود حقیقی: " +
                  that.numberWithCommas(
                    that.roundTo(d.netHaghighi / 1000000000, 0)
                  ) +
                  "میلیارد ریال " +
                  "<br>" +
                  "صنعت:" +
                  d.industry
              )
              .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 0.5);
          })
          .on("mouseleave touchend", function() {
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            tooltip.style("visibility", "hidden");
          })
          .transition()
          .duration(2000)
          .ease(d3.easePolyOut)
          .attr("y", function(d) {
            return yLeft(d.netHaghighi);
          })
          .attr("height", s =>
            Math.max(
              yLeft(0) - yLeft(s.netHaghighi),
              yLeft(s.netHaghighi) - yLeft(0)
            )
          )
          .attr("width", xLeft.bandwidth())
          .attr("fill", function(d) {
            return mycolor(d.netHaghighi);
          })
          .style("opacity", "80%");
      }
      if (this.SortBy1 == "DS") {
        // console.log(this.highestImpcats);
        const xLeft_2 = d3
          .scaleBand()
          .domain(this.highestImpcats.map(x => x.ticker))
          .range([0, (this.width - this.margin.right) / 2])
          .padding(0.15);

        const yLeft_2 = d3
          .scaleLinear()
          .domain([
            0,
            Math.abs(
              Math.max(
                Math.max(
                  ...this.highestImpcats.map(x => {
                    if (x.Value > 0) {
                      return x.Value;
                    } else {
                      return x.Value * -1;
                    }
                  })
                ),
                Math.max(
                  ...this.lowestImpcats.map(x => {
                    if (x.Value > 0) {
                      return x.Value;
                    } else {
                      return x.Value * -1;
                    }
                  })
                )
              ) * 1.2
            )
          ])
          .range([this.height - this.margin.bottom, this.margin.top])
          .nice();
        // eslint-disable-next-line no-unused-vars
        const xRight_2 = d3
          .scaleBand()
          .domain(this.lowestImpcats.map(x => x.ticker))
          .range([this.width, (this.width - this.margin.right) / 2])
          .padding(0.15);

        // eslint-disable-next-line no-unused-vars
        const yRight_2 = d3
          .scaleLinear()
          .domain([
            0,
            Math.abs(
              Math.max(
                Math.max(
                  ...this.highestImpcats.map(x => {
                    if (x.Value > 0) {
                      return x.Value;
                    } else {
                      return x.Value * -1;
                    }
                  })
                ),
                Math.max(
                  ...this.lowestImpcats.map(x => {
                    if (x.Value > 0) {
                      return x.Value;
                    } else {
                      return x.Value * -1;
                    }
                  })
                )
              ) * 1.2
            )
          ])
          .range([this.height - this.margin.bottom, this.margin.top])
          .nice();
        ///////////////
        var mycolor_2 = d3
          .scaleLinear()
          .domain([0, Math.max(...this.highestImpcats.map(x => x.Value)) * 1.2])
          .range(["#66BB6A", "#1B5E20"]);
        var mycolor2_2 = d3
          .scaleLinear()
          .domain([0, Math.max(...this.lowestImpcats.map(x => x.Value)) * 1.2])
          .range(["#a01a58", "#b7094c"]);
        //////////////
        let aXisY2_2 = d3
          .axisLeft(yLeft_2)
          .tickFormat(d => {
            if (d <= 0) {
              return d;
            } else {
              return (
                this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                "  " +
                "میلیارد ریال"
              );
            }
          })
          .tickSizeInner(-this.width / 2 + this.margin.left / 2);
        let aXisY2Axe_2 = chart.append("g").call(aXisY2_2);
        aXisY2Axe_2
          .selectAll("text")
          .style("text-anchor", "start")
          .style("font-size", `${this.width / 1000}em`)
          .style("font-family", "Dirooz FD")
          .style("font-weight", "800");
        aXisY2Axe_2
          .selectAll(".tick line")
          .attr("stroke", "#b0a8b9")
          .style("opacity", "0.2")
          .style("font-family", "Dirooz FD")
          .style("font-weight", "800");
        chart
          .append("g")
          .call(d3.axisBottom(xLeft_2))
          .attr("transform", `translate(0,${this.height - this.margin.bottom})`)
          .selectAll("text")
          .style("Visibility", "hidden");

        ////////////////
        let aXisY1_2 = d3
          .axisRight(yRight_2)
          .tickFormat(d => {
            if (d <= 0) {
              return d;
            } else {
              return (
                this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                "  " +
                "میلیارد ریال"
              );
            }
          })
          .tickSizeInner(-this.width / 2 - this.margin.right / 2);
        var aXisY1Axe_2 = chart
          .append("g")
          .call(aXisY1_2)
          .attr("transform", `translate(${this.width},0)`);

        aXisY1Axe_2
          .selectAll("text")
          .style("text-anchor", "end")
          .style("font-size", `${this.width / 1000}em`)
          .style("font-family", "Dirooz FD")
          .style("font-weight", "800");
        aXisY1Axe_2
          .selectAll(".tick line")
          .attr("stroke", "#b0a8b9")
          .style("opacity", "0.2");

        chart
          .append("g")
          .call(d3.axisBottom(xRight_2))
          .attr("transform", `translate(0,${this.height - this.margin.bottom})`)
          .selectAll("text")
          .style("Visibility", "hidden");

        chart
          .selectAll("text.bar")
          .data(this.highestImpcats)
          .enter()
          .append("text")
          .attr("class", "yAxis-label")
          .attr("text-anchor", "middle")
          .attr("fill", "#70747a")
          .style("font-size", `${this.width / 950}em`)
          .attr("x", d => xLeft_2(d.ticker) + xLeft_2.bandwidth() * 0.5)
          .attr("y", d => {
            return yLeft_2(d["Value"]) - 0.05 * this.height;
          })
          .text(d => d.ticker)
          .attr("transform", function() {
            var me = this;
            var x1 = me.getBBox().x + me.getBBox().width / 2; //the center x about which you want to rotate
            var y1 = me.getBBox().y + me.getBBox().height / 2; //the center y about which you want to rotate

            return `rotate(-90, ${x1}, ${y1})`; //rotate 180 degrees about x and y
          });
        chart
          .selectAll("text.bar")
          .data(this.lowestImpcats)
          .enter()
          .append("text")
          .attr("class", "yAxis-label")
          .attr("text-anchor", "middle")
          .attr("fill", "#70747a")
          .style("font-size", `${this.width / 950}em`)
          .attr("x", d => xRight_2(d.ticker) + xRight_2.bandwidth() * 0.5)
          .attr("y", d => {
            return yRight_2(d["Value"]) - 0.05 * this.height;
          })
          .text(d => d.ticker)
          .attr("transform", function() {
            var me = this;
            var x1 = me.getBBox().x + me.getBBox().width / 2; //the center x about which you want to rotate
            var y1 = me.getBBox().y + me.getBBox().height / 2; //the center y about which you want to rotate

            return `rotate(-90, ${x1}, ${y1})`; //rotate 180 degrees about x and y
          });

        chart
          .append("line")
          .style("stroke", "black")
          .attr("x1", xRight_2(0))
          // eslint-disable-next-line no-unused-vars
          .attr("y1", `${this.height - this.margin.bottom}`)
          .attr("x2", xRight_2(0))
          .attr("y2", `${this.margin.top}`)
          // eslint-disable-next-line no-unused-vars
          .attr(
            "transform",
            `translate(${(this.width - this.margin.right) / 2},0)`
          );
        chart
          .append("line")
          .style("stroke", "steelblue")
          .attr("x1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr("y1", 0)
          .attr(
            "x2",
            `${(this.width - this.margin.right - this.margin.left) / 2}`
          )
          .attr("y1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr(
            "transform",
            `translate(${(this.width - this.margin.right) / 2 + 20},${
              this.margin.top
            })`
          );
        chart
          .append("line")
          .style("stroke", "steelblue")
          .attr("x1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr("y1", 0)
          .attr(
            "x2",
            `${(this.width - this.margin.right - this.margin.left) / 2}`
          )
          .attr("y1", 0)
          // eslint-disable-next-line no-unused-vars
          .attr("transform", `translate(20,${this.margin.top})`);
        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr("x", (this.width - this.margin.right) / 6 + this.margin.left)
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-size", "1em")
          .text("بیشترین تقاضا ");

        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr(
            "x",
            ((this.width - this.margin.right) * 4) / 6 + this.margin.left
          )
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-size", "1em")
          .text("بیشترین عرضه ");

        // eslint-disable-next-line no-unused-vars
        const tooltip = d3
          .select(parent)
          .append("div")
          .attr("class", "d3-tip")
          .style("position", "absolute")
          .style("visibility", "hidden")
          .style("left", this.width / 3 + "px")
          .style("top", this.height / 3 + "px");
        const tooltip2 = d3
          .select(parent)
          .append("div")
          .attr("class", "d3-tip")
          .style("position", "absolute")
          .style("visibility", "hidden")
          .style("left", (this.width * 7) / 12 + "px")
          .style("top", this.height / 3 + "px");
        // eslint-disable-next-line no-unused-vars
        let that = this;
        chart
          .selectAll()
          .data(this.lowestImpcats)
          .enter()
          .append("rect")
          .attr("x", d => xRight_2(d.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mouseenter touchstart", function(event, d) {
            tooltip2
              .html(
                "نماد: " +
                  d.ticker +
                  "<hr/>" +
                  " ارزش معاملات: " +
                  that.numberWithCommas(that.roundTo(d.Value / 1000000000, 0)) +
                  "میلیارد ریال " +
                  "<br>" +
                  " حجم معاملات: " +
                  that.numberWithCommas(that.roundTo(d.Vol / 1000000, 0)) +
                  "میلیون " +
                  "<br>" +
                  "قیمت: " +
                  that.numberWithCommas(that.roundTo(d.Price, 0)) +
                  "<br>"
              )
              .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 0.5);
          })
          .on("mouseleave touchend", function() {
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            tooltip2.style("visibility", "hidden");
          })
          .transition()
          .duration(2000)
          .ease(d3.easePolyOut)
          .attr("y", function(d) {
            return yRight_2(d.Value);
          })
          .attr("height", s =>
            Math.max(
              yRight_2(0) - yRight_2(s.Value),
              yRight_2(s.Value) - yRight_2(0)
            )
          )
          .attr("width", xRight_2.bandwidth())
          .attr("fill", function(d) {
            return mycolor2_2(d.Value);
          });
        chart
          .selectAll()
          .data(this.highestImpcats)
          .enter()
          .append("rect")
          .attr("x", s => xLeft_2(s.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mouseenter touchstart", function(event, d) {
            tooltip
              .html(
                "نماد: " +
                  d.ticker +
                  "<hr/>" +
                  " ارزش معاملات: " +
                  that.numberWithCommas(that.roundTo(d.Value / 1000000000, 0)) +
                  "میلیارد ریال " +
                  "<br>" +
                  " حجم معاملات: " +
                  that.numberWithCommas(that.roundTo(d.Vol / 1000000, 0)) +
                  "میلیون " +
                  "<br>" +
                  "قیمت: " +
                  that.numberWithCommas(that.roundTo(d.Price, 0)) +
                  "<br>"
              )
              .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 0.5);
          })
          .on("mouseleave touchend", function() {
            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            tooltip.style("visibility", "hidden");
          })
          .transition()
          .duration(2000)
          .ease(d3.easePolyOut)
          .attr("y", function(d) {
            return yLeft_2(d.Value);
          })
          .attr("height", s =>
            Math.max(
              yLeft_2(0) - yLeft_2(s.Value),
              yLeft_2(s.Value) - yLeft_2(0)
            )
          )
          .attr("width", xLeft_2.bandwidth())
          .attr("fill", function(d) {
            return mycolor_2(d.Value);
          })
          .style("opacity", "80%");
      }
    }
  }
};
</script>

<style scoped>
.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}
.yaxis text {
  padding-right: 10px;
}
.Chart1title * {
  font-size: 1.2em;
  font-family: "Dirooz FD";
}
.cellItem {
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
  background-color: white;
  border-radius: 4px;
  opacity: 80%;
}

/* Creates a small triangle extender for the tooltip */
.d3-tip:after {
  box-sizing: border-box;
  display: inline;
  font-size: 10px;
  width: 100%;
  line-height: 1;
  color: rgb(139, 129, 129);
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
