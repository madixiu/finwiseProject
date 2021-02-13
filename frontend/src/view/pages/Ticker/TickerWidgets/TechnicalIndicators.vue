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
          <ApexChart
            type="radialBar"
            width="100%"
            height="350"
            :series="[32]"
            :chartOptions="plotOptions"
          />
          <v-btn text color="teal accent-4" @click="reveal = true">
            اطلاعات بیشتر
          </v-btn>
        </div>
      </div>
      <!--end::Header-->
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import ApexChart from "@/view/content/charts/ApexChart";
import { mapGetters } from "vuex";

export default {
  name: "TechnicalIndicators",
  props: ["Indicators"],
  components: {
    ApexChart
  },
  data() {
    return {
      search: "",
      DataItems2: [],
      loading: true,
      plotOptions: {
        radialBar: {
          startAngle: 0,
          endAngle: 225,
          hollow: {
            margin: 0,
            size: "30%",
            background: "#fff",
            image: undefined,
            imageOffsetX: 0,
            imageOffsetY: 0,
            position: "front",
            dropShadow: {
              enabled: true,
              top: 3,
              left: 0,
              blur: 4,
              opacity: 0.24
            }
          },
          track: {
            background: "#fff",
            strokeWidth: "27%",
            margin: 0, // margin is in pixels
            dropShadow: {
              enabled: true,
              top: -3,
              left: 0,
              blur: 4,
              opacity: 0.35
            }
          },
          dataLabels: {
            show: true,
            name: {
              offsetY: -10,
              show: true,
              color: "#888",
              fontSize: "1em"
            },
            value: {
              formatter: function(val) {
                return parseInt(val);
              },
              color: "#111",
              fontSize: "36px",
              show: true
            }
          }
        },
        fill: {
          type: "gradient",
          gradient: {
            shade: "dark",
            type: "horizontal",
            shadeIntensity: 0.5,
            gradientToColors: ["#ABE5A1"],
            inverseColors: true,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100]
          }
        },
        stroke: {
          lineCap: "round"
        },
        labels: ["Percent"]
      }
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
  },
  methods: {
    populateData() {
      this.DataItems2 = this.Indicators;
      this.loading = false;
    }
  },
  mounted() {
    this.populateData();
  },
  watch: {
    notices() {
      // console.log("Watcher");
      this.populateData();
      console.log(this.Indicators);
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
