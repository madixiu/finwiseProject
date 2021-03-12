<template>
  <div class="card card-custom card-stretch gutter-b">
    <v-card>
      <v-card-title>وضعیت تکنیکال سهم</v-card-title>
      <v-divider class="mt-0"></v-divider>
      <div class="row">
        <div class="col-xxl-3 col-lg-3 col-md-4 col-sm-4">
          خرید
          <br />
          <v-chip color="#30cc5a"><span class="chiptext"> 4 </span></v-chip>
        </div>
        <div class="col-xxl-3 col-lg-3 col-md-44 col-sm-4">
          خنثی
          <br />
          <v-chip color="#404e55">
            <span class="chiptext"> 4 </span>
          </v-chip>
        </div>
        <div class="col-xxl-3 col-lg-3 col-md-4 col-sm-4">
          فروش
          <br />
          <v-chip color="#f63538"><span class="chiptext"> 4 </span></v-chip>
        </div>
      </div>
      <div class="row">
        <div class="col-xxl-12 col-lg-12 col-md-12 col-sm-12 mb-2">
          <div id="TechnicalGauge"></div>
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
      loading: true
    };
  },
  methods: {
    populateData() {
      this.DataItems2 = this.Indicators;
      this.loading = false;
    },
    renderChart() {
      if (document.getElementsByTagName("svg")) {
        d3.selectAll("svg").remove();
      }
      this.width = parseInt(d3.select("#TechnicalGauge").style("width"), 10);
      this.height = (this.width * 9) / 16;
      this.margin.top = this.height * 0.2;
      this.margin.bottom = 0;
      this.margin.right = this.width * 0.1;
      this.margin.left = this.width * 0.1;
      var parent = document.getElementById("TechnicalGauge");
      // eslint-disable-next-line no-unused-vars
      let svg = d3
        .select(parent)
        .append("svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
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
        scale = d3.scaleLinear().range([startAngle, endAngle]),
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
        
        .text("خنثی")
        .attr(
          "transform",
          `translate(${(this.width/2)+this.margin.left/10},${0})`
        )
        .style("font-size", "1.5em");
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
      // eslint-disable-next-line no-unused-vars
      // var text = innerD
      //   .append("g")
      //   .append("text")
      //   .attr("class", "text")
      //   .attr("text-anchor", "middle")
      //   .attr("dy", "-0.45em")
      // .classed("monospace", true);
      function update(oldValue, newValue) {
        needle
          .datum({ oldValue: oldValue })
          .transition()
          .duration(tt)
          .attrTween("d", lineTween(newValue))
          .on("end", function() {
            update(newValue, scale(Math.random()));
          });

        // text
        //   .datum({ oldValue: oldValue })
        //   .transition()
        //   .duration(tt)
        //   .attrTween("transform", transformTween(newValue))
        //   .tween("text", textTween(newValue));
      }

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

      update(scale(0), scale(Math.random()));

      window.addEventListener("resize", this.renderChart);
    }
  },
  mounted() {
    this.populateData();
    this.renderChart();
  },
  watch: {
    Indicators() {
      this.populateData();
      this.renderChart();
    }
  }
};
</script>
<style scoped>
.monospace {
  font-family: monospace, "Lucida Console", "Courier New", sans-serif;
  font-size: 16px;
  font-weight: bolder;
}
.chiptext {
  color: white;
}
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
