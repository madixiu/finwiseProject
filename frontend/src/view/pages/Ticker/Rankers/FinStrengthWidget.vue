<template>
  <v-card rounded="lg">
    <v-toolbar dense class="elevation-2" style="height:36px;">
      <v-toolbar-title style="height:20px;font-size:0.95em">
        نسبت های قدرت مالی</v-toolbar-title
      >
    </v-toolbar>

    <div class="d-flex flex-column pt-2">
      <!-- <v-row no-gutters> -->
      <!-- <div class="col-sm-4">
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <v-chip color="danger" label text-color="white" v-on="on">
                امتیاز کلی
                <v-icon left>mdi-label</v-icon>
              </v-chip>
            </template>
            <span class="small">Financial Strength</span>
          </v-tooltip>
        </div> -->
      <!-- <div class="col-sm-2 strong ">{{ this.FinancialStrength }}/10</div> -->
      <!-- <div class="col-sm-6">
          <v-progress-linear
            :value="this.FinancialStrength * 10"
            :color="getColor(this.FinancialStrength * 10)"
            background-color="#E9ECEF"
            rounded
            class=""
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
          <span class="small ">{{ item.now }}</span>
        </template>
        <template v-slot:[`item.industry`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            class=""
            :color="getColor(item.industry)"
            :value="item.industry"
          >
          </v-progress-linear>
        </template>
        <template v-slot:[`item.historic`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            class=""
            :color="getColor(item.historic)"
            :value="item.historic"
          >
          </v-progress-linear>
        </template>
      </v-data-table>
      <v-data-table
        :headers="headers2"
        :hide-default-header="true"
        :items="ValuatedItems2"
        :hide-default-footer="true"
        class="elevation-1 FinancialStrength"
      >
        <template v-slot:[`item.name`]="{ item }">
          <v-chip label small>
            {{ item.name }}
          </v-chip>
        </template>
        <template v-slot:[`item.Value`]="{ item }">
          <div class="valign pt-4 ">
            <b-progress show-value class="align-center">
              <b-progress-bar value="10" variant="piotroski-color-0">
                0</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-1">
                1</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-2">
                2</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-3">
                3</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-4">
                4</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-5">
                5</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-6">
                6</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-7">
                7</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-8">
                8</b-progress-bar
              >
              <b-progress-bar value="10" variant="piotroski-color-9">
                9</b-progress-bar
              >
            </b-progress>
            <p
              class="mdi mdi-navigation altman-pointer-position"
              :style="`margin-right: ${item.percentage}%`"
            ></p>
          </div>
        </template>
      </v-data-table>
      <v-data-table
        :headers="headers3"
        :hide-default-header="true"
        :items="ValuatedItems3"
        :hide-default-footer="true"
        class="elevation-1 FinancialStrength"
      >
        <template v-slot:[`item.name`]="{ item }">
          <v-chip label small>
            {{ item.name }}
          </v-chip>
        </template>
        <template v-slot:[`item.Value`]="{ item }">
          <div class="valign pt-4   ">
            <b-progress show-value>
              <b-progress-bar value="40" variant="altman-color-0">
                DISTRESS</b-progress-bar
              >
              <b-progress-bar value="20" variant="altman-color-1">
                GREY</b-progress-bar
              >
              <b-progress-bar value="40" variant="altman-color-2">
                SAFE</b-progress-bar
              >
            </b-progress>
            <p
              class="mdi mdi-navigation altman-pointer-position"
              :style="`margin-right: ${item.percentage}%`"
            ></p>
          </div>
        </template>
      </v-data-table>
      <v-data-table
        :headers="headers4"
        :hide-default-header="true"
        :items="ValuatedItems4"
        :hide-default-footer="true"
        class="elevation-1 FinancialStrength"
      >
        <template v-slot:[`item.name`]="{ item }">
          <v-chip label small>
            {{ item.name }}
          </v-chip>
        </template>
        <template v-slot:[`item.Value`]="{ item }">
          <div class="valign pt-4 ">
            <b-progress show-value>
              <b-progress-bar value="50" variant="success">
                Not Manipulator</b-progress-bar
              >
              <b-progress-bar value="50" variant="danger">
                Manipulator</b-progress-bar
              >
            </b-progress>
            <p
              class="mdi mdi-navigation beneish-pointer-position"
              :style="`margin-right: ${item.percentage}%`"
            ></p>
          </div>
        </template>
      </v-data-table>
      <v-data-table
        :headers="headers5"
        :hide-default-header="true"
        :items="ValuatedItems5"
        :hide-default-footer="true"
        class="elevation-1 FinancialStrength"
      >
        <template v-slot:[`item.name`]="{ item }">
          <v-chip label small>
            {{ item.name }}
          </v-chip>
        </template>
        <template v-slot:[`item.Value`]="{ item }">
          <div class="">
            <b-progress>
              <b-progress-bar
                :value="item.ROIC / (item.ROIC + item.WACC)"
                variant="success"
              >
                ROIC {{ item.ROIC }}</b-progress-bar
              >
              <b-progress-bar
                :value="item.WACC / (item.ROIC + item.WACC)"
                variant="danger"
              >
                WACC {{ item.WACC }}</b-progress-bar
              >
            </b-progress>
          </div>
        </template>
      </v-data-table>
    </div>
    <!--end::Body-->
    <!-- </div> -->
  </v-card>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "financialStrength",
  props: ["RatioData"],
  data() {
    return {
      search: "",
      FinancialStrength: 5,
      headers: [
        {
          text: "نسبت مالی",
          value: "persianname",
          sortabale: false,
          align: "end"
        },
        { text: "مقدار فعلی", value: "now", sortabale: false },
        { text: "در مقایسه با صنعت", value: "industry", sortabale: false },
        {
          text: "در مقایسه با تاریخ سهم",
          value: "historic",
          sortabale: false
        }
      ],
      ValuatedItems: [],
      ValuatedItems2: [],
      headers2: [
        {
          text: "نسبت مالی",
          value: "name",
          width: "70%",
          align: "start"
        },
        { text: "مقدار فعلی", value: "Value", width: "30%" }
      ],
      ValuatedItems3: [],
      headers3: [
        {
          text: "نسبت مالی",
          value: "name",
          width: "30%",
          align: "start"
        },
        { text: "مقدار فعلی", value: "Value", width: "70%" }
      ],
      ValuatedItems4: [],
      headers4: [
        {
          text: "نسبت مالی",
          value: "name",
          width: "30%",
          align: "start"
        },
        { text: "مقدار فعلی", value: "Value", width: "70%" }
      ],
      ValuatedItems5: [
        {
          name: "WACC vs ROIC",
          Value: 0.5,
          WACC: 0,
          ROIC: 0
        }
      ],
      headers5: [
        {
          text: "نسبت مالی",
          value: "name",
          width: "30%",
          align: "start"
        },
        { text: "مقدار فعلی", value: "Value", width: "70%", align: "start" }
      ]
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"])
    // style() {
    //   return {
    //     margin: `0% 0% 0% ${this.ValuatedItems2.percentage}*100 px`,
    //   };
    // }
  },
  methods: {
    // set FinancialStrength percent
    setFinancialStrengthPercent: function() {
      this.FinancialStrengthPercent = this.FinancialStrength * 10;
    },
    getWaccPercent: function(item) {
      let all = item.WACC + item.ROIC;
      return (100 * item.WACC) / all;
    },
    // get ROIC percent
    getRoicPercent: function(item) {
      let all = item.WACC + item.ROIC;
      return (100 * item.ROIC) / all;
    },
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
    setStyle: function() {
      return `border:1 px `;
    },
    renderRatioData() {
      let l1 = ["CashToDebt", "DebtToEquity", "DebtToEBIT", "InterestCoverage"];
      // eslint-disable-next-line no-unused-vars
      let that = this;
      // console.log(that.ValuatedItems5)
      // console.log(that.ValuatedItems5[0])
      this.RatioData.filter(d => {
        // console.log(d)
        if (l1.includes(d.Ratio)) {
          // console.log(d);
          this.ValuatedItems.push({
            name: d.Ratio,
            persianname: d.displayTitle,
            historic: d.toHistoricAverage,
            now: Math.round(d.RatioValue * 100) / 100,
            industry: d.toIndustryAverage
          });
        }
        if (d.Ratio == "Piotrowski") {
          this.ValuatedItems2.push({
            name: d.Ratio,
            Value: d.RatioValue,
            percentage: d.RatioValue * 10
          });
        }
        if (d.Ratio == "WACC") {
          that.ValuatedItems5[0].WACC = Math.round(d.RatioValue * 100) / 100;
        }
        if (d.Ratio == "ROIC") {
          that.ValuatedItems5[0].ROIC = Math.round(d.RatioValue * 100) / 100;
        }
        if (d.Ratio == "Altman_Z") {
          that.ValuatedItems3.push({
            name: d.Ratio,
            Value: d.RatioValue,
            percentage: d.RatioValue * 10
          });
        }
        if (d.Ratio == "Benish") {
          that.ValuatedItems4.push({
            name: d.Ratio,
            Value: d.RatioValue,
            percentage: d.RatioValue * 10
          });
        }
        // console.log(d.RatioValue);
        // console.log(d.displayTitle);
      });
      // console.log(that.ValuatedItems5)
      // console.log(
      //   that.ValuatedItems5[0].WACC /
      //     (that.ValuatedItems5[0].ROIC + that.ValuatedItems5[0].WACC)
      // );
    }
  },
  watch: {
    RatioData() {
      this.ValuatedItems = [];
      this.ValuatedItems2 = [];
      this.ValuatedItems3 = [];
      this.ValuatedItems4 = [];
      // console.log(this.RatioData);
      if (
        this.RatioData === null ||
        this.RatioData === undefined ||
        this.RatioData == []
      ) {
        this.ValuatedItems = [];
        this.ValuatedItems2 = [];
        this.ValuatedItems3 = [];
        this.ValuatedItems4 = [];
        this.ValuatedItems5 = [];
      } else {
        this.renderRatioData();
      }
    }
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
</style>
