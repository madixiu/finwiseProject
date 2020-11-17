<template>
  <v-card outlined class="MoreStatistics">
    <v-card-title>More Statistics</v-card-title>
    <v-simple-table class="mt-4">
      <template>
        <tbody>
          <tr>
            <td class="text-left">Revenue (TTM) (Mil $)</td>
            <td class="text-right">273,857</td>
          </tr>
          <tr>
            <td class="text-left">EPS (TTM) ($)</td>
            <td class="text-right">3.288</td>
          </tr>
          <tr>
            <td class="text-left">RBeta</td>
            <td class="text-right">1.23</td>
          </tr>
          <tr>
            <td class="text-left">Volatility %</td>
            <td class="text-right">23.57</td>
          </tr>
          <tr>
            <td class="text-left">52-Week Range (undefined)</td>
            <td class="text-right">53.15 - 137.98</td>
          </tr>
          <tr>
            <td class="text-left">Shares Outstanding (Mil)</td>
            <td class="text-right">17,102.54</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-card>
</template>
<script>
export default {};
</script>
<style>
.MoreStatistics {
  direction: ltr;
}
</style>
