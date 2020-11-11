/* eslint-disable */
<template>
  <div>
    <!-- first row -->
    <div class="row h-100 ">
      <div class="col-sm-3">
        <v-card height="250" max-width="500" outlined class="col-sm-4">
          <!-- <v-card-title>شتران</v-card-title> -->
          <div class="row mr-7 mt-1">
            <div class="col-12">
              <span class="tickerName">{{ tickerName }}</span>
            </div>
          </div>

          <div class="row mr-10 mt-2">
            <div class="col-7">
              <span class="tick">{{ tick }}</span>
            </div>
            <div class="col-4">
              <span class="price">{{ price }}</span>
            </div>
          </div>
          <div class="mt-7">
            <table class="tickerCard">
              <tbody>
                <tr>
                  <td>{{ Volume }} :حجم</td>
                  <!-- <td>{{Volume}}</td> -->
                  <td>{{ AverageVolume }} :میانگین حجم</td>
                  <!-- <td>{{Volume}}</td> -->
                </tr>
                <tr>
                  <td>{{ MarketCap }} :ارزش بازار</td>
                  <!-- <td>{{Volume}} :حجم</td>
                  <td>{{Volume}} :حجم</td> -->
                  <td>{{ Volume }} :Enterprise Value</td>
                </tr>
                <tr>
                  <!-- <td>{{Volume}} :حجم</td>
                  <td>{{Volume}} :حجم</td> -->
                  <td>{{ PtoE }} :P/E (TTM)</td>
                  <td>{{ PtoB }} :P/B</td>
                </tr>
              </tbody>
            </table>
          </div>
        </v-card>
      </div>
      <div class="col-md-4">
        <v-card max-width="500" height="250" outlined class="col-sm-3">
          <HorizontalBarChart></HorizontalBarChart>
        </v-card>
      </div>
      <div class="col-sm-5">
        <v-card width="400" height="240" outlined>
          <StockChart></StockChart>
          <!-- <img src="@/assets/PrototypeImages/linechart.png" /> -->
        </v-card>
      </div>
    </div>
    <!-- 2nd row -->
    <div class="row mt-5">
      <div class="col-sm-6 ">
        <!-- <v-card outlined class="mx-auto" max-width="500">
            <img src="@/assets/PrototypeImages/ProfitabilityRank.png" />
        </v-card>
        -->
        <FinancialCharts />
      </div>
      <div class="col-sm-6">
        <!-- <v-card outlined class="mx-auto" max-width="500">
          <img src="@/assets/PrototypeImages/financialStrength.png" />
        </v-card>
          -->
        <MonthlyCharts />
      </div>
    </div>

    <!-- 3rd row -->
    <div class="row">
      <div class="col-sm-6">
        <FinancialStrength />
      </div>
      <div class="col-sm-6">
        <!-- <img src="@/assets/PrototypeImages/valuationRank.png" /> -->
        <ValuationRank />
      </div>
    </div>

    <div class="row">
      <div class="col-sm-4">
        <ValuationReturn />
      </div>
      <div class="col-sm-4">
        <ProfitabilityRank />
      </div>
      <div class="col-sm-4">
        <Dividend />
      </div>
    </div>

    <div class="col-xxl-4 order-1 order-xxl-2">
      <ListWidget3></ListWidget3>
    </div>
  </div>
</template>

<script>
// importing proto type images
// import linechart from "@/assets/PrototypeImages/linechart.png"
// import { LOGIN, LOGOUT } from "@/core/services/store/auth.module";
// import { GChart } from 'vue-google-charts'
import HorizontalBarChart from "@/view/pages/Ticker/charts/HorizontalBarChart";
import StockChart from "@/view/pages/Ticker/charts/StockChart";
import FinancialCharts from "@/view/pages/Ticker/charts/FinancialCharts/FinancialsChartsView";
import MonthlyCharts from "@/view/pages/Ticker/charts/FinancialCharts/MonthlyChartsView";
import FinancialStrength from "@/view/pages/Ticker/Rankers/FinancialStrength";
import ValuationRank from "@/view/pages/Ticker/Rankers/ValuationRank";
import ValuationReturn from "@/view/pages/Ticker/Rankers/Valuation&Return";
import ProfitabilityRank from "@/view/pages/Ticker/Rankers/profitabilityRank";
import Dividend from "@/view/pages/Ticker/Rankers/Dividend";
import ListWidget3 from "@/view/content/widgets/list/Widget3.vue";
export default {
  name: "ticker",
  components: {
    ListWidget3,
    HorizontalBarChart,
    StockChart,
    FinancialCharts,
    MonthlyCharts,
    FinancialStrength,
    ValuationRank,
    ValuationReturn,
    ProfitabilityRank,
    Dividend
    // GChart
  },
  data() {
    return {
      tickerName: "شستا",
      tick: "-0.81(-0.16%)",
      price: "۳۸۰۰",
      Volume: "۱۳۴",
      AverageVolume: "162,120,963",
      MarketCap: "۶۵۴",
      PtoE: "۳۷/۹۶",
      PtoB: "۷/۴۰"
      // end of bar chart data
    };
  },
  computed: {},
  methods: {} // end of methods
};
</script>

<style scoped>
table.tickerCard {
  width: 100%;
  text-align: right;
  border-collapse: collapse;
}
table.tickerCard td,
table.tickerCard th {
  padding: 5px 5px;
  direction: ltr;
}
table.tickerCard tbody td {
  font-size: 10px;
}
.tickerName {
  font-size: 25px;
}
.tick {
  font-size: 14px;
  color: red;
  direction: ltr;
}
.price {
  font-size: 14px;
}
</style>
