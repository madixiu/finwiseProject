<template>
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        بیشترین حجم معاملات
      </h3>
      <v-subheader class="ltr_aligned" v-if="loading == false">
        آخرین به روز رسانی {{ DataItems[0]["persianDate"].slice(10, 16) }}
      </v-subheader>
    </div>
    <div id="chartContainer" class="card-body d-flex flex-column">
      <svg
        :height="height"
        :width="width"
        :viewBox="
          `0 0 ${width + margin.left + margin.right},${height +
            margin.top +
            margin.bottom}`
        "
        preserveAspectRatio="xMidYMid meet"
      >
        <g :transform="`translate(${margin.left}, ${margin.top})`">
          <g v-for="item in this.highestVolumes" :key="item.ticker">
            <rect
              class="boxt"
              :x="scale.x(item.ticker)"
              :y="scale.y(item.Vol)"
              :width="scale.x.bandwidth()"
              :height="height - scale.y(item.Vol)"
              :transform="`translate(${0}, ${-margin.bottom})`"
              style="fill:steelblue"
            ></rect>
          </g>
          <g
            v-axis:x="scale"
            :transform="`translate(0,${this.height - this.margin.bottom})`"
          ></g>
          <g
            v-axis:y="scale"
            :transform="`translate(${this.width - this.margin.right},0)`"
          ></g>
        </g>
        <g :transform="`translate(${margin.left}, ${margin.top})`">
          <g v-for="item in this.highestValues" :key="item.ticker">
            <rect
              class="boxt"
              :x="scale2.x(item.ticker)"
              :y="scale2.y(item.Value)"
              :width="scale2.x.bandwidth()"
              :height="height - scale2.y(item.Value)"
              :transform="`translate(${0}, ${-margin.bottom})`"
              style="fill:steelblue"
            ></rect>
          </g>
          <g
            v-axis2:x="scale2"
            :transform="`translate(0,${this.height - this.margin.bottom})`"
          ></g>
          <g
            v-axis2:y="scale2"
            :transform="`translate(${this.margin.left},0)`"
          ></g>
        </g>
      </svg>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";
// import { scaleLinear, scaleOrdinal, axisBottom } from "d3-scale";
// // import {json} from 'd3-request'
// import { hierarchy, treemap } from "d3-hierarchy";
// // To be explicit about which methods are from D3 let's wrap them around an object
// // Is there a better way to do this?
// // eslint-disable-next-line no-unused-vars
// let d3 = {
//   scaleLinear: scaleLinear,
//   scaleOrdinal: scaleOrdinal,
//   axisBottom: axisBottom,
//   // schemeCategory20: schemeCategory20,
//   // json: json,
//   hierarchy: hierarchy,
//   treemap: treemap
// };
// import data from "@/components/data/map2.json";
// import mapData from "./data/map2.json";
export default {
  // el:"#chartContainer",
  // name: "treemap",
  props: { inputData: Array, inputWidth: Number, inputHeight: Number },
  // the component's data
  data() {
    return {
      highestValues: [],
      highestVolumes: [],
      margin: {
        top: 30,
        right: 100,
        bottom: 20,
        left: 100
      }
    };
  },
  // You can do whatever when the selected node changes
  watch: {
    // eslint-disable-next-line no-unused-vars
  },
  created() {
    // this.loadData();
    this.width = this.inputWidth;
    this.height = this.inputHeight;
    console.log(this.height - this.margin.bottom - this.margin.top);
    this.jsonData = this.inputData;
    this.jsonData.sort((a, b) => b.Value - a.Value);
    this.highestValues = this.jsonData.slice(0, 10);
    console.log(this.highestValues);
    this.jsonData.sort((a, b) => b.Vol - a.Vol);
    this.highestVolumes = this.jsonData.slice(0, 10);
    console.log(this.highestVolumes);
    // this.sortedJson = this.jsonData.sort((a, b) => a.Value - b.Value);
    // this.lowestValues=this.sortedJson.slice(0,10)
    // console.log(this.lowestValues)
  },
  // In the beginning...
  mounted() {},
  // The reactive computed variables that fire rerenders
  computed: {
    scale() {
      const x = d3
        .scaleBand()
        .domain(this.highestVolumes.map(x => x.ticker))
        .rangeRound([
          this.width - this.margin.right,
          (this.width - this.margin.left) / 2
        ])
        .padding(0.15);
      const y = d3
        .scaleLinear()
        .domain([0, Math.max(...this.highestVolumes.map(x => x.Vol)) * 1.2])
        .rangeRound([this.height - this.margin.bottom, this.margin.top])
        .nice();
      return { x, y };
    },
    scale2() {
      const x = d3
        .scaleBand()
        .domain(this.highestValues.map(x => x.ticker))
        .range([this.margin.left, (this.width - this.margin.right) / 2])
        .padding(0.15);
      const y = d3
        .scaleLinear()
        .domain([0, Math.max(...this.highestValues.map(x => x.Value)) * 1.2])
        .range([this.height - this.margin.bottom, this.margin.top])
        .nice();
      return { x, y };
    }
  },
  methods: {},
  directives: {
    axis(el, binding) {
      const axis = binding.arg;
      const axisMethod = { x: "axisBottom", y: "axisRight" }[axis];
      const methodArg = binding.value[axis];
      if (axis == "y") {
        d3.select(el)
          .call(d3[axisMethod](methodArg))
          .attr("class", "yaxis");
      } else {
        d3.select(el)
          .call(d3[axisMethod](methodArg))
          .attr("class", "xaxis");
      }
    },
    axis2(el, binding) {
      const axis = binding.arg;
      const axisMethod = { x: "axisBottom", y: "axisRight" }[axis];
      const methodArg = binding.value[axis];
      if (axis == "y") {
        d3.select(el)
          .call(d3[axisMethod](methodArg))
          .attr("class", "yaxis");
      } else {
        d3.select(el)
          .call(d3[axisMethod](methodArg))
          .attr("class", "xaxis");
      }
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
</style>
