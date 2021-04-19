<template>
  <div class="treemap">
    <!-- <div
      id="tooltip"
      v-if="tooltip && selectedNode.depth == 0"
      class="tooltip"
      :style="{ left: pageX + 'px', top: pageY + 'px' }"
    >
      <span style="font-size:0.8rem">
        {{ tooltipHeaderName }}
      </span>
      <hr />
      <div style="direction:rtl">
        <p style="font-size:0.7rem;direction:rtl">
          <span> {{ tooltipListOfChilds[0].name }}</span>
          <span style="font-size:0.7rem">{{
            tooltipListOfChilds[0].change
          }}</span>
        </p>
      </div>
    </div> -->
    <!-- The SVG structure is explicitly defined in the template with attributes derived from component data -->
    <svg :height="height" style="margin-left: 0px;" :width="width">
      <g style="shape-rendering: crispEdges;" transform="translate(0,20)">
        <!-- The top most element, representing the previous node -->
        <g class="grandparent">
          <rect
            :height="20"
            :width="width - 2"
            :y="margin.top * -1 + 14"
            v-on:click="selectNode"
            :id="parentId"
          ></rect>
          <!-- <g class="parentTitleBox"
          v-for="(child in rootNode)"
          ></g> -->
          <!-- <svg width="15pt" height="15pt" viewBox="0 0 15 15" version="1.1">
            <g id="surface1">
              <path
                style=" stroke:none;fill-rule:nonzero;fill:rgb(15.294118%,23.137255%,47.843137%);fill-opacity:1;"
                d="M 15 7.5 C 15 11.640625 11.640625 15 7.5 15 C 3.359375 15 0 11.640625 0 7.5 C 0 3.359375 3.359375 0 7.5 0 C 11.640625 0 15 3.359375 15 7.5 Z M 15 7.5 "
              />
              <path
                style=" stroke:none;fill-rule:nonzero;fill:rgb(7.058824%,6.666667%,28.627451%);fill-opacity:1;"
                d="M 4.597656 8.480469 L 10.496094 14.378906 C 12.769531 13.386719 14.460938 11.296875 14.890625 8.777344 L 9.269531 3.152344 Z M 4.597656 8.480469 "
              />
              <path
                style=" stroke:none;fill-rule:nonzero;fill:rgb(100%,67.843137%,61.960784%);fill-opacity:1;"
                d="M 6.394531 7.222656 L 9.242188 4.375 C 9.585938 4.03125 9.585938 3.46875 9.242188 3.125 C 8.898438 2.78125 8.335938 2.78125 7.992188 3.125 L 4.242188 6.875 C 3.898438 7.21875 3.898438 7.78125 4.242188 8.125 L 7.992188 11.875 C 8.335938 12.21875 8.898438 12.21875 9.242188 11.875 C 9.585938 11.53125 9.585938
                 10.96875 9.242188 10.625 L 6.394531 7.777344 C 6.242188 7.625 6.242188 7.375 6.394531 7.222656 Z M 6.394531 7.222656 "
              />
              <path
                style=" stroke:none;fill-rule:nonzero;fill:rgb(100%,38.431373%,38.431373%);fill-opacity:1;"
                d="M 9.242188 10.625 L 6.394531 7.777344 C 6.320312 7.703125 6.285156 7.609375 6.28125 7.515625 L 3.984375 7.515625 C 3.988281 7.738281 4.074219 7.957031 4.242188 8.125 L 7.992188 11.875 C 8.335938 12.21875 8.898438 12.21875 9.242188 11.875 C 9.585938 11.53125 9.585938 10.96875 9.242188 10.625 Z M 9.242188 10.625 "
              />
            </g>
          </svg> -->

          <!-- The visible square text element with the id (basically a breadcumb, if you will) -->
          <text class="grandparentText" dy=".65em" :x="width / 2" y="0">
            {{ selectedNode.data.name }}
          </text>
        </g>
        <!-- We can use Vue transitions too! -->
        <transition-group
          name="fade"
          mode="out-in"
          tag="g"
          class="depth"
          v-if="selectedNode"
        >
          <!-- Generate each of the visible squares at a given zoom level (the current selected node) -->
          <g
            class="children"
            v-for="children in selectedNode._children"
            :key="'c_' + children.id"
            @mousemove="mouse_move(children, $event)"
            @mouseleave="tooltip = false"
          >
            <!-- 
              The visible square rect element.
              You can attribute directly an event, that fires a method that changes the current node,
              restructuring the data tree, that reactivly gets reflected in the template.
            -->
            <g v-if="selectedNode.depth == 1" direction="ltr">
              <rect
                class="parent"
                :id="children.id"
                :key="children.data.id"
                :x="x(children.x0)"
                :y="y(children.y0) + 15"
                :width="x(children.x1 - children.x0 + children.parent.x0)"
                :height="y(children.y1 - children.y0 + children.parent.y0)"
                :style="getColor(children.data.change)"
              ></rect>
              <text
                class="parentChildsText"
                dy="1em"
                :key="'name_' + children.data.id"
                :x="x(children.x0) + 6"
                :y="y(children.y0) + 15"
                :style="InnerTickerTextFontSizeAdjust(children)"
              >
                {{ children.data.name }}
              </text>

              <text
                class="parentChildsValue"
                dy="2.3em"
                :key="'change_' + children.data.id"
                :x="x(children.x0) + 6"
                :y="y(children.y0) + 15"
                :style="InnerTickerTextFontSizeAdjust(children)"
              >
                {{ children.data.change }}%
              </text>
            </g>

            <!-- Generate the children squares (only visible on hover of a square) -->
            <g
              v-for="child in children._children"
              :key="'c_' + child.id"
              class="childG"
              direction="ltr"
            >
              <rect
                v-on:click="selectNode"
                class="child"
                :id="child.id"
                :key="child.data.id"
                :height="y(child.y1) - y(child.y0)"
                :width="x(child.x1) - x(child.x0)"
                :x="x(child.x0)"
                :y="y(child.y0)"
                :style="getColor(child.data.change)"
              ></rect>
              <!-- ticker TEXT ********************************* -->
              <text
                class="childTickerName"
                :key="'name_t_' + child.id"
                :x="XText(child.x0, child.x1)"
                :y="YText2(child.y0, child.y1)"
                :style="
                  tickerTextFontSizeAdjust(
                    child.x0,
                    child.x1,
                    child.y0,
                    child.y1
                  )
                "
              >
                {{ child.data.name }}
              </text>
              <text
                class="childTickerValue"
                dy="0.3em"
                :key="'percent_t_' + child.id"
                :x="XText(child.x0, child.x1)"
                :y="YText(child.y0, child.y1)"
                :style="
                  tickerTextFontSizeAdjust(
                    child.x0,
                    child.x1,
                    child.y0,
                    child.y1
                  )
                "
              >
                {{ child.data.change + "%" }}
              </text>
              <!-- ticker TEXT ********************************* -->
            </g>

            <!-- HEADER SQUARES WITH NAMES ***************************** -->
            <g v-if="selectedNode.depth == 0">
              <rect
                v-on:click="selectNode"
                class="parentSquare"
                :x="x(children.x0)"
                :y="y(children.y0)"
                :width="x(children.x1 - children.x0 + children.parent.x0)"
                height="15"
              ></rect>
              <rect
                class="littleSquare"
                :x="x(children.x0) + 5"
                :y="y(children.y0) + 8"
                width="10"
                height="10"
                style="fill:#262931;transform-box:fill-box;"
                transform="rotate(45)"
                transform-origin="50% 50%"
              ></rect>
              <text
                class="parentSquareText"
                v-if="selectedNode.depth == 0"
                dy="0.8em"
                :key="'name_' + children.data.id"
                :x="x(children.x0) + 6"
                :y="y(children.y0)"
              >
                {{ children.data.name }}
              </text>
            </g>
            <!-- HEADER SQUARES WITH NAMES ***************************** -->

            <!-- The visible square text element with the title and value of the child node -->
          </g>
        </transition-group>
      </g>
    </svg>
    <!-- ************* SVG TOOLTIP PLACEMENT ************************* -->

    <!-- <svg v-if="tooltip && selectedNode.depth == 0"
    :height="height"
          :width="width"
    >

      <g id="tooltip"  
          class="tooltip">
          <rect
          :x="pageX"
          :y="pageY"
          height="200"
          width="100"
          style="fill:black">
          </rect>
              <text style="font-size:0.8rem;fill:black" :x="pageX"
          :y="pageY">
              {{tooltipHeaderName}}
          </text>
          </g>
    </svg> -->
  </div>
