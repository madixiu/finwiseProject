<template>
  <div class="card card-custom card-stretch gutter-b">
    <v-skeleton-loader
      type=" table-heading, table-thead"
      v-if="loading"
    ></v-skeleton-loader>
    <v-card v-if="loading == false">
      <v-card-title>وضعیت تکنیکال سهم</v-card-title>

      <div class="row">
        <div class="col-xxl-12 col-lg-12 col-md-12 col-sm-12">
          <div id="TechnicalGauge"></div>
          <!-- <v-btn text color="teal accent-4" @click="reveal = true">
            اطلاعات بیشتر
          </v-btn> -->
        </div>
      </div>
      <!--end::Header-->
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
// import ApexChart from "@/view/content/charts/ApexChart";
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "TechnicalIndicators",
  props: ["Indicators"],
  data() {
    return {
      search: "",
      margin: {
        top: 20,
        right: 200,
        bottom: 0,
        left: 150
      },
      heigh: 200,
      width: 200,
      DataItems2: [],
      loading: true
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      // this.DataItems2 = this.Indicators;
      this.loading = false;
    },
    renderChart() {
      var parent = document.getElementById("TechnicalGauge");
      // eslint-disable-next-line no-unused-vars
      let svg = d3
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
      // eslint-disable-next-line no-unused-vars
      var n = 30;
      var radius = this.width / 2 - this.margin.top * 2;
      var pi = Math.PI,
        // halfPi = pi / 2,
        // tt = 3000,
        // needleRad = 20,
        // scale = d3.scaleLinear().range([startAngle, endAngle]),
        endAngle = pi / 2,
        // eslint-disable-next-line no-unused-vars
        startAngle = -endAngle;
      var data = d3.range(startAngle, endAngle, pi / n);
      var _data = data.slice(0);
      // var colorScale = d3
      //   .scaleSequential(d3.interpolateRdYlGn)
      //   .domain([data[0], data[data.length - 1]]);
      _data.push(endAngle);

      // eslint-disable-next-line no-unused-vars
      var arc = d3
        .arc()
        .innerRadius(radius - radius / 5)
        .outerRadius(radius)
        .startAngle(function(d) {
          return d;
        })
        .endAngle(function(d, i) {
          return _data[i + 1];
        });
      // svg.append(arc)
      // var slice = svg
      //   .append("g")
      //   .selectAll("path.slice")
      //   .data(data);

      // slice
      //   .enter()
      //   .append("path")
      //   .attr("class", "slice")
      //   .attr("d", arc)
      //   .attr("fill", function(d) {
      //     return colorScale(d);
      //   });

      // // eslint-disable-next-line no-unused-vars
      // var needle = svg
      //   .append("g")
      //   .append("path")
      //   .attr("class", "needle")
      //   .attr("fill-opacity", 0.7)
      //   .attr("stroke", "black");
      // // eslint-disable-next-line no-unused-vars
      // var text = svg
      //   .append("g")
      //   .append("text")
      //   .attr("class", "text")
      //   .attr("text-anchor", "middle")
      //   .attr("dy", "-0.45em")
      //   .classed("monospace", true);
      // function update(oldValue, newValue) {
      //   needle
      //     .datum({ oldValue: oldValue })
      //     .transition()
      //     .duration(tt)
      //     .attrTween("d", lineTween(newValue))
      //     .on("end", function() {
      //       update(newValue, scale(Math.random()));
      //     });

      //   text
      //     .datum({ oldValue: oldValue })
      //     .transition()
      //     .duration(tt)
      //     .attrTween("transform", transformTween(newValue))
      //     .tween("text", textTween(newValue));
      // }

      // function textTween(newValue) {
      //   return function(d) {
      //     var that = d3.select(this),
      //       i = d3.interpolate(d.oldValue, newValue);

      //     return function(t) {
      //       that.text(d3.format(".1%")(scale.invert(i(t))));
      //     };
      //   };
      // }

      // function transformTween(newValue) {
      //   return function(d) {
      //     var interpolate = d3.interpolate(d.oldValue, newValue);

      //     return function(t) {
      //       var _in = interpolate(t) - halfPi,
      //         centerX = (radius + 20) * Math.cos(_in),
      //         centerY = (radius + 20) * Math.sin(_in);
      //       return "translate(" + centerX + "," + centerY + ")";
      //     };
      //   };
      // }

      // function lineTween(newValue) {
      //   return function(d) {
      //     var interpolate = d3.interpolate(d.oldValue, newValue);

      //     return function(t) {
      //       var _in = interpolate(t) - halfPi,
      //         _im = _in - halfPi,
      //         _ip = _in + halfPi;

      //       var topX = radius * Math.cos(_in),
      //         topY = radius * Math.sin(_in);

      //       var leftX = needleRad * Math.cos(_im),
      //         leftY = needleRad * Math.sin(_im);

      //       var rightX = needleRad * Math.cos(_ip),
      //         rightY = needleRad * Math.sin(_ip);

      //       return (
      //         d3.line()([
      //           [topX, topY],
      //           [leftX, leftY],
      //           [rightX, rightY]
      //         ]) + "Z"
      //       );
      //     };
      //   };
      // }

      // update(scale(0), scale(Math.random()));
    }
  },
  mounted() {
    this.populateData();
    this.renderChart();
  },
  watch: {
    notices() {
      // console.log("Watcher");
      this.populateData();
      this.renderChart();
      // console.log(this.Indicators);
    }
  }
};
</script>
<style scoped>
.rtl_centerd {
  direction: rtl;
  text-align: center;
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
  font-family: "Dirooz FD" !important;
}
</style>
