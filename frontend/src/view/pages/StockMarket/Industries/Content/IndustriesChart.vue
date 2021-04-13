/* eslint-disable no-unused-vars */
<template>
  <div class="card card-custom">
    <v-card id="ParentCard" :height="cardheight">
      <v-card-title id="ParentCardTitle">
        <span> sss صنایع </span>
      </v-card-title>
      <v-divider id="ParentDivider" class="mt-0 mb-0"></v-divider>
      <div class="row">
        <div class="col-xxl-10 col-lg-10 col-md-10 col-sm-10 mb-2">
          <div id="IndustriesChart"></div>
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
      cardheight: 0,
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
    // inputData() {
    //   this.populateData();
    //   // this.loading = false;
    //   this.renderChart();
    // }
    // ,loading(){
    //   console.log('LoadingCalled')
    // }
  },
  created() {
    this.cardheight = this.heightCalc();
  },
  // In the beginning...
  mounted() {
    // this.initrender();
    // this.populateData();
    // this.renderChart("T","T");
  },
  methods: {
    populateData() {
      if (!(this.inputData === undefined || this.inputData.length == 0)) {
        let ll = Object.assign({}, this.inputData);

        let tList = [];
        for (var tKey in ll) tList.push(ll[tKey]);
        this.DataItems2 = tList;
        if (!this.isEmpty(this.DataItems2)) {
          // this.loading = false;
          this.sortByMarketCap("D1");
          // console.log(this.DataItems2);
        }
      }
    },
    sortByMarketCap(M) {
      let f = [...this.DataItems2];
      f.sort(function(a, b) {
        return b[M] - a[M];
      });
      this.DataItems2 = [...f];
    },
    initrender() {
      if (document.getElementById("IndustriesChart_SVG")) {
        d3.selectAll("#IndustriesChart_SVG").remove();
      }
      this.width = parseInt(d3.select("#IndustriesChart").style("width"), 10);
      this.height =
        parseInt(d3.select("#ParentCard").style("height"), 10) -
        parseInt(d3.select("#ParentDivider").style("height"), 10) -
        parseInt(d3.select("#ParentCardTitle").style("height"), 10);
      this.margin.top = this.height * 0.1;
      this.margin.bottom = 0;
      this.margin.right = this.width * 0.1;
      this.margin.left = this.width * 0.1;
      console.log(this.width);
      console.log(this.height);
      // eslint-disable-next-line no-unused-vars
      var parent = document.getElementById("IndustriesChart");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "IndustriesChart_SVG")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      // eslint-disable-next-line no-unused-vars
      let that = this;
      var n = 20,
        r = 5,
        p = 1000;
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("svg")
        .attr(
          "transform",
          `translate(${this.width * 0.3}, ${this.height * 0.3})`
        )
        .attr("width", this.width * 0.5)
        .attr("height", this.height * 0.5);

      var g = chart
        .selectAll("g")
        .data(d3.range(0, 2 * Math.PI, (2 * Math.PI) / n))
        .enter()
        .append("g")
        .attr("transform", function(d) {
          var x = that.width * 0.4 * (0.35 * Math.cos(d) + 0.5),
            y = that.height * 0.4 * (0.35 * Math.sin(d) + 0.5);
          return "translate(" + [x, y] + ")rotate(" + (d * 180) / Math.PI + ")";
        });
      chart
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`در حال بارگذاری`)
        .attr(
          "transform",
          `translate(${this.margin.left * 2},${this.margin.top * 1.3})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("font-size", `${this.width / 500}em`);
      var moons = g.append("path").attr("fill", "#212529");
      d3.timer(function(t) {
        var θ = 2 * Math.PI * ((t % p) / p);
        moons.attr("d", function(d) {
          return moon((θ + d) % (2 * Math.PI));
        });
      });
      function moon(θ) {
        var rx0 = θ < Math.PI ? r : -r,
          s0 = θ < Math.PI ? 0 : 1,
          rx1 = r * Math.cos(θ),
          s1 =
            θ < Math.PI / 2 || (Math.PI <= θ && θ < (3 * Math.PI) / 2) ? 0 : 1;
        return (
          "M" +
          [0, r] +
          "A" +
          [rx0, r, 0, 0, s0, 0, -r] +
          "A" +
          [rx1, r, 0, 0, s1, 0, r]
        );
      }
    },
    renderChart() {
      this.loading = true;
      this.sortByMarketCap(this.SortBy);
      let Param = this.freq;
      // const tooltip = d3
      //   .select(parent)
      //   .append("div")
      //   .attr("class", "d3-tip")
      //   .style("position", "absolute")
      //   .style("visibility", "hidden");
      if (document.getElementById("IndustriesChart_SVG")) {
        d3.selectAll("#IndustriesChart_SVG").remove();
      }
      var parent = document.getElementById("IndustriesChart");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "IndustriesChart_SVG")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
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
            1.5
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
          ) * 1.5
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
        });
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
      this.loading = false;
      svg
        .append("text")
        .attr("class", "source")
        .attr("x", this.width / 2 + this.margin.right)
        .attr("y", this.height * 0.1)
        .attr("text-anchor", "start")
        .text("Source: FinWise")
        .style("font-weight", "700")
        .style("font-family", "'Tlwg Mono', sans-serif")
        .style("font-size", "10px")
        .style("opacity", "0.3");
      chart
        .append("text")
        .attr("class", "source")
        .attr("x", 0)
        .attr("y", this.height * 0.1)
        .attr("text-anchor", "start")
        .text("بازدهی")
        .style("font-weight", "700")
        .style("font-family", "Vazir")
        .style("font-size", "1em");
      chart
        .append("text")
        .attr("class", "source")
        .attr("x", 0)
        .attr("y", this.height * 0.8)
        .attr("text-anchor", "start")
        .text("ارزش بازار روز")
        .style("font-weight", "700")
        .style("font-family", "Vazir")
        .style("font-size", "1em");
    },
    heightCalc() {
      if (screen.height * 2 > screen.width) {
        // console.log(screen.height * 0.5)
        return Math.max(600, screen.height * 0.75);
      } else {
        if (screen.height * 1.5 > screen.width) {
          return Math.max(600, screen.height * 0.7);
        } else {
          if (screen.height > screen.width) {
            return Math.max(600, screen.height * 0.65);
          }
          // console.log(screen.width * 0.5)
          else return Math.max(600, screen.height * 0.6);
        }
      }
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
