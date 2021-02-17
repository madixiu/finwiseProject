/* eslint-disable no-unused-vars */
<template>
  <div class="card card-custom card-stretch gutter-b">
    <!-- <v-skeleton-loader
      type=" table-heading,table-row@12"
      v-if="loading"
    ></v-skeleton-loader> -->
    <v-card>
      <v-card-title>نمودار وضعیت بازار</v-card-title>
      <div class="row">
        <div
          id="Chartcontainer"
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
   name: "ChartVol",
  props: { inputData: Array, inputWidth: Number, inputHeight: Number },
  data() {
    return {
      tooltip: false,
      tooltipData1: "",
      tooltipData2: "",
      tooltipData3: "",
      tooltipData4: "",
      loading: true,
      highestValues: [],
      highestVolumes: [],
      margin: {
        top: 50,
        right: 75,
        bottom: 50,
        left: 100
      }
    };
  },
  watch: {
    inputData() {
      this.loading = false;
      // this.renderData();
    }
  },
  created() {
    this.renderData();
    // // this.loadData();

    // // this.sortedJson = this.jsonData.sort((a, b) => a.Value - b.Value);
    // // this.lowestValues=this.sortedJson.slice(0,10)
    // // console.log(this.lowestValues)
  },
  // In the beginning...
  mounted() {
    this.renderChart();
  },
  // The reactive computed variables that fire rerenders
  computed: {
    // scale() {
    //   const x = d3
    //     .scaleBand()
    //     .domain(this.highestVolumes.map(x => x.ticker))
    //     .rangeRound([
    //       this.width - this.margin.right,
    //       (this.width - this.margin.left) / 2
    //     ])
    //     .padding(0.15);
    //   const y = d3
    //     .scaleLinear()
    //     .domain([0, Math.max(...this.highestVolumes.map(x => x.Vol)) * 1.2])
    //     .rangeRound([this.height - this.margin.bottom, this.margin.top])
    //     .nice();
    //   return { x, y };
    // },
    // scale2() {
    //
    //   return { x, y };
    // }
  },
  methods: {
    renderData() {
      this.width = this.inputWidth;
      this.height = this.inputHeight;
      // console.log(this.height - this.margin.bottom - this.margin.top);
      this.jsonData = this.inputData;
      this.jsonData.sort((a, b) => b.Value - a.Value);
      this.highestValues = this.jsonData.slice(0, 10);
      // console.log(this.highestValues);
      this.jsonData.sort((a, b) => b.Vol - a.Vol);
      this.highestVolumes = this.jsonData.slice(0, 10);
      // console.log(this.highestVolumes);
    },
    renderChart() {
      // if (document.getElementsByTagName("svg")) {
      //   d3.selectAll("svg").remove();
      // }

      var parent = document.getElementById("Chartcontainer");
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
      // eslint-disable-next-line no-unused-vars
      const xLeft = d3
        .scaleBand()
        .domain(this.highestValues.map(x => x.ticker))
        .range([0, (this.width - this.margin.right) / 2])
        .padding(0.15);

      const yLeft = d3
        .scaleLinear()
        .domain([0, Math.max(...this.highestValues.map(x => x.Value)) * 1.2])
        .range([this.height - this.margin.bottom, this.margin.top])
        .nice();
      // eslint-disable-next-line no-unused-vars
      const xRight = d3
        .scaleBand()
        .domain(this.highestVolumes.map(x => x.ticker))
        .range([
          this.width - this.margin.right,
          (this.width - this.margin.right) / 2
        ])
        .padding(0.15);

      // eslint-disable-next-line no-unused-vars
      const yRight = d3
        .scaleLinear()
        .domain([0, Math.max(...this.highestVolumes.map(x => x.Vol)) * 1.2])
        .range([this.height - this.margin.bottom, this.margin.top])
        .nice();
      ///////////////
      var mycolor = d3
        .scaleLinear()
        .domain([0, Math.max(...this.highestValues.map(x => x.Value)) * 1.2])
        .range(["#66BB6A", "#1B5E20"]);
      var mycolor2 = d3
        .scaleLinear()
        .domain([0, Math.max(...this.highestVolumes.map(x => x.Vol)) * 1.2])
        .range(["#4DD0E1", "#006064"]);
      //////////////
      chart
        .append("g")
        .call(d3.axisLeft(yLeft))
        .selectAll("text")
        .style("text-anchor", "start")
        // .attr("dx", "-8em")
        .style("font-size", "0.9em");
      chart
        .append("g")
        .call(d3.axisBottom(xLeft))
        .attr("transform", `translate(0,${this.height - this.margin.bottom})`)
        .selectAll("text")
        .attr("dy", "1em")
        .style("font-size", "1.5em");
      ////////////////
      chart
        .append("g")
        .call(d3.axisRight(yRight))
        .attr("transform", `translate(${this.width - this.margin.right},0)`)
        .selectAll("text")
        .style("text-anchor", "end")
        .style("font-size", "0.9em");
      chart
        .append("g")
        .call(d3.axisBottom(xRight))
        .attr("transform", `translate(0,${this.height - this.margin.bottom})`)
        .selectAll("text")
        .attr("dy", "1em")
        .style("font-size", "1.5em");
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
        .style("font-size", "1.2em")
        .text("بیشترین ارزش معاملات");

      chart
        .append("text")
        .attr("class", "Chart1title")
        .attr(
          "x",
          ((this.width - this.margin.right) * 4) / 6 + this.margin.left
        )
        .attr("y", (this.margin.top * 3) / 4)
        .attr("text-anchor", "middle")
        .style("font-size", "1.2em")
        .text("بیشترین حجم معاملات");

      const tooltipBox = chart.append("g");

      chart
        .selectAll()
        .data(this.highestVolumes)
        .enter()
        .append("rect")
        .attr("x", s => xRight(s.ticker))
        .attr("y", this.height - this.margin.bottom)
        .on(
          "touchenter mouseenter",

          function(s) {
            // return this.MouseIn(s);
            // console.log(s.srcElement.__data__.ticker);
            tooltipBox
              .attr("fill", "black")
              .call(callout2, s.srcElement.__data__);
          }
        )
        .on("touchleave mouseleave", function() {
          tooltipBox.call(callout2, null);
        })
        .transition()
        .duration(2000)
        .ease(d3.easePolyOut)
        .attr("y", function(d) {
          return yRight(d.Vol);
        })
        .attr("height", s =>
          Math.max(yRight(0) - yRight(s.Vol), yRight(s.Vol) - yRight(0))
        )
        .attr("width", xRight.bandwidth())
        .attr("fill", function(d) {
          return mycolor2(d.Vol);
        });
      chart
        .selectAll()
        .data(this.highestValues)
        .enter()
        .append("rect")
        .attr("x", s => xLeft(s.ticker))
        .attr("y", this.height - this.margin.bottom)
        .on(
          "touchenter mouseenter",

          function(s) {
            // return this.MouseIn(s);
            // console.log(s.srcElement.__data__.ticker);
            tooltipBox
              .attr("fill", "black")
              .call(callout2, s.srcElement.__data__);
          }
        )
        .on("touchleave mouseleave", function() {
          tooltipBox.call(callout2, null);
        })
        .transition()
        .duration(2000)
        .ease(d3.easePolyOut)
        .attr("y", function(d) {
          return yLeft(d.Value);
        })
        .attr("height", s =>
          Math.max(yLeft(0) - yLeft(s.Value), yLeft(s.Value) - yLeft(0))
        )
        .attr("width", xLeft.bandwidth())
        .attr("fill", function(d) {
          return mycolor(d.Value);
        })
        .style("opacity", "80%");
      var BHeight = 100;
      var Bwidth = 500;
      var callout2 = (g, value) => {
        if (!value) return g.style("display", "none");
        g.style("display", null).style("pointer-events", "none");
        // console.log
        // eslint-disable-next-line no-unused-vars
        // const pathnew = g
        //   .selectAll("pathnew")
        //   .data([null])
        //   .join("rect")
        //   .attr("x", 500)
        //   .attr("y", 100)
        //   .attr("height", BHeight)
        //   .attr("width", Bwidth)
        //   .attr("fill", "#001170")
        //   .style("fill", "steelblue")
        //   .style("stroke-dasharray", "3,3");
        var offsetText1x = Bwidth / 3;
        var offsetText1Y = BHeight / 3;
        // var offsetText2Y = 2*BHeight / 3;
        // g

        // eslint-disable-next-line no-unused-vars
        const text2 = g
          .selectAll("text")
          .data([null])
          .join("text")
          .data(value.ticker)
          .attr(
            "transform",
            `translate(${((this.width - this.margin.left - this.margin.right) *
              3) /
              4 +
              offsetText1x},${offsetText1Y + this.margin.top})`
          )
          .text(value.ticker)

          .style("fill", "black")
          .style("font-size", "1.5em")
          .style("Opacity", "1 ");
        // eslint-disable-next-line no-unused-vars
        const text3 = g
          .join("text")
          .data(value.Value)
          .attr("transform", `translate(${300},${300})`)
          .text(value.Value)
          .style("fill", "black")
          .style("font-size", "1.5em")
          .style("Opacity", "1 ");
        // eslint-disable-next-line no-unused-vars
        // eslint-disable-next-line no-unused-vars
      };
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
