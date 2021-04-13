<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        بررسی اندیکاتورها
      </h3>
    </div>
    <div class="card-body d-flex flex-column">
      <div class="row">
        <div class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12">
          <div
            class="card card-custom  col-xxl-12 col-lg-12 col-md-12 col-sm-12"
          >
            <v-card id="ParentCard" :height="cardheight">
              <v-card-title id="ParentCardTitle">
                <span> مجموع </span><br />
              </v-card-title>
              <v-divider id="ParentDivider" class="mt-0 mb-0"></v-divider>
              <div id="ChartGeneral"></div>
            </v-card>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12">
          <div
            class="card card-custom  col-xxl-12 col-lg-12 col-md-12 col-sm-12"
          >
            <v-card :height="cardheight">
              <v-card-title> <span> Moving Average </span><br /> </v-card-title>
              <v-divider class="mt-0 mb-0"></v-divider>
              <div id="ChartGeneral2"></div>
            </v-card>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12">
          <div
            class="card card-custom col-xxl-12 col-xl-12 col-lg-12 col-md-12 col-sm-12"
          >
            <v-card :height="cardheight">
              <v-card-title> <span> Indicators </span><br /> </v-card-title>
              <v-divider class="mt-0 mb-0"></v-divider>
              <div id="ChartGeneral3"></div>
            </v-card>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-3 col-md-6 col-lg-6 col-xs-12">
          <div
            class="card card-custom col-xxl-12 col-xl-12 col-lg-12 col-md-12 col-sm-12"
          >
            <v-card :height="cardheight">
              <v-card-title>
                <h6>تایم فریم <v-chip small>روزانه</v-chip></h6>
                <h6>
                  آخرین بروزرسانی :

                  <span class="cellItem">{{
                    this.lastUpdate.substring(0, 4) +
                      "/" +
                      this.lastUpdate.substring(4, 6) +
                      "/" +
                      this.lastUpdate.substring(6, 8)
                  }}</span>
                </h6>
              </v-card-title>
              <v-divider class="mt-0 "></v-divider>
              <v-data-table
                :headers="headers"
                :items="DataItems2"
                dense
                disable-sort
                :items-per-page="10"
                class="elevation-1 FinancialStrength"
              >
                <template v-slot:[`item.title`]="{ item }">
                  <v-chip small label>
                    <span>{{ item.title }} </span></v-chip
                  >
                </template>
                <template v-slot:[`item.Value`]="{ item }">
                  <span class="cellItem">{{
                    numberWithCommas(roundTo(item.Value, 2))
                  }}</span>
                </template>
              </v-data-table>
            </v-card>
          </div>
        </div>
      </div>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import * as d3 from "d3";
