<template>
  <v-card outlined class="ValuationRank">
    <div class="row">
      <div class="col-sm-4">
        <span class="mr-3 strong">Valuation Rank</span>
      </div>
      <div class="col-sm-2 strong">{{ this.ValuationRank }}/10</div>
      <div class="col-sm-5">
        <v-progress-linear
          :value="this.ValuationRankPercent"
          :color="getColor(this.ValuationRank * 10)"
          background-color="#E9ECEF"
          rounded
          height="15"
        >
        </v-progress-linear>
      </div>
    </div>

    <table class="Valuation">
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
          <td>PE Ratio</td>
          <td>24.52</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Forward PE Ratio</td>
          <td>21.33</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>PE Ratio without NRI</td>
          <td>68.38</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Owner-Earnings</td>
          <td>17.82</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>PB Ratio</td>
          <td>194.33</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>PS Ratio</td>
          <td>12.6</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Free-Cash-Flow</td>
          <td>9.7</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Operating-Cash-Flow</td>
          <td>12.7</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>EV-to-EBIT</td>
          <td>27.07</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>EV-to-EBITDA</td>
          <td>23.3</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>EV-to-Revenue</td>
          <td>7.05</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>PEG Ratio</td>
          <td>3.33</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Shiller PE Ratio</td>
          <td>50.16</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Current Ratio</td>
          <td>1.47</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Quick Ratio</td>
          <td>1.43</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Days Inventory</td>
          <td>8.14</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Days Sales Outstanding</td>
          <td>23.83</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              >
              </v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Days Payable</td>
          <td>76.17</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
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
                :value="this.ValuationRankPercent"
                :color="getColor(this.ValuationRank * 10)"
                background-color="#E9ECEF"
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
      ValuationRank: 1,
      ValuationRankPercent: 0
    };
  },
  mounted() {
    this.setValuationRankPercent();
  },

  methods: {
    setValuationRankPercent: function() {
      this.ValuationRankPercent = this.ValuationRank * 10;
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
table.Valuation {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
table.Valuation td,
table.Valuation th {
  padding: 3px 2px;
}
table.Valuation tbody td {
  font-size: 10px;
  color: #000000;
  text-align: center;
}
table.Valuation thead {
  background: #eff1f7;
}
table.Valuation thead th {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  text-align: center;
  border-left: 1px solid #ffffff;
}
table.Valuation thead th:first-child {
  border-left: none;
}
.ValuationRank {
  direction: ltr;
}
</style>
