/* eslint-disable no-unused-vars */
<template>
  <div
    class="col-xxl-12 col-lg-12 col-md-12 col-sm-12"
    style="padding-right:0px"
  >
    <!-- <div
    class="card card-custom card-stretch gutter-b col-xxl-12 col-lg-12 col-md-12 col-sm-12"
  > -->
    <v-skeleton-loader type="card" v-show="loading"></v-skeleton-loader>

    <v-card :loading="loading" shaped>
      <v-toolbar dense class="elevation-2">
        <v-toolbar-title>
          ارزش معاملات
          <span class="cellItemTradesValueChart mr-2">
            {{
              this.numberWithCommas(
                this.roundTo(
                  (this.jsonData.Tepix + this.jsonData.IFB) / 1000000000,
                  0
                )
              )
            }}
            میلیارد ریال
          </span>
        </v-toolbar-title>
      </v-toolbar>
      <!-- <v-card-title
        >ارزش معاملات
        <span class="cellItemTradesValueChart mr-2">
          {{
            this.numberWithCommas(
              this.roundTo(
                (this.jsonData.Tepix + this.jsonData.IFB) / 1000000000,
                0
              )
            )
          }}
          میلیارد ریال
        </span></v-card-title
      >
      <v-divider class="mt-0"></v-divider> -->
      <div id="ChartContainer_TradeValue"></div>
    </v-card>
  </div>
</template>

