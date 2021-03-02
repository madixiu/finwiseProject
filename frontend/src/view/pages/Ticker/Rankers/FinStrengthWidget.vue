<template>
  <!--begin::Mixed Widget 14-->
  <div class="card card-custom card-stretch gutter-b">
    <!--begin::Header-->
    <div class="card-header border-0 pt-2">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        نسبت های قدرت مالی
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body d-flex flex-column">
      <div class="row FinancialStrength valign">
        <div class="col-sm-4">
          <v-tooltip left>
            <template v-slot:activator="{ on }">
              <v-chip color="danger" label text-color="white" v-on="on">
                امتیاز کلی
                <v-icon left>mdi-label</v-icon>
              </v-chip>
            </template>
            <span class="small">Financial Strength</span>
          </v-tooltip>
        </div>
        <div class="col-sm-2 strong blured">{{ this.FinancialStrength }}/10</div>
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
      </div>
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
            <span class="small blured">{{ item.now }}</span>
        </template>
        <template v-slot:[`item.industry`]="{ item }">
          <v-progress-linear
            background-color="#E9ECEF"
            :height="15"
            :width="150"
            :rounded="true"
            class="blured"
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
            class="blured"
            :color="getColor(item.FinancialStrength * 100)"
            :value="item.historic * 100"
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
          <div class="valign pt-4 blured">
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
          <div class="valign pt-4 blured  ">
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
          <div class="valign pt-4 blured">
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
          <div class="blured">
            <b-progress>
              <b-progress-bar :value="getRoicPercent(item)" variant="success">
                ROIC {{ item.ROIC }}</b-progress-bar
              >
              <b-progress-bar :value="getWaccPercent(item)" variant="danger">
                WACC {{ item.WACC }}</b-progress-bar
              >
            </b-progress>
          </div>
        </template>
      </v-data-table>
    </div>
    <!--end::Body-->
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "financialStrength",
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
      ValuatedItems: [
        {
          name: "Cash-To-Debt",
          persianname: "نسبت نقد به بدهی",
          historic: 0.6,
          now: "30%",
          industry: 0.2,
          FinancialStrength: 0.8
        },
        {
          name: "Equity-to-Asset",
          persianname: "نسبت سرمایه به دارایی",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "Debt-to-Equity	",
          persianname: "نسبت بدهی به سرمایه",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "Debt-to-EBITDA",
          persianname: "نسبت بدهی به سود قبل از مالیات",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        },
        {
          name: "Interest Coverage",
          persianname: "پوشش بهره",
          historic: 5,
          now: "70%",
          industry: 0.6,
          FinancialStrength: 0.8
        }
      ],
      ValuatedItems2: [
        {
          name: "Piotroski F-Score",
          Value: 0.6,
          percentage: 50
        }
      ],
      headers2: [
        {
          text: "نسبت مالی",
          value: "name",
          width: "70%",
          align: "start"
        },
        { text: "مقدار فعلی", value: "Value", width: "30%" }
      ],
      ValuatedItems3: [
        {
          name: "Altman Z-Score",
          Value: 0.6,
          Content: 0.6,
          percentage: 30
        }
      ],
      headers3: [
        {
          text: "نسبت مالی",
          value: "name",
          width: "30%",
          align: "start"
        },
        { text: "مقدار فعلی", value: "Value", width: "70%" }
      ],
      ValuatedItems4: [
        {
          name: "Beneish M-Score",
          Value: 0.6,
          percentage: 25
        }
      ],
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
          Value: 0.6,
          WACC: 10,
          ROIC: 15
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
      console.log(this.ValuatedItems2.percentage);
      return `border:1 px `;
    }
  },
  mounted() {
    // this.setFinancialStrengthPercent();
    // reference; kt_stats_widget_7_chart
  }
};
</script>
<style scoped>
.blured { 
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(10px);
}
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.valign * {
  vertical-align: middle;
}
</style>