export default {
  name: "TechnicalDetailsWidget",
  props: ["notices"],
  data() {
    return {
      search: "",
      loading: true,
      errorinData: false,
      margin: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0
      },
      height: 0,
      width: 0,

      Indicators: [
        "Signal_PSAR",
        "Signal_PSAR",
        "Signal_Aroon",
        "Signal_Williams",
        "Signal_Ultimate",
        "Signal_Awesome",
        "Signal_CCI",
        "Signal_MOM",
        "Signal_MFI",
        "Signal_ADX",
        "Signal_StochRSI",
        "Signal_MACD",
        "Signal_Stoch",
        "Signal_RSI"
      ],
      mas: [
        "Signal_HMA",
        "Signal_VAMA",
        "Signal_KETLER",
        "Signal_ICHI",
        "Signal_SMA200",
        "Signal_SMA100",
        "Signal_SMA50",
        "Signal_SMA20",
        "Signal_SMA10",
        "Signal_SMA5",
        "Signal_EMA200",
        "Signal_EMA100",
        "Signal_EMA50",
        "Signal_EMA20",
        "Signal_EMA10",
        "Signal_EMA5"
      ],
      headers: [
        {
          text: "عنوان",
          value: "title"
        },
        {
          text: "مقدار محاسبه شده",
          value: "Value"
        }
      ],
      lastUpdate: "",
      cardheight: 0,
      sum: 0,
      neutral: 0,
      positive: 0,
      negative: 0,
      sumMa: 0,
      neutralMa: 0,
      postivieMa: 0,
      negativeMa: 0,
      sumIndic: 0,
      neutralIndic: 0,
      postivieIndic: 0,
      negativeIndic: 0,
      DataItems2: []
    };
  },
  methods: {
    numberWithCommas(x) {
      if (!isNaN(x)) {
        let parts = x.toString().split(".");
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        return parts.join(".");
      } else {
        return "-";
      }
    },
    roundTo(n, digits) {
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
    populateData() {
      this.loading = true;
      try {
        let that1 = this;
        this.DataItems2 = [...this.notices];
        this.lastUpdate = this.notices[2]["Value"];
        // eslint-disable-next-line no-unused-vars
        var newArray = this.DataItems2.filter(function(el) {
          return (
            el.title != "persiandate" &&
            el.title != "firm" &&
            el.title != "sum_signal" &&
            el.title != "engdate" &&
            that1.Indicators.indexOf(el.title) < 0 &&
            that1.mas.indexOf(el.title) < 0
          );
        });
        ////
        var Moving = this.DataItems2.filter(function(el) {
          return that1.mas.indexOf(el.title) >= 0;
        });
        var Indic = this.DataItems2.filter(function(el) {
          return that1.Indicators.indexOf(el.title) >= 0;
        });

        Moving.forEach(function(element) {
          let val = element.Value;
          if (val == 1) {
            that1.positive = that1.positive + 1;
            that1.sum = that1.sum + 1;
            that1.postivieMa = that1.postivieMa + 1;
            that1.sumMa = that1.sumMa + 1;
          }
          if (val == -1) {
            that1.negative = that1.negative + 1;
            that1.sum = that1.sum - 1;
            that1.negativeMa = that1.negativeMa + 1;
            that1.sumMa = that1.sumMa - 1;
          }
          if (val == 0) {
            that1.neutral = that1.neutral + 1;
            that1.neutralMa = that1.neutralMa + 1;
          }
        });
        Indic.forEach(function(element) {
          let val = element.Value;
          if (val == 1) {
            that1.positive = that1.positive + 1;
            that1.sum = that1.sum + 1;
            that1.postivieIndic = that1.postivieIndic + 1;
            that1.sumIndic = that1.sumIndic + 1;
          }
          if (val == -1) {
            that1.negative = that1.negative + 1;
            that1.sum = that1.sum - 1;
            that1.negativeIndic = that1.negativeIndic + 1;
            that1.sumIndic = that1.sumIndic - 1;
          }
          if (val == 0) {
            that1.neutral = that1.neutral + 1;
            that1.neutralIndic = that1.neutralIndic + 1;
          }
        });
        // this.sum = this.DataItems2[0].sum_signal;
        if (this.sum > 17) {
          this.sum = 17;
        }
        if (this.sum < -17) {
          this.sum = -17;
        }
        this.DataItems2 = newArray;
        this.errorinData = false;
        // console.log("done");
        // console.log( this.DataItems2);
      } catch {
        console.error("error");
        this.DataItems2 = [];
        this.loading = false;
        this.errorinData = true;
      }
    },
    initrender() {
      if (document.getElementById("ChartGeneral_svg")) {
        d3.selectAll("#ChartGeneral_svg").remove();
      }
      if (document.getElementById("ChartGeneral_svg")) {
        d3.selectAll("#ChartGeneral2_svg").remove();
      }
      if (document.getElementById("ChartGeneral_svg")) {
        d3.selectAll("#ChartGeneral3_svg").remove();
      }
      this.width = parseInt(d3.select("#ChartGeneral").style("width"), 10);
      this.height =
        parseInt(d3.select("#ParentCard").style("height"), 10) -
        parseInt(d3.select("#ParentDivider").style("height"), 10) -
        parseInt(d3.select("#ParentCardTitle").style("height"), 10);
      this.margin.top = this.height * 0.15;
      this.margin.bottom = 0;
      this.margin.right = this.width * 0.1;
      this.margin.left = this.width * 0.1;
      let that = this;
      var n = 20,
        r = 5,
        p = 1000;
      // eslint-disable-next-line no-unused-vars
      var parent = document.getElementById("ChartGeneral");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "ChartGeneral_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
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
      var parent2 = document.getElementById("ChartGeneral2");
      // eslint-disable-next-line no-unused-vars
      var svg2 = d3
        .select(parent2)
        .append("svg")
        .attr("id", "ChartGeneral2_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      const chart2 = svg2
        .append("svg")
        .attr(
          "transform",
          `translate(${this.width * 0.3}, ${this.height * 0.3})`
        )
        .attr("width", this.width * 0.5)
        .attr("height", this.height * 0.5);

      var g2 = chart2
        .selectAll("g")
        .data(d3.range(0, 2 * Math.PI, (2 * Math.PI) / n))
        .enter()
        .append("g")
        .attr("transform", function(d) {
          var x = that.width * 0.4 * (0.35 * Math.cos(d) + 0.5),
            y = that.height * 0.4 * (0.35 * Math.sin(d) + 0.5);
          return "translate(" + [x, y] + ")rotate(" + (d * 180) / Math.PI + ")";
        });
      // eslint-disable-next-line no-unused-vars
      chart2
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
      var moons2 = g2.append("path").attr("fill", "#212529");
      d3.timer(function(t) {
        var θ = 2 * Math.PI * ((t % p) / p);
        moons2.attr("d", function(d) {
          return moon((θ + d) % (2 * Math.PI));
        });
      });
      var parent3 = document.getElementById("ChartGeneral3");
      // eslint-disable-next-line no-unused-vars
      var svg3 = d3
        .select(parent3)
        .append("svg")
        .attr("id", "ChartGeneral3_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      const chart3 = svg3
        .append("svg")
        .attr(
          "transform",
          `translate(${this.width * 0.3}, ${this.height * 0.3})`
        )
        .attr("width", this.width * 0.5)
        .attr("height", this.height * 0.5);

      var g3 = chart3
        .selectAll("g")
        .data(d3.range(0, 2 * Math.PI, (2 * Math.PI) / n))
        .enter()
        .append("g")
        .attr("transform", function(d) {
          var x = that.width * 0.4 * (0.35 * Math.cos(d) + 0.5),
            y = that.height * 0.4 * (0.35 * Math.sin(d) + 0.5);
          return "translate(" + [x, y] + ")rotate(" + (d * 180) / Math.PI + ")";
        });
      chart3
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
      // eslint-disable-next-line no-unused-vars
      var moons3 = g3.append("path").attr("fill", "#212529");
      d3.timer(function(t) {
        var θ = 2 * Math.PI * ((t % p) / p);
        moons3.attr("d", function(d) {
          return moon((θ + d) % (2 * Math.PI));
        });
      });
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
    getFullMA() {
      if (this.sumMa > 10.2) {
        return "خرید قوی";
      }
      if (this.sumMa > 3.4) {
        return "خرید";
      }
      if (this.sumMa > -3.4) {
        return "خنثی";
      }
      if (this.sumMa > -10.2) {
        return "فروش";
      }
      if (this.sumMa < -10.2) {
        return "فروش قوی";
      }
    },
    getFullColorMA() {
      if (this.sumMa > 10.2) {
        return "#30cc5a";
      }
      if (this.sumMa > 3.4) {
        return "#379a58";
      }
      if (this.sumMa > -3.4) {
        return "#404e55";
      }
      if (this.sumMa > -10.2) {
        return "#b33b43";
      }
      if (this.sumMa < -10.2) {
        return "#f63538";
      }
    },
    getFullIN() {
      if (this.sumIndic > 10.2) {
        return "خرید قوی";
      }
      if (this.sumIndic > 3.4) {
        return "خرید";
      }
      if (this.sumIndic > -3.4) {
        return "خنثی";
      }
      if (this.sumIndic > -10.2) {
        return "فروش";
      }
      if (this.sumIndic < -10.2) {
        return "فروش قوی";
      }
    },
    getFullColorIN() {
      if (this.sumIndic > 10.2) {
        return "#30cc5a";
      }
      if (this.sumIndic > 3.4) {
        return "#379a58";
      }
      if (this.sumIndic > -3.4) {
        return "#404e55";
      }
      if (this.sumIndic > -10.2) {
        return "#b33b43";
      }
      if (this.sumIndic < -10.2) {
        return "#f63538";
      }
    },
    renderChart() {
      if (document.getElementById("ChartGeneral_svg")) {
        d3.selectAll("#ChartGeneral_svg").remove();
      }
      if (document.getElementById("ChartGeneral2_svg")) {
        d3.selectAll("#ChartGeneral2_svg").remove();
      }
      if (document.getElementById("ChartGeneral3_svg")) {
        d3.selectAll("#ChartGeneral3_svg").remove();
      }
      this.width = parseInt(d3.select("#ChartGeneral").style("width"), 10);
      this.height =
        parseInt(d3.select("#ParentCard").style("height"), 10) -
        parseInt(d3.select("#ParentDivider").style("height"), 10) -
        parseInt(d3.select("#ParentCardTitle").style("height"), 10);
      this.margin.top = this.height * 0.1;
      this.margin.bottom = this.height * 0.1;
      this.margin.right = this.width * 0.1;
      this.margin.left = this.width * 0.1;
      // eslint-disable-next-line no-unused-vars
      var parent = document.getElementById("ChartGeneral");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "ChartGeneral_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      var parent2 = document.getElementById("ChartGeneral2");
      // eslint-disable-next-line no-unused-vars
      var svg2 = d3
        .select(parent2)
        .append("svg")
        .attr("id", "ChartGeneral2_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      var parent3 = document.getElementById("ChartGeneral3");
      // eslint-disable-next-line no-unused-vars
      var svg3 = d3
        .select(parent3)
        .append("svg")
        .attr("id", "ChartGeneral3_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      // eslint-disable-next-line no-unused-vars
      const chart = svg
        .append("g")
        .attr("transform", `translate(${this.margin.left}, ${this.margin.top})`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      const chart2 = svg2
        .append("g")

        .attr(
          "transform",
          `translate(${this.margin.left}, ${this.margin.top})`
        );
      const chart3 = svg3
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
        .innerRadius(radius - radius / 10)
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
          `translate(${(this.width - this.margin.left - this.margin.right) /
            2}, ${this.height * 0.6})`
        );
      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`خنثی : ${this.neutral}`)
        .attr("transform", `translate(${0},${this.margin.top * 2})`)
        .style("font-family", "Vazir-Medium-FD")
        .style("font-size", `${this.width / 330}em`);

      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`خرید : ${this.positive}`)
        .attr(
          "transform",
          `translate(${this.width * 0.2},${this.margin.top * 2})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("fill", "green")
        .style("font-size", `${this.width / 330}em`);
      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`فروش : ${this.negative}`)
        .attr(
          "transform",
          `translate(${-this.width * 0.2},${this.margin.top * 2})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("fill", "red")
        .style("font-size", `${this.width / 330}em`);
      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text("خنثی")
        .attr("transform", `translate(${0},${-1.1 * radius})`)
        .style("font-size", `${this.width / 330}em`);
      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "start")
        .text("فروش")
        .attr(
          "transform",
          `translate(${-2 * this.margin.left},${-1.1 *
            radius *
            Math.sin((3 * pi) / 4)})`
        )
        .style("font-size", `${this.width / 330}em`);
      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "end")
        .text("خرید قوی")
        .attr("transform", `translate(${1.05 * radius},${0})`)
        .style("font-size", `${this.width / 330}em`);
      innerD
        .append("g")
        .append("text")

        .text("فروش قوی")
        .attr("transform", `translate(${-1.05 * radius},${0})`)
        .style("font-size", `${this.width / 330}em`);
      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "end")
        .text("خرید")
        .attr(
          "transform",
          `translate(${2 * this.margin.left},${-1.1 *
            radius *
            Math.sin(pi / 4)})`
        )
        .style("font-size", `${this.width / 330}em`);
      innerD
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .style("fill", this.getFullColor)
        .text(this.getFull())
        .attr("transform", `translate(${0},${this.margin.top})`)
        .style("font-size", `${this.width / 175}em`);

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
      var innerD2 = chart2
        .append("g")
        .attr(
          "transform",
          `translate(${(this.width - this.margin.left - this.margin.right) /
            2}, ${this.height * 0.6})`
        );
      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`خنثی : ${this.neutralMa}`)
        .attr("transform", `translate(${0},${this.margin.top * 2})`)
        .style("font-family", "Vazir-Medium-FD")
        .style("font-size", `${this.width / 330}em`);

      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`خرید : ${this.postivieMa}`)
        .attr(
          "transform",
          `translate(${this.width * 0.2},${this.margin.top * 2})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("fill", "green")
        .style("font-size", `${this.width / 330}em`);
      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`فروش : ${this.negativeMa}`)
        .attr(
          "transform",
          `translate(${-this.width * 0.2},${this.margin.top * 2})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("fill", "red")
        .style("font-size", `${this.width / 330}em`);

      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text("خنثی")
        .attr("transform", `translate(${0},${-1.1 * radius})`)
        .style("font-size", `${this.width / 330}em`);
      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "start")
        .text("فروش")
        .attr(
          "transform",
          `translate(${-2 * this.margin.left},${-1.1 *
            radius *
            Math.sin((3 * pi) / 4)})`
        )
        .style("font-size", `${this.width / 330}em`);
      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "end")
        .text("خرید قوی")
        .attr("transform", `translate(${1.05 * radius},${0})`)
        .style("font-size", `${this.width / 330}em`);
      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "start")
        .text("فروش قوی")
        .attr("transform", `translate(${-1.05 * radius},${0})`)
        .style("font-size", `${this.width / 330}em`);
      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "end")
        .text("خرید")
        .attr(
          "transform",
          `translate(${2 * this.margin.left},${-1.1 *
            radius *
            Math.sin((3 * pi) / 4)})`
        )
        .style("font-size", `${this.width / 330}em`);
      innerD2
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .style("fill", this.getFullColorMA)
        .text(this.getFullMA())
        .attr("transform", `translate(${0},${this.margin.top})`)
        .style("font-size", `${this.width / 175}em`);

      var slice2 = innerD2
        .append("g")
        .selectAll("path.slice")
        .data(data);

      // eslint-disable-next-line no-unused-vars
      slice2
        .enter()
        .append("path")
        .attr("class", "slice")
        .attr("d", arc)
        .attr("fill", function(d) {
          return colorScale(d);
        });
      var innerD3 = chart3
        .append("g")
        .attr(
          "transform",
          `translate(${(this.width - this.margin.left - this.margin.right) /
            2}, ${this.height * 0.6})`
        );
      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`خنثی : ${this.neutralIndic}`)
        .attr("transform", `translate(${0},${this.margin.top * 2})`)
        .style("font-family", "Vazir-Medium-FD")
        .style("font-size", `${this.width / 330}em`);

      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`خرید : ${this.postivieIndic}`)
        .attr(
          "transform",
          `translate(${this.width * 0.2},${this.margin.top * 2})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("fill", "green")
        .style("font-size", `${this.width / 330}em`);
      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`فروش : ${this.negativeIndic}`)
        .attr(
          "transform",
          `translate(${-this.width * 0.2},${this.margin.top * 2})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("fill", "red")
        .style("font-size", `${this.width / 330}em`);

      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text("خنثی")
        .attr("transform", `translate(${0},${-1.1 * radius})`)
        .style("font-size", `${this.width / 330}em`);
      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "start")
        .text("فروش")
        .attr(
          "transform",
          `translate(${-2 * this.margin.left},${-1.1 *
            radius *
            Math.sin((3 * pi) / 4)})`
        )
        .style("font-size", `${this.width / 330}em`);
      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "end")
        .text("خرید قوی")
        .attr("transform", `translate(${1.05 * radius},${0})`)
        .style("font-size", `${this.width / 330}em`);
      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "start")
        .text("فروش قوی")
        .attr("transform", `translate(${-1.05 * radius},${0})`)
        .style("font-size", `${this.width / 330}em`);
      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "end")
        .text("خرید")
        .attr(
          "transform",
          `translate(${2 * this.margin.left},${-1.1 *
            radius *
            Math.sin((3 * pi) / 4)})`
        )
        .style("font-size", `${this.width / 330}em`);
      innerD3
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .style("fill", this.getFullColorIN)
        .text(this.getFullIN())
        .attr("transform", `translate(${0},${this.margin.top})`)
        .style("font-size", `${this.width / 175}em`);
      var slice3 = innerD3
        .append("g")
        .selectAll("path.slice")
        .data(data);

      // eslint-disable-next-line no-unused-vars
      slice3
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
      var needle2 = innerD2
        .append("g")
        .append("path")
        .attr("class", "needle")
        .attr("fill-opacity", 1)
        .attr("stroke", "black")
        .attr("stroke-width", "2px");
      var needle3 = innerD3
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
      function update2(oldValue, newValue) {
        needle2
          .datum({ oldValue: oldValue })
          .transition()
          .duration(tt)
          .attrTween("d", lineTween(newValue));
      }
      function update3(oldValue, newValue) {
        needle3
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
      update2(scale(this.sumMa), scale(this.sumMa));
      update3(scale(this.sumIndic), scale(this.sumIndic));
      window.addEventListener("resize", this.renderChart);
    },
    heightCalc() {
      if (screen.height * 2 > screen.width) {
        // console.log(screen.height * 0.5)
        return Math.max(300, screen.height * 0.35);
      } else {
        if (screen.height * 1.5 > screen.width) {
          return Math.max(400, screen.height * 0.4);
        } else {
          if (screen.height > screen.width) {
            return Math.max(400, screen.height * 0.55);
          }
          // console.log(screen.width * 0.5)
          else return Math.max(400, screen.height * 0.7);
        }
      }
    },
    renderNodata() {
      // console.log('NoDataLaunched')
      if (document.getElementById("ChartGeneral_svg")) {
        d3.selectAll("#ChartGeneral_svg").remove();
      }
      if (document.getElementById("ChartGeneral2_svg")) {
        d3.selectAll("#ChartGeneral2_svg").remove();
      }
      if (document.getElementById("ChartGeneral3_svg")) {
        d3.selectAll("#ChartGeneral3_svg").remove();
      }
      this.width = parseInt(d3.select("#ChartGeneral").style("width"), 10);
      this.height =
        parseInt(d3.select("#ParentCard").style("height"), 10) -
        parseInt(d3.select("#ParentDivider").style("height"), 10) -
        parseInt(d3.select("#ParentCardTitle").style("height"), 10);
      this.margin.top = this.height * 0.15;
      this.margin.bottom = 0;
      this.margin.right = this.width * 0.1;
      this.margin.left = this.width * 0.1;
      var parent = document.getElementById("ChartGeneral");
      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(parent)
        .append("svg")
        .attr("id", "ChartGeneral_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      const chart = svg
        .append("svg")
        .attr(
          "transform",
          `translate(${this.width * 0.3}, ${this.height * 0.3})`
        )
        .attr("width", this.width * 0.5)
        .attr("height", this.height * 0.5);
      chart
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`دیتا موجود نیست`)
        .attr(
          "transform",
          `translate(${this.margin.left * 2},${this.margin.top * 1.3})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("font-size", `${this.width / 400}em`);
      var parent2 = document.getElementById("ChartGeneral2");
      // eslint-disable-next-line no-unused-vars
      var svg2 = d3
        .select(parent2)
        .append("svg")
        .attr("id", "ChartGeneral2_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      const chart2 = svg2
        .append("svg")
        .attr(
          "transform",
          `translate(${this.width * 0.3}, ${this.height * 0.3})`
        )
        .attr("width", this.width * 0.5)
        .attr("height", this.height * 0.5);
      // eslint-disable-next-line no-unused-vars
      chart2
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`دیتا موجود نیست`)
        .attr(
          "transform",
          `translate(${this.margin.left * 2},${this.margin.top * 1.3})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("font-size", `${this.width / 400}em`);
      var parent3 = document.getElementById("ChartGeneral3");
      // eslint-disable-next-line no-unused-vars
      var svg3 = d3
        .select(parent3)
        .append("svg")
        .attr("id", "ChartGeneral3_svg")
        .attr("viewBox", `0 0 ${this.width},${this.height}`)
        .attr("preserveAspectRatio", "xMidYMid meet");
      const chart3 = svg3
        .append("svg")
        .attr(
          "transform",
          `translate(${this.width * 0.3}, ${this.height * 0.3})`
        )
        .attr("width", this.width * 0.5)
        .attr("height", this.height * 0.5);
      chart3
        .append("g")
        .append("text")
        .attr("text-anchor", "middle")
        .text(`دیتا موجود نیست`)
        .attr(
          "transform",
          `translate(${this.margin.left * 2},${this.margin.top * 1.3})`
        )
        .style("font-family", "Vazir-Medium-FD")
        .style("font-size", `${this.width / 400}em`);
      // eslint-disable-next-line no-unused-vars
      // eslint-disable-next-line no-unused-vars
    }
  },
  created() {
    this.cardheight = this.heightCalc();
  },
  mounted() {
    this.initrender();
    // this.populateData();
    // if (!this.errorinData) {
    //   this.renderChart();
    // }
  },
  watch: {
    notices: {
      // eslint-disable-next-line no-unused-vars
      handler: function(val, oldVal) {
        this.populateData();
        // console.log(this.errorinData);
        if (!(this.DataItems2 === undefined || this.DataItems2.length == 0)) {
          if (!this.errorinData) {
            // console.log(this.errorinData)
            this.renderChart();
            this.loading = false;
          }
        } else {
          // console.log(this.errorinData)
          this.loading = false;
          this.renderNodata();
        }
      },
      deep: true
    }
    // notices() {
    //   this.populateData();
    //   console.log(this.errorinData);
    //   if (!(this.DataItems2 === undefined || this.DataItems2.length == 0)) {
    //     if (!this.errorinData) {
    //       this.renderChart();
    //     this.loading = false;
    //     }
    //   } else {
    //     this.loading = false;
    //     this.errorinData = true;
    //   }
    // }
  }
};
</script>
<style scoped>
.cellItem {
  direction: ltr;
  text-align: right;
  font-family: "Vazir-Medium-FD";
  font-weight: 700;
  font-size: 1.1em;
}
.FinancialStrength {
  direction: rtl;
  text-align: right;
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
</style>