</template>

<script>
import { scaleLinear, scaleOrdinal, scaleQuantize } from "d3-scale";
// import {json} from 'd3-request'
import { hierarchy, treemap } from "d3-hierarchy";
// To be explicit about which methods are from D3 let's wrap them around an object
// Is there a better way to do this?
let d3 = {
  scaleLinear: scaleLinear,
  scaleOrdinal: scaleOrdinal,
  scaleQuantize: scaleQuantize,
  // schemeCategory20: schemeCategory20,
  // json: json,
  hierarchy: hierarchy,
  treemap: treemap
};
// import data from "@/components/data/map2.json";
// import mapData from "./data/map2.json";
export default {
  // name: "treemap",
  props: { inputData: Object, inputWidth: Number, inputHeight: Number },
  // the component's data
  data() {
    return {
      jsonData: {
        name: "نقشه بازار",
        children: [
          {
            name: "استخراج زغال سنگ",
            children: [
              {
                name: "کشرق",
                close: 108622,
                change: 1.8,
                value: 9124248000000,
                tickerFull: "صنعتی و معدنی شمال شرق شاهرود"
              },
              {
                name: "کپرور",
                close: 45906,
                change: -3.27,
                value: 24789240000000,
                tickerFull: "فرآوری زغال سنگ پروده طبس"
              },
              {
                name: "کطبس",
                close: 67050,
                change: 3.2,
                value: 12404250000000,
                tickerFull: "ذغال‌سنگ‌ نگین‌ ط‌بس‌"
              }
            ]
          }
        ]
      },
      pageX: null,
      MainScaleNode: null,
      pageY: null,
      tooltip: false,
      rootNode: {},
      tooltipHeaderName: null,
      tooltipListOfChilds: [],
      margin: {
        top: 20,
        right: 0,
        bottom: 0,
        left: 0
      },
      width: 1250,
      height: 550,
      selected: null,
      colors: [
        "fill:#f63538", // 0 lightest Red
        "fill:#eb363a", // 1
        "fill:#e0373c", // 2
        "fill:#c9393f", // 3
        "fill:#b33b43", // 4
        "fill:#9c3d46", // 5
        "fill:#86374a", // 6
        "fill:#6f414d", // 7
        "fill:#584351", // 8 darkest Red
        "fill:#414554", // 9 Black
        "fill:#404e55", // 10 darkest Green
        "fill:#3f5655", // 11
        "fill:#3d6756", // 12
        "fill:#398957", // 13
        "fill:#379a58", // 14
        "fill:#35ab59", // 15
        "fill:#33bc5a", // 16
        "fill:#32c45a", // 17
        "fill:#30cc5a" // 18 lightes Green
      ]
    };
  },
  // You can do whatever when the selected node changes
  watch: {
    // eslint-disable-next-line no-unused-vars

    selectedNode(newData, oldData) {
      // console.log("The selected node changed...");
      // console.log(newData.data);
      // console.log(oldData.depth);
      if (newData.depth == 1) {
        // this.initialize()
        this.accumulate(this.rootNode, this);
        this.InnerScaleTreemap(this.rootNode);
      } else if (newData.depth == 0 && oldData.depth == 1) {
        this.initialize();
        this.accumulate(this.rootNode, this);
        this.treemap(this.rootNode);
      }

      // console.log(newData.y0,newData.x0,newData.y1,newData.x1);
    }
  },
  created() {
    // this.loadData();
    this.width = this.inputWidth;
    this.height = this.inputHeight;
    this.jsonData = this.inputData;

    // this.jsonData = null;
  },
  // In the beginning...
  mounted() {
    // var that = this;
    // console.log(this.getColor(-1));

    // An array with colors (can probably be replaced by a vuejs method)
    // that.color = d3.scaleOrdinal(d3.schemeCategory20)
    // that.color = d3.scaleOrdinal().range(['#5EAFC6', '#FE9922', '#93c464', '#75739F'])
    // loads the data and calls the initialization methods
    // d3.json('@components/data/map2.json',
    // function (error, data) {
    //   if (error) console.log(error)
    // that.jsonData = this.data;
    // console.log(this.jsonData);
    this.initialize();
    this.accumulate(this.rootNode, this);
    this.treemap(this.rootNode);
    // console.log(that.InnerScaleTreemap(that.rootNode));
    // that.MainScaleNode = that.InnerScaleTreemap(that.rootNode)
    // }
    // )
  },
  // The reactive computed variables that fire rerenders
  computed: {
    myColor() {
      return d3
        .scaleLinear()
        .domain([1, 10])
        .range(["#FFFFFF", "#000000"]);
    },
    positiveColor() {
      return (
        d3
          .scaleLinear()
          .domain([0.05, 6])
          // .range(["#404e55", "#3f5655", "#3d6756", "#398957", "#379a58", "#35ab59", "#33bc5a", "#32c45a", "#30cc5a"]);
          .range(["#404e55", "#30cc5a"])
      );
    },
    negativeColor() {
      return (
        d3
          .scaleLinear()
          .domain([-2, -0.05])
          // .range(["#f63538", "#eb363a","#e0373c", "#c9393f", "#b33b43", "#9c3d46", "#86374a", "#6f414d", "#584351"]);
          .range(["#f63538", "#584351"])
      );
    },
    // The grandparent id
    parentId() {
      if (
        this.selectedNode.parent === undefined ||
        this.selectedNode.parent === null
      ) {
        return this.selectedNode.id;
      } else {
        return this.selectedNode.parent.id;
      }
    },
    // Returns the x position within the current domain
    // Maybe it can be replaced by a vuejs method
    x() {
      return d3
        .scaleLinear()
        .domain([0, this.width])
        .range([0, this.width]);
    },
    // Returns the y position within the current domain
    // Maybe it can be replaced by a vuejs method
    y() {
      return d3
        .scaleLinear()
        .domain([0, this.height - this.margin.top - this.margin.bottom])
        .range([0, this.height - this.margin.top - this.margin.bottom]);
    },

    yParent2() {
      return d3
        .scaleLinear()
        .domain([0, this.height])
        .range([0, this.height]);
    },
    yParent() {
      return d3
        .scaleLinear()
        .domain([0, this.height - this.margin.top - this.margin.bottom])
        .range([0, this.height - this.margin.top - this.margin.bottom]);
    },
    // The D3 function that recursively subdivides an area into rectangles
    treemap() {
      return (
        d3
          .treemap()
          // .tile(d3.treemapResquarify)
          .size([this.width, this.height])
          .round(false)
          .paddingTop(15)
          // .paddingOuter(1)
          .paddingRight(1)
          .paddingLeft(1)
          .paddingBottom(1)
      );
    },

    // The current selected node
    selectedNode() {
      let node = null;

      if (this.selected) {
        let nd = this.getNodeById(this.rootNode, this.selected, this);

        if (nd._children) {
          node = nd;
        } else {
          node = nd.parent;
        }
      } else {
        node = this.rootNode;
      }

      // Recalculates the y and x domains
      this.x.domain([node.x0, node.x0 + (node.x1 - node.x0)]);
      this.y.domain([node.y0, node.y0 + (node.y1 - node.y0)]);

      /*
      **** IMPORTANT *****
      SUPRISINGLY it works the way we want by this LOG line!!!
      have to figure out a way to get rid  of this!!!!!
      */
      console.log(this.MainScaleNode);
      // this.MainScaleNode
      return node;
    }
  },
  methods: {
    // Called once, to create the hierarchical data representation
    initialize() {
      let that = this;

      if (that.jsonData) {
        that.rootNode = d3
          .hierarchy(that.jsonData)
          .eachBefore(function(d) {
            d.id = (d.parent ? d.parent.id + "." : "") + d.data.name;
          })
          .sum(d => d.value)
          .sort(function(a, b) {
            return b.height - a.height || b.value - a.value;
          });
        that.rootNode.x = that.rootNode.y = 0;
        that.rootNode.x1 = that.width;
        that.rootNode.y1 = that.height;
        that.rootNode.depth = 0;
      }
    },
    // Calculates the accumulated value (sum of children values) of a node - its weight,
    // represented afterwards in the area of its square
    accumulate(d, context) {
      d._children = d.children;

      if (d._children) {
        d.value = d._children.reduce(function(p, v) {
          return p + context.accumulate(v, context);
        }, 0);
        return d.value;
      } else {
        return d.value;
      }
    },
    // Helper method - gets a node by its id attribute
    getNodeById(node, id, context) {
      if (node.id === id) {
        return node;
      } else if (node._children) {
        for (var i = 0; i < node._children.length; i++) {
          var nd = context.getNodeById(node._children[i], id, context);
          if (nd) {
            return nd;
          }
        }
      }
    },
    // When a user clicks a square, changes the selected data attribute
    // which fires the computed selectedNode, which in turn finds the Node by the id of the square clicked
    // and the template reflects the changes
    selectNode(event) {
      // console.log(event.target.id);
      // console.log(event.target);
      this.selected = event.target.id;

      // this.accumulate(this.selected,this)
    },
    XText(x0, x1) {
      return (x1 - x0) / 2 + x0;
    },
    YText(y0, y1) {
      return (y1 - y0) / 2 + y0 - 5;
    },
    YText2(y0, y1) {
      return (y1 - y0) / 4 + y0 - 5;
      // return (y1 - y0) / 2 +y0-7;
    },
    test(input) {
      return d3
        .scaleLinear()
        .domain([0, input])
        .range([0, this.width]);
    },
    test2(input) {
      return d3
        .scaleLinear()
        .domain([0, input])
        .range([0, this.height]);
    },
    mouse_move(key, eve) {
      // let tool = document.getElementById("tooltip")
      this.tooltip = true;
      this.tooltipHeaderName = key.data.name;
      this.tooltipListOfChilds = key.data.children;
      this.pageX = eve.pageX;
      this.pageY = eve.pageY;
      // console.log(key.data.name);
      // let t = eve.target.id.split(".");
      // console.log("MM ", t[t.length - 1]);
      // console.log(this.tooltipHeaderName,this.tooltipListOfChilds);
      // console.log(eve);
    },
    InnerScaleTreemap(input) {
      let t = d3
        .treemap()
        .size([this.width, this.height])
        .round(false)
        .paddingBottom(15);

      // return treemap(input)
      this.MainScaleNode = t(input);
      // return this.MainScaleNode;
      // this.MainScaleNode = null;
    },
    InnerTickerTextFontSizeAdjust(children) {
      let width = children.parent.x1 - children.parent.x0;

      let height = children.parent.y1 - children.parent.y0;

      let c =
        ((children.x1 - children.x0) * (children.y1 - children.y0) * 100) /
        (height * width);
      if (c >= 4) return "font-size:1.4rem";
      if (c < 4 && c >= 3) return "font-size:1.3em";
      if (c < 3 && c >= 2) return "font-size:1.2em";
      if (c < 2 && c >= 1) return "font-size:1em";
      if (c < 1 && c >= 0.8) return "font-size:0.95rem";
      if (c < 0.8 && c >= 0.6) return "font-size:0.75rem";
      if (c < 0.6 && c >= 0.5) return "font-size:0.65rem";

      if (c < 0.5 && c >= 0.1) return "font-size:0.5rem";
      if (c < 0.1 && c >= 0.07) return "font-size:0.4rem";
      if (c < 0.07 && c >= 0.04) return "font-size:0.3rem";
    },
    tickerTextFontSizeAdjust(x0, x1, y0, y1) {
      let c = ((x1 - x0) * (y1 - y0) * 100) / (this.height * this.width);
      // console.log(c);
      let constant = 0.7335775996;
      // console.log(name);
      // console.log(Math.pow(c,0.2)/constant);
      if (c < 0.1) return "font-size:0rem";
      else return `font-size:${Math.pow(c, 0.5) / constant}em`;

      // if (c >= 4) return "font-size:2em";
      // if (c < 4 && c >= 3) return "font-size:2.6em";
      // if (c < 3 && c >= 2) return "font-size:1.2rem";
      // if (c < 2 && c >= 1) return "font-size:1rem";
      // if (c < 1 && c >= 0.8) return "font-size:0.95rem";
      // if (c < 0.8 && c >= 0.6) return "font-size:0.75rem";
      // if (c < 0.6 && c >= 0.5) return "font-size:0.65rem";

      // if (c < 0.5 && c >= 0.1) return "font-size:0.5rem";
      // if (c < 0.1) return "font-size:0rem";
    },
    getColor(val) {
      // console.log(this.positiveColor(0.05));

      // let color = this.colors[1];
      let color = "fill:#414554";
      // let min = -2.0;
      // let max = 5.0;
      // let positiveBase = (4.95) / 9.0;
      // let positiveBase = 0.49444444444444446;
      // let negativeBase = -0.22777777777777775;
      // val = parseFloat(val);
      if (0.05 > val && val > -0.05) {
        // console.log(val);
        // console.log("black");
        color = "fill:#414554"; // color 0
      } else if (0.05 <= val && val <= 6) {
        // console.log("pos");
        color = "fill:" + this.positiveColor(val);
      } else if (-2 <= val && val <= -0.05) {
        // console.log("neg");
        color = "fill:" + this.negativeColor(val);
      } else if (val > 6) color = "fill:#30cc5a";
      else if (val < -2) color = "fill:#f63538";

      return color;
    }
  }
};
</script>

