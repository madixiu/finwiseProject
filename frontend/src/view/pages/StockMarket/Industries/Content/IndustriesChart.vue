/* eslint-disable no-unused-vars */
<template>
  <div class="card card-custom card-stretch gutter-b">
    <!-- <v-skeleton-loader
      type=" table-heading,table-row@12"
      v-if="loading"
    ></v-skeleton-loader> -->

    <v-card>
      <v-card-title>بازدهی صنایع</v-card-title>
      <v-divider class="mt-0 "></v-divider>
      <div class="row">
        <div class="col-xxl-10 col-lg-10 col-md-10 col-sm-10 mb-2">
          <div id="TechnicalGauge"></div>
        </div>
        <div class="col-xxl-2 col-lg-2 col-md-2 col-sm-2 mb-2 rtl_aligned">
          <v-card>
            <v-card-title>تنظیمات</v-card-title>
            <v-divider class="mt-0"></v-divider>
            <b-form-group label="مرتب سازی بر اساس :" class="px-5">
              <b-form-radio-group
                :click="this.renderChart()"
                v-model="SortBy"
                :options="options"
                name="radio-inline"
              ></b-form-radio-group>
            </b-form-group>
            <v-divider class="mt-0"></v-divider>
            <b-form-group label="بازه محاسبه بازده:" class="px-5">
              <b-form-radio-group
                :click="this.renderChart()"
                v-model="freq"
                :options="options2"
                name="radio-inline2"
              ></b-form-radio-group>
            </b-form-group>
            <v-divider class="mt-0"></v-divider>
          </v-card>
        </div>
      </div>
      <!--end::Header-->
    </v-card>
  </div>
</template>

