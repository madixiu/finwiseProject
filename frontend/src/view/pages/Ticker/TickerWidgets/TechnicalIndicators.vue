<template>
  <div id="TechnicalindicatorChartparentDiv">
    <!-- <v-card rounded="lg"> -->
    <!-- <v-card-title>وضعیت تکنیکال سهم</v-card-title>
      <v-divider class="mt-0"></v-divider> -->
    <div class="d-flex flex-column" v-if="!this.$store.getters.isAuthenticated">
      <div class="d-flex justify-content-center my-2">
        <v-icon size="30px">mdi-lock</v-icon>
      </div>
      <div
        class="d-flex justify-content-center"
        v-show="!this.$store.getters.isAuthenticated"
      >
        <v-btn small color="#ebebeb" dark @click="onClick">
          <v-icon small class="pl-1 pr-0" color="#4177a5"
            >mdi-account-circle</v-icon
          >
          <span style="color:#4177a5">ورود</span>
        </v-btn>
      </div>
    </div>
    <div :class="[this.$store.getters.isAuthenticated == true ? '' : 'blured']">
      <!-- <div class="row"> -->
      <!-- <div class="col-xxl-12 col-lg-12 col-md-12 col-sm-12"> -->
      <!-- <div> -->
      <!--//? d3 Gauge -->
      <div id="TechnicalGauge"></div>
      <!-- </div> -->
      <!-- </div> -->

      <v-card
        rounded="lg"
        outlined
        elevation="2"
        class="mx-2"
        v-show="this.$store.getters.isAuthenticated"
      >
        <v-row no-gutters class="d-flex flex-row px-3">
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خرید</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#30cc5a">{{ positive }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column align-center">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">خنثی</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#414554">{{ neutral }}</span></v-col
            >
          </v-col>
          <v-col class="d-flex flex-column">
            <v-col class="d-flex justify-content-center"
              ><span style="font-size:0.9em">فروش</span></v-col
            >
            <v-col class="d-flex justify-content-center py-0"
              ><span style="color:#f63538">{{ negative }}</span></v-col
            >
          </v-col>
        </v-row>
      </v-card>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "TechnicalIndicators",
  props: ["Indicators"],
  data() {
    return {
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
      sum: 0,
      positive: 0,
      negative: 0,
      neutral: 0
    };
  },
  methods: {
    onClick() {
      this.$router.push({ name: "login" });
    },
    populateData() {
      this.DataItems2 = this.Indicators;
      if (!(this.DataItems2 === undefined || this.DataItems2.length == 0)) {
        this.loading = false;
        this.positive = 0;
        this.negative = 0;
        this.neutral = 0;
        this.sum = 0;
        // this.sum=this.DataItems2.sum_signal

        var allkeys = Object.keys(this.DataItems2[0]);
        var signals = allkeys.filter(item => {
          return String(item).includes("Signal");
        });
        let that = this;
        signals.forEach(function(element) {
          let val = that.DataItems2[0][String(element)];
          if (val == 1) {
            that.positive = that.positive + 1;
            that.sum = that.sum + 1;
          }
          if (val == -1) {
            that.negative = that.negative + 1;
            that.sum = that.sum - 1;
          }
          if (val == 0) {
            that.neutral = that.neutral + 1;
          }
        });

        // this.sum = this.DataItems2[0].sum_signal;
        if (this.sum > 17) {
          this.sum = 17;
        }
        if (this.sum < -17) {
          this.sum = -17;
        }
      }
    },
    initrender() {
      // console.log("initrender");
      // if (document.getElementsByTagName("svg")) {
      //   d3.selectAll("svg").remove();
      // }
      if (document.getElementById("chartContainer")) {
        document.getElementById("chartContainer").remove();
      }
      this.width = parseInt(
        d3.select("#TechnicalindicatorChartparentDiv").style("width"),
        10
      );
      this.height = (this.width * 9) / 16;
      this.margin.top = this.height * 0.7;
      this.margin.bottom = 0;
      this.margin.right = this.width * 0.1;
      this.margin.left = this.width * 0.1;

      var parent = document.getElementById("TechnicalGauge");

      d3.select(parent)
        .append("svg")
        .attr("id", "chartContainer")
        .attr("viewBox", `0 0 ${this.width} ${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
    },
    getFull() {
      if (this.sum > 10.2) {
        return "خرید قوی";
      }
      if (this.sum > 3.4) {
        return "خرید";
      }
      if (this.sum > -3.4) {
        return "خنثی";
      }
      if (this.sum > -10.2) {
        return "فروش";
      }
      if (this.sum < -10.2) {
        return "فروش قوی";
      }
    },
    getFullColor() {
      if (this.sum > 10.2) {
        return "#30cc5a";
      }
      if (this.sum > 3.4) {
        return "#379a58";
      }
      if (this.sum > -3.4) {
        return "#404e55";
      }
      if (this.sum > -10.2) {
        return "#b33b43";
      }
      if (this.sum < -10.2) {
        return "#f63538";
      }
    },
    renderChart() {
      // console.log("renderChart");
      var parent = document.getElementById("chartContainer");
      var svg = d3.select(parent);
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left / 2}, ${this.margin.top})`
        );

      var n = 5,
        radius = this.width / 2 - this.margin.right * 2,
        needleRad = this.width / 200,
        pi = Math.PI,
        halfPi = pi / 2,
        endAngle = pi / 2,
        startAngle = -endAngle,
        data = d3.range(startAngle, endAngle, pi / n),
        _data = data.slice(0),
        tt = 3000,
        scale = d3
          .scaleLinear()
          .range([startAngle, endAngle])
          .domain([-17, 17]),
        // colorScale = d3
        //   .scaleSequential(d3.interpolateRdYlGn)
        //   .domain([data[0], data[data.length - 1]]);
        colorScale = d3
          .scaleQuantize()
          .domain([data[0], data[data.length - 1]])
          .range([
            "#f63538",
            "#eb363a",
            "#e0373c",
            "#c9393f",
            "#b33b43",
            "#9c3d46",
            "#86374a",
            "#584351",
            "#414554",
            "#404e55",
            "#3f5655",
            "#3d6756",
            "#398957",
            "#379a58",
            "#35ab59",
            "#33bc5a",
            "#32c45a",
            "#30cc5a"
          ]);
      _data.push(endAngle);
      var arc = d3
        .arc()
        .innerRadius(radius - radius / 3)
        .outerRadius(radius)
        .startAngle(function(d) {
          return d;
        })
        .endAngle(function(d, i) {
          return _data[i + 1];
        });
      var innerD = chart
        .append("g")
        .attr(
          "transform",
          `translate(${(this.width - this.margin.left) / 2}, ${(this.height -
            this.margin.top) /
            2})`
        );
      chart
        .append("g")
        .append("text")
        .attr("text-anchor", "start")
        .text("خنثی")
        .attr(
          "transform",
          `translate(${this.width / 2 - this.margin.left / 4},${(-2 *
            this.margin.top) /
            3})`
        )
        .style("font-size", "0.8em")
        .style("font-family", "Vazir-Light-FD");
      chart
        .append("g")
        .append("text")

        .text("فروش")
        .attr(
          "transform",
          `translate(${this.width / 4},${-0.4 * this.margin.top})`
        )
        .style("font-size", "0.8em")
        .style("font-family", "Vazir-Light-FD");
      chart
        .append("g")
        .append("text")

        .text("خرید قوی")
        .attr(
          "transform",
          `translate(${(7 * this.width) / 8},${this.margin.top / 5})`
        )
        .style("font-size", "0.8em")
        .style("font-family", "Vazir-Light-FD");
      chart
        .append("g")
        .append("text")

        .text("فروش قوی")
        .attr(
          "transform",
          `translate(${(1 * this.width) / 7},${this.margin.top / 5})`
        )
        .style("font-size", "0.8em")
        .style("font-family", "Vazir-Light-FD");
      chart
        .append("g")
        .append("text")

        .text("خرید")
        .attr(
          "transform",
          `translate(${0.72 * this.width},${-0.4 * this.margin.top})`
        )
        .style("font-size", "0.8em")
        .style("font-family", "Vazir-Light-FD");

      //? final statement
      chart
        .append("g")
        .append("text")

        .style("fill", this.getFullColor)
        .text(this.getFull())
        .attr(
          "transform",
          `translate(${this.width / 2},${0.7 * this.margin.top})`
        )
        .style("font-size", "0.9em")
        .style("font-family", "Vazir-Light-FD");

      var slice = innerD
        .append("g")
        .selectAll("path.slice")
        .data(data);

      slice
        .enter()
        .append("path")
        .attr("class", "slice")
        .attr("d", arc)
        .attr("fill", function(d) {
          return colorScale(d);
        });
      var needle = innerD
        .append("g")
        .append("path")
        .attr("class", "needle")
        .attr("fill-opacity", 1)
        .attr("stroke", "black")
        .attr("stroke-width", "2px");
      function update(oldValue, newValue) {
        needle
          .datum({ oldValue: oldValue })
          .transition()
          .duration(tt)
          .attrTween("d", lineTween(newValue));
      }

      function lineTween(newValue) {
        return function(d) {
          var interpolate = d3.interpolate(d.oldValue, newValue);

          return function(t) {
            var _in = interpolate(t) - halfPi,
              _im = _in - halfPi;
            // _ip = _in -halfPi/3;

            var topX = radius * Math.cos(_in),
              topY = radius * Math.sin(_in);

            var leftX = needleRad * Math.cos(_im),
              leftY = needleRad * Math.sin(_im);

            var rightX = needleRad * Math.cos(_im),
              rightY = needleRad * Math.sin(_im);

            return (
              d3.line()([
                [topX, topY],
                [leftX, leftY],
                [rightX, rightY]
              ]) + "Z"
            );
          };
        };
      }

      update(scale(this.sum), scale(this.sum));
      window.addEventListener("resize", this.renderChart);
    }
  },
  mounted() {
    // if (!this.$store.getters.isAuthenticated) {
    //   this.populateData();
    //   this.initrender();
    // }
  },
  watch: {
    Indicators() {
      // this.chartKey += 1;
      this.initrender();
      this.populateData();
      if (!(this.DataItems2 === undefined || this.DataItems2.length == 0)) {
        this.renderChart();
      }
    }
  }
};
</script>
<style scoped>
.blured {
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(10px);
}
</style>
