<template>
  <div>
    <v-card :loading="!inputDataIndex.length" rounded="lg">
      <v-toolbar
        dense
        class="IndexChartToolbars elevation-2"
        style="height:36px;"
      >
        <v-toolbar-title style="height:20px;font-size:0.95em"
          >شاخص کل</v-toolbar-title
        >
      </v-toolbar>
      <!-- <v-skeleton-loader
        v-if="inputDataIndex.length == 0"
        v-bind="attrs"
        type="card"
      ></v-skeleton-loader> -->
      <!-- // ! fix cols in small devices optimize all childs with flex -->
      <div class="d-flex" v-show="inputDataIndex.length != 0">
        <div
          class="col-xxl-4 col-lg-4 col-md-12 col-sm-12 d-flex"
          style="padding-left:0px;flex-direction:column;justify-content:center"
          v-if="inputDataIndex.length != 0"
        >
          <div class="d-flex flex-column" style="width:100%">
            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-between"
                style="
                  padding-bottom: 15px;
                  padding-top: 15px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">
                    شاخص کل :
                  </span>
                </v-col>
                <v-col class="flex-item">
                  <span>
                    {{ roundTo(latestIndex, 0).toLocaleString() }}
                  </span>
                  <div class="d-flex flex-row">
                    <v-col class="flex-item pt-0 pb-0 pl-0 pr-2">
                      <span
                        dir="ltr"
                        v-bind:class="[
                          lastestIndexChange > 0
                            ? 'greenItem cellItem '
                            : 'redItem cellItem'
                        ]"
                      >
                        {{
                          parseFloat(
                            roundTo(lastestIndexChange, 0)
                          ).toLocaleString()
                        }}</span
                      >
                    </v-col>
                    <v-col class="flex-item pt-0 pb-0 pr-0 pl-0">
                      <span>
                        <v-icon
                          v-bind:class="[
                            lastestIndexChange > 0 ? 'greenItem' : 'redItem'
                          ]"
                          >mdi-chevron-{{
                            lastestIndexChange > 0 ? "up" : "down "
                          }}</v-icon
                        ></span
                      >
                    </v-col>
                  </div>
                </v-col>
              </div>
              <!-- here -->
            </v-card>

            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-between"
                style="
                  padding-bottom: 15px;
                  padding-top: 15px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">
                    شاخص هم وزن :
                  </span>
                </v-col>
                <v-col class="flex-item">
                  <span class="cellItem ">{{
                    roundTo(latestSW, 0).toLocaleString()
                  }}</span>
                  <div class="d-flex flex-row">
                    <v-col class="flex-item pt-0 pb-0 pl-0 pr-2">
                      <span
                        dir="ltr"
                        v-bind:class="[
                          lastestSWChange > 0
                            ? 'greenItem cellItem'
                            : 'redItem cellItem'
                        ]"
                      >
                        {{ roundTo(lastestSWChange, 0).toLocaleString() }}</span
                      >
                    </v-col>
                    <v-col class="flex-item pt-0 pb-0 pr-0 pl-0">
                      <span>
                        <v-icon
                          v-bind:class="[
                            lastestSWChange > 0 ? 'greenItem' : 'redItem'
                          ]"
                          >mdi-chevron-{{
                            lastestSWChange > 0 ? "up" : "down "
                          }}</v-icon
                        ></span
                      >
                    </v-col>
                  </div>
                </v-col>
              </div>
            </v-card>

            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-between"
                style="
                  padding-bottom: 15px;
                  padding-top: 15px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">
                    شاخص فرابورس:
                  </span>
                </v-col>
                <v-col class="flex-item">
                  <span class="cellItem ">{{
                    roundTo(IFBlatestIndex, 0).toLocaleString()
                  }}</span>
                  <div class="d-flex flex-row">
                    <v-col class="flex-item pt-0 pb-0 pl-0 pr-2">
                      <span
                        dir="ltr"
                        v-bind:class="[
                          IFBLatestChange > 0
                            ? 'greenItem cellItem '
                            : 'redItem cellItem'
                        ]"
                      >
                        {{ roundTo(IFBLatestChange, 0) }}</span
                      >
                    </v-col>
                    <v-col class="flex-item pt-0 pb-0 pr-0 pl-0">
                      <span>
                        <v-icon
                          v-bind:class="[
                            IFBLatestChange > 0 ? 'greenItem' : 'redItem'
                          ]"
                          >mdi-chevron-{{
                            IFBLatestChange > 0 ? "up" : "down "
                          }}</v-icon
                        ></span
                      >
                    </v-col>
                  </div>
                </v-col>
              </div>
            </v-card>
            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-around align-items-baseline"
                style="
                  padding-bottom: 10px;
                  padding-top: 10px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">
                    ارزش بازار بورس :
                  </span>
                </v-col>
                <v-col class="flex-item">
                  <span class="cellItem2 pl-2"
                    >{{
                      roundTo(MarketCapTotal / 1000000000, 0).toLocaleString()
                    }}
                  </span>
                  <span class="cellItem2">میلیارد ریال</span>
                </v-col>
              </div>
            </v-card>
            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-around align-items-baseline"
                style="
                  padding-bottom: 10px;
                  padding-top: 10px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">ارزش بازار فرابورس :</span>
                </v-col>
                <v-col class="flex-item">
                  <span class="cellItem2 pl-2"
                    >{{
                      roundTo(
                        IFBMarketCapTotal / 1000000000,
                        0
                      ).toLocaleString()
                    }}
                  </span>
                  <span class="cellItem2">میلیارد ریال</span>
                </v-col>
              </div>
            </v-card>
            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-around align-items-baseline"
                style="
                  padding-bottom: 10px;
                  padding-top: 10px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">
                    ارزش معاملات بورس :
                  </span>
                </v-col>
                <v-col class="flex-item">
                  <span class="cellItem2 pl-2"
                    >{{
                      roundTo(latestTradeValue / 1000000000, 0).toLocaleString()
                    }}
                  </span>
                  <span class="cellItem2">میلیارد ریال</span>
                </v-col>
              </div>
            </v-card>
            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-around align-items-baseline"
                style="
                  padding-bottom: 10px;
                  padding-top: 10px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">ارزش معاملات فرابورس :</span>
                </v-col>
                <v-col class="flex-item">
                  <span class="cellItem2 pl-2"
                    >{{
                      roundTo(
                        latestTradeValueIFB / 1000000000,
                        0
                      ).toLocaleString()
                    }}
                  </span>
                  <span class="cellItem2">میلیارد ریال</span>
                </v-col>
              </div>
            </v-card>
            <v-card rounded="lg" elevation="5" style="margin-bottom:3px">
              <div
                class="d-flex flex-row justify-content-around align-items-baseline"
                style="
                  padding-bottom: 10px;
                  padding-top: 10px;"
              >
                <v-col class="flex-item">
                  <span class="cellHeader">خالص ورود حقیقی:</span>
                </v-col>
                <v-col class="flex-item">
                  <span class="cellItem2 pl-2"
                    >{{
                      roundTo(NetHHStockMarket / 1000000000, 0).toLocaleString()
                    }}
                  </span>
                  <span class="cellItem2">میلیارد ریال</span>
                </v-col>
              </div>
            </v-card>
          </div>
        </div>
        <div
          id="Chartcontainer_index"
          class="col-xxl-8 col-lg-8 col-md-12 col-sm-12"
        ></div>
      </div>
      <!--end::Header-->
    </v-card>
  </div>
  <!-- </div> -->
