<template>
  <!-- <div class="card card-custom"> -->
  <!-- <v-skeleton-loader
      type=" table-heading,table-row@12"
      v-if="loading"
    ></v-skeleton-loader> -->
  <v-card rounded="lg">
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em"
        >نمودار وضعیت بازار</v-toolbar-title
      >
      <v-spacer></v-spacer>
      <v-radio-group
        class="mt-5"
        row
        v-model="SortBy1"
        mandatory
        @change="renderChart1()"
      >
        <v-radio
          class="radioBTN"
          label="بیشترین ورود و خروج حقیقی"
          value="HH"
        ></v-radio>
        <v-radio
          class="radioBTN"
          label="بیشترین عرضه تقاضای لحظه ای"
          value="DS"
        ></v-radio>
      </v-radio-group>
    </v-toolbar>
    <!-- // ? TOOLTIP PLACEMENT ************************** -->
    <div
      :style="tooltipPosition"
      v-if="LeaveHHTooltip || EnterHHTooltip"
      class="D3TestTooltip"
    >
      <div class="D3TestTopDivTooltip">
        <span>
          {{ tooltipData.ticker }}
        </span>
      </div>
      <div class="D3TestMiddleDivTooltip">
        <span style="color:#000;font-size:0.8em" class="mr-1"
          >میلیارد ریال</span
        >
        <span style="color:#000;font-size:0.8em" class="mr-1">{{
          numberWithCommas(roundTo(tooltipData.TradeValue / 1000000000, 0))
        }}</span>
        <span style="color:#000;font-size:0.8em" dir="rtl">ارزش معاملات:</span>
      </div>
      <div class="D3TestMiddleDivTooltip">
        <span style="color:#000;font-size:0.8em" class="mr-1">میلیون</span>
        <span style="color:#000;font-size:0.8em" class="mr-1">{{
          numberWithCommas(roundTo(tooltipData.TradeVolume / 1000000, 0))
        }}</span>
        <span style="color:#000;font-size:0.8em" dir="rtl">حجم معاملات:</span>
      </div>
      <div class="D3TestMiddleDivTooltip">
        <span style="color:#000;font-size:0.8em" class="mr-1"
          >میلیارد ریال</span
        >
        <span
          v-if="EnterHHTooltip"
          style="color:#000;font-size:0.8em"
          class="mr-1"
          >{{
            numberWithCommas(roundTo(tooltipData.netHaghighi / 1000000000, 0))
          }}</span
        >
        <span v-else style="color:#000;font-size:0.8em" class="mr-1">{{
          numberWithCommas(
            roundTo((tooltipData.netHaghighi * -1) / 1000000000, 0)
          )
        }}</span>
        <span v-if="EnterHHTooltip" style="color:#000;font-size:0.8em" dir="rtl"
          >ورود حقیقی:</span
        >

        <span v-else style="color:#000;font-size:0.8em" dir="rtl"
          >خروج حقیقی:</span
        >
      </div>
      <div class="D3TestBottomDivTooltip">
        <span style="color:#000;font-size:0.8em" class="mr-1">{{
          tooltipData.industry
        }}</span>
        <span style="color:#000;font-size:0.8em" dir="rtl">صنعت:</span>
      </div>
    </div>
    <div
      :style="tooltipPosition"
      v-if="HighestImpactTooltip || LowestImpactTooltip"
      class="D3TestTooltip"
    >
      <div class="D3TestTopDivTooltip">
        <span>
          {{ tooltipData.ticker }}
        </span>
      </div>
      <div class="D3TestMiddleDivTooltip">
        <span style="color:#000;font-size:0.8em" class="mr-1"
          >میلیارد ریال</span
        >
        <span style="color:#000;font-size:0.8em" class="mr-1">{{
          numberWithCommas(roundTo(tooltipData.Value / 1000000000, 0))
        }}</span>
        <span style="color:#000;font-size:0.8em" dir="rtl">ارزش معاملات:</span>
      </div>
      <div class="D3TestMiddleDivTooltip">
        <span style="color:#000;font-size:0.8em" class="mr-1">میلیون</span>
        <span style="color:#000;font-size:0.8em" class="mr-1">{{
          numberWithCommas(roundTo(tooltipData.Vol / 1000000, 0))
        }}</span>
        <span style="color:#000;font-size:0.8em" dir="rtl">حجم معاملات:</span>
      </div>

      <div class="D3TestBottomDivTooltip">
        <span style="color:#000;font-size:0.8em" class="mr-1">{{
          tooltipData.Price.toLocaleString()
        }}</span>
        <span style="color:#000;font-size:0.8em" dir="rtl">قیمت:</span>
      </div>
    </div>
    <div id="ChartContainer_HH"></div>
  </v-card>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "ChartHH",
  props: { inputDataHH: Array, inputDataQ: Array },
  data() {
    return {
      //? tooltip
      tooltipData: {},
      LeaveHHTooltip: false,
      EnterHHTooltip: false,
      HighestImpactTooltip: false,
      LowestImpactTooltip: false,
      pageX: null,
      pageY: null,
      //********* */
      jsonData: [],
      jsonData2: [],
      loading: true,
      fontsizeOf: 1,
      datasizeOf: 10,
      shortenNames: false,
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
  computed: {
    tooltipPosition() {
      let res = {};
      if (this.LeaveHHTooltip)
        res = {
          right: this.width - this.pageX + 100 + "px",
          bottom: this.height - this.pageY + 40 + "px"
        };
      else if (this.LowestImpactTooltip)
        res = {
          right: this.width - this.pageX + 100 + "px",
          bottom: this.height - this.pageY + 40 + "px"
        };
      else if (this.HighestImpactTooltip) {
        res = {
          right: this.width - this.pageX - 150 + "px",
          bottom: this.height - this.pageY + 40 + "px"
        };
      } else {
        res = {
          right: this.width - this.pageX - 150 + "px",
          bottom: this.height - this.pageY + 40 + "px"
        };
      }
      return res;
    }
  },
  mounted() {
    this.initrender();
    ////this.renderData1();
    ////this.initrender();
    ////if (this.isRealValue(this.highestValues)) {
    ////  this.renderChart1();
    ////}
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
        this.highestValues = this.jsonData.slice(0, this.datasizeOf);
        this.jsonData.sort((a, b) => a.netHaghighi - b.netHaghighi);
        this.highestVolumes = this.jsonData.slice(0, this.datasizeOf);
      }
      if (!(this.inputDataQ === undefined || this.inputDataQ.length == 0)) {
        this.jsonData2 = [...this.inputDataQ[1]];
        this.jsonData2.sort((a, b) => b.Value - a.Value);
        this.highestImpcats = this.jsonData2.slice(0, this.datasizeOf);

        this.jsonData3 = [...this.inputDataQ[0]];
        this.jsonData3.sort((a, b) => b.Value - a.Value);
        this.lowestImpcats = this.jsonData3.slice(0, this.datasizeOf);
      }
    },
    initrender() {
      if (document.getElementById("ChartContainer_HH_svg")) {
        d3.selectAll("#ChartContainer_HH_svg").remove();
      }

      this.width =
        0.85 * parseInt(d3.select("#ChartContainer_HH").style("width"), 10);
      this.height = (this.width * 6) / 16;
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
      if (parseInt(d3.select("#ChartContainer_HH").style("width"), 10) > 1000) {
        this.fontsizeOf = 1.1;
        this.datasizeOf = 10;
        this.shortenNames = false;
      }
      if (
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) > 800 &&
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) < 1000
      ) {
        this.fontsizeOf = 0.9;
        this.datasizeOf = 8;
        this.shortenNames = true;
      }
      if (
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) > 600 &&
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) < 800
      ) {
        this.fontsizeOf = 0.9;
        this.datasizeOf = 5;
        this.shortenNames = true;
      }
      if (
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) > 400 &&
        parseInt(d3.select("#ChartContainer_HH").style("width"), 10) < 600
      ) {
        this.fontsizeOf = 0.9;
        this.width =
          0.7 * parseInt(d3.select("#ChartContainer_HH").style("width"), 10);
        this.height = (this.width * 16) / 16;
        this.margin.top = this.height * 0.08;
        this.margin.bottom = this.height * 0.05;
        this.margin.right =
          parseInt(d3.select("#ChartContainer_HH").style("width"), 10) * 0.15;
        this.margin.left =
          parseInt(d3.select("#ChartContainer_HH").style("width"), 10) * 0.15;
        this.datasizeOf = 5;
        this.shortenNames = true;
      }
      if (parseInt(d3.select("#ChartContainer_HH").style("width"), 10) < 400) {
        this.fontsizeOf = 0.8;
        this.width =
          0.7 * parseInt(d3.select("#ChartContainer_HH").style("width"), 10);
        this.height = (this.width * 16) / 16;
        this.margin.top = this.height * 0.08;
        this.margin.bottom = this.height * 0.05;
        this.margin.right =
          parseInt(d3.select("#ChartContainer_HH").style("width"), 10) * 0.15;
        this.margin.left =
          parseInt(d3.select("#ChartContainer_HH").style("width"), 10) * 0.15;
        this.datasizeOf = 5;
        this.shortenNames = true;
      }
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
        .attr("preserveAspectRatio", "xMidYMid meet")
        .style(
          "background",
          "url(../../media/logos/fadedfinwise.png) no-repeat center "
        );

      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );

      if (this.SortBy1 == "HH") {
        const xLeft = d3
          .scaleBand()
          .domain(this.highestValues.map(x => x.ticker))
          .range([0, this.width / 2])
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
          ////.domain([
          ////  0,
          ////  Math.max(...this.highestValues.map(x => x.netHaghighi)) * 1.2
          ////])
          .range([this.height - this.margin.bottom, 0])
          .nice();

        const xRight = d3
          .scaleBand()
          .domain(this.highestVolumes.map(x => x.ticker))
          .range([this.width, this.width / 2])
          .padding(0.15);

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
          .range([this.height - this.margin.bottom, 0])
          .nice();
        ///////////////
        var EnterHHColor = d3
          .scaleLinear()
          .domain([
            0,
            Math.max(...this.highestValues.map(x => x.netHaghighi)) * 1.2
          ])
          .range(["#00CC18", "#00ad13"]);
        var LeaveHHColor = d3
          .scaleLinear()
          .domain([
            0,
            Math.min(...this.highestVolumes.map(x => x.netHaghighi)) * 1.2
          ])
          .range(["#F50800", "#DC0600"]);
        //////////////
        let aXisY2 = d3
          .axisLeft(yLeft)
          .tickFormat(d => {
            if (d <= 0) {
              return d;
            } else {
              if (this.shortenNames) {
                return (
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                  "  " +
                  "B Rial"
                );
              } else {
                return (
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                  "  " +
                  "میلیارد ریال"
                );
              }
            }
          })
          .tickSizeInner(-this.width / 2 + this.margin.left / 2);
        let aXisY2Axe = chart.append("g").call(aXisY2);
        aXisY2Axe
          .selectAll("text")
          .style("text-anchor", "start")
          .attr("transform", `translate(0,0)`)
          ////.attr("dx", "-8em")
          ////.style("font-size", `${this.width / 1000}em`)
          .style("font-size", `${this.fontsizeOf}em`)
          .style("font-family", "Vazir-Light-FD")
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
              if (this.shortenNames) {
                return (
                  "B Rial" +
                  " " +
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0))
                );
              } else {
                return (
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                  "  " +
                  "میلیارد ریال"
                );
              }
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
          ////.style("font-size", `${this.width / 1000}em`)
          .style("font-size", `${this.fontsizeOf}em`)
          .style("font-family", "Vazir-Light-FD")
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
          .attr("class", "HH_Q_Chart-yAxis-label")
          .attr("text-anchor", "middle")
          .attr("dy", "-3px")
          .attr("fill", "#000")
          .style("font-weight", `500`)
          .style("font-size", `0.85em`)
          .attr("x", d => xLeft(d.ticker) + xLeft.bandwidth() * 0.5)
          .attr("y", d => {
            return yLeft(d["netHaghighi"]) - 0.05 * this.height;
          })
          .html(d => {
            if (d.Type == "سهم بورس" || d.Type == "سهم فرابورس") {
              return (
                '<a href="/ticker/Overview/Overall/' +
                d.ID +
                '">' +
                d.ticker +
                "</a>"
              );
            } else {
              return d.ticker;
            }
          })
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
          .attr("class", "HH_Q_Chart-yAxis-label")
          .attr("text-anchor", "middle")
          .attr("dy", "-3px")
          .attr("fill", "#000")
          .style("font-weight", `500`)
          .style("font-size", `0.85em`)
          .attr("x", d => xRight(d.ticker) + xRight.bandwidth() * 0.5)
          .attr("y", d => {
            return yRight(d["netHaghighi"]) - 0.05 * this.height;
          })
          .html(d => {
            if (d.Type == "سهم بورس" || d.Type == "سهم فرابورس") {
              return (
                '<a href="/ticker/Overview/Overall/' +
                d.ID +
                '">' +
                d.ticker +
                "</a>"
              );
            } else {
              return d.ticker;
            }
          })
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

          .attr("y1", `${this.height - this.margin.bottom}`)
          .attr("x2", xRight(0))
          .attr("y2", `0`)

          .attr("transform", `translate(${this.width / 2},0)`);
        ////chart
        ////  .append("line")
        ////  .style("stroke", "steelblue")
        ////  .attr("x1", 0)

        ////  .attr("y1", 0)
        ////  .attr("x2", `${this.width / 2}`)
        ////  .attr("y1", 0)

        ////  .attr("transform", `translate(${this.width / 2},${0})`);
        ////chart
        ////  .append("line")
        ////  .style("stroke", "steelblue")
        ////  .attr("x1", 0)

        ////  .attr("y1", 0)
        ////  .attr("x2", `${this.width / 2}`)
        ////  .attr("y1", 0);

        ////.attr("transform", `translate(0,${this.margin.top})`);
        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr("x", this.width * 0.25)
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-family", "Vazir-Light-FD")
          .style("font-size", `${this.fontsizeOf}em`)
          .text("بیشترین ورود حقیقی");

        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr("x", this.width * 0.75)
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-family", "Vazir-Light-FD")
          .style("font-size", `${this.fontsizeOf}em`)
          .text("بیشترین خروج حقیقی");

        ////const tooltip = d3
        ////// .select(parent)
        ////  .append("div")
        ////  .attr("class", "d3-tip")
        ////  .style("position", "absolute")
        ////  .style("visibility", "hidden")
        ////  .style("left", this.width / 3 + "px")
        ////  .style("top", this.height / 3 + "px");
        ////const tooltip2 = d3
        ////  .select(parent)
        ////  .append("div")
        ////  .attr("class", "d3-tip")
        ////  .style("position", "absolute")
        ////  .style("visibility", "hidden")
        ////  .style("left", (this.width * 7) / 12 + "px")
        ////  .style("top", this.height / 3 + "px");

        let that = this;
        chart
          .selectAll()
          .data(this.highestVolumes)
          .enter()
          .append("rect")
          .attr("x", d => xRight(d.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mousemove touchstart", function(event, d) {
            that.tooltipData = d;
            that.LeaveHHTooltip = true;
            let coordinates = d3.pointer(event);
            that.pageX = coordinates[0];
            that.pageY = coordinates[1];
            ////tooltip2
            ////  .html(
            ////    "نماد: " +
            ////      d.ticker +
            ////      "<hr/>" +
            ////      " ارزش معاملات: " +
            ////      that.numberWithCommas(
            ////        that.roundTo(d.TradeValue / 1000000000, 0)
            ////      ) +
            ////      "میلیارد ریال " +
            ////      "<br>" +
            ////      " حجم معاملات: " +
            ////      that.numberWithCommas(
            ////        that.roundTo(d.TradeVolume / 1000000, 0)
            ////      ) +
            ////      "میلیون " +
            ////      "<br>" +
            ////      "خروج حقیقی: " +
            ////      that.numberWithCommas(
            ////        that.roundTo((d.netHaghighi * -1) / 1000000000, 0)
            ////      ) +
            ////      "میلیارد ریال " +
            ////      "<br>" +
            ////      "صنعت:" +
            ////      d.industry
            ////  )
            ////  .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(20)
              .style("opacity", 0.7);
          })
          .on("mouseleave touchend", function() {
            that.LeaveHHTooltip = false;

            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            ////tooltip2.style("visibility", "hidden");
          })
          .transition()
          .duration(700)
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
            return LeaveHHColor(d.netHaghighi);
          })
          .attr("stroke", "#3e3e4e");
        chart
          .selectAll()
          .data(this.highestValues)
          .enter()
          .append("rect")
          .attr("x", s => xLeft(s.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mousemove touchstart", function(event, d) {
            that.tooltipData = d;
            that.EnterHHTooltip = true;
            let coordinates = d3.pointer(event);
            that.pageX = coordinates[0];
            that.pageY = coordinates[1];
            ////tooltip
            ////  .html(
            ////    "نماد: " +
            ////      d.ticker +
            ////      "<hr/>" +
            ////      " ارزش معاملات: " +
            ////      that.numberWithCommas(
            ////        that.roundTo(d.TradeValue / 1000000000, 0)
            ////      ) +
            ////      "میلیارد ریال " +
            ////      "<br>" +
            ////      " حجم معاملات: " +
            ////      that.numberWithCommas(
            ////        that.roundTo(d.TradeVolume / 1000000, 0)
            ////      ) +
            ////      "میلیون " +
            ////      "<br>" +
            ////      "ورود حقیقی: " +
            ////      that.numberWithCommas(
            ////        that.roundTo(d.netHaghighi / 1000000000, 0)
            ////      ) +
            ////      "میلیارد ریال " +
            ////      "<br>" +
            ////      "صنعت:" +
            ////      d.industry
            ////  )
            ////  .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(20)
              .style("opacity", 0.7);
          })
          .on("mouseleave touchend", function() {
            that.EnterHHTooltip = false;

            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            ////tooltip.style("visibility", "hidden");
          })
          .transition()
          .duration(700)
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
            return EnterHHColor(d.netHaghighi);
          })
          .attr("stroke", "#3e3e4e");
        ////.style("opacity", "80%");
      }
      if (this.SortBy1 == "DS") {
        const xLeft_2 = d3
          .scaleBand()
          .domain(this.highestImpcats.map(x => x.ticker))
          .range([0, this.width / 2])
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
          .range([this.height - this.margin.bottom, 0])
          .nice();

        const xRight_2 = d3
          .scaleBand()
          .domain(this.lowestImpcats.map(x => x.ticker))
          .range([this.width, this.width / 2])
          .padding(0.15);

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
          .range([this.height - this.margin.bottom, 0])
          .nice();
        ///////////////
        var HighestImpactColor = d3
          .scaleLinear()
          .domain([0, Math.max(...this.highestImpcats.map(x => x.Value)) * 1.2])
          .range(["#00CC18", "#00ad13"]);
        var LowestImpactColor = d3
          .scaleLinear()
          .domain([0, Math.max(...this.lowestImpcats.map(x => x.Value)) * 1.2])
          .range(["#F50800", "#DC0600"]);
        //////////////
        let aXisY2_2 = d3
          .axisLeft(yLeft_2)
          .tickFormat(d => {
            if (d <= 0) {
              return d;
            } else {
              if (this.shortenNames) {
                return (
                  "B Rial" +
                  " " +
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0))
                );
              } else {
                return (
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                  "  " +
                  "میلیارد ریال"
                );
              }
            }
          })
          .tickSizeInner(-this.width / 2 + this.margin.left / 2);
        let aXisY2Axe_2 = chart.append("g").call(aXisY2_2);
        aXisY2Axe_2
          .selectAll("text")
          .style("text-anchor", "start")
          ////.style("font-size", `${this.width / 1000}em`)
          .style("font-size", `${this.fontsizeOf}em`)
          .style("font-family", "Vazir-Light-FD")
          .style("font-weight", "800");
        aXisY2Axe_2
          .selectAll(".tick line")
          .attr("stroke", "#b0a8b9")
          .style("opacity", "0.2")
          .style("font-family", "Vazir-Light-FD")
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
              if (this.shortenNames) {
                return (
                  "B Rial" +
                  " " +
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0))
                );
              } else {
                return (
                  this.numberWithCommas(this.roundTo(d / 1000000000, 0)) +
                  "  " +
                  "میلیارد ریال"
                );
              }
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
          ////.style("font-size", `${this.width / 1000}em`)
          .style("font-size", `${this.fontsizeOf}em`)
          .style("font-family", "Vazir-Light-FD")
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
          .attr("class", "HH_Q_Chart-yAxis-label")
          .attr("text-anchor", "middle")
          .attr("dy", "-3px")
          .attr("fill", "#000")
          .style("font-weight", `500`)
          .style("font-size", `0.85em`)
          .attr("x", d => xLeft_2(d.ticker) + xLeft_2.bandwidth() * 0.5)
          .attr("y", d => {
            return yLeft_2(d["Value"]) - 0.05 * this.height;
          })
          .html(d => {
            if (d.Type == "stock") {
              return (
                '<a href="/ticker/Overview/Overall/' +
                d.ID +
                '">' +
                d.ticker +
                "</a>"
              );
            } else {
              return d.ticker;
            }
          })
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
          .attr("class", "HH_Q_Chart-yAxis-label")
          .attr("text-anchor", "middle")
          .attr("dy", "-3px")

          .attr("fill", "#000")
          .style("font-weight", `500`)
          .style("font-size", `0.85em`)
          .attr("x", d => xRight_2(d.ticker) + xRight_2.bandwidth() * 0.5)
          .attr("y", d => {
            return yRight_2(d["Value"]) - 0.05 * this.height;
          })
          .html(d => {
            if (d.Type == "stock") {
              return (
                '<a href="/ticker/Overview/Overall/' +
                d.ID +
                '">' +
                d.ticker +
                "</a>"
              );
            } else {
              return d.ticker;
            }
          })
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

          .attr("y1", `${this.height - this.margin.bottom}`)
          .attr("x2", xRight_2(0))
          .attr("y2", `${0}`)

          .attr("transform", `translate(${this.width / 2},0)`);
        ////chart
        ////  .append("line")
        ////  .style("stroke", "steelblue")
        ////  .attr("x1", 0)

        ////  .attr("y1", 0)
        ////  .attr("x2", `${this.width / 2}`)
        ////  .attr("y1", 0)

        ////  .attr("transform", `translate(${this.width / 2},${0})`);
        ////chart
        ////  .append("line")
        ////  .style("stroke", "steelblue")
        ////  .attr("x1", 0)

        ////  .attr("y1", 0)
        ////  .attr("x2", `${this.width / 2}`)
        ////  .attr("y1", 0)

        ////  .attr("transform", `translate(0,${0})`);
        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr("x", this.width * 0.25)
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-family", "Vazir-Light-FD")
          .style("font-size", `${this.fontsizeOf}em`)
          .text("بیشترین تقاضا");

        chart
          .append("text")
          .attr("class", "Chart1title")
          .attr("x", this.width * 0.75)
          .attr("y", (this.margin.top * 3) / 4)
          .attr("text-anchor", "middle")
          .style("font-family", "Vazir-Light-FD")
          .style("font-size", `${this.fontsizeOf}em`)
          .text("بیشترین عرضه");

        ////const tooltip = d3
        ////  .select(parent)
        ////  .append("div")
        ////  .attr("class", "d3-tip")
        ////  .style("position", "absolute")
        ////  .style("visibility", "hidden")
        ////  .style("left", this.width / 3 + "px")
        ////  .style("top", this.height / 3 + "px");
        ////const tooltip2 = d3
        ////  .select(parent)
        ////  .append("div")
        ////  .attr("class", "d3-tip")
        ////  .style("position", "absolute")
        ////  .style("visibility", "hidden")
        ////  .style("left", (this.width * 7) / 12 + "px")
        ////  .style("top", this.height / 3 + "px");

        let that = this;
        chart
          .selectAll()
          .data(this.lowestImpcats)
          .enter()
          .append("rect")
          .attr("x", d => xRight_2(d.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mousemove touchstart", function(event, d) {
            that.tooltipData = d;
            that.LowestImpactTooltip = true;
            let coordinates = d3.pointer(event);
            that.pageX = coordinates[0];
            that.pageY = coordinates[1];
            ////tooltip2
            ////  .html(
            ////    "نماد: " +
            ////      d.ticker +
            ////      "<hr/>" +
            ////      " ارزش معاملات: " +
            ////      that.numberWithCommas(that.roundTo(d.Value / 1000000000, 0)) +
            ////      "میلیارد ریال " +
            ////      "<br>" +
            ////      " حجم معاملات: " +
            ////      that.numberWithCommas(that.roundTo(d.Vol / 1000000, 0)) +
            ////      "میلیون " +
            ////      "<br>" +
            ////      "قیمت: " +
            ////      that.numberWithCommas(that.roundTo(d.Price, 0)) +
            ////      "<br>"
            ////  )
            ////  .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(20)
              .style("opacity", 0.7);
          })
          .on("mouseleave touchend", function() {
            that.LowestImpactTooltip = false;

            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            ////tooltip2.style("visibility", "hidden");
          })
          .transition()
          .duration(700)
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
            return LowestImpactColor(d.Value);
          })
          .attr("stroke", "#3e3e4e");
        chart
          .selectAll()
          .data(this.highestImpcats)
          .enter()
          .append("rect")
          .attr("x", s => xLeft_2(s.ticker))
          .attr("y", this.height - this.margin.bottom)
          .on("mousemove touchstart", function(event, d) {
            that.tooltipData = d;
            that.HighestImpactTooltip = true;
            let coordinates = d3.pointer(event);
            that.pageX = coordinates[0];
            that.pageY = coordinates[1];
            ////tooltip
            ////  .html(
            ////    "نماد: " +
            ////      d.ticker +
            ////      "<hr/>" +
            ////      " ارزش معاملات: " +
            ////      that.numberWithCommas(that.roundTo(d.Value / 1000000000, 0)) +
            ////      "میلیارد ریال " +
            ////      "<br>" +
            ////      " حجم معاملات: " +
            ////      that.numberWithCommas(that.roundTo(d.Vol / 1000000, 0)) +
            ////      "میلیون " +
            ////      "<br>" +
            ////      "قیمت: " +
            ////      that.numberWithCommas(that.roundTo(d.Price, 0)) +
            ////      "<br>"
            ////  )
            ////  .style("visibility", "visible");
            d3.select(this)
              .transition()
              .duration(20)
              .style("opacity", 0.7);
          })
          .on("mouseleave touchend", function() {
            that.HighestImpactTooltip = false;

            d3.select(this)
              .transition()
              .duration(200)
              .style("opacity", 1);
            ////tooltip.style("visibility", "hidden");
          })
          .transition()
          .duration(700)
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
            return HighestImpactColor(d.Value);
          })
          .attr("stroke", "#3e3e4e");
        ////.style("opacity", "80%");
      }
      window.addEventListener("resize", this.initrender);
      window.addEventListener("resize", this.renderData1);
      window.addEventListener("resize", this.renderChart1);
    }
  }
};
</script>

