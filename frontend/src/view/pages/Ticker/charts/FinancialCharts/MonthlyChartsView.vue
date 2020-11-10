<template>
  <v-card outlined class="ml-3 mr-3">
    <v-container>
      <v-row>
        <v-col class="col-3">
          Monthly
        </v-col>
        <v-col
          class="col-3 d-flex justify-content-center align-items-center selector"
        >
          <v-select :items="items" label="Annual" outlined dense></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <AmountSell />
        </v-col>
        <v-col>
          <ProduceSell />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>
<script>
import AmountSell from "@/view/pages/Ticker/charts/FinancialCharts/AmountSell";
import ProduceSell from "@/view/pages/Ticker/charts/FinancialCharts/ProduceSell";
export default {
  components: {
    AmountSell,
    ProduceSell
  },
  data: () => ({
    items: ["Annual", "Quarterly"]
  })
};
</script>
<style scoped>
.selector {
  direction: ltr;
}
</style>
