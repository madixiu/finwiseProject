<template>
  <v-card outlined class="DividendCard">
    <div class="row">
      <div class="col-sm-12">
        <span class="strong mr-2">Dividend & Buy Back</span>
      </div>
    </div>
    <table class="Dividend">
      <thead>
        <tr>
          <th class="col-3"></th>
          <th class="col-1">Current</th>
          <th class="col-4">Vs Industry</th>
          <th class="col-4">Vs History</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Dividend Yield %</td>
          <td>0.71</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Dividend Payout Ratio</td>
          <td>0.24</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>3-Year Dividend Growth Rate</td>
          <td>11.2</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Forward Dividend Yield %</td>
          <td>0.73</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>5-Year Yield-on-Cost %</td>
          <td>1.21</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>3-Year Average Share Buyback Ratio</td>
          <td>5.9</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.DividendPercent"
                :color="getColor(this.Dividend * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
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
      Dividend: 6,
      DividendPercent: 0
    };
  },
  mounted() {
    this.setDividendPercent();
  },
  methods: {
    setDividendPercent: function() {
      this.DividendPercent = this.Dividend * 10;
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
table.Dividend {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
table.Dividend td,
table.Dividend th {
  padding: 3px 2px;
}
table.Dividend tbody td {
  font-size: 10px;
  color: #000000;
  text-align: center;
}
table.Dividend thead {
  background: #eff1f7;
}
table.Dividend thead th {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  text-align: center;
  border-left: 1px solid #ffffff;
}
table.Dividend thead th:first-child {
  border-left: none;
}
.DividendCard {
  direction: ltr;
}
</style>