<script>
import * as d3 from "d3";
// eslint-disable-next-line no-unused-vars
export default {
  name: "ChartTradeValue",
  props: { inputDataTV: Array },
  data() {
    return {
      loading: true,
      highestValues: [],
      highestVolumes: [],
      jsonData: {},
      min: 0,
      max: 10,
      number: 3,
      height: 0,
      width: 0,
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
    inputDataTV() {
      if (!(this.inputDataTV === undefined || this.inputDataTV.length == 0)) {
        this.loading = false;
        this.renderData();
        this.renderChart();
      }
    }
  },
  // In the beginning...
  mounted() {
    this.initrender();

    if (!(this.inputDataTV === undefined || this.inputDataTV.length == 0)) {
      this.loading = false;
      this.renderData();
      this.renderChart();
    }
  },
  computed: {},
  methods: {
    isRealValue(obj) {
      return obj && obj !== "null" && obj !== "undefined";
    },
    initrender() {
      if (document.getElementById("chartContainer_TradeValue_svg")) {
        d3.select("#chartContainer_TradeValue_svg").remove();
      }
      this.width = parseInt(
        d3.select("#ChartContainer_TradeValue").style("width"),
        10
      );
      this.height = (this.width * 10) / 16;
      this.margin.top = this.height * 0.05;
      this.margin.bottom = this.height * 0.05;
      this.margin.right = this.width * 0.05;
      this.margin.left = this.width * 0.05;
      this.offsetY = this.margin.top;
      var parent = document.getElementById("ChartContainer_TradeValue");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "chartContainer_TradeValue_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        
      // eslint-disable-next-line no-unused-vars
    },
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
    isNull(obj, key) {
      return obj[key] == null || obj[key] === undefined || obj[key] === "null";
    },
    validate(obj) {
      let objKeys = Object.keys(obj);
      objKeys.forEach(key => {
        if (this.isNull(obj, key)) {
          obj[key] = 0;
        }
        if (typeof obj[key] == "object") {
          this.validate(obj[key]);
        }
      });
    },
    renderData() {
      this.jsonData = {
        Haghighi: 0,
        Hoghughi: 0,
        Stock: 0,
        StockBlock: 0,
        HaghTradeValues: 0,
        HaghTradeValuesBlock: 0,
        ETF: 0,
        ETFBlock: 0,
        Bond: 0,
        BondBlock: 0,
        Blocks: 0,
        IFB: 0,
        Tepix: 0,
        Total2: 0
      };
      if (this.inputDataTV[0] !== null) {
        this.jsonData.Haghighi = this.inputDataTV[0][0]["Haghighi"] * 100;
        this.jsonData.Hoghughi = this.inputDataTV[0][0]["Hoghughi"] * 100;
      }

      if (this.inputDataTV[2] !== null) {
        this.jsonData.Bond = this.inputDataTV[2].filter(item => {
          if (item["Type"] == "BondTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.BondBlock = this.inputDataTV[2].filter(item => {
          if (item["Type"] == "BondTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.ETF = this.inputDataTV[2].filter(item => {
          if (item["Type"] == "ETFTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.ETFBlock = this.inputDataTV[2].filter(item => {
          if (item["Type"] == "ETFTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.HaghTradeValues = this.inputDataTV[2].filter(item => {
          if (item["Type"] == "HaghTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.HaghTradeValuesBlock = this.inputDataTV[2].filter(
          item => {
            if (item["Type"] == "HaghTradeValues_2_3_4") {
              if (item["sum"] == item["sum"]) {
                return true;
              }
            }
          }
        )[0]["sum"];
        this.jsonData.Stock = this.inputDataTV[2].filter(item => {
          if (item["Type"] == "StockTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.StockBlock = this.inputDataTV[2].filter(item => {
          if (item["Type"] == "StockTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.validate(this.jsonData);
        this.jsonData.Blocks =
          this.jsonData.StockBlock +
          this.jsonData.HaghTradeValuesBlock +
          this.jsonData.ETFBlock +
          this.jsonData.BondBlock;
        this.jsonData.Total =
          this.jsonData.Blocks +
          this.jsonData.Bond +
          this.jsonData.Stock +
          this.jsonData.ETF +
          this.jsonData.HaghTradeValues;
      }
      if (this.inputDataTV[3] !== null) {
        this.jsonData.Tepix = this.inputDataTV[3][0]["TradeValue"] = this
          .inputDataTV[3][0]["TradeValue"]
          ? this.inputDataTV[3][0]["TradeValue"]
          : 0;
        this.jsonData.IFB = this.inputDataTV[3][1]["TradeValue"] = this
          .inputDataTV[3][1]["TradeValue"]
          ? this.inputDataTV[3][1]["TradeValue"]
          : 0;
        this.jsonData.Total2 = this.jsonData.Tepix + this.jsonData.IFB;
      } 
    },
    renderChart() {
      if (document.getElementById("chartContainer_TradeValue_svg")) {
        d3.select("#chartContainer_TradeValue_svg").remove();
      }
      let leftOffset = 2 * this.margin.left;
      let BoxWidth = this.width * 0.7;
      let BoxHeight = this.height * 0.1;
      let parent = document.getElementById("ChartContainer_TradeValue");
      let svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "chartContainer_TradeValue_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .style('background','url(../../media/logos/fadedfinwise.png) no-repeat center ')
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );

      const tooltip = d3
        .select(parent)
        .append("div")
        .attr("class", "d3-tip")
        .style("position", "absolute")
        .style("visibility", "hidden");

      chart
        .append("g")
        .append("text")
        .text("کل ارزش معاملات")
        .attr(
          "transform",
          `translate(${this.margin.left * 2.8},${this.margin.top +
            BoxHeight * 0.5})`
        )
        .style("font-size", `${this.width / 500}em`);
      const that = this;
      chart
        .append("rect")
        .attr("x", leftOffset * 1.5)
        .attr("y", this.margin.top)
        .attr("height", BoxHeight)
        .attr("width", BoxWidth)
        .attr("fill", "#845EC2")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5);
          tooltip
            .text(
              "کل ارزش معاملات:" +
                that.numberWithCommas(
                  that.roundTo(that.jsonData.Total / 1000000000000, 2)
                ) +
                "هزار میلیارد ریال"
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });

      let c1 = chart
        .append("rect")
        .attr("x", leftOffset * 1.5)
        .attr("y", BoxHeight + this.margin.top + this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#4B4453")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              (BoxWidth * that.jsonData.IFB) / that.jsonData.Total2
            );
          tooltip
            .text(
              "ارزش معاملات فرابورس:" +
                that.numberWithCommas(
                  that.roundTo(
                    (that.jsonData.IFB * 100) / that.jsonData.Total2,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", that.margin.top * 2 + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)

            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });

      c1.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr("width", (BoxWidth * that.jsonData.IFB) / that.jsonData.Total2);
      let c2 = chart
        .append("rect")
        .attr(
          "x",
          leftOffset * 1.5 +
            (BoxWidth * that.jsonData.IFB) / that.jsonData.Total2
        )
        .attr("y", BoxHeight + this.margin.top + this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#00C0A3")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              (BoxWidth * that.jsonData.Tepix) / that.jsonData.Total2
            );
          tooltip
            .text(
              "ارزش معاملات بورس:" +
                that.numberWithCommas(
                  that.roundTo(
                    (that.jsonData.Tepix * 100) / that.jsonData.Total2,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 2 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c2.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr("width", (BoxWidth * that.jsonData.Tepix) / that.jsonData.Total2);
      chart
        .append("g")
        .append("text")
        .html(
          "<span class='dot'></span>" +
            "بورس" +
            " - فرابورس" +
            "<span class='dot'></span>"
        )
        .attr(
          "transform",
          `translate(${leftOffset * 1.5 * 0.8},${BoxHeight +
            this.margin.top +
            this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", `${this.width / 500}em`);

      let c3 = chart
        .append("rect")
        .attr("x", leftOffset * 1.5)
        .attr("y", 2 * BoxHeight + this.margin.top + 2 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#00896F")

        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .transition()
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr("width", (BoxWidth * that.jsonData.Hoghughi) / 100);
          tooltip
            .text(
              "ارزش معاملات حقوقی:" +
                that.numberWithCommas(that.roundTo(that.jsonData.Hoghughi, 2)) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 3 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c3.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr("width", (BoxWidth * that.jsonData.Hoghughi) / 100);
      let c4 = chart
        .append("rect")
        .attr("x", leftOffset * 1.5 + (BoxWidth * this.jsonData.Hoghughi) / 100)
        .attr("y", 2 * BoxHeight + this.margin.top + 2 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#B0A8B9")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr("width", (BoxWidth * that.jsonData.Haghighi) / 100);
          tooltip
            .text(
              "ارزش معاملات حقیقی:" +
                that.numberWithCommas(that.roundTo(that.jsonData.Haghighi, 2)) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 3 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c4.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr("width", (BoxWidth * this.jsonData.Haghighi) / 100);
      /////////// Stock: 0,
      chart
        .append("g")
        .append("text")
        .text("حقیقی - حقوقی")
        .attr(
          "transform",
          `translate(${leftOffset * 1.5 * 0.8},${2 * BoxHeight +
            this.margin.top +
            2 * this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", `${this.width / 500}em`);
      let c5 = chart
        .append("rect")
        .attr("x", leftOffset * 1.5)
        .attr("y", 3 * BoxHeight + this.margin.top + 3 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#4B4453")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .transition()
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              BoxWidth * (that.jsonData.Blocks / that.jsonData.Total)
            );
          tooltip
            .text(
              "ارزش معاملات بلوکی:" +
                that.numberWithCommas(
                  that.roundTo(
                    (that.jsonData.Blocks / that.jsonData.Total) * 100,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 4 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c5.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr("width", BoxWidth * (this.jsonData.Blocks / this.jsonData.Total));
      let c6 = chart
        .append("rect")
        .attr(
          "x",
          leftOffset * 1.5 +
            BoxWidth * (this.jsonData.Blocks / this.jsonData.Total)
        )
        .attr("y", 3 * BoxHeight + this.margin.top + 3 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#00896F")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .transition()
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              BoxWidth * (1 - that.jsonData.Blocks / that.jsonData.Total)
            );
          tooltip
            .text(
              "ارزش معاملات عادی:" +
                that.numberWithCommas(
                  that.roundTo(
                    100 - (that.jsonData.Blocks * 100) / that.jsonData.Total,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 4 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c6.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr(
          "width",
          BoxWidth * (1 - that.jsonData.Blocks / that.jsonData.Total)
        );
      chart
        .append("g")
        .append("text")
        .text("عادی - بلوکی")
        .attr(
          "transform",
          `translate(${leftOffset * 1.5 * 0.8},${3 * BoxHeight +
            this.margin.top +
            3 * this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", `${this.width / 500}em`);

      let c7 = chart
        .append("rect")
        .attr("x", leftOffset * 1.5)
        .attr("y", 4 * BoxHeight + this.margin.top + 4 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#B0A8B9")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .transition()
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              BoxWidth *
                ((that.jsonData.StockBlock + that.jsonData.Stock) /
                  that.jsonData.Total)
            );
          tooltip
            .text(
              "ارزش معاملات سهام:" +
                that.numberWithCommas(
                  that.roundTo(
                    ((that.jsonData.StockBlock + that.jsonData.Stock) * 100) /
                      that.jsonData.Total,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 4 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c7.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr(
          "width",
          BoxWidth *
            ((this.jsonData.StockBlock + this.jsonData.Stock) /
              this.jsonData.Total)
        );

      let c10 = chart
        .append("rect")
        .attr(
          "x",
          leftOffset * 1.5 +
            BoxWidth *
              ((this.jsonData.StockBlock + this.jsonData.Stock) /
                this.jsonData.Total)
        )
        .attr("y", 4 * BoxHeight + this.margin.top + 4 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#00896F")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .transition()
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              BoxWidth *
                ((that.jsonData.ETF + that.jsonData.ETFBlock) /
                  that.jsonData.Total)
            );
          tooltip
            .text(
              "ارزش معاملات صندوق های قابل معامله :" +
                that.numberWithCommas(
                  that.roundTo(
                    ((that.jsonData.ETF + that.jsonData.ETFBlock) * 100) /
                      that.jsonData.Total,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 4 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c10
        .transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr(
          "width",
          BoxWidth *
            ((this.jsonData.ETF + this.jsonData.ETFBlock) / this.jsonData.Total)
        );
      let c8 = chart
        .append("rect")
        .attr(
          "x",
          leftOffset * 1.5 +
            BoxWidth *
              ((this.jsonData.StockBlock + this.jsonData.Stock) /
                this.jsonData.Total) +
            BoxWidth *
              ((this.jsonData.ETF + this.jsonData.ETFBlock) /
                this.jsonData.Total)
        )
        .attr("y", 4 * BoxHeight + this.margin.top + 4 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .attr("fill", "#4B4453")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .transition()
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              BoxWidth *
                ((that.jsonData.Bond + that.jsonData.BondBlock) /
                  that.jsonData.Total)
            );
          tooltip
            .text(
              "ارزش معاملات اوراق :" +
                that.numberWithCommas(
                  that.roundTo(
                    ((that.jsonData.BondBlock + that.jsonData.Bond) * 100) /
                      that.jsonData.Total,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 4 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c8.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr(
          "width",
          BoxWidth *
            ((this.jsonData.Bond + this.jsonData.BondBlock) /
              this.jsonData.Total)
        );
      chart
        .append("g")
        .append("text")
        .text("نوع دارایی")
        .attr(
          "transform",
          `translate(${leftOffset * 1.5 * 0.8},${4 * BoxHeight +
            this.margin.top +
            4 * this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", `${this.width / 500}em`);
      let c9 = chart
        .append("rect")
        .attr(
          "x",
          leftOffset * 1.5 +
            BoxWidth *
              ((this.jsonData.StockBlock + this.jsonData.Stock) /
                this.jsonData.Total) +
            BoxWidth *
              ((this.jsonData.ETF + this.jsonData.ETFBlock) /
                this.jsonData.Total) +
            BoxWidth *
              ((this.jsonData.Bond + this.jsonData.BondBlock) /
                this.jsonData.Total)
        )
        .attr("y", 4 * BoxHeight + this.margin.top + 4 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#00896F")
        .on("mouseenter touchstart", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 0.5)
            .transition()
            .duration(1000)
            .ease(d3.easePolyOut)
            .attr(
              "width",
              BoxWidth *
                (1 -
                  (that.jsonData.Bond +
                    that.jsonData.BondBlock +
                    that.jsonData.ETF +
                    that.jsonData.ETFBlock +
                    that.jsonData.StockBlock +
                    that.jsonData.Stock) /
                    that.jsonData.Total)
            );
          tooltip
            .text(
              "ارزش معاملات غیره :" +
                that.numberWithCommas(
                  that.roundTo(
                    (1 -
                      (that.jsonData.Bond +
                        that.jsonData.BondBlock +
                        that.jsonData.ETF +
                        that.jsonData.ETFBlock +
                        that.jsonData.StockBlock +
                        that.jsonData.Stock) /
                        that.jsonData.Total) *
                      100,
                    2
                  )
                ) +
                "درصد "
            )
            .attr("class", "d3-tip")
            .style("visibility", "visible")
            .style("left", that.margin.left + "px")
            .style("top", 4 * that.margin.top + "px");
        })
        .on("mouseleave touchend", function() {
          d3.select(this)
            .transition()
            .duration(200)
            .style("opacity", 1);
          tooltip.style("visibility", "hidden");
        });
      c9.transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr(
          "width",
          BoxWidth *
            (1 -
              (this.jsonData.Bond +
                this.jsonData.BondBlock +
                this.jsonData.ETF +
                this.jsonData.ETFBlock +
                this.jsonData.StockBlock +
                this.jsonData.Stock) /
                this.jsonData.Total)
        );
    }
  }
};
</script>

<style>
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
.cellItemTradesValueChart {
  font-family: "Vazir-Light-FD";
  color: rgb(82, 82, 82);
  font-weight: 600;
  font-size: 0.8em;
}
</style>