</template>

<script>
import * as d3 from "d3";
// //import  roundTo  from "@/assets/js/utils.js";
export default {
  name: "IndexChart",
  props: { inputDataIndex: Array, inputDataNetHH: Array },
  data() {
    return {
      //// loading: true,
      attrs: {
        class: "mb-6",
        boilerplate: true,
        elevation: 2
      },
      latestIndex: 0,
      lastestIndexChange: 0,
      latestSW: 0,
      lastestSWChange: 0,
      latestTradeValue: 0,
      MarketCapTotal: 0,
      IFBlatestIndex: 0,
      IFBLatestChange: 0,
      IFBMarketCapTotal: 0,
      latestTradeValueIFB: 0,
      NetHHStockMarket: 0,
      indexData: [],
      fontsizeOf: 1,
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
    },
    inputDataNetHH() {
      // console.log(this.inputDataNetHH);
      if (this.isRealValue(this.inputDataNetHH)) {
        this.NetHHStockMarket = this.inputDataNetHH[0].NetInHaghighi;
      }
    }
    // indexData(newValue, oldValue) {
    //   if (oldValue.length == 0 && newValue != 0) {
    //     this.initrender();
    //    if (this.isRealValue(this.indexData)) {
    //     this.renderChart();
    //   }
    //   }
    // }
  },
  // In the beginning...
  mounted() {
    // this.renderData();
    this.initrender();
    // if (!(this.indexData === undefined || this.indexData.length == 0)) {
    //   this.renderChart();
    // }
  },
  methods: {
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
      return parseFloat(n);
    },
    isRealValue(obj) {
      return obj && obj !== "null" && obj !== "undefined";
    },
    initrender() {
      if (document.getElementById("Chartcontainer_index_svg")) {
        d3.selectAll("#Chartcontainer_index_svg").remove();
      }

      this.width =
        0.9 * parseInt(d3.select("#Chartcontainer_index").style("width"), 10);
      this.height = (this.width * 7) / 16;
      this.margin.top = this.height * 0.05;
      this.margin.bottom = this.height * 0.05;
      this.margin.right =
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.03;
      this.margin.left =
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.07;
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
      if (
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) > 800
      ) {
        //? console.log("8");
        this.fontsizeOf = 1.3;
      }
      if (
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) > 600 &&
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) < 800
      ) {
        //? console.log("6");
        this.fontsizeOf = 1.1;
        this.width =
          0.87 *
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10);
        this.height = (this.width * 10) / 16;
        this.margin.top = this.height * 0.08;
        this.margin.bottom = this.height * 0.05;
        this.margin.right =
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10) *
          0.03;
        this.margin.left =
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.1;
      }
      if (
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) > 400 &&
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) < 600
      ) {
        //? console.log("4");
        this.fontsizeOf = 1.2;
        this.width =
          0.87 *
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10);
        this.height = (this.width * 16) / 16;
        this.margin.top = this.height * 0.08;
        this.margin.bottom = this.height * 0.05;
        this.margin.right =
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10) *
          0.03;
        this.margin.left =
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.1;
      }
      if (
        parseInt(d3.select("#Chartcontainer_index").style("width"), 10) < 400
      ) {
        //? console.log("3");
        this.fontsizeOf = 1.2;
        this.width =
          0.7 * parseInt(d3.select("#Chartcontainer_index").style("width"), 10);
        this.height = (this.width * 16) / 16;
        this.margin.top = this.height * 0.08;
        this.margin.bottom = this.height * 0.05;
        this.margin.right =
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10) *
          0.05;
        this.margin.left =
          parseInt(d3.select("#Chartcontainer_index").style("width"), 10) * 0.2;
      }
    },
    renderData() {
      if (
        !(this.inputDataIndex === undefined || this.inputDataIndex.length == 0)
      ) {
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
        // eslint-disable-next-line no-unused-vars
        var data2 = data.filter(function(d) {
          if (d.date.getHours() >= 8 && d.Market == 2) {
            return d;
          }
        });
        let Uniques = [];
        data = data.filter(function(d) {
          if (
            d.date.getHours() >= 8 &&
            d.date.getHours() <= 13 &&
            d.Market == 1 &&
            !Uniques.includes(d.Index)
          ) {
            Uniques.push(d.Index);
            return d;
          }
        });
        var lastItem = data.pop();
        var lastItem2 = data2.pop();

        this.latestIndex = lastItem["Index"];
        this.lastestIndexChange = lastItem["IndexChange"];
        this.lastestSWChange = lastItem["SW_Index_Change"];
        this.latestSW = lastItem["SW_Index"];
        this.latestTradeValue = lastItem["TradeValue"];
        this.MarketCapTotal = lastItem["MarketCapTotal"];
        this.IFBlatestIndex = lastItem2["Index"];
        this.IFBLatestChange = lastItem2["IndexChange"];
        this.latestTradeValueIFB = lastItem2["TradeValue"];
        this.IFBMarketCapTotal = lastItem2["MarketCapTotal"];
        this.indexData = [...data];
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
          "url(../../media/logos/fadedfinwise3.png) no-repeat bottom 50px right 20px "
        );
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
          }) * 0.9999,
          d3.max(this.indexData, function(d) {
            return d.value;
          }) * 1.0001
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
          .style("font-family", "Vazir-Light-FD")
          .style("stroke-opacity", ".1");

      let xAxisAxe = chart.append("g").call(xAxis);
      xAxisAxe
        .selectAll("text")
        // .style("font-size", `${this.width / 700}em`)
        .style("font-size", `${this.fontsizeOf}em`)
        .style("font-family", "Vazir-Light-FD")
        .style("font-weight", "800");
      var yAxis = g =>
        g
          .attr("class", "yAxis")
          // .attr("transform", `translate(${this.margin.left},0)`)
          .transition()
          .duration(1000)
          .call(d3.axisLeft(yScale))
          .style("stroke-opacity", ".1")
          .style("font-family", "Vazir-Light-FD");
      let yAxisAxe = chart.append("g").call(yAxis);
      yAxisAxe
        .selectAll("text")
        .style("text-anchor", "start")
        // .attr("transform", `translate(${-this.margin.left},0)`)
        // .style("font-size", `${this.width / 700}em`)
        .style("font-size", `${this.fontsizeOf}em`)
        .style("font-family", "Vazir-Light-FD")
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
      let that = this;
      // eslint-disable-next-line no-unused-vars
      var callout2 = (g, value1, value2, value) => {
        if (!value2) return g.style("display", "none");
        g.style("display", null).style("pointer-events", "none");
        const path = g
          .selectAll("path")
          .data([null])
          .join("path")
          .attr("fill", "white")
          .attr("stroke", "black")
          .style("stroke-dasharray", "2, 6")
          .style("Opacity", "0.4 ");
        path.attr(
          "d",
          `M${0} ${0} L${0} ${that.height -
            that.margin.top -
            yScale(that.indexData[value2].value)} L${0} ${that.margin.top -
            yScale(that.indexData[value2].value)}`
        );
        // eslint-disable-next-line no-unused-vars
        const circle = g
          .selectAll("circle")
          .data([null])
          .join("circle")
          .attr("fill", "steelblue")
          .attr("stroke-width", 2)
          .style("stroke", "black");

        circle
          .attr("r", "5")
          .attr("cx", "0")
          .attr("cy", "0");
        // eslint-disable-next-line no-unused-vars
        const text = g
          .selectAll("text")
          .data([null])
          .join("text")
          .call(text =>
            text
              .selectAll("tspan")
              .data((value + "").split(/\n/))
              .join("tspan")
              .attr("x", 0)
              .attr("y", (d, i) => `${i * 1.1}em`)
              .style("font-weight", (_, i) => (i ? null : "bold"))
              // .style("font-size", "14px")
              .style("font-size", `${this.fontsizeOf}em`)
              .style("font-family", "Vazir-Light-FD")
              .text(d => d.split("-")[0])
          )
          .style("fill", "black");

        //eslint-disable-next-line no-unused-vars
        const { x, y, width: w, height: h } = text.node().getBBox();
        text
          .attr("transform", `translate(${w},${-h})`)
          .style("font-family", "Vazir-Light-FD")
          .style("font-size", `${this.fontsizeOf * 0.7}em`);
        const pathnew = g
          .selectAll("pathnew")
          .data([null])
          .join("path")
          .attr("fill", "#001170")
          .style("font-family", "Vazir-Light-FD")
          .style("stroke", "black")
          .style("stroke-dasharray", "3,3")
          .style("Opacity", "0.8");
        pathnew
          .attr(
            "d",
            `M${0} ${that.height -
              that.margin.top -
              yScale(that.indexData[value2].value)} H-6 
              l7,-5l5,5H 25 V
              ${that.height -
                that.margin.top -
                yScale(that.indexData[value2].value) +
                40} H-30 V${that.height -
              that.margin.top -
              yScale(that.indexData[value2].value)}z`
          )
          .attr("stroke", "black");

        const text2 = g
          .selectAll("text2")
          .data([null])
          .join("text")
          .call(text2 =>
            text2
              .selectAll("tspan")
              .data((value + "").split(/\n/))
              .join("tspan")
              .attr("x", 0)
              .attr("y", (d, i) => `${i * 1.1}em`)
              .style("font-weight", (_, i) => (i ? null : "bold"))
              .style("font-family", "Vazir-Light-FD")
              .text(d => d.split("-")[1].split(" ")[0])
          )
          .style("fill", "white")
          .style("font-family", "Vazir-Light-FD")
          .style("font-size", "11px")
          .style("Opacity", "1 ");
        // eslint-disable-next-line no-unused-vars
        const { x2, y2, width: w2, height: h2 } = text2.node().getBBox();
        text2.attr(
          "transform",
          `translate(${w2 / 2},${that.height -
            that.margin.top -
            yScale(that.indexData[value2].value) +
            20})`
        );
        const pathnew2 = g
          .selectAll("pathnew2")
          .data([null])
          .join("path")
          .attr("fill", "gray")
          .style("stroke", "black")
          // .style("stroke-dasharray", ("3,3"))
          .style("Opacity", "0.4");
        pathnew2
          .attr("d", `M${-10} ${-10} H${90} V${-50} H${-10}z`)
          .attr("stroke", "black");
      };

      svg.on("touchmove mousemove", function(event) {
        const x1 = d3.pointer(event, this)[0];
        const y1 = d3.pointer(event, this)[1];
        if (x1 - that.margin.left < that.width - that.margin.right) {
          const date = xScale.invert(x1 - that.margin.left);
          // eslint-disable-next-line no-unused-vars
          const y2 = yScale.invert(y1 - that.margin.top);
          const idx = d3.bisect(dates, date);
          tooltip
            .attr(
              "transform",
              `translate(${xScale(that.indexData[idx].date)},${yScale(
                that.indexData[idx].value
              )})`
            )
            .call(
              callout2,
              x1,
              idx,
              `${formatValue(that.indexData[idx].value)}-${formatDate(
                that.indexData[idx].date
              )}-`
            );
        }
      });

      svg.on("touchend mouseleave", () => tooltip.call(callout2, null));
      svg
        .append("text")
        // .attr("class", "title")
        .attr("x", this.width / 2 + this.margin.left)
        .attr("y", 40)
        .attr("text-anchor", "middle")
        .text("شاخص کل");
      window.addEventListener("resize", this.initrender);
      window.addEventListener("resize", this.renderChart);
    }
  }
};
</script>

<style scoped>
.IndexChartToolbars /deep/ .v-toolbar__content {
  height: 36px !important;
}
.flex-item {
  /* background-color:brown; */
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  align-items: center;
  justify-content: flex-start;
  padding-top: 0px;
  padding-bottom: 0px;
  order: 0;
}
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
  font-size: 1em;
}
.cellItem2 {
  font-family: "Vazir-Medium-FD";
  /* font-weight: 600; */
  direction: ltr;
  font-size: 0.8em;
}
.redItem {
  color: red !important;
  font-size: 1em;
  font-family: "Vazir-Medium-FD" !important;
}
.greenItem {
  color: green !important;
  font-size: 1em;
  font-family: "Vazir-Medium-FD" !important;
}
.Chart1title * {
  font-size: 1.2em;
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
  font-family: "Vazir-Light-FD";
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
