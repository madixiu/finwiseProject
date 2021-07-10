<template>
  <div class="card card-custom card-stretch gutter-b" id="parentDiv">
    <v-card >
      <v-card-title>وضعیت تکنیکال سهم</v-card-title>
      <v-divider class="mt-0"></v-divider>
      <div v-show="this.$store.getters.isAuthenticated">
        <div class="row">
          <div
            class="col-xxl-4 col-lg-4 col-md-4 col-sm-12"
            style="direction: rtl;text-align:center"
          >
            <span>خرید </span>

            <br />
            <span class="chiptext" style="color:#30cc5a">{{ positive }}</span>
          </div>
          <div
            class="col-xxl-4 col-lg-4 col-md-4 col-sm-12"
            style="direction: rtl;text-align:center"
          >
            <span>خنثی </span>
            <br />

            <span class="chiptext" style="color:#414554">{{ neutral }} </span>
          </div>
          <div
            class="col-xxl-4 col-lg-4 col-md-4 col-sm-12"
            style="direction: rtl;text-align:center"
          >
            <span>فروش </span>
            <br />
            <span class="chiptext" style="color:#f63538">{{ negative }}</span>
          </div>
        </div>
        <div class="row">
          <div class="col-xxl-12 col-lg-12 col-md-12 col-sm-12 mb-2">
            <div id="TechnicalGauge"></div>
          </div>
        </div>
      </div>
      <div
        class="lockedTechnical"
        v-show="!this.$store.getters.isAuthenticated"
      >
        <div class="row lockedTechnical">
          <v-icon class="lockIcon" size="30px">mdi-lock</v-icon>
        </div>
        <div class="row lockedTechnical">
          <v-btn
            color="#607d8b"
            class="ma-2 mt-1"
            elevation="5"
            style="margin: auto;"
            @click="onClick"
            >ورود</v-btn
          >
        </div>
      </div>

      <!--end::Header-->
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import * as d3 from "d3";

export default {
  name: "TechnicalIndicators",
  props: ["Indicators"],
  data() {
    return {
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
      if (document.getElementsByTagName("svg")) {
        d3.selectAll("svg").remove();
      }
      this.width = parseInt(d3.select("#parentDiv").style("width"), 10);
      this.height = (this.width * 9) / 16;
      this.margin.top = this.height * 0.5;
      this.margin.bottom = 0;
      this.margin.right = this.width * 0.1;
      this.margin.left = this.width * 0.1;
      // eslint-disable-next-line no-unused-vars
      var parent = document.getElementById("TechnicalGauge");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "chartContainer")
        .attr("viewBox", `0 0 ${this.width} ${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      // eslint-disable-next-line no-unused-vars
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
      var parent = document.getElementById("chartContainer");
      var svg = d3.select(parent);
      if (document.getElementsByTagName("svg")) {
        d3.selectAll("g").remove();
      }
      const chart = svg
        .append("g")
        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      // eslint-disable-next-line no-unused-vars
      var n = 5,
        // eslint-disable-next-line no-unused-vars
        radius = this.width / 2 - this.margin.right * 2,
        // eslint-disable-next-line no-unused-vars
        needleRad = this.width / 200,
        pi = Math.PI,
        // eslint-disable-next-line no-unused-vars
        halfPi = pi / 2,
        endAngle = pi / 2,
        startAngle = -endAngle,
        data = d3.range(startAngle, endAngle, pi / n),
        // eslint-disable-next-line no-unused-vars
        _data = data.slice(0),
        // eslint-disable-next-line no-unused-vars
        tt = 3000,
        // eslint-disable-next-line no-unused-vars
        scale = d3
          .scaleLinear()
          .range([startAngle, endAngle])
          .domain([-17, 17]),
        // eslint-disable-next-line no-unused-vars

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
        .innerRadius(radius - radius / 20)
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
        .style("font-size", "1.3em");
      chart
        .append("g")
        .append("text")

        .text("فروش")
        .attr(
          "transform",
          `translate(${this.width / 4},${-0.4 * this.margin.top})`
        )
        .style("font-size", "1.1em");
      chart
        .append("g")
        .append("text")

        .text("خرید قوی")
        .attr(
          "transform",
          `translate(${(7 * this.width) / 8},${this.margin.top / 5})`
        )
        .style("font-size", "1.1em");
      chart
        .append("g")
        .append("text")

        .text("فروش قوی")
        .attr(
          "transform",
          `translate(${(1 * this.width) / 7},${this.margin.top / 5})`
        )
        .style("font-size", "1.1em");
      chart
        .append("g")
        .append("text")

        .text("خرید")
        .attr(
          "transform",
          `translate(${0.72 * this.width},${-0.4 * this.margin.top})`
        )
        .style("font-size", "1.1em");
      chart
        .append("g")
        .append("text")

        .style("fill", this.getFullColor)
        .text(this.getFull())
        .attr(
          "transform",
          `translate(${this.width / 2},${0.7 * this.margin.top})`
        )
        .style("font-size", "2.3em");

      var slice = innerD
        .append("g")
        .selectAll("path.slice")
        .data(data);

      // eslint-disable-next-line no-unused-vars
      slice
        .enter()
        .append("path")
        .attr("class", "slice")
        .attr("d", arc)
        .attr("fill", function(d) {
          return colorScale(d);
        });

      // eslint-disable-next-line no-unused-vars
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
    if (!this.$store.getters.isAuthenticated) {
      this.populateData();
      this.initrender();
    }
  },
  watch: {
    Indicators() {
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
.lockIcon {
  margin-top: 90px;
  margin-left: auto;
  margin-right: auto;
}
.lockedTechnical {
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  height: 50%;
  text-align: center;
}
.monospace {
  font-family: monospace, "Lucida Console", "Courier New", sans-serif;
  font-size: 16px;
  font-weight: bolder;
}
.chiptext {
  font-family: "Vazir-Medium-FD";
  font-size: 2.4em;
  text-align: center;
}
.rtl_centerd {
  font-size: 1em;
  direction: rtl;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left;
}
.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
}
.greenItem {
  color: #088a2f93 !important;
}
.titleHeaders {
  padding: 5px;
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
.v-timeline {
  direction: ltr !important;

  text-align: left;
}
.v-timeline:before {
  margin-left: 50%;
}
.customAlert {
  font-family: "Vazir-Medium-FD" !important;
}
</style>
