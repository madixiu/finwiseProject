<template>
  <v-card outlined class="mr-2 ValueationReturn">
    <div class="row">
      <div class="col-sm-12">
        <span class="strong mr-2">Valuation & Return</span>
      </div>
    </div>
    <table class="Valueation">
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
          <td>Price-to-Tangible-Book</td>
          <td>26.61</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Intrinsic-Value-Projected-FCF</td>
          <td>2.37</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Intrinsic-Value-DCF (Earnings Based)</td>
          <td>1.2</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Median-PS-Value</td>
          <td>2</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Peter-Lynch-Fair-Value</td>
          <td>4.87</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Price-to-Graham-Number</td>
          <td>6.36</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Earnings Yield (Greenblatt) %</td>
          <td>3.68</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
        </tr>
        <tr>
          <td>Forward Rate of Return (Yacktman) %</td>
          <td>9.61</td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
                background-color="#E9ECEF"
                rounded
                height="15"
              ></v-progress-linear>
            </div>
          </td>
          <td>
            <div class="col-11" style="position: relative;">
              <v-progress-linear
                :value="this.ValuationPercent"
                :color="getColor(this.Valuation * 10)"
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
      Valuation: 7,
      ValuationPercent: 0
    };
  },
  mounted() {
    this.setValuationPercent();
  },
  methods: {
    setValuationPercent: function() {
      this.ValuationPercent = this.Valuation * 10;
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
<style>
table.Valueation {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
table.Valueation td,
table.Valueation th {
  padding: 3px 2px;
}
table.Valueation tbody td {
  font-size: 10px;
  color: #000000;
  text-align: center;
}
table.Valueation thead {
  background: #eff1f7;
}
table.Valueation thead th {
  font-size: 13px;
  font-weight: bold;
  color: #000000;
  text-align: center;
  border-left: 1px solid #ffffff;
}
table.Valueation thead th:first-child {
  border-left: none;
}
.ValueationReturn {
  direction: ltr;
}
</style>
