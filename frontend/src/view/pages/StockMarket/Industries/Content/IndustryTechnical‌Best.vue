<template>
  <div>
    <v-card>
      <v-card-title>تکنیکال بهترین</v-card-title>
      <v-subheader class="ltr_aligned" v-if="loading == false">
        <!-- آخرین به روز رسانی {{ DataItems[0]["persianDate"].slice(10, 16) }} -->
        آخرین به روز رسانی
      </v-subheader>

      <v-data-table
        v-if="loading == false"
        :headers="mvheaders"
        :items="filteredItems"
        :hide-default-footer="true"
        class="elevation-1 FinancialStrength"
        :header-props="{ sortIcon: null }"
        :items-per-page="10"
      >
        <template v-slot:[`item.ticker`]="{ item }">
          <v-chip
            small
            label
            :to="{ name: 'TickerOverall', params: { id: item.ID } }"
            >{{ item.ticker }}</v-chip
          >
        </template>
        <template v-slot:[`item.MarketCap`]="{ item }">
          <span
            >{{ numberWithCommas(roundTo(item.MarketCap / 1000000000, 2))
            }}<br />
            میلیارد ریال</span
          >
        </template>
        <template v-slot:[`item.Vol`]="{ item }">
          <span
            >{{ numberWithCommas(roundTo(item.Vol / 1000000, 2)) }}<br />
            میلیون</span
          >
        </template>
        <template v-slot:[`item.Value`]="{ item }">
          <span
            >{{ numberWithCommas(roundTo(item.Value / 1000000000, 2)) }}<br />
            میلیارد ریال</span
          >
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      filteredItems: [],
      loading: false,
      mvheaders: [
        { text: "رتبه", value: "Rank", sortabale: false },
        { text: "شاخص", value: "Index", sortabale: false },
        { text: "مقدار", value: "Vol", sortabale: false }
      ]
    };
  },
  mounted() {},
  methods: {
    numberWithCommas(x) {
      let parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
    // populateData() {
    //   this.DataItems = this.mostviewed;
    // },
    roundTo(n, digits) {
      let negative = false;
      if (digits === undefined) {
        digits = 0;
      }
      if (n < 0) {
        negative = true;
        n = n * -1;
      }
      let multiplicator = Math.pow(10, digits);
      n = parseFloat((n * multiplicator).toFixed(11));
      n = (Math.round(n) / multiplicator).toFixed(digits);
      if (negative) {
        n = (n * -1).toFixed(digits);
      }
      return n;
    }
  }
};
</script>
<style scoped>
.ltr_aligned {
  direction: ltr !important;
  text-align: left !important;
}
.FinancialStrength td {
  direction: rtl;
  text-align: right;
  font-family: "Vazir-Medium-FD";
}
</style>