<style scoped>
.radioBTN /deep/ .v-input--selection-controls__ripple {
  height: 16px !important;
  width: 16px !important;
  left: -3px !important;
  top: calc(50% - 15px) !important;
}
.radioBTN /deep/ .v-icon.v-icon {
  font-size: 18px !important;
}
/* .radioBTN /deep/ .v-application--is-rtl /deep/ .v-input--selection-controls__input {
  margin-left: 0px !important;
} */
.radioBTN /deep/ .v-input--selection-controls__input {
  margin-left: 0px !important;
}

.radioBTN /deep/ label {
  display: inline-block;
  margin-bottom: 0rem;
}
.radioBTN /deep/ .v-label {
  font-size: 0.8em !important;
}
.radioBTN /deep/ .theme--light.v-label {
  color: #000 !important;
  font-size: 0.7em !important;
  font-family: "Vazir-Light-FD";
}
.redItem {
  color: red;
  font-size: 0.8em;
}
.greenItem {
  color: green;
  font-size: 0.8em;
}
.D3TestTooltip {
  position: absolute;
  /* top: 20px; */
  /* right: 0px; */
  width: auto;
  height: auto;
  /* padding: 15px;
  padding-right: 5px;
  padding-left: 5px;
  margin-left: 20px;
  margin-top: 20px; */
  border-width: 1px;
  border-style: solid;
  border-color: #bdbdbd;
  border-radius: 8px;
  display: flex;
  /* cursor: pointer; */
  /* flex-wrap: nowrap; */
  flex-direction: column;
  justify-content: center;
  align-items: stretch;
  align-content: center;
  z-index: 95;
}
.D3TestTopDivTooltip {
  border-radius: 8px 8px 0px 0px;
  background-color: #d7d7d7;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  padding-right: 22px;
  padding-left: 22px;
}
.D3TestBottomDivTooltip {
  border-radius: 0px 0px 8px 8px;

  background-color: #eaeaea;
  direction: ltr;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  align-content: center;
  padding-right: 22px;
  padding-left: 22px;
}
.D3TestMiddleDivTooltip {
  border-radius: 0px 0px 0px 0px;
  background-color: #eaeaea;
  direction: ltr;
  display: flex;
  border-bottom: 1px solid #bdbdbd;
  justify-content: flex-end;
  align-items: center;
  align-content: center;
  padding-right: 22px;
  padding-left: 22px;
}

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
  font-family: "Vazir-Light-FD";
}
.cellItem {
  font-family: "Vazir-Light-FD";
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