<script>
import * as d3 from "d3";
// eslint-disable-next-line no-unused-vars
export default {
  name: "ChartTradeValue",
  props: { inputData: Object },
  data() {
    return {
      options: [
        { text: "بازدهی", value: "D1" },
        { text: "ارزش بازار", value: "marketCap" },
        { text: "ارزش معاملات", value: "TradeValue" },
        { text: "بازدهی تاریحی", value: "T" }
      ],
      options2: [
        { text: "امروز", value: "D1" },
        { text: "یک هفته", value: "W1" },
        { text: "یک ماه اخیر", value: "M1" },
        { text: "۳ ماهه اخیر", value: "M3" },
        { text: "یکساله", value: "Y1" }
      ],
      search: "",
      margin: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0
      },
      height: 0,
      width: 0,
      DataItems2: [],
      loading: true,
      SortBy: "D1",
      freq: "D1"
    };
  },
  watch: {
    inputData() {
      this.populateData();
      this.loading = false;
      this.renderChart();
    }
  },
  // In the beginning...
  mounted() {
    this.initrender();
    this.populateData();
    // this.renderChart("T","T");
  },
  computed: {},
  methods: {
    isEmpty(obj) {
      for (var prop in obj) {
        if (obj.hasOwnProperty(prop)) {
          return false;
        }
      }

      return JSON.stringify(obj) === JSON.stringify({});
    },
    populateData() {
      // this.inputData;
      var tList = [];
      for (var tKey in this.inputData) tList.push(this.inputData[tKey]);
      this.DataItems2 = tList;
      if (!this.isEmpty(this.DataItems2)) {
        this.loading = false;
        this.sortByMarketCap("D1");
        // console.log(this.DataItems2);
      }
    },
    sortByMarketCap(M) {
      let f = this.DataItems2;
      f.sort(function(a, b) {
        return b[M] - a[M];
      });
      this.DataItems2 = f;
    },
    initrender() {
      if (document.getElementsByTagName("svg")) {
        d3.selectAll("svg").remove();
      }
      this.width = parseInt(d3.select("#TechnicalGauge").style("width"), 10);
      this.height = (this.width * 6) / 16;
      this.margin.top = this.height * 0.1;
      this.margin.bottom = this.height * 0.05;
      this.margin.right = this.width * 0.05;
      this.margin.left = this.width * 0.05;
      // eslint-disable-next-line no-unused-vars
      var parent = document.getElementById("TechnicalGauge");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "chartContainer")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      // eslint-disable-next-line no-unused-vars
    },
    renderChart() {
      this.loading=true
      this.sortByMarketCap(this.SortBy);
      let Param = this.freq;
      var parent = document.getElementById("chartContainer");
      var svg = d3.select(parent);
      // const tooltip = d3
      //   .select(parent)
      //   .append("div")
      //   .attr("class", "d3-tip")
      //   .style("position", "absolute")
      //   .style("visibility", "hidden");
      if (document.getElementsByTagName("svg")) {
        d3.selectAll("g").remove();
      }
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      const xLeft = d3
        .scaleBand()
        .domain(Object.entries(this.DataItems2).map(item => item[1].Name))
        .range([0, this.width - this.margin.right - this.margin.left])
        .padding(0.15);
      // console.log(d3.min(Object.entries(this.DataItems2).map(item => item[1]['D1'])))
      const yLeft = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(Object.entries(this.DataItems2).map(item => item[1][Param])) *
            1.1
        ])
        .range([
          (this.height - this.margin.bottom - this.margin.top) / 2,
          this.margin.top
        ])
        .nice();
      const yLeft2 = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(
            Object.entries(this.DataItems2).map(item => item[1]["marketCap"])
          ) * 1.1
        ])
        .range([
          (this.height - this.margin.bottom - this.margin.top) / 2,
          this.height - this.margin.bottom - this.margin.top
        ])
        .nice();
      // window.addEventListener("resize", this.renderChart);
      var aXisY1 = d3
        .axisLeft(yLeft)
        .tickFormat(d => {
          if (d <= 0) {
            return d;
          } else {
            return d + "  " + "درصد";
          }
        })
        .tickSizeInner(-this.width + this.margin.right + this.margin.left);

      var aXisY1Axe = chart.append("g").call(aXisY1);
      aXisY1Axe
        .selectAll(".tick text")
        .style("text-anchor", "start")
        .attr("stroke", "#00896f")
        .style("font-size", function() {
          return 1300 / this.width + "em";
        });
      aXisY1Axe
        .selectAll(".tick line")
        .attr("stroke", "#b0a8b9")
        .style("opacity", "0.2");
      aXisY1Axe.selectAll(".domain").attr("stroke", "#00896f");

      var aXisY2 = d3
        .axisLeft(yLeft2)
        .tickFormat(d => {
          if (d <= 0) {
            return d;
          } else {
            return d / 10000000000000 + "  " + "همت";
          }
        })
        .tickSizeInner(-this.width + this.margin.right + this.margin.left);

      var aXisY2Axe = chart.append("g").call(aXisY2);
      //
      aXisY2Axe
        .selectAll(".tick text")
        .style("text-anchor", "start")
        .attr("stroke", "#00896f")
        .style("font-size", function() {
          return 1300 / this.width + "em";
        });
      aXisY2Axe
        .selectAll(".tick line")
        .attr("stroke", "#b0a8b9")
        .style("opacity", "0.2");
      chart
        .append("g")
        .call(d3.axisBottom(xLeft))
        .attr("transform", `translate(0,${yLeft(0)})`)
        .selectAll("text")
        .attr("dy", "1em")
        .style("Visibility", "hidden");
      var colorScale = d3
        .scaleQuantize()
        .domain([-100, 100])
        .range([
          "#f63538",
          "#eb363a",
          "#e0373c",
          "#c9393f",
          "#b33b43",
          "#379a58",
          "#35ab59",
          "#33bc5a",
          "#32c45a",
          "#30cc5a"
        ]);
      chart
        .selectAll("text.bar")
        .data(Object.entries(this.DataItems2))
        .enter()
        .append("text")
        .attr("class", "yAxis-label")
        .attr("text-anchor", "middle")
        .attr("fill", "#70747a")
        .attr("x", d => xLeft(d[1].Name) + xLeft.bandwidth() * 0.5)
        .attr("y", d => {
          if (d[1][Param] > 0) {
            return (
              yLeft(d[1][Param]) -
              0.1 * (this.height - this.margin.bottom - this.margin.top)
            );
          } else {
            return (
              2 * yLeft(0) -
              yLeft(d[1][Param]) -
              0.1 * (this.height - this.margin.bottom - this.margin.top)
            );
          }
        })
        .text(d => d[1].Name)
        .attr("transform", function() {
          var me = this;
          var x1 = me.getBBox().x + me.getBBox().width / 2; //the center x about which you want to rotate
          var y1 = me.getBBox().y + me.getBBox().height / 2; //the center y about which you want to rotate

          return `rotate(-90, ${x1}, ${y1})`; //rotate 180 degrees about x and y
        });
      // .attr("dx", "-.8em")
      // .attr("dy", ".15em")
      // .attr("transform", "rotate(-90)");
      // let that=this
      chart
        .selectAll()
        .data(Object.entries(this.DataItems2))
        .enter()
        .append("rect")
        .attr("x", s => xLeft(s[1].Name))
        .attr("y", yLeft(0))
        .transition()
        .duration(2000)
        .ease(d3.easePolyOut)
        .attr("y", function(d) {
          // return Math.min(yLeft(0),yLeft(d[1].D1))
          {
            if (d[1][Param] > 0) {
              return yLeft(d[1][Param]);
            } else {
              return 2 * yLeft(0) - yLeft(d[1][Param]);
            }
          }
        })
        .attr("height", s =>
          Math.abs(yLeft(0) - yLeft(s[1][Param]), yLeft(s[1][Param]) - yLeft(0))
        )
        .attr("width", xLeft.bandwidth())
        .attr("fill", "#845ec2")
        .attr("opacity", "0.8")
        .attr("fill", function(d) {
          return colorScale(d[1][Param]);
        })
        // .on("mousemove touchstart", function() {
        //   d3.select(this)
        //     .transition()
        //     .duration(200)
        //     .style("opacity", 0.5)
        //     .transition()
        //     .duration(1000)
        //     .ease(d3.easePolyOut)
        //   tooltip
        //     .text(
        //       "ارزش معاملات اوراق :" +
        //         "درصد "
        //     )
        //     .attr("class", "d3-tip")
        //     .style("visibility", "visible")
        //     .style("left", that.margin.left + "px")
        //     .style("top", that.margin.top + "px");
        // })
        // .on("mousemove touchend", function() {
        //   d3.select(this)
        //     .transition()
        //     .duration(200)
        //     .style("opacity", 1);
        //   tooltip.style("visibility", "hidden");
        // });

      chart
        .selectAll()
        .data(Object.entries(this.DataItems2))
        .enter()
        .append("rect")
        .attr("x", s => xLeft(s[1].Name))
        .attr("y", yLeft2(0))
        .transition()
        .duration(2000)
        .ease(d3.easePolyOut)
        .attr("y", function(d) {
          return Math.min(yLeft(0), yLeft2(d[1].marketCap));
        })
        .attr("height", s =>
          Math.max(
            yLeft2(0) - yLeft2(s[1].marketCap),
            yLeft2(s[1].marketCap) - yLeft2(0)
          )
        )
        .attr("width", xLeft.bandwidth())
        .attr("fill", "#4b4453")
        .style("font-size", function() {
          return 1200 / this.width + "em";
        });

      window.addEventListener("resize", this.renderChart);
      this.loading=false
    }
  }
};
</script>

<style scoped>
.axis1 line {
  stroke: "red" !important;
  opacity: 0.5;
}
.rtl_aligned {
  direction: rtl;
  text-align: right;
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
</style>
