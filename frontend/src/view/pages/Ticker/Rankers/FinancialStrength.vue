<template>
  <v-card outlined class="mr-2 FinancialStrength">
    <div class="row">
      <div class="col-sm-4">
        <span class="mr-3 strong">Financial Strength</span>
      </div>
      <div class="col-sm-2 strong">{{ this.FinancialStrength }} /10</div>
      <div class="col-sm-5">
        <v-progress-linear
          :value="this.FinancialStrengthPercent"
          :color="getColor(this.FinancialStrength * 10)"
          background-color="#E9ECEF"
          rounded
          height="15"
        >
        </v-progress-linear>
      </div>
    </div>
    <table class="Financial">
      <thead>
        <tr>
          <th class="col-2"></th>
          <th class="col-2">Current</th>
          <th class="col-4">Vs Industry</th>
          <th class="col-4">Vs History</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Cash-To-Debt</td>
          <td>0.83</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Equity-to-Asset</td>
          <td>0.23</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Debt-to-Equity</td>
          <td>1.56</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Debt-to-EBITDA</td>
          <td>1.36</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Interest Coverage</td>
          <td>22.02</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#e9ecef"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.FinancialStrengthPercent"
                :color="getColor(this.FinancialStrength * 10)"
                background-color="#e9ecef"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <table class="Financial2">
      <thead>
        <tr>
          <td class="col-2"></td>
          <td class="col-2"></td>
          <td class="col-7"></td>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Piotroski F-Score</td>
          <td>7</td>
          <td class="d-flex justify-content-center align-items-center">
            <div class="col-11">
              <b-progress show-value>
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
              <p class="mdi mdi-navigation piotroski-pointer-position"></p>
            </div>
          </td>
        </tr>
        <tr>
          <td>Altman Z-Score</td>
          <td>6.56</td>
          <td class="d-flex justify-content-center align-items-center">
            <div class="col-11">
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
              <p class="mdi mdi-navigation altman-pointer-position"></p>
            </div>
          </td>
        </tr>
        <tr>
          <td>Beneish M-Score</td>
          <td>-2.63</td>
          <td class="d-flex justify-content-center align-items-center">
            <div class="col-sm-11">
              <b-progress show-value>
                <b-progress-bar value="50" variant="success">
                  Not Manipulator</b-progress-bar
                >
                <b-progress-bar value="50" variant="danger">
                  Manipulator</b-progress-bar
                >
              </b-progress>
              <p class="mdi mdi-navigation beneish-pointer-position"></p>
            </div>
          </td>
        </tr>
        <tr>
          <td>WACC vs ROIC</td>
          <td></td>
          <td class="d-flex justify-content-center align-items-center">
            <div class="col-sm-11">
              <b-progress>
                <b-progress-bar :value="getRoicPercent()" variant="success">
                  ROIC {{ ROIC }}%</b-progress-bar
                >
                <b-progress-bar :value="getWaccPercent()" variant="danger">
                  WACC {{ WACC }}%</b-progress-bar
                >
              </b-progress>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      FinancialStrength: 5,
      FinancialStrengthPercent: 0,
      WACC: 7.27,
      ROIC: 24.02
    };
  },
  mounted() {
    this.setFinancialStrengthPercent();
  },
  methods: {
    // set FinancialStrength percent
    setFinancialStrengthPercent: function() {
      this.FinancialStrengthPercent = this.FinancialStrength * 10;
    },
    getWaccPercent: function() {
      let all = this.WACC + this.ROIC;
      return (100 * this.WACC) / all;
    },
    // get ROIC percent
    getRoicPercent: function() {
      let all = this.WACC + this.ROIC;
      return (100 * this.ROIC) / all;
    }
  }
};
</script>
<style scoped>
/* this is for blue table  */
table.Financial {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
table.Financial td,
table.Financial th {
  padding: 3px 2px;
}
table.Financial tbody td {
  font-size: 10px;
  color: #000000;
  text-align: center;
}
table.Financial thead {
  background: #eff1f7;
}
table.Financial thead th {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  text-align: center;
  border-left: 1px solid #ffffff;
}
table.Financial thead th:first-child {
  border-left: none;
}
/* part two */
table.Financial2 {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
table.Financial2 td,
table.Financial th {
  padding: 3px 2px;
}
table.Financial2 tbody td {
  font-size: 10px;
  color: #000000;
  text-align: top;
}
table.Financial2 thead th {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  text-align: center;
  border-left: 1px solid #ffffff;
}
table.Financial2 thead th:first-child {
  border-left: none;
}
.piotroski-pointer-position {
  margin-left: 128px;
}
.FinancialStrength {
  direction: ltr;
}
</style>
