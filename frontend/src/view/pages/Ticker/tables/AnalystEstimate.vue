<template>
  <v-card outlined class="AnalystEstimate"> 
        <v-card-title>Analyst Estimate</v-card-title>
        <v-simple-table class="mt-4">
          <template>
            <tbody>
              <tr>
                <td></td>
                <td class="text-right">Sep 2020</td>
                <td class="text-right">Sep 2021</td>
                <td class="text-right"  >Sep 2022</td>
              </tr>
               <tr>
                <td class="text-left">Revenue (Mil $)</td>
                <td class="text-right">272600.30</td>
                <td class="text-right">309237.00</td>
                <td class="text-right">325830.00</td>
              </tr>
               <tr>
                <td class="text-left">EBIT (Mil $)</td>
                <td class="text-right">64644.68</td>
                <td class="text-right">74935.99</td>
                <td class="text-right">78644.13</td>
              </tr>
               <tr>
                <td class="text-left">EBITDA (Mil $)</td>
                <td class="text-right">75876.49</td>
                <td class="text-right">86470.52</td>
                <td class="text-right">90656.47</td>
              </tr>
               <tr>
                <td class="text-left">EPS ($)</td>
                <td class="text-right">3.22</td>
                <td class="text-right">3.84</td>
                <td class="text-right">4.30</td>
              </tr>
               <tr>
                <td class="text-left">EPS without NRI ($)</td>
                <td class="text-right">3.05</td>
                <td class="text-right">3.83</td>
                <td class="text-right">4.30</td>
              </tr>
              <tr>
                <td class="text-left">EPS Growth Rate (%)</td>
                <td class="text-right"></td>
                <td class="text-right">10.52</td>
                <td class="text-right"></td>
              </tr>
              <tr>
                <td class="text-left">Dividends per Share ($)</td>
                <td class="text-right">0.80</td>
                <td class="text-right">0.88</td>
                <td class="text-right">1.02</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
  </v-card>

</template>
<script>
export default {
  
}
</script>
<style>
.AnalystEstimate {
  direction: ltr;
}
</style>