<style scoped>
text {
  pointer-events: none;
}

.grandparent text {
  /* font-weight: bold; */
  fill: wheat;
  font-weight: 600;
}

rect {
  fill: none;
  stroke: #262931;
}

/* rect.parent,
.grandparent rect {
  stroke-width: 1px;
} */

.grandparent rect {
  fill: #1e1e2d;
  /* color: aliceblue; */
}
.parentSquare {
  stroke: #bbb;
}
.parentText {
  fill: blanchedalmond;
}
/* .grandparent:hover rect {
  fill: #ee9700;
} */
/* g .children {
  margin-top: 20px;
} */
.child {
  cursor: pointer;
  stroke: rgb(36, 30, 30);
  /* margin-bottom: 20px !important; */
}
.child:hover {
  opacity: 80%;
}
.childG:hover * {
  text-shadow: 1px 1px #000000;
}
.childTickerName {
  fill: white;
  text-anchor: middle;
  font-family: "Vazir-Medium-FD";
}
.childTickerValue {
  fill: white;
  text-align: center;
  text-anchor: middle;
  font-family: "Vazir-Medium-FD";
}
/* .parent:hover {
  cursor: pointer;
  stroke:yellow
} */

.children rect.parent,
.grandparent rect {
  cursor: pointer;
}
.parentSquareText {
  fill: white;
  font-size: 0.6rem;
  text-anchor: end;
}

