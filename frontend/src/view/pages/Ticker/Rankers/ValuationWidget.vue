<template>
  <!--begin::Mixed Widget 14-->
  <!-- <div class="card card-custom card-stretch gutter-b"> -->
  <v-card rounded="lg">
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em">
        نسبت های ارزش گذاری</v-toolbar-title
      >
    </v-toolbar>
    <div class="d-flex flex-column pt-2">
      <!-- <div class="row FinancialStrength valign"> -->
      <!-- <v-row no-gutters>
        <div class="col-sm-4">
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <v-chip color="danger" label text-color="white" v-on="on">
                امتیاز کلی
                <v-icon left>mdi-label</v-icon>
              </v-chip>
            </template>
            <span class="small">Valuation</span>
          </v-tooltip>
        </div>
        <div class="col-sm-2 strong blured">
          {{ this.FinancialStrength }}/10
        </div>
        <div class="col-sm-6">
          <v-progress-linear
            :value="this.FinancialStrength * 10"
            :color="getColor(this.FinancialStrength * 10)"
            background-color="#E9ECEF"
            rounded
            class="blured"
            height="25"
          >
          </v-progress-linear>
        </div>
      </v-row> -->
      <v-data-table
        :headers="headers"
        :items="ValuatedItems"
        :hide-default-footer="true"
        class="elevation-1 FinancialStrength"
        :header-props="{ sortIcon: null }"
      >
        <template v-slot:[`item.persianname`]="{ item }">
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <v-chip label small v-on="on">{{ item.persianname }}</v-chip>
            </template>
            <span class="small">{{ item.name }}</span>
          </v-tooltip>
        </template>
        <template v-slot:[`item.now`]="{ item }">
          <span class="">{{ item.now }}</span>
        </template>
        <template v-slot:[`item.industry`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            :color="getColor(item.industry * 100)"
            :value="item.industry * 100"
          >
          </v-progress-linear>
        </template>
        <!-- <template v-slot:[`item.historic`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            :color="getColor(item.historic * 100)"
            :value="item.historic * 100"
          >
          </v-progress-linear>
        </template> -->
      </v-data-table>
      <!-- </div> -->
    </div>
    <!--end::Body-->
    <!-- </div> -->
  </v-card>
  <!--end::Mixed Widget 14-->
</template>

<script>
export default {
  name: "ValuationWidget",
  props: ["RatioData", "LiveData", "ComponentData"],
  data() {
    return {
      search: "",
      FinancialStrength: 5,
      headers: [
        {
          text: "نسبت مالی",
          value: "persianname",
          sortabale: false
        },
        { text: "مقدار فعلی", value: "now", sortabale: false },
        { text: "در مقایسه با صنعت", value: "industry", sortabale: false }
        // {
        //   text: "در مقایسه با تاریخ سهم",
        //   value: "historic",
        //   sortabale: false
        // }
      ],
      sharecount: 0,
      closingPrice: 0,
      ValuatedItems: []
    };
  },
  methods: {
    // set FinancialStrength percent
    getColor: function(value) {
      if (value >= 80) {
        return "#0DCD0A";
      } else if (value < 80 && value >= 60) {
        return "#72FF59";
      }
      if (value < 60 && value >= 40) {
        return "#FFCE00";
      } else if (value < 40 && value >= 20) {
        return "#FD6700";
      } else if (value < 20) {
        return "#FF0000";
      }
      return "";
    },
    renderLiveData() {
      this.sharecount = this.LiveData[0].ShareCount;
      // console.log("🚀 ~ file: ValuationWidget.vue ~ line 196 ~ renderLiveData ~ this.sharecount", this.sharecount)
      this.closingPrice = this.LiveData[0].close;
      // console.log("🚀 ~ file: ValuationWidget.vue ~ line 197 ~ renderLiveData ~ this.closingPrice", this.closingPrice)
    },
    renderRatioComponentData() {
      let that = this;
      if (
        this.RatioData === null ||
        this.RatioData === undefined ||
        this.RatioData == [] ||
        this.ComponentData === null ||
        this.ComponentData === undefined ||
        this.ComponentData == []
      ) {
        // console.log("Either Empty");
      } else {
        this.ComponentData.filter(d => {
          if (d.Component == "AllEarningsWithNRI(TTM)") {
            that.ValuatedItems.push({
              name: "P/E Ratio",
              persianname: "نسبت P/E",
              historic: 0,
              now:
                Math.round(
                  ((that.sharecount * that.closingPrice) /
                    (d.ComponentValue * 1000000)) *
                    100
                ) / 100,
              industry: 0
            });
          }
          if (d.Component == "AllEquity") {
            that.ValuatedItems.push({
              name: "P/B Ratio",
              persianname: "نسبت P/B",
              historic: 0,
              now:
                Math.round(
                  ((that.sharecount * that.closingPrice) /
                    (d.ComponentValue * 1000000)) *
                    100
                ) / 100,
              industry: 0
            });
          }
          // if (d.Component == "AllOperationalCashFlow(TTM)") {
          // }
          if (d.Component == "AllRevenue(TTM)") {
            that.ValuatedItems.push({
              name: "P/S Ratio",
              persianname: "نسبت P/S",
              historic: 0,
              now:
                Math.round(
                  ((that.sharecount * that.closingPrice) /
                    (d.ComponentValue * 1000000)) *
                    100
                ) / 100,
              industry: 0
            });
          }
          if (d.Component == "EarningWithoutNRI(TTM)") {
            that.ValuatedItems.push({
              name: "P/E Ratio Without NRI",
              persianname: "نسبت P/E بدون درآمد متفرقه",
              historic: 0,
              now:
                Math.round(
                  ((that.sharecount * that.closingPrice) /
                    (d.ComponentValue * 1000000)) *
                    100
                ) / 100,
              industry: 0
            });
          }
          if (d.Component == "FCF(TTM)") {
            that.ValuatedItems.push({
              name: "P/Free Cash Flow",
              persianname: "قیمت به جریان نقدی عملیاتی",
              historic: 0,
              now:
                Math.round(
                  ((that.sharecount * that.closingPrice) /
                    (d.ComponentValue * 1000000)) *
                    100
                ) / 100,
              industry: 0
            });
          }
        });
      }
    }
  },
  watch: {
    LiveData() {
      if (
        this.LiveData === null ||
        this.LiveData === undefined ||
        this.LiveData == []
      ) {
        this.sharecount = 0;
        this.closingPrice = 0;
      } else {
        this.renderLiveData();
      }
    },
    RatioData() {
      this.ValuatedItems = [];
      if (
        this.RatioData === null ||
        this.RatioData === undefined ||
        this.RatioData == []
      ) {
        this.ValuatedItems = [];
      } else {
        this.renderRatioComponentData();
      }
      // console.log(this.RatioData);
    },
    ComponentData() {
      this.ValuatedItems = [];
      if (
        this.ComponentData === null ||
        this.ComponentData === undefined ||
        this.ComponentData == []
      ) {
        this.ValuatedItems = [];
      } else {
        this.renderRatioComponentData();
      }
      // console.log(this.ComponentData);
    }
    // this.setFinancialStrengthPercent();
    // reference; kt_stats_widget_7_chart
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.valign * {
  vertical-align: middle;
}
.blured {
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(10px);
}
</style>
