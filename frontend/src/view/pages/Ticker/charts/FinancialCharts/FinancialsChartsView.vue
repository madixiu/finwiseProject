<template>
  <v-card outlined class="ml-3 mr-3">
    <v-card-title>Financials</v-card-title>
    <v-container>
      <v-row>
        <v-col
          class="col-3 d-flex justify-content-center align-items-center selector"
        >
          <v-select :items="items" outlined dense></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <RevIncome />
        </v-col>
        <v-col>
          <CashDebt />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <CashFlow />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>
<script>
import CashDebt from "@/view/pages/Ticker/charts/FinancialCharts/CashDebt";
import RevIncome from "@/view/pages/Ticker/charts/FinancialCharts/RevIncome";
import CashFlow from "@/view/pages/Ticker/charts/FinancialCharts/CashFlow";
export default {
  components: {
    RevIncome,
    CashDebt,
    CashFlow
  },
  data: () => ({
    items: ["Annual", "Quarterly"]
  })
};
</script>

<style>
.selector {
  direction: ltr;
}
</style>