.children rect.parent {
  fill: #bbb;
  fill-opacity: 0.9;
}

.children:hover rect.child {
  fill: #bbb;
}

.children text {
  font-size: 0.8em;
}

.grandparent text {
  font-size: 0.8em;
  /* color: rgb(255, 255, 255); */
}
.grandparentText {
  color: #bbb !important;
  text-anchor: middle;
}
.parentChildsText {
  fill: white;
  font-size: 0.6rem;
  text-anchor: start;
  font-family: "Vazir-Medium-FD";
}
.parentChildsValue {
  fill-opacity: 1;
  fill: white;
  text-anchor: start;
  font-family: "Vazir-Medium-FD";
}
.parentSquare {
  /* fill: #262931; */
  /* fill: #262b42; */
  fill: #262931;
}
.littleSquare {
  fill: #262931;
}
.list-enter-active,
.list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active for <2.1.8 */ {
  opacity: 0;
}
.children:hover rect.child {
  stroke: #ffd614;
  stroke-width: 2px;
}
.children:hover rect.parentSquare {
  stroke: #ffd614;
  fill: #ffd614 !important;
  stroke-width: 2px;
}
.children:hover rect.littleSquare {
  stroke: #ffd614;
  fill: #ffd614 !important;
  stroke-width: 2px;
}
.children:hover text.parentSquareText {
  fill: black !important;
}
#tooltip {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 120px;
  height: auto;
  padding: 5px;
  background-color: white;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
  -webkit-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  -moz-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  pointer-events: none;
}
</style>
