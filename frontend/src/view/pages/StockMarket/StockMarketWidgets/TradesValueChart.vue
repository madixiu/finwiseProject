<template>
  <div
    class="col-xxl-12 col-lg-12 col-md-12 col-sm-12"
    style="padding-right:0px"
  >
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
      <v-skeleton-loader
        type="card"
        v-show="loading"
        v-bind="attrs"
      ></v-skeleton-loader>
      <div
        id="tooltipAll"
        class="tooltipTradeChartValue"
        :style="tooltipPosition"
        v-if="tooltip1"
      >
        <v-row
          style="font-size: 0.7rem; direction: rtl"
          class="tooltipTreeMapRow"
        >
          <v-card width="100%" class="tooltipTreeMapRow">
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em">کل</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(roundTo(jsonData.Total / 1000000000000, 2))
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>میلیارد ریال</span></v-col>
            </v-row>
          </v-card>
        </v-row>
      </div>
      <div
        id="tooltipBourseFaraBourse"
        class="tooltipTradeChartValue"
        :style="tooltipPosition"
        v-if="tooltip2"
      >
        <v-row
          style="font-size: 0.7rem; direction: rtl"
          class="tooltipTreeMapRow"
        >
          <v-card width="100%" class="tooltipTreeMapRow">
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> فرابورس</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(
                      roundTo((jsonData.IFB * 100) / jsonData.Total2, 2)
                    )
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> بورس</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(
                      roundTo((jsonData.Tepix * 100) / jsonData.Total2, 2)
                    )
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
          </v-card>
        </v-row>
      </div>
      <div
        id="tooltipHH"
        class="tooltipTradeChartValue"
        :style="tooltipPosition"
        v-if="tooltip3"
      >
        <v-row
          style="font-size: 0.7rem; direction: rtl"
          class="tooltipTreeMapRow"
        >
          <v-card width="100%" class="tooltipTreeMapRow">
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> حقوقی</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{ numberWithCommas(roundTo(jsonData.Hoghughi, 2)) }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> حقیقی</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{ numberWithCommas(roundTo(jsonData.Haghighi, 2)) }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
          </v-card>
        </v-row>
      </div>
      <div
        id="tooltipBlock"
        class="tooltipTradeChartValue"
        :style="tooltipPosition"
        v-if="tooltip4"
      >
        <v-row
          style="font-size: 0.7rem; direction: rtl"
          class="tooltipTreeMapRow"
        >
          <v-card width="100%" class="tooltipTreeMapRow">
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> عادی</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    roundTo(100 - (jsonData.Blocks * 100) / jsonData.Total, 2)
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> بلوکی</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(
                      roundTo((jsonData.Blocks / jsonData.Total) * 100, 2)
                    )
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
          </v-card>
        </v-row>
      </div>
      <div
        id="tooltipAssetType"
        class="tooltipTradeChartValue"
        :style="tooltipPosition"
        v-if="tooltip5"
      >
        <v-row
          style="font-size: 0.7rem; direction: rtl"
          class="tooltipTreeMapRow"
        >
          <v-card width="100%" class="tooltipTreeMapRow">
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> سهام</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(
                      roundTo(
                        ((jsonData.StockBlock + jsonData.Stock) * 100) /
                          jsonData.Total,
                        2
                      )
                    )
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  > صندوق های بورسی</span
                >
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(
                      roundTo(
                        ((jsonData.ETF + jsonData.ETFBlock) * 100) /
                          jsonData.Total,
                        2
                      )
                    )
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"> اوراق</span>
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(
                      roundTo(
                        ((jsonData.BondBlock + jsonData.Bond) * 100) /
                          jsonData.Total,
                        2
                      )
                    )
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
            <v-row style="margin-right:0px;margin-left:0px">
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  > سایر دارایی ها</span
                >
              </v-col>
              <v-col class="flex-item">
                <span style="font-size: 1.3em"
                  >{{
                    numberWithCommas(
                      roundTo(
                        (1 -
                          (jsonData.Bond +
                            jsonData.BondBlock +
                            jsonData.ETF +
                            jsonData.ETFBlock +
                            jsonData.StockBlock +
                            jsonData.Stock) /
                            jsonData.Total) *
                          100,
                        2
                      )
                    )
                  }}
                </span>
              </v-col>
              <v-col class="flex-item"><span>درصد</span></v-col>
            </v-row>
          </v-card>
        </v-row>
      </div>
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
      attrs: {
        class: "mb-6",
        boilerplate: true,
        elevation: 2
      },
      loading: true,
      tooltip1: false,
      tooltip2: false,
      tooltip3: false,
      tooltip4: false,
      tooltip5: false,
      highestValues: [],
      highestVolumes: [],
      pageX: null,
      pageY: null,
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
        this.renderData();
        this.renderChart();
        this.loading = false;
      }
    }
  },
  // In the beginning...
  mounted() {
    this.initrender();

    if (!(this.inputDataTV === undefined || this.inputDataTV.length == 0)) {
      this.renderData();
      this.renderChart();
      this.loading = false;
    }
  },
  computed: {
    tooltipPosition() {
      if (this.pageX > this.width / 2) {
        if (this.pageY > this.height / 2) {
          let res = {
            right: this.width - this.pageX + 10 + "px",
            bottom: this.height - this.pageY + 70 + "px"
          };
          return res;
        } else {
          let res = {
            right: this.width - this.pageX + "px",
            top: this.pageY + "px"
          };
          return res;
        }
      } else {
        if (this.pageY > this.height * (2 / 3)) {
          let res = {
            left: this.pageX + 10 + "px",
            bottom: this.height - this.pageY + 70 + "px"
          };
          return res;
        }
        return {
          left: this.pageX + "px",
          top: this.pageY + "px"
        };
      }
    }
  },
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
        .attr("preserveAspectRatio", "xMidYMid meet");

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
        .style(
          "background",
          "url(../../media/logos/fadedfinwise.png) no-repeat center "
        );
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );

      // const tooltip = d3
      //   .select(parent)
      //   .append("div")
      //   .attr("class", "d3-tip")
      //   .style("position", "absolute")
      //   .style("visibility", "hidden");

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
        .on("mousemove touchstart", event => {
          that.tooltip1 = true;
          let coordinates = d3.pointer(event);
          that.pageX = coordinates[0];
          that.pageY = coordinates[1];
        })
        .on("mouseleave touchend", function() {
          that.tooltip1 = false;
          // d3.select(this)
          //   .transition()
          //   .duration(200)
          //   .style("opacity", 1);
          // tooltip.style("visibility", "hidden");
        });

      let c1 = chart
        .append("rect")
        .attr("x", leftOffset * 1.5)
        .attr("y", BoxHeight + this.margin.top + this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .style("fill", "#4B4453")
        .on("mouseenter touchstart", function() {
          that.tooltip2 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip2 = false;
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
          that.tooltip2 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip2 = false;
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
          that.tooltip3 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip3 = false;
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
          that.tooltip3 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip3 = false;
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
          that.tooltip4 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip4 = false;
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
          that.tooltip4 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip4 = false;
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
          that.tooltip5 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip5 = false;
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
          that.tooltip5 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip5 = false;
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
          that.tooltip5 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip5 = false;
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
          that.tooltip5 = true;
        })
        .on("mouseleave touchend", function() {
          that.tooltip5 = false;
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

<style scoped>
div.tooltipTradeChartValue {
  position: absolute;
  /* top: 20px; */
  /* right: 0px; */
  width: auto;
  height: auto;
  padding: 15px;
  padding-right: 5px;
  padding-left: 5px;
  margin-left: 20px;
  margin-top: 20px;
  z-index: 1000;
  background-color: #f4f1de;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  -webkit-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  -moz-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  pointer-events: none;
}
.tooltipTreeMapRow {
  width: 100%;
  padding-top: 2px;
  margin-right: 0px !important;
  margin-left: 0px !important;
  padding-right: 0px;
  /* margin-bottom:1px; */

  /* border:1px solid; */
  /* border-color:crimson; */
}
.flex-item {
  /* background-color:brown; */
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  align-items: center;
  justify-content: center;
  /* border:1px solid;
  border-color:crimson; */
  /* flex-grow: 0; */
  /* flex-shrink: ; */
  /* flex-basis: auto; */
  /* align-self: auto; */
  order: 0;
}
</style>
