<template>
  <!--begin::Mixed Widget 14-->
  <div>
    <v-card>
      <!--begin::Header-->
      <div class="card-header border-0 pt-2">
        <!-- <h3 class="card-title font-weight-bolder FinancialStrength">
        بیشترین تقاضا
      </h3> -->
        <v-card-title>
          بیشترین تقاضا
        </v-card-title>
        <v-subheader class="ltr_aligned" v-if="loading == false">
          آخرین به روز رسانی {{ DataItems[0]["persianDate"].slice(10, 16) }}
        </v-subheader>
      </div>
      <!--end::Header-->
      <!--begin::Body-->
      <div class="card-body d-flex flex-column">
        <v-tabs vertical>
          <v-tab
            v-for="item in markets"
            :key="item.key"
            @click="GetFiltered(item.key)"
          >
            {{ item.shorthanded }}
          </v-tab>

          <v-tab-item v-for="itemR in markets" :key="itemR.key">
            <div class="FinancialStrength" v-if="loading">
              <b-spinner small></b-spinner>
              در حال بارگزاری
            </div>

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
                  >{{ numberWithCommas(roundTo(item.Value / 1000000000, 2))
                  }}<br />
                  میلیارد ریال</span
                >
              </template>
            </v-data-table>
          </v-tab-item>
        </v-tabs>
      </div>
      <!--end::Body-->
    </v-card>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
// import axios from "axios";
export default {
  name: "highestDemand",
  //   props: ["mostviewed"],
  data() {
    return {
      selectedMarket: 1,
      loading: true,
      DataItems: [],
      markets: [
        { key: 1, value: "بورس", shorthanded: "بورس" },
        { key: 2, value: "فرابورس", shorthanded: "فرابورس" },
        { key: 20, value: "پایه فرابورس", shorthanded: "پایه فرابورس" }
      ],
      WebsocketRequest: true,
      mvheaders: [
        { text: "رتبه", value: "Rank", sortabale: false },
        { text: "نماد", value: "ticker", sortabale: false },
        { text: "حجم تقاضا", value: "Vol", sortabale: false },
        { text: "ارزش تقاضا", value: "Value", sortabale: false },
        { text: "تعداد", value: "Count", sortabale: false }
      ]
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    filteredItems() {
      return this.DataItems.filter(item => {
        return item.marketID == this.selectedMarket;
      });
    }
  },
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
    },
    liveData() {
      let interval = setInterval(() => {
        if (!this.WebsocketRequest) {
          clearInterval(interval);
          return;
        }
        let barier = { request: "get" };
        this.$socketMarketHighestDemands.send(JSON.stringify(barier));
      }, 300000);
    },
    liveChecker() {
      let date = new Date();
      if (date.getHours() > 8 && date.getHours() < 15) {
        this.WebsocketRequest = true;
        this.liveData();
      } else {
        this.WebsocketRequest = false;
      }
    },
    GetFiltered(selectedItem) {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });
      this.selectedMarket = selectedItem;
    }
  },
  mounted() {
    this.$socketMarketHighestDemands.send(JSON.stringify({ request: "get" }));
    this.liveChecker();
    this.$socketMarketHighestDemands.onmessage = data => {
      // store.dispatch ('setMarketWatchItems',JSON.parse(data.data))
      this.DataItems = JSON.parse(data.data);
      if (JSON.parse(data.data) != "noData" && !!this.DataItems.length)
        this.loading = false;
    };
    // watch: {
    //   mostviewed() {
    //     this.populateData();
    //   }
    // }
  },
  destroyed() {
    let barier = { request: "halt" };
    this.$socketMarketHighestDemands.send(JSON.stringify(barier));
    this.WebsocketRequest = false;
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.rtl_centerd {
  direction: rtl;
  text-align: center;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left !important;
}
.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
}
.greenItem {
  color: #088a2f93 !important;
}
.titleHeaders {
  padding: 5px;
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
</style>
