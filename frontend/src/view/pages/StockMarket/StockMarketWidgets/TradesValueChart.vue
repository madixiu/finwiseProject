/* eslint-disable no-unused-vars */
<template>
  <div class="card card-custom card-stretch gutter-b">
    <!-- <v-skeleton-loader
      type=" table-heading,table-row@12"
      v-if="loading"
    ></v-skeleton-loader> -->
    <v-card>
      <v-card-title>ارزش معاملات</v-card-title>
      <div class="row">
        <div
          id="Chartcontainer2"
          class="col-xxl-12 col-lg-12 col-md-12 col-sm-12"
        ></div>
      </div>
      <!--end::Header-->
    </v-card>
  </div>
</template>

<script>
import * as d3 from "d3";
export default {
  name: "ChartTradeValue",
  props: { inputData: Array, inputWidth: Number, inputHeight: Number },
  data() {
    return {
      tooltip: false,
      loading: true,
      highestValues: [],
      highestVolumes: [],
      jsonData: {},
      min: 0,
      max: 10,
      number: 3,
      margin: {
        top: 20,
        right: 200,
        bottom: 10,
        left: 150
      },
      offsetY: 50
    };
  },
  watch: {
    inputData() {
      this.loading = false;
      this.renderData();
      this.renderChart();
    }
  },
  created() {
    this.renderData();
  },
  // In the beginning...
  mounted() {
    this.renderChart();
  },
  computed: {},
  methods: {
    isNull(obj, key) {
      return obj[key] == null || obj[key] === undefined || obj[key] === "null";
    },
    validate(obj) {
      var objKeys = Object.keys(obj);
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
      this.width = this.inputWidth;
      this.height = 700;
      // console.log(this.height - this.margin.bottom - this.margin.top);
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
      if (this.inputData[0] !== null) {
        this.jsonData.Haghighi = this.inputData[0][0]["Haghighi"] * 100;
        this.jsonData.Hoghughi = this.inputData[0][0]["Hoghughi"] * 100;
      }

      if (this.inputData[2] !== null) {
        this.jsonData.Bond = this.inputData[2].filter(item => {
          if (item["Type"] == "BondTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.BondBlock = this.inputData[2].filter(item => {
          if (item["Type"] == "BondTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.ETF = this.inputData[2].filter(item => {
          if (item["Type"] == "ETFTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.ETFBlock = this.inputData[2].filter(item => {
          if (item["Type"] == "ETFTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.HaghTradeValues = this.inputData[2].filter(item => {
          if (item["Type"] == "HaghTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.HaghTradeValuesBlock = this.inputData[2].filter(item => {
          if (item["Type"] == "HaghTradeValues_2_3_4") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.Stock = this.inputData[2].filter(item => {
          if (item["Type"] == "StockTradeValues") {
            if (item["sum"] == item["sum"]) {
              return true;
            }
          }
        })[0]["sum"];
        this.jsonData.StockBlock = this.inputData[2].filter(item => {
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
        console.log(this.jsonData);
      }
      if (this.inputData[3] !== null) {
        this.jsonData.Tepix = this.inputData[3][0]["TradeValue"] = this
          .inputData[3][0]["TradeValue"]
          ? this.inputData[3][0]["TradeValue"]
          : 0;
        this.jsonData.IFB = this.inputData[3][1]["TradeValue"] = this
          .inputData[3][1]["TradeValue"]
          ? this.inputData[3][1]["TradeValue"]
          : 0;
        this.jsonData.Total2 = this.jsonData.Tepix + this.jsonData.IFB;
        console.log(this.jsonData);
      }
    },
    renderChart() {
      if (document.getElementsByTagName("svg")) {
        d3.selectAll("svg").remove();
      }
      var leftOffset = 2 * this.margin.left;
      var BoxWidth = this.width - this.margin.right - this.margin.left;
      var BoxHeight = 3 * this.margin.top;
      var parent = document.getElementById("Chartcontainer2");
      var svg = d3
        .select(parent)
        .append("svg")
        .attr(
          "viewBox",
          `0 0 ${this.width + this.margin.right + this.margin.left},${this
            .height +
            this.margin.bottom +
            this.margin.top}`
        )
        .attr("preserveAspectRatio", "xMidYMid meet");
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      chart
        .append("rect")
        .attr("x", leftOffset)
        .attr("y", this.margin.top)
        .attr("height", BoxHeight)
        .attr("width", BoxWidth)
        .attr("fill", "#001170")
        .style("fill", "steelblue");
      chart
        .append("g")
        .append("text")
        .text("کل ارزش معاملات")
        .attr(
          "transform",
          `translate(${this.margin.left * 1.7},${this.margin.top * 1.5})`
        )
        .style("font-size", "2.5em");
      chart
        .append("rect")
        .attr("x", leftOffset)
        .attr("y", BoxHeight + this.margin.top + this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr("width", (BoxWidth * this.number) / 10)
        .attr("fill", "#001170")
        .style("fill", "steelblue");

      chart
        .append("rect")
        .attr(
          "x",
          leftOffset +
            ((this.width - this.margin.right - this.margin.left) *
              this.number) /
              10
        )
        .attr("y", BoxHeight + this.margin.top + this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", 0)
        .transition()
        .duration(1000)
        .ease(d3.easePolyOut)
        .attr("width", BoxWidth * (1 - this.number / 10))
        .attr("fill", "#001170")
        .style("fill", "red");
      chart
        .append("g")
        .append("text")
        .text("بورس - فرابورس")
        .attr(
          "transform",
          `translate(${leftOffset * 0.8},${BoxHeight +
            this.margin.top +
            this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", "2.5em");
      chart
        .append("rect")
        .attr("x", leftOffset)
        .attr("y", 2 * BoxHeight + this.margin.top + 2 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", (BoxWidth * this.jsonData.Haghighi) / 100)
        .style("fill", "#e63946");
      chart
        .append("rect")
        .attr("x", leftOffset + (BoxWidth * this.jsonData.Haghighi) / 100)
        .attr("y", 2 * BoxHeight + this.margin.top + 2 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", (BoxWidth * this.jsonData.Hoghughi) / 100)
        .style("fill", "#1d3557");
      /////////// Stock: 0,
      chart
        .append("g")
        .append("text")
        .text("حقیقی - حقوقی")
        .attr(
          "transform",
          `translate(${leftOffset * 0.8},${2 * BoxHeight +
            this.margin.top +
            2 * this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", "2.5em");
      chart
        .append("rect")
        .attr("x", leftOffset)
        .attr("y", 3 * BoxHeight + this.margin.top + 3 * this.offsetY)
        .attr("height", BoxHeight)
        .attr(
          "width",
          BoxWidth * (1 - this.jsonData.Blocks / this.jsonData.Total)
        )
        .attr("fill", "#001170")
        .style("fill", "green");
      chart
        .append("rect")
        .attr(
          "x",
          leftOffset +
            BoxWidth * (1 - this.jsonData.Blocks / this.jsonData.Total)
        )
        .attr("y", 3 * BoxHeight + this.margin.top + 3 * this.offsetY)
        .attr("height", BoxHeight)
        .attr("width", BoxWidth * (this.jsonData.Blocks / this.jsonData.Total))
        .style("fill", "red");
      chart
        .append("g")
        .append("text")
        .text("عادی - بلوکی")
        .attr(
          "transform",
          `translate(${leftOffset * 0.8},${3 * BoxHeight +
            this.margin.top +
            3 * this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", "2.5em");

      chart
        .append("rect")
        .attr("x", leftOffset)
        .attr("y", 4 * BoxHeight + this.margin.top + 4 * this.offsetY)
        .attr("height", BoxHeight)
        .attr(
          "width",
          BoxWidth *
            ((this.jsonData.StockBlock + this.jsonData.Stock) /
              this.jsonData.Total)
        )
        .style("fill", "yellow");

      chart
        .append("rect")
        .attr(
          "x",
          leftOffset +
            BoxWidth *
              ((this.jsonData.StockBlock + this.jsonData.Stock) /
                this.jsonData.Total)
        )
        .attr("y", 4 * BoxHeight + this.margin.top + 4 * this.offsetY)
        .attr("height", BoxHeight)
        .attr(
          "width",
          BoxWidth *
            ((this.jsonData.ETF + this.jsonData.ETFBlock) / this.jsonData.Total)
        )
        .attr("fill", "#001170")
        .style("fill", "Black");
      chart
        .append("rect")
        .attr(
          "x",
          leftOffset +
            BoxWidth *
              ((this.jsonData.StockBlock + this.jsonData.Stock) /
                this.jsonData.Total) +
            BoxWidth *
              ((this.jsonData.ETF + this.jsonData.ETFBlock) /
                this.jsonData.Total)
        )
        .attr("y", 4 * BoxHeight + this.margin.top + 4 * this.offsetY)
        .attr("height", BoxHeight)
        .attr(
          "width",
          BoxWidth *
            ((this.jsonData.Bond + this.jsonData.BondBlock) /
              this.jsonData.Total)
        )
        .attr("fill", "#001170")
        .style("fill", "blue");
      chart
        .append("g")
        .append("text")
        .text("نوع دارایی")
        .attr(
          "transform",
          `translate(${leftOffset * 0.8},${4 * BoxHeight +
            this.margin.top +
            4 * this.offsetY +
            0.5 * BoxHeight})`
        )
        .style("font-size", "2.5em");
      chart
        .append("rect")
        .attr(
          "x",
          leftOffset +
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
        )
        .attr("fill", "#001170")
        .style("fill", "pink");
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
</style>
