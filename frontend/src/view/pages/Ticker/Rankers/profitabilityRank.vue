<template>
  <v-card outlined class="profitabilityRank">
    <div class="row">
      <div class="col-sm-4">
        <span class="strong mr-2">Profitability Rank</span>
      </div>
      <div class="col-sm-2 small">{{ this.FinancialStrength }}/10</div>
      <div class="col-sm-5">
        <v-progress-linear
          :value="this.FinancialStrengthPercent"
          :color="getColor(this.FinancialStrength * 10)"
          background-color="#e9ecef"
          rounded
          height="15"
        >
        </v-progress-linear>
      </div>
    </div>
    <table class="profitability">
      <thead>
        <tr>
          <th class="col-2"></th>
          <th class="col-2">Current</th>
          <th class="col-4">Vs Industry</th>
          <th class="col-4">Vs History</th>
        </tr>
      </thead>
      <tbody class="table-body">
        <tr>
          <td>Operating Margin %</td>
          <td>24.52</td>
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
        <tr>
          <td>Net Margin %</td>
          <td>21.33</td>
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
        <tr>
          <td>ROE %</td>
          <td>68.38</td>
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
        <tr>
          <td>ROA %</td>
          <td>17.82</td>
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
        <tr>
          <td>ROC (Joel Greenblatt) %</td>
          <td>194.33</td>
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
        <tr>
          <td>3-Year Revenue Growth Rate</td>
          <td>12.6</td>
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
        <tr>
          <td>3-Year EBITDA Growth Rate</td>
          <td>9.7</td>
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
        <tr>
          <td>3-Year EPS without NRI Growth Rate</td>
          <td>12.7</td>
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
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      FinancialStrength: 5,
      FinancialStrengthPercent: 0
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

    getColor: function(value) {
      if (value > 80) {
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
    }
  }
};
</script>
<style scoped>
/* this is for blue table  */
table.profitability {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
table.profitability td,
table.profitability th {
  padding: 3px 2px;
}
table.profitability tbody td {
  font-size: 10px;
  color: #000000;
  text-align: center;
}
table.profitability thead {
  background: #eff1f7;
}
table.profitability thead th {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  text-align: center;
  border-left: 1px solid #ffffff;
}
table.profitability thead th:first-child {
  border-left: none;
}
.profitabilityRank {
  direction: ltr;
}
</style>
