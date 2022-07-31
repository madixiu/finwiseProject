<template>
  <v-card rounded="lg">
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em">
        نسبت های بازگشت سرمایه</v-toolbar-title
      >
    </v-toolbar>

    <div class="d-flex flex-column pt-2">
      <!-- <v-row no-gutters>
        <div class="col-sm-4">
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <v-chip color="danger" label text-color="white" v-on="on">
                امتیاز کلی
                <v-icon left>mdi-label</v-icon>
              </v-chip>
            </template>
            <span class="small">Valuation & Return</span>
          </v-tooltip>
        </div>
        <div class="col-sm-2 strong blured">
          {{ this.FinancialStrength }}/10
        </div>
        <div class="col-sm-6">
          <v-progress-linear
            class="blured"
            :value="this.FinancialStrength * 10"
            :color="getColor(this.FinancialStrength * 10)"
            background-color="#E9ECEF"
            rounded
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
            <span>{{ item.name }}</span>
          </v-tooltip>
        </template>
        <template v-slot:[`item.now`]="{ item }">
          <span>{{ item.now }}</span>
        </template>
        <!-- <template v-slot:[`item.industry`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            :color="getColor(item.FinancialStrength * 100)"
            :value="item.industry * 100"
          >
          </v-progress-linear>
        </template>
        <template v-slot:[`item.historic`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            :color="getColor(item.FinancialStrength * 100)"
            :value="item.historic * 100"
          >
          </v-progress-linear>
        </template> -->
      </v-data-table>
    </div>
    <!--end::Body-->
    <!-- </div> -->
  </v-card>
  <!--end::Mixed Widget 14-->
</template>

<script>
export default {
  name: "PWidget",
  props: ["RatioData", "liveData"],
  data() {
    return {
      search: "",
      lastPrice: 0,
      headers: [
        {
          text: "نسبت مالی",
          value: "persianname",
          sortabale: false
        },
        { text: "مقدار فعلی", value: "now", sortabale: false }
        // { text: "در مقایسه با صنعت", value: "industry", sortabale: false },
        // {
        //   text: "در مقایسه با تاریخ سهم",
        //   value: "historic",
        //   sortabale: false
        // }
      ],
      ValuatedItems: []
    };
  },
  methods: {
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
    FillRatios() {
      let that = this;
      this.RatioItems = this.RatioData;
      if (
        this.RatioItems === undefined ||
        this.RatioItems.length == 0 ||
        this.liveData === undefined ||
        this.liveData.length == 0
      ) {
        this.RatioItems = [];
        this.lastPrice = 0;
      } else {
        this.lastPrice = this.liveData[0].last;
        this.RatioItems.filter(d => {
          if (d.RatioValue > 0 && d.RatioValue != undefined) {
            this.ValuatedItems.push({
              name: d.Ratio,
              persianname: "قیمت به " + d.displayTitle,
              now: Math.round((that.lastPrice / d.RatioValue) * 100)
            });
          }
        });
      }
    }
  },
  watch: {
    RatioData() {
      if (this.ValuatedItems.length != 0) {
        this.ValuatedItems = [];
      }
      this.FillRatios();
      // console.log(this.RatioData);
    },
    liveData() {
      if (this.ValuatedItems.length != 0) {
        this.ValuatedItems = [];
      }
      // console.log(this.liveData)
      this.FillRatios();
    }
  }
};
</script>
